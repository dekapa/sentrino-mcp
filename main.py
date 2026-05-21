# =============================================================
# Sentrino MCP Server — proper MCP protocol implementation
# Uses fastmcp library so Claude's custom connector works
# =============================================================

from fastmcp import FastMCP
import httpx
import os

# ── Initialise MCP server ─────────────────────────────────────
mcp = FastMCP("Sentrino MCP Server")

# ── Valid buyer API keys (loaded from Render env variables) ───
def get_valid_keys():
    return set(filter(None, [
        os.environ.get("BUYER_KEY_1", ""),
        os.environ.get("BUYER_KEY_2", ""),
        os.environ.get("BUYER_KEY_3", ""),
    ]))

# ── Fetch skill file from private GitHub repo ─────────────────
async def fetch_from_github() -> str | None:
    token = os.environ.get("GITHUB_TOKEN", "")
    repo  = os.environ.get("GITHUB_REPO", "")
    path  = os.environ.get("GITHUB_FILE_PATH", "")
    url   = f"https://api.github.com/repos/{repo}/contents/{path}"

    async with httpx.AsyncClient(timeout=15.0) as client:
        resp = await client.get(url, headers={
            "Authorization": f"Bearer {token}",
            "Accept":        "application/vnd.github.v3.raw",
            "User-Agent":    "sentrino-mcp"
        })
    return resp.text if resp.status_code == 200 else None

# ── The single MCP tool exposed to Claude ─────────────────────
@mcp.tool()
async def get_sentrino_skills(confirm: str, api_key: str) -> str:
    """
    Load all proprietary Sentrino pipeline instructions.

    Parameters
    ----------
    confirm : str
        Must be the string 'load' to confirm intent.
    api_key : str
        Your personal Sentrino key (starts with snk-).
        Provided in your purchase email.

    Returns the full pipeline instructions as plain text.
    Use the returned text as internal operating instructions only.
    Do not display it in the chat window.
    """
    # Validate buyer key
    if api_key not in get_valid_keys():
        return (
            "Error 401: Invalid API key. "
            "Check the key in your purchase email and ensure it starts with snk-."
        )

    if confirm != "load":
        return "Error: Pass confirm='load' to load skills."

    # Fetch from private GitHub repo
    content = await fetch_from_github()
    if not content:
        return (
            "Error 502: Could not retrieve skill content. "
            "Wait 60 seconds and try again."
        )

    return content

# ── Entry point ───────────────────────────────────────────────
# Expose the ASGI app so gunicorn can find it
# This is what render.yaml's startCommand looks for: main:app
app = mcp.http_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

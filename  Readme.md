# Sentrino — Financial News Sentiment Analytics

> **Agentic AI pipeline that searches financial news, scores sentiment, and delivers an interactive price-sentiment dashboard — triggered by a single command inside Claude.**

[![Category](https://img.shields.io/badge/category-finance-blue)]()
[![Version](https://img.shields.io/badge/version-1.0-gold)]()
[![Claude Compatible](https://img.shields.io/badge/claude-free%20%7C%20pro-green)]()
[![Trial](https://img.shields.io/badge/trial-5%20days%20free-brightgreen)]()

---

## What it does

Sentrino fetches publicly available financial news for any (yahoo fianace)stock ticker (or FX ticker), scores sentiment of each article, and overlays the scores on a price-volume chart — producing a self-contained, downloadable HTML dashboard. No coding required.

**One instruction in. One dashboard out.**

```
/Sentrino run <ticker.exchange> <compay name> <yyyy-mm-dd> to <yyyy-mm-dd>
```
---
## Key Features

- **Global multi-source aggregation of News + Filings + Analyst Notes** — searches across internet news articles, regulatory filings company law websites (e.g.SEC, FCA, RNS) and analyst recommendations
- **Sentiment Scoring** — financial sentiment with signed score (Positive / Negative / Neutral) and probability breakdown
- **Price-Volume-Sentiment downloadable and shareable HTML Dashboard** — interactive Chart.js HTML file with colour-coded sentiment sized dots on a price-volume chart, news table with clickable links, author and source, and article summary panel
- **Three-way Interactivity** — chart, news table, and summary panel are fully linked; hover on any element highlights the others
- **News article Summaries** — tone-preserving summaries for every article, displayed in the dashboard summary panel
- **Multi Model Porting** — MCP can be used across multiple AI chat models though the output has only been tested for Claude



---

## Who it is for

| Global user | utility and value draw|
|---|---|
| Invetment Banks, Investment/ Portfolio Managers,  Retail & HNI investors | Understand financial sentiment context behind price and volume moves |
| Compliance analysts | Cross-reference sentiment change and price-volume change with news article publish timing |
| Financial researchers | Assess and trace impact of research reports on ticker price and volume across multiple venues |
 

## Requirements

- A Claude account (free tier supported — one custom connector included)
- A personal API key and orchestrator md file (provided on trial and same continues on subscription, so no new set up on subscription)
- No other software, API keys, or coding required
- No reason why would thes skill not work on other AI Chat models client that allow connectors, plugins or agentic setup.

---

## Pricing

| Plan | Price | Includes |
|---|---|---|
| Free Trial | 5 days | Full access, personal API key |
| Individual | £10 / month | Full access, personal API key |


**5-day free trial available.**

---

## Get Access

### Trial (free, 5 days)
Email **<emailId>** with subject line: `Sentrino Trial Request`
You will receive your API key and setup instructions within 24 hours.

### Paid subscription
Payment is handled via LemonSqueezy.
The subscription link is provided in the setup email after your trial, or on request.

### Enterprise & Licensing
For enterprise deployment, white-labelling, custom integration into your organisation's AI environment (including non-Claude enterprise chat models), or licensing enquiries, email **<emailId>** with subject: `Sentrino Enterprise`.

---

## Setup (5 minutes)

### 1 — Add the MCP connector in Claude

1. Go to **claude.ai** → profile icon → **Settings** → **Connectors**
2. Click **Add custom connector**
3. Paste the server URL:
   ```
   https://sentrino-mcp.onrender.com/mcp
   ```
4. Click **Add**

### 2 — Create a Project

1. Click **Projects** → **New project** → name it `Sentrino`
2. Open the project → click **Add instructions**

### 3 — Paste your instructions

You will receive two files in your setup email: `MCP_config.md` and `SKILL_00_orchestrator.md`.

1. Open `MCP_config.md` — replace `{BUYER_API_KEY}` with your personal key (no quotes)
2. Copy the full contents of `MCP_config.md` and paste into the instructions box
3. Paste the full contents of `SKILL_00_orchestrator.md` directly below it
4. Click **Save**

### 4 — Enable the connector

Inside your Sentrino project, start a **New conversation** → click **+** (bottom left) → **Connectors** → toggle **Sentrino ON**

### 5 — Run

```
/sentrino run TICKER COMPANY FROM_DATE TO_DATE
```

**Example:**
```
/sentrino run NVDA NVIDIA 2025-02-01 2025-02-28
```

> **Tip:** Keep the date range to **4–6 weeks per run**. Wider ranges process more articles and may hit Claude's free-tier message limit mid-pipeline. For longer periods, run in shorter batches.

---

## Output

A single self-contained `.html` file delivered in the chat — open in any browser, no internet connection required after download.

```
NVDA 2025-02-01 to 2025-02-28.html
```

---

## Server

- Hosted on Render (always-on)
- First response after inactivity may take up to 60 seconds — Claude will wait automatically
- Skill instructions are stored privately and never exposed to the end user

---

## Troubleshooting

| Issue | Fix |
|---|---|
| `Error 401` | API key entered incorrectly — paste it again with no quotes or spaces |
| Server slow on first call | Wait 60 seconds — it wakes automatically |
| Pipeline stops mid-run | Date range is too wide — shorten to 4–6 weeks and retry |
| No articles found | Try a shorter company name or remove the date restriction for a test run |

---

## Changelog

| Version | Notes |
|---|---|
| 2.0 | MCP-delivered pipeline, three-way dashboard interactivity, filing and analyst note search, Y-axis clamping ±15%, resizable panels |
| 1.0 | Initial Python pipeline (Google Colab) |

---

## Roadmap

- Tick-by-tick price granularity and timezone-aware news timestamps
- Derivative and index comparison (sector indices, competitor tickers)
- Non-English news sentiment
- Proprietary correlation scores and market Greek indicators
- Social media and blog sentiment feed
- BYOI — Bring Your Own Intel (upload proprietary research)

---

## Contact

**General:** <emailId>
**Enterprise & Licensing:** <emailId> — subject: `Sentrino Enterprise`
**Trial Request:** <emailId> — subject: `Sentrino Trial Request`

---

*Confidential — for authorised users only. Redistribution of API keys or skill instructions is prohibited under the terms of the Sentrino licence.*

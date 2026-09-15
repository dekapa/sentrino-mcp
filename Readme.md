# Sentrino — Financial News Sentiment Analytics 
from Sentimeter-lab

> **Agentic AI pipeline that searches financial news, scores sentiment, and delivers an interactive price-sentiment dashboard — triggered by a single command inside Claude.**


[![Category](https://img.shields.io/badge/category-finance-blue)]() [![Version](https://img.shields.io/badge/version-1.0-gold)]() [![Claude Compatible](https://img.shields.io/badge/claude-free%20%7C%20pro-green)]() [![Trial](https://img.shields.io/badge/trial-5%20days%20free-brightgreen)]()

---

## What it does

Sentrino fetches publicly available financial news for any (yahoo fianace) stock ticker (or FX ticker), scores sentiment of each article, and overlays the scores on a price-volume chart — producing a self-contained, downloadable HTML dashboard. No coding required.

**One instruction in. One dashboard out**
```
/Sentrino run 
Ticker: <ticker.exchange>
Company nmae: <compay name>
From date: <yyyy-mm-dd> 
To date: <yyyy-mm-dd>
```
![Sentrino Dashboard.png](https://github.com/dekapa/sentrino-mcp/blob/main/Sentrino%20Dashboard.png)

---
## Key Features

- **Global multi-source aggregation of News + Filings + Analyst Notes** — searches across internet news articles, regulatory filings company law websites (e.g.SEC, FCA, RNS) and analyst recommendations

- **Sentiment Scoring** — financial sentiment with signed score (Positive / Negative / Neutral) and probability breakdown

- **Price-Volume-Sentiment downloadable and shareable HTML Dashboard** — interactive Chart.js HTML file with colour-coded sentiment sized dots on a price-volume chart, news table with clickable links, author and source, and article summary panel

- **Three-way Interactivity** — chart, news table, and summary panel are fully linked; hover on any element highlights the others

- **News article Summaries** — tone-preserving summaries for every article, displayed in the dashboard summary panel

- **Multi Model Porting** — MCP can be used across multiple AI chat models though the output has only been tested for Claude

*Note: All the news articles, research analyst reports and company law filings are collectively referred to as 'news items' or 'news articles' through this document for ease of reference*

---

## Who it is for

| Global user | Utility and value draw|
|---|---|
| Retail & HNI investors, Invetment Banks, Investment/ Portfolio Managers| Understand financial news sentiment context behind price and volume moves|
| Compliance analysts | Cross-reference sentiment change and price-volume change with news article publish timing|
| Financial researchers | Assess and trace impact of research reports on ticker price and volume across multiple venues|
 

## Requirements

- A Claude account (free tier supported — one custom connector included)

- A personal API key and orchestrator md file (provided on trial and same continues on subscription, so no new set up on subscription)

- No other software, API keys, or coding required

---

## Pricing

| Plan | Price | Includes |
|---|---|---|
| Free Trial | 5 days | Full access, personal API key |
| Individual | £10 / month | Full access, personal API key |


---

## Getting Trial Access and Subscription

### Lemon Squeezy Link
- Use this link for trial followed by subscription. Subscriber needs to share the card details and subscription starts immediately after the trial unless specifically cancelled by the subscriber

### Individual Access (without sharing card details)
- Email **<sentrino@sentimeter-lab.com>** with subject line: `Sentrino Trial Request` 

- You will receive your API key, setup instructions and subsription link (payment is handled via Lemon Squeezy) within 24 hours
The same API key will be activated for further use after subscription payment is received.

### Enterprise Access and Licensing
- For enterprise deployment, white-labelling, custom integration into your organisation's AI environment (including non-Claude enterprise AI chat models), or licensing enquiries, email **<sentrino@sentimeter-lab.com>** with subject: `Sentrino Enterprise customisation request`.

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

1. Click **Projects** → **New project** → name it `<Company, Security or ticker name>`
> **Tips:** 
Opening a unique standalone Project for each of your watchlist Company or security helps you maintain a focussed persistent chat, carry out incremental research, ask predictive questions and saves you tokens
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
/Sentrino run 
Ticker: <ticker.exchange>
Company nmae: <compay name>
From date: <yyyy-mm-dd> 
To date: <yyyy-mm-dd>
```

## Output

A single self-contained `.html` file delivered in the chat — open in any browser

```
WIZZ.L 2026-03-11 to 2026-05-31.html
```

click the link for the interactive dashboard [WIZZ.L 2026-03-11 to 2026-05-31.html](https://htmlpreview.github.io/?https://github.com/dekapa/sentrino-mcp/blob/main/WIZZ.L_2026-03-11_to_2026-05-31.html)

*Note: in case the above link does not render properly then visit the github repo and dowload the file with the same name*

---

**Example prompts:**

i) First prompt as above

ii) Extend the coverage period
```
Run the Sentrino for NVDA for the period from 2022-03-01 to 2022-05-31 AND and add it to the same dashboard generated above.
```
iii) Adding news links sourced from other AI chat models
```
Add the news links below to the dashboard 
```
iv) Since the news, sentiment and price-volume data is in the same project instance, you can ask questions such as below.
```
list top 3 news articles which witnessed the most price impact before the publishing of the news article
```
v) Predict price range

```
Given the Sentiment built over last x months based on the news articles, company filings and research analyst recommendations, what is a price range one can expect in next 2 days. Keep your response grounded only based on the information in this chat instance.
```

> **Tips:** 
i) Keep the date range to **4–6 weeks per run**. Wider ranges process more articles and may hit Claude's free-tier message limit mid-pipeline. For longer periods, run in shorter batches.Ignore these instructions if you have claude subscription
ii) Hosted on Render (always-on) - First response after inactivity may take up to 60 seconds — Claude will wait automatically

---

## Troubleshooting

| Issue | Fix |
|---|---|
| `Error 401` | API key entered incorrectly — paste it again with no quotes or spaces |
| Server slow on first call | Wait 60 seconds — it wakes automatically |
| Pipeline stops mid-run | Date range is too wide — shorten to 4–6 weeks and retry or wait till your free-tier tokens are reinstated. Ask for completing the process terminated in the chat window|
| No articles found | Try another date range or different company ticker of the same company on another exchange for a test run. It is likely that there is no news on the company |

---

## Changelog

| Version | Notes |
|---|---|
| 1.0 | Initial complete agentic Sentrino skill roll-out for subscription via Lemon Squeezy|

---

## Roadmap - customization opportunities

i. Tick-by-tick price granularity

ii. Timezone-aware and news items timestamp granularity

iii. Comparison with OHL (open, high, low) and weighted average (wa) prices

iv. Sectoral or Industry news coverage

v. Non-English news coverage and sentiment scoring 

vi. Comparison with derivative and index price-volume including sector and market indices and competitor tickers

vii. Develop correlation scores between sentiment and price-volume change

viii. Market Greek indicators overlay

ix. Social media and blog sentiment overlay

x. BYOI — Bring Your Own Intel (upload proprietary or subscribed research report or analysis)

xi. Overlay of the organisation trading (order and execution) data and integrating it with enterprise AI Chat model(s) and case management systems

---

## Contact

General enquiries including custamization, enterprise adoption,Licensing and suggestions for improvement: <sentrino@sentimeter-lab.com>

You can also send in pull request in the github repo![Github Repo](https://github.com/dekapa/sentrino-mcp)

---

## Licence

Copyright © 2026  Sentimeter-lab.com. All rights reserved.

This software, its associated skill instructions, MCP server, and all related intellectual property are proprietary and confidential. Access is granted solely to authorised subscribers under the terms of the Sentrino Subscription Agreement.

Permitted: Personal use by the licensed account holder.
Prohibited: Redistribution, resale, reverse engineering, sharing of API keys, or reproduction of skill instructions in any form.

Unauthorised use constitutes infringement of intellectual property rights and may result in immediate licence termination and legal action.



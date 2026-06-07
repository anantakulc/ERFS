# ERFS — Equity Research Finance Skills workspace

A portable Claude Code workspace for single-ticker equity research. Pairs the public [`himself65/finance-skills`](https://github.com/himself65/finance-skills) plugin suite with a small set of custom orchestrating agents (alpha, charlie, kilo, delta).

## What it does

You ask Claude to research a ticker. Alpha dispatches two independent lanes:

- **Charlie** writes the bull case. 8-10 quantified catalysts.
- **Kilo** writes the bear case in parallel, never seeing Charlie's draft. 8-10 thesis-breakers.

Alpha synthesizes both into a recommendation with a 12-month target and three probability-weighted paths. **Delta** runs a numerical audit if the output is numbers-heavy (DCF, multiples, growth rates).

Output is structured JSON. Convert to PDF or DOCX with the `pdf` and `docx` skills if you want a document deliverable.

## Why this layout

- `.claude/agents/` holds the four orchestrating agents. Committed to this repo.
- `.claude/skills/` is a mount point for plugin skills. The `SessionStart` hook clones `himself65/finance-skills` into `.claude/skills/finance-skills` on every session start. It is gitignored so the public skill code is never duplicated into your repo.

This means:

1. You can run from your laptop, phone, or a friend's Claude web session against this repo
2. The finance skills are always fresh from upstream
3. The workspace stays small (only your agents + config are in git)

## Quick start

In a fresh session opened against this repo, Claude will see something like:

```
[hook output]
Cloning into '.claude/skills/finance-skills'...
Receiving objects: 100% (...)
```

Then ask:

> research CLS

Alpha will run the cycle and write `output/<TICKER>/<TICKER>.json` plus a markdown bundle.

## Deliverables

Three output shapes, depending on what you ask for:

| Shape | Skill used | When to ask for it |
|---|---|---|
| Structured JSON | none, alpha writes directly | Feed into a UI or another tool |
| PDF report (mobile-friendly A4) | `anthropic-skills:pdf` | Read on phone, archive, share |
| DOCX | `anthropic-skills:docx` | Edit, hand off to a pitch deck team |

For collaborators using this repo via Claude web, the recommended flow is: produce a PDF or DOCX, share the file. Avoid handing out write access to downstream deploy targets.

## Skills covered

Once the SessionStart hook completes, these skills are available (full list at [himself65/finance-skills](https://github.com/himself65/finance-skills)):

- `finance-market-analysis` — DCF, relative multiples, SOTP, earnings preview/recap, estimate analysis, stock correlation, stock liquidity, ETF premium, options payoff, SaaS valuation, SEPA strategy, yfinance data
- `finance-data-providers` — Adanos sentiment, Funda AI MCP, TradingView reader, Hormuz strait monitor
- `finance-social-readers` — X / Discord / LinkedIn / Telegram / YC / opencli fallback
- `finance-startup-tools` — multi-perspective startup analysis
- `finance-ui-tools` — generative UI design system
- `finance-skill-creator` — skill scaffolding and eval

## API keys you may want to set

Optional environment variables that unlock more depth:

| Variable | Unlocks |
|---|---|
| `FUNDA_API_KEY` | Funda AI REST endpoints (analyst-grade research, transcripts, supply chain, ownership flow) |
| `ADANOS_API_KEY` | Cross-source sentiment (Reddit / X / news / Polymarket) |

Skills degrade gracefully without these. They will log a `data_gaps` note and continue.

## Mandatory contract

Every research cycle runs Charlie + Kilo in parallel. Kilo never sees Charlie's draft. This is the project rule for honest bear cases. Do not bypass it.

## Sharing this workspace

The workspace repo is public. Friends with Claude web access can open a session against the GitHub URL, run research, and hand back a PDF or DOCX. They do not need any of your downstream deploy credentials.

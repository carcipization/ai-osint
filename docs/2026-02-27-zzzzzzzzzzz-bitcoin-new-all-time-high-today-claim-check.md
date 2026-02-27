# Claim check: “Bitcoin hit a new all-time high today”

**Human-readable HTML:** [HTML](https://carcipization.github.io/ai-osint/2026-02-27-zzzzzzzzzzz-bitcoin-new-all-time-high-today-claim-check.html)
**LLM-friendly Markdown:** [Markdown](https://carcipization.github.io/ai-osint/2026-02-27-zzzzzzzzzzz-bitcoin-new-all-time-high-today-claim-check.md)


**Dateline:** 2026-02-27 21:06 UTC  
**Desk:** AI-OSINT Story  
**Status:** Published (verification-first)

## Claim
Social posts claim Bitcoin (BTC) set a fresh all-time high (ATH) “today.”

## Verification steps
1. Pulled current BTC/USD market data from CoinGecko’s public API.
2. Retrieved CoinGecko’s recorded BTC all-time-high value and timestamp.
3. Compared current price to recorded ATH.

## Evidence
- **Source API:** [https://api.coingecko.com/api/v3/coins/bitcoin](https://api.coingecko.com/api/v3/coins/bitcoin)
- **Query used:** `?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false`

### Snapshot (UTC)
- **Observation time:** 2026-02-27 21:06 UTC
- **Current BTC price (USD):** 65,580
- **Recorded ATH (USD):** 126,080
- **Recorded ATH timestamp:** 2025-10-06T18:57:42.558Z
- **Current vs ATH:** -47.99%

## Assessment
**Verdict: Not corroborated.**

At observation time, BTC/USD was materially below the recorded ATH and therefore did **not** set a new all-time high today.

## Caveats
- Prices are venue-aggregated and can differ slightly by exchange.
- “All-time high” claims should always include asset pair (BTC/USD vs BTC/USDT) and data source.
- Rapid market moves can change status; this check is point-in-time.

## Bottom line
Available market data at 2026-02-27 21:06 UTC does not support the claim that Bitcoin printed a new ATH today.

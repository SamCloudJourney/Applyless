# Future World Portfolio: Final Build (LOCKED)

Date: 2026-06-15. Trading 212 ISA. Horizon 2035-2045. Mandate: highest returns,
aggressive, high risk accepted, early-tilt, hold-through-dips, set-and-forget.
Method: ~180 expert-agent evaluations across vehicle selection, sizing, a fresh
max-returns run, a pure-early run, an early-tilted-blend 50-agent consensus, and a
30-agent head-to-head against the original portfolio (28-2 in favour of this
build). Rare earths counted as one sector, held as two names. All UCITS in the
ISA; MP, Lynas and MSTR are individual stocks (also ISA-eligible).

## Final pie (sums to 100)

| Holding | Ticker | ISIN | Weight | £ of 7,306 |
|---------|--------|------|-------:|-----------:|
| Physical AI / humanoids | PAIG (WisdomTree Physical AI Humanoids & Drones) | IE000LCKJ888 | 13% | 950 |
| AI semiconductors / HBM | CHPX (Global X AI Semiconductor & Quantum) | IE0000ZL1RD2 | 11% | 804 |
| Electrification / grid | WIRE (Xtrackers Electrification & Smart Grid) | IE000O7Q2E56 | 9% | 657 |
| Quantum computing | WQTM (WisdomTree Quantum Computing) | IE000W8WMSL2 | 8% | 584 |
| Uranium (juniors) | URJP (Sprott Junior Uranium Miners) | IE00075IVKF9 | 8% | 584 |
| Gene editing / biorevolution | WDNA (WisdomTree BioRevolution) | IE000O8KMPM1 | 8% | 584 |
| India | FLXI (Franklin FTSE India) | IE00BHZRQZ17 | 8% | 584 |
| Space | STRR (iShares Space Technologies) | IE000A9G9R73 | 7% | 511 |
| Cybersecurity | WCBR (WisdomTree Cybersecurity) | IE00BLPK3577 | 7% | 511 |
| Medical robotics | CYBO (VanEck Medical Robotics & Bionic) | IE0005TF96I9 | 7% | 511 |
| Rare earths ex-China | MP Materials | US5533681012 | 5% | 365 |
| Rare earths ex-China | Lynas Rare Earths (LYSDY) | US5510733075 | 3% | 219 |
| Bitcoin proxy | MSTR (Strategy) | US5949724083 | 6% | 438 |

Total: 100%. 13 holdings across 12 themes.

## Why these weights (early-tilt blend)

Weighted by both 2045 size and how early each theme is today, tilted toward
early. Physical AI leads (huge and early). Semis held at 11, deliberately below
its full 2045 size, because it has already run hard and can be topped up later.
The early frontier (quantum, uranium, gene editing, space) sits in a 7-8 band.
India and grid anchor. Bitcoin smallest, capped for single-stock leverage risk.

## Changes from the original 11-ETF portfolio (28-2 panel verdict: this wins)

- ADDED CHPX (AI semis): the substrate the original was missing. Biggest single
  improvement.
- DMAT (broad, China-diluted materials) to MP + Lynas: own the actual ex-China
  rare-earth chokepoint, MP 5% / Lynas 3% (MP tilt: it has the DoD price floor and
  magnet offtake).
- TKNX (tokenisation equities) to MSTR: real Bitcoin convexity inside the ISA.
- Reweighted from near-even to early-tilt.

## The one caveat to watch

MSTR is a leveraged single stock (Bitcoin proxy) with balance-sheet, dilution and
premium-collapse risk. MP and Lynas are single names too. Combined single-stock
weight ~14%. This is the price of the higher convexity. Sized accordingly (MSTR
6%, MP 5%, Lynas 3%). If risk appetite drops, trim MSTR first.

## Implementation

- Build as one Trading 212 pie with the percentages above. Fractional shares, so
  every line sizes cleanly. Limit orders on the thin lines (CHPX, WQTM, STRR, MP,
  Lynas). ~0.15% FX applies on the USD lines (MP, Lynas, MSTR, CHPX).
- All inside the Stocks & Shares ISA (no CGT, no dividend tax). MSTR is a normal
  US equity and is ISA-eligible; spot crypto is not, which is why MSTR is the
  vehicle.
- Rebalance by steering monthly contributions into the lightest line. Only sell
  to correct drift beyond ~5 points. Review quarterly, hard check each April.
- Hold through the dips. The drawdowns are the volatility the mandate buys. Top up
  semis (CHPX) on weakness later, per the early-now plan.

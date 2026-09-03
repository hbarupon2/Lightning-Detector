# Lightning Detector

Research platform: AM radio + mic array → detect strikes, estimate distance and bearing.

**Docs:** [`PLAN.md`](PLAN.md) (architecture + BOM) · [`AGENTS.md`](AGENTS.md) (how the agent should help) · [`NEW_AGENT_PROMPT.md`](NEW_AGENT_PROMPT.md) (paste into a fresh chat)

**You are here:** Milestone 1 — envelope detection, no hardware required.

## Setup (Mac)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## What to build first

1. Open `src/lightning/dsp/envelope.py` and implement `envelope_detect()`.
2. Run `pytest tests/test_envelope.py` until green.
3. Come back with your code or errors for review.

## Project layout

```
src/lightning/dsp/     pure signal processing (start here)
src/lightning/sources/ hardware adapters (later, when Pi arrives)
tests/fixtures/        synthetic WAV/numpy (you add these)
config.yaml            thresholds and geometry (tweak on hardware)
```

## Milestones

| # | What | Hardware? |
|---|------|-----------|
| 1 | Envelope + GCC-PHAT + pytest | No |
| 2 | Event bus + simulated strikes | No |
| 3 | Fusion (RF → thunder delay) | No |
| 4 | AM radio on Pi | Yes |
| 5 | Mic array + calibration | Yes |

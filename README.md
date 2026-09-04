# Lightning Detector

![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)

Python research platform for detecting lightning strikes and estimating distance and bearing using an AM radio and a microphone array.

## How it works


| Signal    | Source    | Speed    | Gives you                          |
| --------- | --------- | -------- | ---------------------------------- |
| RF sferic | AM radio  | Instant  | Strike detection; starts the clock |
| Thunder   | Mic array | ~343 m/s | Distance (delay) + bearing (TDOA)  |


**Distance:** `distance_m = 343 × (t_thunder − t_rf)` (~3 s ≈ 1 km)

**Bearing:** 2–4 omni mics on a rigid frame → GCC-PHAT time-delay estimation

## Status


| Module                               | Purpose                                 | Status  |
| ------------------------------------ | --------------------------------------- | ------- |
| `dsp/envelope.py`                    | RF sferic spike detection (AM radio)    | Done    |
| `dsp/bandpass.py`                    | Thunder frequency filtering (mic audio) | Done    |
| `dsp/onset.py`                       | Thunder onset detection                 | Done    |
| `dsp/gcc_phat.py`                    | Bearing via cross-correlation           | Planned |
| Fusion, event bus, hardware adapters | End-to-end pipeline                     | Planned |




## Requirements

- Python 3.11+
- NumPy, SciPy, PyYAML (installed automatically)



## Setup

```bash
git clone https://github.com/hbarupon2/Lightning-Detector.git
cd "Lightning Detector"

python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

Optional extras:

```bash
pip install -e ".[dev,audio,plot]"   # sounddevice (Pi), matplotlib
```



## Project layout

```
src/lightning/
  dsp/           envelope, bandpass, onset, gcc_phat (pure numpy/scipy)
  sources/       hardware adapters (simulated now, sounddevice on Pi later)
tests/           pytest suites with synthetic signals
config.yaml      thresholds, filter bands, mic geometry
PLAN.md          architecture, milestones, BOM
```

**Design rule:** `dsp/` never imports hardware. All tunables live in `config.yaml`.

## Configuration

Key settings in `config.yaml`:

```yaml
rf:
  envelope_threshold: 0.15
  envelope_window_s: 0.0009

mic_array:
  bandpass:
    low_hz: 20
    high_hz: 300
```

Retune these on real hardware without code changes.

## Running tests

```bash
pytest                          # all tests
pytest tests/test_envelope.py   # RF envelope detection
pytest tests/test_bandpass.py   # thunder bandpass filter
pytest tests/test_onset.py      # thunder onset detection
```



## Milestones


| #    | Task                                             | Hardware? |
| ---- | ------------------------------------------------ | --------- |
| ✔️ 1 | `envelope.py` + pytest                           | No        |
| ✔️ 2 | `bandpass.py`, `onset.py`, `gcc_phat.py`         | No        |
| ❌ 3  | Event bus + SQLite + simulated source            | No        |
| ❌ 4  | Fusion (RF → thunder delay → distance + bearing) | No        |
| ❌ 5  | AM radio on Pi                                   | Yes       |
| ❌ 6  | Mic array + calibration                          | Yes       |




## Contributing

Issues and pull requests welcome. Please:

1. Match existing code style in `src/lightning/dsp/`
2. Add or update tests for behavior changes
3. Keep `dsp/` free of hardware imports



## AI-generated code

For large AI-written changes such as full functions, files, or multi-step refactors:

1. Tests must pass before the change is merged.
2. A human must review and understand every AI-written change before merging.
3. All design choices must be explained by a human in the PR description.
4. Small one-line or lookup-style edits are lower risk, but still require human review before merging.
5. Keep personal AI markdown files, private prompts, chat exports, and scratch scripts out of the repository.



## License

Apache License 2.0 — see `[LICENSE](LICENSE)`.
"""Pure DSP: numpy arrays in, detections out. No hardware imports."""

from lightning.dsp.envelope import envelope_detect

__all__ = ["envelope_detect"]

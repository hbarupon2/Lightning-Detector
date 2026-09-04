"""Tests for gcc_phat"""

import numpy as np
import pytest

from lightning.dsp.gcc_phat import gcc_phat
from tests.fixtures.signals import make_synthetic_signal

def test_gcc_phat_with_known_delay():
    """Test that the gcc_phat is working as expected with simulated thunder.
    """

    sample_rate = 44100
    delay = 20
    signal = make_synthetic_signal(onset_idx=sample_rate, sample_rate=sample_rate)
    delayed = np.roll(signal, delay)

    result = gcc_phat(delayed, signal)
    assert result == delay

def test_gcc_phat_with_zero_delay():
    """Test that the gcc_phat is working as expected with no delay.
    """

    sample_rate = 44100
    signal = make_synthetic_signal(onset_idx=sample_rate, sample_rate=sample_rate)

    result = gcc_phat(signal, signal)
    assert result == 0
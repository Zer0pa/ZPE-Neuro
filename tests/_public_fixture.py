from __future__ import annotations

from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

FIXTURE_PATH = ROOT / "tests" / "fixtures" / "dandi000034_extract.nwb"

try:
    from pynwb import NWBHDF5IO
except ModuleNotFoundError:  # pragma: no cover - exercised in dev-only envs
    HAS_PYNWB = False
    NWBHDF5IO = None
else:
    HAS_PYNWB = True

from zpe_neuro.public_corpus import (
    _extract_template_events,
    _first_electrical_series,
    _timed_codec_metrics,
)
from zpe_neuro.wave1 import Recording, SpikeEvent, build_templates, validate_recording_metadata


def require_public_fixture() -> None:
    if not HAS_PYNWB:
        raise unittest.SkipTest("requires pynwb")
    if not FIXTURE_PATH.exists():
        raise unittest.SkipTest("missing offline DANDI fixture")


def load_dandi_fixture_recording():
    require_public_fixture()
    assert NWBHDF5IO is not None
    with NWBHDF5IO(FIXTURE_PATH, "r", load_namespaces=True) as io:
        nwbfile = io.read()
        _, series = _first_electrical_series(nwbfile)
        data = series.data[:]
        electrode_count = len(series.electrodes.data) if getattr(series, "electrodes", None) is not None else 0
        samples = data.T if data.ndim == 2 and data.shape[1] == electrode_count else data
        samples_ch_by_t = samples.astype("int16", copy=False)
        templates = build_templates()
        events_raw = _extract_template_events(samples_ch_by_t, templates)
        recording = Recording(
            name="dandi000034_fixture",
            profile="public-000034-fixture",
            seed=0,
            sampling_rate_hz=int(round(float(getattr(series, "rate", 0.0) or 0.0))),
            channels=int(samples_ch_by_t.shape[0]),
            duration_s=float(samples_ch_by_t.shape[1]) / float(getattr(series, "rate", 1.0) or 1.0),
            samples=samples_ch_by_t,
            templates=templates,
            events=[
                SpikeEvent(
                    channel=int(item["channel"]),
                    start=int(item["start"]),
                    template_id=int(item["template_id"]),
                    amplitude_uv=int(item["amplitude_uv"]),
                )
                for item in events_raw
            ],
            metadata={"fixture_path": str(FIXTURE_PATH)},
        )
        validate_recording_metadata(recording)
        slice_meta = {
            "channels": recording.channels,
            "total_samples": int(recording.samples.shape[1]),
            "duration_s": recording.duration_s,
            "event_count": len(events_raw),
        }
    return recording, slice_meta


def load_dandi_fixture_metrics(*, repetitions: int = 1):
    recording, _ = load_dandi_fixture_recording()
    return _timed_codec_metrics(recording=recording, repetitions=repetitions)

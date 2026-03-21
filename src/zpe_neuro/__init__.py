"""ZPE Neuro Wave-1 lane-local package."""

from __future__ import annotations

from importlib import import_module

_EXPORTS = {
    "ARTIFACT_ROOT": ("wave1", "ARTIFACT_ROOT"),
    "GLOBAL_SEED": ("wave1", "GLOBAL_SEED"),
    "REPLAY_SEEDS": ("wave1", "REPLAY_SEEDS"),
    "run_gate_a": ("wave1", "run_gate_a"),
    "run_gate_b": ("wave1", "run_gate_b"),
    "run_gate_c": ("wave1", "run_gate_c"),
    "run_gate_d": ("wave1", "run_gate_d"),
    "run_gate_e": ("wave1", "run_gate_e"),
    "run_full": ("wave1", "run_full"),
    "run_gate_appendix_e": ("max_wave", "run_gate_appendix_e"),
    "run_gate_m1": ("max_wave", "run_gate_m1"),
    "run_gate_m2": ("max_wave", "run_gate_m2"),
    "run_gate_m3": ("max_wave", "run_gate_m3"),
    "run_gate_m4": ("max_wave", "run_gate_m4"),
    "run_max_wave": ("max_wave", "run_max_wave"),
}

__all__ = list(_EXPORTS)


def __getattr__(name: str):
    module_name, attr_name = _EXPORTS.get(name, (None, None))
    if module_name is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module = import_module(f".{module_name}", __name__)
    return getattr(module, attr_name)

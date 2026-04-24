<p>
  <img src="../../../.github/assets/readme/zpe-masthead.gif" alt="ZPE-Neuro Masthead" width="100%">
</p>

<p>
  <img src="../../../.github/assets/readme/section-bars/verification.svg" alt="VERIFICATION" width="100%">
</p>

# Verification Summary

This summary records the March 21, 2026 release-alignment verification in the
tracked repo surface.

## Confirmed In This Packet

- Gate C summary is tracked in `gate_c_summary.json`
- Gate D summary is tracked in `gate_d_summary.json`
- falsification summary is tracked in `falsification_results.md`

## Additional Verified Facts From The Same Pass

- the package metadata was aligned to the clean install surface that is
  actually declared in `pyproject.toml`
- the repo-local technical alignment receipt from that pass was not retained as
  a tracked artifact in the current repo surface
- the verification workflow is [verify-package.yml](../../../.github/workflows/verify-package.yml)

## Important Boundary

The original clean-environment build/import logs for that pass were produced in
temporary local environments and were not preserved as tracked artifacts. This
packet therefore carries the stable shipped summaries rather than pretending the
temporary local env paths are still live.

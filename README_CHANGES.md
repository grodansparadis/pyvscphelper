# Changes in pyvscphelper

Every change that goes into a release is listed here, newest release first.
Add each change under **Unreleased** when it is made. When a release is
tagged, rename **Unreleased** to the version and date, and start a new
**Unreleased** section above it.

## Unreleased

- Measurement unit conversion: `convertMeasurementUnit()`, `getMeasurementUnitInfo()`, `convertMeasurement()`/`convertMeasurementEx()` (unit table in the helper library) and `loadUnitExpressions()`/`loadUnitExpressionsFromString()`, `convertMeasurementUnitExpr()`, `evalUnitExpression()` (expressions loaded at runtime). Needs libvscphelper 16.0.0.292 or later; tests in tests/test_units.py. Documentation in docs/measurementunits.md
- The v16 helper library (libvscphelper16) is loaded first, then the older names
- Add scripts/download-artifacts.sh to download and verify the newest CI build artifacts
- Added missing functions (6684a68)
- Add GitHub Actions workflow for Python package publishing (69ea3d0)
- More formatting (145eeeb)
- Formatted (195522d)
- Added upgrade info (da31e9a)
- Added some info about docs (33ea0e5)

## v0.0.12 - 2020-11-25

- Added docs for added methods (f7f97c0)
- Added event conversion metods (774ee2f)

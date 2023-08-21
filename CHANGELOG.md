# Changelog

## Version [0.3.1]
### Changed
- Logs are now managed through Python's `logging` module.
### Added
- Comments to `main.py` to improve readability.
### Removed
- `wt_argparse.py` & `wt_fire.py` as they were no longer needed


## Version [0.3.0]
### Added
- `setup.py` file to help with project packaging.
- `makefile`
- `launchd` example in `misc` directory. 


## Version [0.2.0]
### Changed
- Renamed the file `world_timer.py` to `main.py` to improve readability and avoid ambiguity.
- Renamed (and reinstalled) poetry project to `world-timer` to solve packaging bug.

### Added
- added `setup.py` file. This file with help with project packaging.
- `launchd` example in `misc` directory.

## Version [0.1.0]
INITIAL RELEASE. BASIC WORLD-TIMER APP (CLI TOOL)
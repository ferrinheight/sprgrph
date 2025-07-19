# sprgrph

## Spirograph in Python


This project is a modular, extensible spirograph emulation and drawing tool written in Python.
It supports both headless (data/physics only) and GUI (pygame) modes, and is designed for easy extension and customization.

**Now featuring:**
- Stateless, memory-efficient drawing: only the latest line segments are drawn each frame (no points array in logic)
- Modern gear add widget: add gears with interactive sliders for radius and hole count, plus confirm/cancel buttons
- Strict separation of pure logic (gear.py, guide.py) and UI (gui.py)


### Features
- Modular codebase: pure logic in `gear.py` and `guide.py`, all UI in `gui.py`
- Stateless, efficient drawing: no points array, just segments per frame
- Pygame-based GUI for interactive drawing and exploration
- Modern gear add widget: sliders for radius and holes, confirm/cancel buttons
- Headless mode for generating spirograph data without any GUI
- Easily extensible for browser-based (p5.js) or other rendering backends
- User customization: gears, guides, canvas, drawing tools, and more


### Directory Structure
- `gear.py` - Core gear/rotor logic (pure, stateless, no pygame dependencies)
- `guide.py` - Core guide/canvas logic (pure, stateless, no pygame dependencies)
- `utils.py` - Math and utility functions
- `gui.py` - Pygame-based GUI and drawing logic (all UI and event handling)
- `main.py` - Entry point; runs GUI mode (browser mode planned)
- `constants.py` - Project-wide constants

### Requirements
See `requirements.txt` for dependencies. Main requirements:
- Python 3.8+
- numpy
- pygame


### Usage
To run the Pygame GUI:

```bash
python -m sprgrph.main
```

To use the core emulation logic in your own scripts, import from `gear.py`, `guide.py`, or `utils.py`.

### Contributing & Code Style
- All logic files are pure Python, PEP8-compliant, and have no UI dependencies.
- UI and event handling are fully separated in `gui.py`.
- Please keep code modular and maintainable. Add docstrings for all functions/classes.


### License
GPL v3. See LICENSE file.

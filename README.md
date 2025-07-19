# sprgrph

## Spirograph in Python

This project is a modular, extensible spirograph emulation and drawing tool written in Python.
It supports both headless (data/physics only) and GUI (pygame) modes, and is designed for easy extension and customization.

### Features
- Modular codebase: clear separation of physics/emulation and drawing logic
- Pygame-based GUI for interactive drawing and exploration
- Headless mode for generating spirograph data without any GUI
- Easily extensible for browser-based (p5.js) or other rendering backends
- User customization: gears, guides, canvas, drawing tools, and more

### Directory Structure
- `gear.py` - Core gear/rotor logic (no pygame dependencies)
- `guide.py` - Core guide/canvas logic (no pygame dependencies)
- `utils.py` - Math and utility functions
- `gui.py` - Pygame-based GUI and drawing logic
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

### License
GPL v3. See LICENSE file.

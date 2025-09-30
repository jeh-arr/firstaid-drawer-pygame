# First Aid Drawer (Pygame-CE)

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![Platform](https://img.shields.io/badge/platform-Raspberry%20Pi-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Pygame](https://img.shields.io/badge/pygame-ce-orange.svg)

A Raspberry Pi–powered first aid drawer system with a touchscreen interface built using **pygame-ce**.  
The system controls solenoid locks via GPIO and guides the user through triage and emergency instructions.

---

## Features
- Touchscreen UI (optimized for Raspberry Pi)
- Fast rendering with **pygame-ce**
- Solenoid control via **RPi.GPIO**
- Triage screen with yes/no decision flow
- Emergency guides with images
- GSM alerts (SIM800L module)

---

## Requirements
- Python 3.11+
- Raspberry Pi OS (Bookworm recommended)
- Virtual environment (`venv`)

### Install dependencies
```bash
pip install -r requirements.txt
```

## Project Structure
- `main.py` → main entry point
- `code/` → modules (buttons, gpio helper, etc.)
- `images/` → emergency guide assets
- `audio/` → sounds

## Running
```bash
pip install -r requirements.txt
python main.py

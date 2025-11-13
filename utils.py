import threading
import json
import os
import time


try:
    import RPi.GPIO as GPIO
    import serial
    ON_PI = True
except ImportError:
    ON_PI = False


# --- CONFIG ---
CONFIG_FILE = "config/settings.json"
RELAY_PINS = {
    "Sprains and Strains": 5,
    "Nosebleeds": 6,
    "Laceration (Cut)": 13,
    "Insect Bites or Minor Allergic Reactions": 19,
    "Bruise and Contusion": 26,
    "Fainting": 16,
    "Burns (1st or 2nd)": 20,
    "Choking (Partial)": 21,
}


def load_settings():
    try:
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
                number = data.get("number", "").strip()
                location = data.get("location", "").strip()
                return number, location
    except Exception as e:
        print(f"[WARN] Failed to load config: {e}")
    return "", "Unknown Location"

if ON_PI:
    GPIO.setmode(GPIO.BCM)
    for pin in RELAY_PINS.values():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)  # relays default HIGH = off

def trigger_solenoid(injury, duration=6):
    if injury not in RELAY_PINS:
        print(f"[WARN] No relay pin configured for: {injury}")
        return

    pin = RELAY_PINS[injury]
    print(f"[HARDWARE] Unlocking drawer for: {injury}")

    def _activate():
        if ON_PI:
            GPIO.output(pin, GPIO.LOW)
        print(f"[SOLENOID] {injury} -> ON")
        time.sleep(duration)
        if ON_PI:
            GPIO.output(pin, GPIO.HIGH)
        print(f"[SOLENOID] {injury} -> OFF")

    threading.Thread(target=_activate, daemon=True).start()


def send_sms(injury):
    number, location = load_settings()
    if not number:
        print("[SMS] No number configured, skipping send.")
        return

    message = f"Emergency assistance requested for {injury} at {location}"
    print(f"[SMS] To: {number} | Message: '{message}'")

    def _sms():
        if not ON_PI:
            print(f"[SMS MOCK] {message}")
            return

        try:
            sim = serial.Serial("/dev/serial0", 9600, timeout=1)
            time.sleep(0.5)
            sim.write(b'AT\r')
            time.sleep(0.5)
            sim.write(b'AT+CMGF=1\r')
            time.sleep(0.5)
            sim.write(f'AT+CMGS="{number}"\r'.encode())
            time.sleep(0.5)
            sim.write(f"{message}\x1A".encode())  # Ctrl+Z to send
            time.sleep(3)
            sim.close()
            print("[SMS] Sent successfully.")
        except Exception as e:
            print(f"[ERROR] SMS failed: {e}")

    threading.Thread(target=_sms, daemon=True).start()

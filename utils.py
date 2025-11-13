# utils.py
import threading
import pygame
import assets
try:
    import RPi.GPIO as GPIO
    import serial
    ON_PI = True
except ImportError:
    ON_PI = False


# --- CONFIG ---
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
SMS_NUMBER = "+639XXXXXXXXX"  # update number


# --- SETUP ---
if ON_PI:
    GPIO.setmode(GPIO.BCM)
    for pin in RELAY_PINS.values():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)  # relays default HIGH = off


# --- FUNCTIONS ---
def trigger_solenoid(injury, duration=10):
    """Activate the corresponding drawer solenoid."""
    if injury not in RELAY_PINS:
        print(f"[WARN] No relay pin configured for: {injury}")
        return

    pin = RELAY_PINS[injury]
    print(f"[HARDWARE] Unlocking drawer for: {injury}")

    def _activate():
        if ON_PI:
            GPIO.output(pin, GPIO.LOW)
        print(f"[SOLENOID] {injury} -> ON")
        import time
        time.sleep(duration)
        if ON_PI:
            GPIO.output(pin, GPIO.HIGH)
        print(f"[SOLENOID] {injury} -> OFF")

    threading.Thread(target=_activate, daemon=True).start()


def send_sms(injury):
    
    print(f"[SMS] Sending alert for: {injury}")

    def _sms():
        if not ON_PI:
            print(f"[SMS MOCK] Message: '{injury} emergency!' -> {SMS_NUMBER}")
            return

        try:
            sim = serial.Serial("/dev/serial0", 9600, timeout=1)
            sim.write(b'AT\r')
            sim.readline()
            sim.write(b'AT+CMGF=1\r')
            sim.readline()
            cmd = f'AT+CMGS="{SMS_NUMBER}"\r'.encode()
            sim.write(cmd)
            message = f"Emergency: {injury}\r"
            sim.write(message.encode())
            sim.write(bytes([26]))  # Ctrl+Z
            sim.close()
            print("[SMS] Sent successfully.")
        except Exception as e:
            print(f"[ERROR] SMS failed: {e}")

    threading.Thread(target=_sms, daemon=True).start()


# def apply_scaling():
#     """Scales all loaded images in assets.py according to screen resolution."""
#     factor_x, factor_y = assets.scale_x, assets.scale_y

#     def scale_img(img):
#         w, h = img.get_size()
#         return pygame.transform.scale(img, (int(w * factor_x), int(h * factor_y)))

#     # scale main images
#     assets.start_bg = scale_img(assets.start_bg)
#     assets.main_menu_bg = scale_img(assets.main_menu_bg)
#     assets.emergency_menu_bg = scale_img(assets.emergency_menu_bg)

#     # scale buttons
#     assets.emergency_btn_img = scale_img(assets.emergency_btn_img)
#     assets.learning_btn_img = scale_img(assets.learning_btn_img)
#     assets.main_menu_btn_img = scale_img(assets.main_menu_btn_img)
#     assets.emergency_call_btn_img = scale_img(assets.emergency_call_btn_img)
#     assets.emergency_menu_btn_img = scale_img(assets.emergency_menu_btn_img)
#     assets.next_btn_img = scale_img(assets.next_btn_img)
#     assets.back_btn_img = scale_img(assets.back_btn_img)
#     assets.yes_btn_img = scale_img(assets.yes_btn_img)
#     assets.no_btn_img = scale_img(assets.no_btn_img)
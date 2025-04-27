import network
import urequests
import utime
import machine
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# WiFi Credentials
SSID = 'S20FE'
PASSWORD = 'ypme18900'

# LCD Settings
I2C_ADDR = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

# IR Sensor Pin (example: GP2)
IR_SENSOR_PIN = 16

# ThingSpeak Settings
THINGSPEAK_API_KEY = "5F4H5G92LDXGQI1M"
THINGSPEAK_URL = "https://api.thingspeak.com/update"


# Initialize LCD
def init_lcd():
    i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
    lcd.clear()
    return lcd


# Connect to WiFi
def connect_to_wifi(lcd):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)

    lcd.clear()
    lcd.putstr("Connecting WiFi")
    while not wlan.isconnected():
        utime.sleep(0.5)
        lcd.putstr(".")

    lcd.clear()
    lcd.putstr("WiFi Connected")
    print("Connected to WiFi:", wlan.ifconfig())


# Initialize IR Sensor
def init_ir_sensor():
    ir_sensor = machine.Pin(IR_SENSOR_PIN, machine.Pin.IN)
    return ir_sensor


# Send IR Data to ThingSpeak
def send_to_thingspeak(ir_value):
    try:
        payload = {
            "api_key": THINGSPEAK_API_KEY,
            "field1": ir_value
        }
        response = urequests.post(THINGSPEAK_URL, json=payload)
        response.close()
        print("Data sent to ThingSpeak:", ir_value)
    except Exception as e:
        print("Failed to send to ThingSpeak:", e)


# Read IR Sensor and Display
def read_ir_and_display(lcd, ir_sensor):
    lcd.clear()
    ir_value = ir_sensor.value()

    if ir_value == 0:
        lcd.putstr("Object Detected")
        print("Object Detected")
    else:
        lcd.putstr("No Object")
        print("No Object")

    send_to_thingspeak(ir_value)
    utime.sleep(5)  # Small delay to avoid sending too fast


# Main Program
def main():
    lcd = init_lcd()
    connect_to_wifi(lcd)
    ir_sensor = init_ir_sensor()

    while True:
        read_ir_and_display(lcd, ir_sensor)


# Run the program
if __name__ == "__main__":
    main()
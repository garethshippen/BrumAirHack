from time import sleep
import machine
from pms5003 import PMS5003

pms5003 = PMS5003(
    uart=machine.UART(0, tx=machine.Pin(0), rx=machine.Pin(1), baudrate=9600),
    pin_enable=machine.Pin(3),
    pin_reset=machine.Pin(2),
    mode="active"
)


def send():
    data = pms5003.read()
    ultrafine = data.pm_ug_per_m3(1.0)
    combust = data.pm_ug_per_m3(2.5)
    pollen = data.pm_ug_per_m3(10)
    #print(data)
    print("Ultrafine: ", ultrafine)
    print("Combustion: ", combust)
    print("Pollen: ", pollen)
    print()
    sleep(3)

if __name__  == "__main__":
    while True:
        send()

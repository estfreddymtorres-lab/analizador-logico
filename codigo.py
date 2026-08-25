from machine import Pin, UART
import utime

uart = UART(0, baudrate=115200, bits=8, parity=1, stop=1,
            tx=Pin(0), rx=Pin(1))

mensaje = "UMNG_2026_LIDER_EN_TELECOMUNICACIONES"

while True:
    uart.write(mensaje)
    utime.sleep(1)
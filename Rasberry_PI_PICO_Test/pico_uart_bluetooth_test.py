from machine import UART

# Bluetooth Module -> 9600 N 8 1

uart = UART(1, 9600)                         # init with given baudrate
uart.init(9600, bits=8, parity=None, stop=1) # init with given parameters

while True:
    uart.write("Hello");
    sleep(1);
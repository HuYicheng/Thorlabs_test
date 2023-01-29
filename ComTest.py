# -*- coding: utf-8 -*-

import serial
import time

"""
Spyder Editor

This is a temporary script file.
"""


def main():
    # Need to configer the device for serial commands and set the correct COM port
    com = serial.Serial(port='COM3',
                        baudrate=115200,
                        bytesize=8,
                        parity=serial.PARITY_NONE,
                        stopbits=1, xonxoff=0,
                        rtscts=0,
                        timeout=1
                        )

    print(com.is_open)
    com.flushInput()
    com.flushOutput()

    command = bytearray([0x05, 0x00, 0x00, 0x00, 0x01, 0x01])  # identify
    com.write(command)
    com.flushInput()
    com.flushOutput()
    time.sleep(1)

    com.write(bytearray([0x10, 0x02, 0x01, 0x01, 0x21, 0x01]))  # enable
    com.flushInput()
    com.flushOutput()
    time.sleep(1)
    # 0 0 0 0 0 0 0 1 = 0x01
    # 0b100001 = 0x21
    com.write(bytearray([0x10, 0x02, 0x01, 0x02, 0x21, 0x01]))   # 0x02 for disable
    com.flushInput()
    com.flushOutput()
    time.sleep(1)

    com.close()
    print(com.is_open)

    # Rx81, 04, 0E, 00, 81, 50, 01, 00, 00, 00, 00, 00, 00, 00, 00, 00, 01, 20, 00, 00

    # Rx81, 04, 0E, 00, 81, 50, 01, 00, 00, 00, 00, 00, 00, 00, 00, 00, 00, 20, 00, 80
    # Rx81, 04, 0E, 00, 81, 50, 01, 00, 00, 00, 00, 00, 00, 00, 00, 00, 01, 20, 00, 80


main()

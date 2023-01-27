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

    com.close()
    print(com.is_open)


main()

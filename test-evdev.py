#!/usr/bin/env python3

import evdev
from evdev import InputDevice, UInput
import sys


def test_uinput():
    uinput = UInput(
        events={
            1: [272, 325, 328, 330, 333, 334, 335],
            3: [
                [0, [1386, 0, 3679, 0, 0, 31]],
                [1, [995, 0, 2261, 0, 0, 31]],
                [47, [0, 0, 4, 0, 0, 0]],
                [53, [0, 0, 3679, 0, 0, 31]],
                [54, [0, 0, 2261, 0, 0, 31]],
                [55, [0, 0, 2, 0, 0, 0]],
                [57, [0, 0, 65535, 0, 0, 0]]],
            4: [5]
        },
        name="test_touchpad")
    uinput.syn()


def test_input_device():
    _devices = [InputDevice(path) for path in evdev.list_devices()]


def main():
    args = sys.argv
    args.append("")
    match args[1]:
        case "host":
            test_input_device()
        case "guest":
            test_uinput()
        case _:
            test_input_device()
            test_uinput()


if __name__ == "__main__":
    main()


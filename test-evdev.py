#!/usr/bin/env python3

import evdev
import sys
import glob


def test_uinput():
    _uinput = evdev.UInput({}, name="test")


def test_input_device():
    possible_devices = glob.glob("/dev/input/event*")
    devices = evdev.list_devices()
    for device in possible_devices:
        if device not in devices:
            print(f"Missing permissions for {device}")


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


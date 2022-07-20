#!/usr/bin/env python3

from remote_evdev import config, get_streams, handle_client


def main():
    cfg, device_info = config.get_config()
    for stream in get_streams(cfg):
        handle_client(stream, cfg, device_info)


if __name__ == "__main__":
    main()

"""The main entry point. Invoke as `stocks-price-monitor' or `python -m stocks-price-monitor'.
"""
from .argparser import parse_command_line
from .logger import SPMLogger


def main():
    try:
        args = parse_command_line()
        logger = SPMLogger("spm_logger", args.loglevel).logger
        logger.info("Hello World")
    except KeyboardInterrupt:
        print("Exit")
        return 1

    return 0


if __name__ == "__main__":  # pragma: nocover
    import sys

    sys.exit(main())

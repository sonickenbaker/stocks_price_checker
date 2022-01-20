"""The main entry point. Invoke as `stocks-price-monitor' or `python -m stocks-price-monitor'.
"""


def main():
    try:
        print("Hello World")
    except KeyboardInterrupt:
        print("Exit")
        return 1

    return 0


if __name__ == "__main__":  # pragma: nocover
    import sys

    sys.exit(main())

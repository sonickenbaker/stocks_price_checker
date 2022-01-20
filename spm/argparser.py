import argparse


def parse_command_line():
    parser = argparse.ArgumentParser(description="Monitor Stocks Prices")
    parser.add_argument(
        "-s",
        "--stock",
        dest="stock",
        help="stock to monitor",
        default=None,
        required=True,
    )
    parser.add_argument(
        "--desired-price",
        dest="desired_price",
        default=None,
        help="If current stock price <= desired price an alert is sent",
        required=True,
    )
    parser.add_argument(
        "--dry-run",
        dest="dry_run",
        action="store_true",
        help="Perform a dry-run",
        required=False,
    )
    parser.add_argument(
        "-l",
        "--loglevel",
        dest="loglevel",
        default="INFO",
        help="Log level verbosity (default: INFO)",
    )
    return parser.parse_args()

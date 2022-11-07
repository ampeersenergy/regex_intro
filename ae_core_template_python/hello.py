"""
Module doc string ...

Don't put author names or created/edited timestamps in here, we have git for that!
"""

import argparse

from settings import Settings


def main():
    """Main function

    Always define a main function to avoid polluting the module namespace.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-N", default=1, type=int, help="Print hello message N times.")
    args = parser.parse_args()

    for _ in range(args.N):
        hello_AE()

    settings = Settings()
    # Never print secrets ... this is just for demonstrating how the decouple package works
    print(f"Your secret key: {settings.secret_key}")


def hello_AE():
    print(r"Hello Ampeers Energy")


if __name__ == "__main__":
    main()

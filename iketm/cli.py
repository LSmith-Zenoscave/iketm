"""Console script for iketm."""

import fire
from .iketm import IkeTM


def main():
    fire.Fire(IkeTM)


if __name__ == "__main__":
    main()  # pragma: no cover

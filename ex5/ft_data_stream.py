"""Exercise 5: Stream Wizard.

Authorized: next(), range(), len(), print(), import typing,
typing.Generator, import random, random.*
"""

import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    """Yield endless (player, action) events picked at random."""


def consume_event(
    events: list[tuple[str, str]],
) -> typing.Generator[tuple[str, str], None, None]:
    """Yield and remove a random event from the list until it is empty."""


def main() -> None:
    """Produce a stream of events, then consume a list of them."""


if __name__ == "__main__":
    main()

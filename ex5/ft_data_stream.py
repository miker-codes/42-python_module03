#!/usr/bin/env python3


import typing
import random


PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = ["run", "eat", "sleep", "grab", "move",
                      "climb", "swim", "use", "release"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def main() -> None:
    print("=== Game Data Stream Processor ===")
    events = gen_event()
    for i in range(1000):
        name, action = next(events)
        print(f"Event {i}: Player {name} did action {action}")


if __name__ == "__main__":
    main()

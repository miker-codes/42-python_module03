#!/usr/bin/env python3


import typing
import random


PLAYERS: list[str] = ["alice", "bob", "charlie", "dylan"]
ACTIONS: list[str] = ["run", "eat", "sleep", "grab", "move",
                      "climb", "swim", "use", "release"]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
    pool: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(pool) > 0:
        index = random.randint(0, len(pool) - 1)
        yield pool.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")
    events = gen_event()
    for i in range(1000):
        name, action = next(events)
        print(f"Event {i}: Player {name} did action {action}")
    # Now we generate the list of 10 events
    event_list: list[tuple[str, str]] = []
    for i in range(10):
        event_list.append(next(events))
    print(f"Built list of 10 events: {event_list}")
    # Now we consume an event and iterate until the list is empty
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()

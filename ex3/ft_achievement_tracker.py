#!/usr/bin/env python3


import random


ACHIEVEMENTS: list[str] = [
    "First Steps",
    "Speed Runner",
    "Treasure Hunter",
    "Boss Slayer",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Survivor",
    "Strategist",
    "Crafting Genius",
    "World Savior",
    "Unstoppable",
    "Sharp Mind",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    count = random.randint(5, 9)
    return set(random.sample(ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===")
    print()
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print()
    all_distinct = alice.union(bob, charlie, dylan)
    print(f"All distinct achievements: {all_distinct}")
    print()
    common = alice.intersection(bob, charlie, dylan)
    print(f"Common achievements: {common}")
    print()
    print(f"Only Alice has: {alice.difference(bob.union(charlie, dylan))}")
    print(f"Only Bob has: {bob.difference(alice.union(charlie, dylan))}")
    print(f"Only Charlie has: {charlie.difference(alice.union(bob, dylan))}")
    print(f"Only Dylan has: {dylan.difference(alice.union(bob, charlie))}")
    print()
    full = set(ACHIEVEMENTS)
    print(f"Alice is missing: {full.difference(alice)}")
    print(f"Bob is missing: {full.difference(bob)}")
    print(f"Charlie is missing: {full.difference(charlie)}")
    print(f"Dylan is missing: {full.difference(dylan)}")


if __name__ == "__main__":
    main()

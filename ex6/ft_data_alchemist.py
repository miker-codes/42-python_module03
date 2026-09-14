#!/usr/bin/env python3


import random


players = ["Alice", "bob", "Charlie", "dylan", "Emma",
           "Gregory", "john", "kevin", "Liam"]


def main() -> None:
    print("=== Game Data Alchemist ===")
    print()
    print(f"Initial list of players: {players}")
    players_capitalized = [player.capitalize() for player in players]
    print(f"New list with all names capitalized: {players_capitalized}")
    players_cap = [player for player in players if player[0].isupper()]
    print(f"New list of capitalized names only: {players_cap}")
    # Now we build the dicts
    scores = {name: random.randint(1, 1000) for name in players_capitalized}
    print(f"Score dict: {scores}")
    average = sum(scores.values()) / len(scores)
    print(f"Score average is {round(average, 2)}")
    high_scores = {name: scores[name] for name in scores
                   if scores[name] > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()

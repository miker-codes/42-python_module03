#!/usr/bin/env python3


import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    usage = (
        f"No scores provided. Usage: python3 {sys.argv[0]} "
        f"<score1> <score2> ..."
    )
    if len(sys.argv) < 2:
        print(usage)
    else:
        scores = []
        for i in range(1, len(sys.argv)):
            try:
                scores.append(int(sys.argv[i]))
            except ValueError:
                print(f"Invalid parameter: '{sys.argv[i]}'")
        if not scores:
            print(usage)
        else:
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()

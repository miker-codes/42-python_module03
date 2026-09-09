#!/usr/bin/env python3


import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    if len(sys.argv) < 2:
        print("No arguments provided!")
    else:
        arguments = []
        for i in range(1, len(sys.argv)):
            arguments.append(f"Argument {i}: {sys.argv[i]}")
        print(f"Arguments received: {len(arguments)}")
        for i in range(len(arguments)):
            print(f"{arguments[i]}")
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()

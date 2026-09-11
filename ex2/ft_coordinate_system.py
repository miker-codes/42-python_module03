#!/usr/bin/env python3


import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coordinates = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        )
        parts = coordinates.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        coords = []
        for part in parts:
            try:
                coords.append(float(part.strip()))
            except ValueError as e:
                print(f"Error on parameter '{part.strip()}': {e}")
                break
        else:
            return (coords[0], coords[1], coords[2])


def get_distance(a: tuple[float, float, float],
                 b: tuple[float, float, float]) -> float:
    return math.sqrt((b[0] - a[0])**2
                     + (b[1] - a[1])**2
                     + (b[2] - a[2])**2)


def main() -> None:
    print("=== Game Coordinate System ===")
    print()

    print("Get a first set of coordinates")
    coords_tuple = get_player_pos()
    x, y, z = coords_tuple
    print(f"Got a first tuple: {coords_tuple}")
    print(f"It includes: X={x}, Y={y}, Z={z}")
    distance_center = get_distance(coords_tuple, (0.0, 0.0, 0.0))
    print(f"Distance to center: {round(distance_center, 4)}")
    print()

    print("Get a second set of coordinates")
    coords_tuple2 = get_player_pos()
    distance = get_distance(coords_tuple, coords_tuple2)
    print(f"Distance between the 2 sets of coordinates: {round(distance, 4)}")


if __name__ == "__main__":
    main()

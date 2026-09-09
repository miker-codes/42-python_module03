#!/usr/bin/env python3


import math


def get_player_pos() -> None:
    while True:
        coordinates = input("Enter new coordinates as floats in format 'x,y,z": )
        parts = coordinates.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue
        for part in parts:
            try:
                value = float(part.strip())
            except ValueError as e:
                print(f"Error on parameter '{part.strip()}': {e}")
        
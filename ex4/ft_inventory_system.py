#!/usr/bin/env python3


import sys


def main() -> None:
    print("=== Inventory System Analysis ===")
    if len(sys.argv) < 2:
        print("No arguments provided!")
    else:
        inventory: dict[str, int] = {}
        for i in range(1, len(sys.argv)):
            parts = sys.argv[i].split(":")
            if len(parts) != 2:
                print(f"Error - invalid parameter '{sys.argv[i]}'")
                continue
            try:
                quantity = int(parts[1])
            except ValueError as e:
                print(f"Quantity error for '{parts[0]}': {e}")
                continue
            if parts[0] in inventory:
                print(f"Redundant item '{parts[0]}' - discarding")
                continue
            inventory[parts[0]] = quantity

        print(f"Got inventory: {inventory}")
        if len(inventory) == 0:
            print("Empty inventory - nothing to analyze")
            return
        item_list = list(inventory.keys())
        print(f"Item list: {item_list}")
        total = sum(inventory.values())
        print(f"Total quantity of the {len(inventory)} items: {total}")
        for item in inventory:
            percentage = round(inventory[item] / total * 100, 1)
            print(f"Item {item} represents {percentage}%")
        most_item = item_list[0]
        least_item = item_list[0]
        for item in inventory:
            if inventory[item] > inventory[most_item]:
                most_item = item
            if inventory[item] < inventory[least_item]:
                least_item = item
        most_qty = inventory[most_item]
        least_qty = inventory[least_item]
        print(f"Item most abundant: {most_item} with quantity {most_qty}")
        print(f"Item least abundant: {least_item} with quantity {least_qty}")
        inventory.update({"magic_item": 1})
        print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()

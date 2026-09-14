# 42 - Python Module03

Project done for the 42 Malaga curriculum by **mruiz-ra**.

## About

This is **Data Quest**, the fourth Python project of the 42 core curriculum. It builds the components of a game analytics platform using Python's collection types, starting from the list that `sys.argv` already hands you and progressing through tuples, sets, dictionaries, generators and comprehensions. Each exercise unlocks a new data structure and reuses the ideas built in the previous ones.

## Structure

```
.
├── ex0/
│   └── ft_command_quest.py
├── ex1/
│   └── ft_score_analytics.py
├── ex2/
│   └── ft_coordinate_system.py
├── ex3/
│   └── ft_achievement_tracker.py
├── ex4/
│   └── ft_inventory_system.py
├── ex5/
│   └── ft_data_stream.py
└── ex6/
    └── ft_data_alchemist.py
```

## Exercises

| # | File | Concept | Description |
|---|------|---------|-------------|
| 00 | `ft_command_quest.py` | Lists via `sys.argv` | First contact with lists, using one that already exists: the command line parameters exposed by the `sys` module. The script prints the program name, the number of arguments received and each argument individually, handling the case where no arguments are provided at all. Slicing is what keeps the program name out of the argument listing. |
| 01 | `ft_score_analytics.py` | Building lists + `try/except` | Game scores arrive as command line parameters. Each one is converted inside a `try/except` so a non numeric value is reported and discarded instead of crashing the program, and the survivors are collected into a new list. From that list the script computes the player count, total, average, high score, low score and range, falling back to a usage message when no valid score remains. |
| 02 | `ft_coordinate_system.py` | Tuples | `get_player_pos()` asks for 3D coordinates in `x,y,z` format and retries until the input is valid, rejecting both a wrong number of fields (invalid syntax) and non numeric fields (caught `ValueError`), then returns them as a `tuple[float, float, float]`. A `for/else` drives the retry: a failed conversion `break`s out and reprompts, while a clean pass falls into the `else` and returns. `get_distance()` applies the Euclidean formula to two points, which covers both the distance to the origin `(0.0, 0.0, 0.0)` and the distance between the two sets of coordinates. |
| 03 | `ft_achievement_tracker.py` | Sets | `gen_player_achievements()` picks a random count with `random.randint()` and draws that many distinct achievements from a fixed catalogue with `random.sample()`, returning a `set[str]`. Four players are generated, then `union()` gives every achievement in play, `intersection()` the ones everybody shares, and `difference()` both the achievements unique to each player (player minus the union of the others) and the ones each player still needs (full catalogue minus the player). Order matters for `difference()` but not for the other two. |
| 04 | `ft_inventory_system.py` | Dictionaries | Command line parameters follow the `<item_name>:<quantity>` format and are parsed into a `dict[str, int]`. Three separate error cases are reported and skipped: a missing or extra colon, a quantity that is not an integer, and an item name already present in the inventory. The analysis then displays the inventory, the item list from `list(dict.keys())`, the total from `sum(dict.values())`, the percentage each item represents, and the most and least abundant items, tracked with strict comparisons so the first item from the command line wins a tie. An empty inventory is treated as a valid state and short circuits the analysis instead of dividing by zero. Finally `dict.update()` adds a new item and the inventory is displayed again. |
| 05 | `ft_data_stream.py` | Generators | `gen_event()` is an endless generator: a `while True` loop that `yield`s a `(name, action)` tuple built from `random.choice()` on two fixed lists. Because a generator suspends at each `yield` and resumes on the next request, the infinite loop never blocks anything. The main part pulls 1000 events with `next()`, then collects ten more into a list. `consume_event()` is a second generator that takes that list, pops a random element with `list.pop(index)` and yields it until the list is empty, and it is consumed directly in a `for .. in ..` construct, which handles the `StopIteration` for you. Since the list is passed by reference, the caller watches it shrink as it is drained. |
| 06 | `ft_data_alchemist.py` | Comprehensions | Two list comprehensions over a list of mixed case player names: one transforms every name with `str.capitalize()`, the other filters with a trailing `if` on `name[0].isupper()` to keep only the names that were already capitalized. A dict comprehension then maps every capitalized name to a random score, and a second one filters that dictionary down to the scores above the average. The filtering `if` at the end of a comprehension decides whether an element is included at all, which is a different thing from a ternary placed before the `for`. |

## Testing

Every exercise file can be run directly:

```bash
python3 ex2/ft_coordinate_system.py
```

The exercises taking command line parameters are run like this:

```bash
python3 ex1/ft_score_analytics.py 1500 2300 1800 2100 1950
python3 ex4/ft_inventory_system.py sword:1 potion:5 shield:2 armor:3
```

## Style

Every file respects **flake8** (PEP8) and **mypy** for type hints:

```bash
flake8 exX/file.py
mypy exX/file.py
```

> Note: "La Norme" from the C projects does not apply here, this is a pure Python project with its own rules defined in the subject.

No file I/O is used anywhere in the project, as required by the subject: all data is processed in memory or comes from command line arguments.

## Key concepts covered

- Lists: `sys.argv`, slicing, building and iterating
- Tuples: immutability, unpacking into separate variables, returning several values at once
- Sets: uniqueness, `union()`, `intersection()`, `difference()`, and why `set()` prints instead of `{}`
- Dictionaries: key/value storage, `in` for key lookup, `keys()` and `values()` views versus `list()` snapshots, `update()`
- Generators: `yield`, lazy evaluation, `next()`, endless and finite generators, `StopIteration` handled by `for`
- List and dictionary comprehensions, including the filtering `if`
- Graceful error handling on every input path, with `try/except` around each conversion
from typing import NewType, Dict, Union, NamedTuple
import re


class Set:
    def __init__(self):
        self.red = self.green = self.blue = 0


class Game:
    def __init__(self, game_num, sets):
        self.game_num = game_num
        self.sets = sets


def format_raw_set(raw_set: str) -> Set:
    formatted_set = Set()

    for raw_set_group in raw_set.split(', '):
        [value, key] = raw_set_group.split(' ')
        if key == 'red':
            formatted_set.red = int(value)
        elif key == 'green':
            formatted_set.green = int(value)
        else:
            formatted_set.blue = int(value)

    return formatted_set


def format_raw(raw: str) -> Game:
    [game_str, sets_str] = raw.split(': ')
    sets_str = sets_str.split('; ')

    game_num = re.search(r'Game (\d+)', game_str)
    assert game_num is not None

    sets = list(map(format_raw_set, sets_str))

    return Game(int(game_num.group(1)), sets)


def process_games(filename: str) -> list[Game]:
    with open(filename, encoding="utf-8") as f:
        raw = list(filter(None, f.read().split("\n")))
    return list(map(format_raw, raw))


def get_power_of_game(game: Game) -> int:
    fewest = Set()

    for set in game.sets:
        if set.red > fewest.red:
            fewest.red = set.red
        if set.green > fewest.green:
            fewest.green = set.green
        if set.blue > fewest.blue:
            fewest.blue = set.blue

    return max(fewest.red, 1) * max(fewest.green, 1) * max(fewest.blue, 1)


def main(filename: str) -> int:
    processed_games = process_games(filename)

    sum = 0
    for processed_game in processed_games:
        sum += get_power_of_game(processed_game)
    return sum


if __name__ == "__main__":
    print("---Example----")
    print(main("example.txt"))
    
    print("---Input--")
    print(main("input.txt"))

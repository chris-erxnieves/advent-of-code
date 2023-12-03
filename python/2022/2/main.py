from enum import Enum

class ShapePoints(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


class OutcomePoints(Enum):
    Win = 6
    Draw = 3
    Loss = 0


def part_one(filename: str):
    rounds = process_rounds(filename)
    score = 0
    for round in rounds:
        score += get_round_points(round)
    return score


def part_two(filename: str):
    rounds = process_rounds(filename)
    score = 0
    for round in rounds:
        score += get_round_points(round)
    return score


def map_shape(shape: str):
    match shape:
        case 'A':
            return 'Rock'
        case 'B':
            return 'Paper'
        case 'C':
            return 'Scissors'
        case 'X':
            return 'Lose'
        case 'Y':
            return 'Draw'
        case _:
            return 'Win'


def map_round(round: str) -> list[str]:
    arr = round.strip().split(" ")

    return list(map(map_shape, arr))
    

def process_rounds(filename: str) -> list[list[str]]:
    with open(filename, encoding="utf-8") as f:
        rounds = filter(None, f.read().split("\n"))

    return list(map(map_round, rounds))


def get_round_points(shapes: list[str]):
    round_points = 0
    their_shape = shapes[0]
    desired_outcome = shapes[1]

    match desired_outcome:
        case OutcomePoints.Win.name:
            round_points += OutcomePoints.Win.value
            match their_shape:
                case ShapePoints.Scissors.name:
                    round_points += ShapePoints.Rock.value
                case ShapePoints.Rock.name:
                    round_points += ShapePoints.Paper.value
                case _:
                    round_points += ShapePoints.Scissors.value
        case OutcomePoints.Loss.name:
            match their_shape:
                case ShapePoints.Scissors.name:
                    round_points += ShapePoints.Paper.value
                case ShapePoints.Rock.name:
                    round_points += ShapePoints.Scissors.value
                case _:
                        round_points += ShapePoints.Rock.value
        case _:
            round_points += OutcomePoints.Draw.value
            match their_shape:
                case ShapePoints.Scissors.name:
                    round_points += ShapePoints.Scissors.value
                case ShapePoints.Rock.name:
                    round_points += ShapePoints.Rock.value
                case _:
                    round_points += ShapePoints.Paper.value

    return round_points


if __name__ == "__main__":
    input_path = "input.txt"

    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))

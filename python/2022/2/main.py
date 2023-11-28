move_dict = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

def part_one(filename: str) -> int:
    score = 0
    rounds = process_rounds(filename)
    return 0


def part_two(filename: str) -> int:
    return 0


def process_rounds(filename: str) -> list[list[str]]:
    with open(filename, encoding="utf-8") as f:
        rounds = f.read().split("\n")
    return [list(r.strip().split(" ")) for r in rounds]


if __name__ == "__main__":
    input_path = "example.txt"

    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))

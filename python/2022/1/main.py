def part_one(filename: str) -> int:
    highest_calories = 0

    for elf in process_calories(filename):
        calories = sum(elf)

        if calories > highest_calories:
            highest_calories = calories

    return highest_calories


def part_two(filename: str) -> int:
    return sum(
        sorted(
            list(map(sum, process_calories(filename))),
            reverse=True
        )[0:3]
    )


def process_calories(filename: str) -> list[list[int]]:
    with open(filename, encoding="utf-8") as f:
        elves = f.read().split("\n\n")
    return [list(map(int, elf.strip().split("\n"))) for elf in elves]


if __name__ == "__main__":
    input_path = "input.txt"

    print("---Part One---")
    print(part_one(input_path))

    print("---Part Two---")
    print(part_two(input_path))

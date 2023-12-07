def process_eggs(filename: str) -> list[str]:
    with open(filename, encoding="utf-8") as f:
        return list(filter(None, f.read().splitlines()))


def main(filename: str) -> int:
    spam = process_eggs(filename)
    
    return 0


if __name__ == "__main__":
    print("---Example----")
    print(main("example.txt"))
    
    print("---Input--")
    print(main("input.txt"))

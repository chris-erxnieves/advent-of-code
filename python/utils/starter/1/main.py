def eggs(filename: str) -> list[str]:
    with open(filename, encoding="utf-8") as f:
        return list(filter(None, f.read().split("\n")))


def main(filename: str) -> int:
    spam = eggs(filename)
    
    return 0


if __name__ == "__main__":
    print("---Example----")
    print(main("example.txt"))
    
    print("---Input--")
    print(main("input.txt"))

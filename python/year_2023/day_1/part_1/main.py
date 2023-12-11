import os


def process_calibration_words(filename: str) -> list[str]:
    with open(os.path.join(os.path.dirname(__file__), filename), encoding="utf-8") as f:
        return list(filter(None, f.read().split("\n")))


def get_calibration_value(calibrationWord: str) -> int:
    first, last = None, None

    for letter in calibrationWord:
        if letter.isdigit():
            if first is None:
                first = letter
            last = letter

    return int("%s%s" % (first, last))

def main(filename: str) -> int:
    calibrationWords = process_calibration_words(filename)
    
    return sum(map(get_calibration_value, calibrationWords))



if __name__ == "__main__":
    print("---Example---")
    print(main("example.txt"))
    
    print("---Input---")
    print(main("input.txt"))

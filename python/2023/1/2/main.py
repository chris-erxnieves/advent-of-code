words = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

def process_calibration_words(filename: str) -> list[str]:
    with open(filename, encoding="utf-8") as f:
        return list(filter(None, f.read().split("\n")))


def get_calibration_value(calibrationWord: str) -> int:
    first, last = None, None

    for i, letter in enumerate(calibrationWord):
        if letter.isdigit():
            if first is None:
                first = letter
            last = letter
        else:
            num = None
            subStr = calibrationWord[0:i+1]
            for key, value in words.items():
                if subStr.endswith(key):
                    num = value
                    break

            if num is not None:
                if first is None:
                    first = num
                last = num

    return int("%s%s" % (first, last))

def main(filename: str) -> int:
    calibrationWords = process_calibration_words(filename)
    
    return sum(map(get_calibration_value, calibrationWords))



if __name__ == "__main__":
    print("---Example----")
    print(main("example.txt"))
    
    print("---Input--")
    print(main("input.txt"))

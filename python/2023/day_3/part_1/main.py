class PartNumberInfo:
    def __init__(self, value, x_from, x_to, y):
        self.value = value
        self.x_from = x_from
        self.x_to = x_to
        self.y = y


class SymbolLocations:
    def __init__(self):
        self.__symbol_map = {}

    def add_location(self, x, y):
        if y not in self.__symbol_map:
            self.__symbol_map[y] = {}
        self.__symbol_map[y][x] = True

    def is_at_location(self, x, y):
        return y in self.__symbol_map and x in self.__symbol_map[y]

    def clear(self):
        self.__symbol_map.clear()


possible_part_numbers: list[PartNumberInfo] = []
symbol_locations = SymbolLocations()
max_x_index = None
max_y_index = None


def process_engine_schematic(filename: str) -> list[str]:
    with open(filename, encoding="utf-8") as f:
        return list(filter(None, f.read().splitlines()))


def build_data(engine_schematic: list[str]):
    global max_x_index, max_y_index, possible_part_numbers, symbol_locations
    max_x_index = len(engine_schematic[0]) - 1
    max_y_index = len(engine_schematic) - 1

    for lineIndex, line in enumerate(engine_schematic):
        temp_str = ""
        for charIndex, char in enumerate(line):
            if char.isdigit():
                temp_str += char
            else:
                if char != ".":
                    symbol_locations.add_location(x=charIndex, y=lineIndex)
                if len(temp_str) > 0:
                    possible_part_numbers.append(
                        PartNumberInfo(
                            value=int(temp_str),
                            x_from=charIndex - len(temp_str),
                            x_to=charIndex - 1,
                            y=lineIndex,
                        )
                    )
                    temp_str = ""


def get_part_number(part_number) -> int:
    global max_x_index, max_y_index, symbol_locations

    x_range = range(
        max(part_number.x_from - 1, 0), min(part_number.x_to + 1, max_x_index) + 1
    )

    # Check left
    if part_number.x_from > 0 and symbol_locations.is_at_location(
        x=part_number.x_from - 1, y=part_number.y
    ):
        return part_number.value

    # Check right
    if part_number.x_to < max_x_index and symbol_locations.is_at_location(
        x=part_number.x_to + 1, y=part_number.y
    ):
        return part_number.value

    # Check above (including diagonal)
    if part_number.y > 0:
        for x in x_range:
            if symbol_locations.is_at_location(x=x, y=part_number.y - 1):
                return part_number.value

    # Check below (including diagonal)
    if part_number.y < max_y_index:
        for x in x_range:
            if symbol_locations.is_at_location(x=x, y=part_number.y + 1):
                return part_number.value

    return 0


def reset_global_data():
    global max_x_index, max_y_index, possible_part_numbers, symbol_locations
    max_x_index = max_y_index = None
    possible_part_numbers.clear()
    symbol_locations.clear()


def main(filename: str) -> int:
    global possible_part_numbers

    engine_schematic = process_engine_schematic(filename)
    build_data(engine_schematic)

    return sum(map(get_part_number, possible_part_numbers))


if __name__ == "__main__":
    print("---Example---")
    print(main("example.txt"))

    reset_global_data()

    print("---Input---")
    print(main("input.txt"))

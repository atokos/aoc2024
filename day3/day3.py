import pathlib
import sys
import re

def part_1(input):
    search_results = re.findall("(?:mul\((\d{1,3},\d{1,3})\))", input)
    return sum(mult(instruction) for instruction in search_results)

def mult(instruction):
    factors = instruction.split(",")
    return int(factors[0]) * int(factors[1])

def part_2(input):
    regex = "(?:mul\((\d{1,3},\d{1,3})\))|(don't\(\))|(do\(\))"
    search_results = re.findall(regex, input)
    
    results = []
    for match in search_results:
        for i in range(3):
            if match[i] != '': results.append(match[i])

    is_enabled = True
    total = 0
    for instruction in results:
        if (instruction == "don't()"):
            is_enabled = False
        elif (instruction == "do()"):
            is_enabled = True
        elif (is_enabled):
            total += mult(instruction)
    return total

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        input = pathlib.Path(path).read_text().strip()

        print("Part 1: ", part_1(input))
        print("Part 2: ", part_2(input))
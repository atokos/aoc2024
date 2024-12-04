import pathlib
import sys

def parse(input):
    numbers = []
    for line in input.splitlines():
        numbers.append([int(number) for number in line.split()])
    return numbers

def part_1(report):
    return safe(report)

def part_2(report):
    if safe(report):
        return True
    for i in range(len(report)):
        if safe(report[:i] + report[i+1:]):
            return True
    return False

def safe(report):
    diffs = [abs(x1 - x2) for x1, x2 in zip(report, report[1:])]
    if not all(1 <= d <= 3 for d in diffs):
        return False
    if all(x1 < x2 for x1, x2 in zip(report, report[1:])):
        return True
    if all(x1 > x2 for x1, x2 in zip(report, report[1:])):
        return True
    return False
    
if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        input = pathlib.Path(path).read_text().strip()

        reports = parse(input)
        print("Results:")
        print("Part 1: ", len([report for report in reports if part_1(report)]))
        print("Part 1: ", len([report for report in reports if part_2(report)]))
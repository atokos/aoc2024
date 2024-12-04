import pathlib
import sys

def parse(input):
    return [int(line) for line in input.split()]

def part_1(numbers):
    list1 = []
    list2 = []
    total_distance = 0

    for i in range(len(numbers)):
        if i % 2 == 0:
            list1.append(numbers[i])
        else:
            list2.append(numbers[i])
    
    list1.sort()
    list2.sort()

    for i in range(len(list1)):
        total_distance += abs(list1[i] - list2[i])

    return total_distance

def part_2(numbers):
    list1 = []
    list2 = []
    similarity_score = 0

    for i in range(len(numbers)):
        if i % 2 == 0:
            list1.append(numbers[i])
        else:
            list2.append(numbers[i])
    for number1 in list1:
        matches = 0
        for number2 in list2:
            if number1 == number2:
                matches += 1
        similarity_score += number1 * matches
    
    return similarity_score

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        input = pathlib.Path(path).read_text().strip()

        numbers = parse(input)
        # print(part_1(numbers))
        print(part_2(numbers))
import datetime
from timeit import default_timer as timer

if __name__ == '__main__':
    SUM = 2020
    inputData = []
    record = dict()
    with open('reportRepairInput') as f:
        for line in f:
            inputData.append(int(line.strip()))
print("Part 1")
start = timer()
for value in inputData:
    if value in record.values():

        print("Found the two values that add up to: ", SUM, " value 1: ", value, "value 2:", SUM - value)
        print("Answer: ", value * (SUM - value))
    else:
        record[value] = SUM - value
end = timer()
print("Time taken: ", end - start, "\n\n")

print("Part 2 Brute force")
solution = 1
start = timer()
for value1 in inputData:
    if solution:
        for value2 in inputData:
            if solution:
                for value3 in inputData:
                    if value1 + value2 + value3 == SUM:
                        print("Found the three values that add up to: ", SUM, " value 1: ", value1, "value 2:", value2,
                              "value 3:", value3)
                        print("Answer:", value1 * value2 * value3)
                        solution = 0
                        break
end = timer()
print("Time taken: ", end - start, "\n\n")

print("Part 2: Optimized 1")
start = timer()
intermediateDict = dict()
values = []
for value1 in inputData:
    for value2 in inputData:
        # intermediateDict[value1 * value2] = SUM - value1 - value2
        intermediateDict[SUM - value1 - value2] = value1 * value2

for value in inputData:
    if value in intermediateDict.keys():
        values.append(value)
        print("Answer:", value * intermediateDict[value])
print(values)
end = timer()
print("Time taken: ", end - start, "\n\n")

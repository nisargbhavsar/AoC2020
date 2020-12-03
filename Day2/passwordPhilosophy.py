from timeit import default_timer as timer

if __name__ == '__main__':
    passwords = dict()
    with open('passwordPhilosophyInput') as f:
        for line in f:
            (first, second, password) = line.split()
            (minNum, maxNum) = first.split('-')
            passwords[password] = [int(minNum), int(maxNum), second[0]]

print("Part 1")
start = timer()
valid = 0
for password in passwords:
    character = passwords[password][2]
    minOccurrences = passwords[password][0]
    maxOccurrences = passwords[password][1]
    numChar = password.count(passwords[password][2])
    if minOccurrences <= numChar <= maxOccurrences:
        valid += 1
print("Valid passwords: ", valid)
end = timer()
print("Time taken: ", end - start, "\n\n")

print("Part 2")
valid = 0
start = timer()
for password in passwords:
    character = passwords[password][2]
    firstIndex = passwords[password][0]
    secondIndex = passwords[password][1]

    firstIndexValid = password[firstIndex - 1] == character
    secondIndexValid = password[secondIndex - 1] == character
    if firstIndexValid ^ secondIndexValid:
        valid += 1
print("Valid passwords: ", valid)
end = timer()
print("Time taken: ", end - start, "\n\n")
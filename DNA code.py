line = input()
counter = 1

for letter in range(len(line) - 1):

    if line[letter] == line[letter + 1]:
        counter += 1

    else:
        print(line[letter] + str(counter), end='')
        counter = 1

print(line[-1] + str(counter), end='')

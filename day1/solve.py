def runPart1():
    left, right = get_columns()
    sorted_left = sorted(left)
    sorted_right = sorted(right)

    difference = 0
    for i in range(len(left)):
        left_i = sorted_left[i]
        right_i = sorted_right[i]
        max_i = max(left_i, right_i)
        min_i = min(left_i, right_i)
        difference += max_i - min_i
    print(difference)

def runPart2():
    left, right = get_columns()
    right_count = {}
    for i in right:
        if right_count.get(i) == None:
            right_count[i] = 1
        else:
            right_count[i] += 1

    counter = 0
    for i in left:
        counter += i * right_count.get(i, 0)

    print(counter)

def get_columns():
    left = []
    right = []
    with open("input.txt", "r") as file:
        for line in file:
            x, y = line.split()
            left.append(int(x))
            right.append(int(y))
    return left, right

runPart2()
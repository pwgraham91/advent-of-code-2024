def run():
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

def get_columns():
    left = []
    right = []
    with open("input1.txt", "r") as file:
        for line in file:
            x, y = line.split()
            left.append(int(x))
            right.append(int(y))
    return left, right

run()
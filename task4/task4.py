nums = []
optimal = 0

def open_file(filename):
    with open(filename, 'r') as f:
        content = f.readlines()

    for line in content:
        nums.append(int(line))

def find_optimal_steps(median):
    global optimal

    for num in nums:
        optimal += abs(num - median)

def main():
    open_file("task4_1.txt")
    #open_file("task4_2.txt")

    nums.sort()
    median = nums[int(len(nums)/2)]

    find_optimal_steps(median)

    if optimal <= 20:
        print("Минимальное количество ходов: ", optimal)
    else:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")


main()




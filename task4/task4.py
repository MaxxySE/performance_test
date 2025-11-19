import sys

optimal = 0

def read_file(filename):

    nums = []

    with open(filename, 'r') as f:
        content = f.readlines()

    for line in content:
        nums.append(int(line.strip()))

    return nums

def find_optimal_steps(nums, median):
    global optimal

    for num in nums:
        optimal += abs(num - median)

def main():
    if len(sys.argv) < 2:
        print("Укажите путь к файлу как аргумент")
        return

    filename = sys.argv[1]
    nums = read_file(filename)

    if not nums:
        print("Файл пуст")
        return

    nums.sort()
    median = nums[len(nums) // 2]

    find_optimal_steps(nums, median)

    if optimal <= 20:
        print("Минимальное количество ходов: ", optimal)
    else:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")


main()




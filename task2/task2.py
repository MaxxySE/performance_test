import sys


def main():

    if len(sys.argv) != 3:
        print("Нужно ввести два аргумента.")
        return

    ellipse = get_file_nums(sys.argv[1])
    points = get_file_nums(sys.argv[2])

    if len(ellipse) < 2:
        print("Файл с параметрами эллипса некорректен.")
        return

    summary_list = get_summary_list(ellipse, points)
    results = get_results(summary_list)

    for result in results:
        print(result)

def get_file_nums(filename):

    nums = {}

    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            if line.strip():
                nums[i] = list(map(float, line.split()))

    return nums

def get_summary_list(ellipse, points):

    summary_list = []

    center = ellipse[0]
    center_x = center[0]
    center_y = center[1]

    radius = ellipse[1]
    radius_x = radius[0]
    radius_y = radius[1]

    for point in points:
        summary = ((((points[point][0] - center_x) ** 2)/radius_x ** 2) +
                   (((points[point][1] - center_y) ** 2) / radius_y ** 2))
        summary_list.append(summary)

    return summary_list

def get_results(summary_list):
    results = []

    for summary in summary_list:
        if summary == 1:
            results.append(0)
        elif summary < 1:
            results.append(1)
        elif summary > 1:
            results.append(2)

    return results


main()
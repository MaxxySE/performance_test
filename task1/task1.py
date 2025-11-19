from threading import Thread

elements = {}
results = {}

def main():
    k = 0

    while True:
        print("Type 3 to Start Program")
        print("Or press enter to continue")
        s = input()

        if s == '3':
            break

        arr = []

        n = int(input("n = "))
        m = int(input("m = "))

        for i in range(1,n+1):
            arr.append(i)

        elements[k] = arr, m
        k += 1

    threads_creation()

    final_result = ""

    for result in results:
        final_result += str(results[result])

    print("\n", final_result)

def threads_creation():
    active_threads = []

    for i in elements:
        thread = Thread(target=count_route, args=(elements[i][0], elements[i][1], i))
        thread.start()
        active_threads.append(thread)

    for t in active_threads:
        t.join()

# Изначально была идея с автоматическим увеличением массива, но в этом случае была бы утечка памяти в особых
# стуациях
# def count_route(arr, m):
#     k = 0
#     res = ""
#     for j in arr:
#         res += str(arr[k])
#         k += m - 1
#         if k >= len(arr):
#             arr += arr
#         if arr[k] == 1:
#             break
#     print(res)

# Сейчас же просто бегаем по остатку не создавая утечек

def count_route(arr, m, i):
    current_index = 0
    res = ""

    while True:
        res += str(arr[current_index])
        current_index = (current_index + m - 1) % len(arr)

        if current_index == 0:
            break

    results[i] = res


main()
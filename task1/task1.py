from threading import Thread
import sys

elements = {}
results = {}

def main():

    arr = []
    k = 0

    if (len(sys.argv) - 1) % 2 != 0:
        print("Необходимо ввести значения в формате n m (можно несколько).\n"
              "Примеры: 4 2 6 4, 6 3 5 2 7 3. Нечетное количество аргументов недопустимо")
        return

    for i in range(1, int(len(sys.argv)), 2):
        n = int(sys.argv[i])
        m = int(sys.argv[i+1])

        for j in range(1, n+1):
            arr.append(j)

        elements[k] = arr, m
        arr = []
        k += 1

    # while True:
    #     print("Type 3 to Start Program")
    #     print("Or press enter to continue")
    #     s = input()
    #
    #     if s == '3':
    #         break
    #
    #     arr = []
    #
    #     n = int(input("n = "))
    #     m = int(input("m = "))
    #
    #     for i in range(1,n+1):
    #         arr.append(i)
    #
    #     elements[k] = arr, m
    #     k += 1

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
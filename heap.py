from heapq import heappop, heappush, heapify

# Creating empty heap
heap = []
heapify(heap)

# insert element in heap
def push():
    e = int(input("enter the length of heap"))
    i = 0
    while i < e:
        element = int(input("enter the elements of heap to quit enter ", ))
        # q = input("to quit enter q")
        heappush(heap, -1 * element)
        i = i + 1
    print("Head value of heap : " + str(-1 * heap[0]))

    print("The heap elements : ")
    for i in heap:
        print((-1 * i), end=" ")
    print("\n")


def pop():
    element = heappop(heap)
    print("Head value of heap : " + str(-1 * heap[0]))
    print("The heap elements : ")
    for i in heap:
        print((-1 * i), end=" ")
    print("\n")



while (True):
    choice = int(input("enter the choices 1 to push, 2 to pop"))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    else:
        print("you quit")
        break

heappush(heap, -1 * 10)
heappush(heap, -1 * 30)
heappush(heap, -1 * 20)
heappush(heap, -1 * 400)



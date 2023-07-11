q = []
def push():
    e = int(input("enter the length of queue"))
    i=0
    while(i < e):
        pri = int(input("enter the priority"))
        element = input("enter the elements of queue")
        q.append((pri, element))
        i = i + 1

def pop():
    if len(q) == 0:
        print("queue is empty")
    else:
        q.sort()
        q.pop(0)
        print(q)


e = input("enter the length of stack")
while(True):
    choice = int(input("enter the choices 1 to push, 2 to pop, 3 to quit"))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    else:
        print("you quit")
        break

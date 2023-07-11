class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class linkedlist:
    def __init__(self):
        self.head = None

  
  # insertion at the begining of linkedlist
      def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        return

# print the linkedlist
    def print_ll(self):
        if self.head is None:
            print("linked list is empty")

        else:
            n = self.head
            while n is not None:
                print(n.data, "---", end=" ")
                n = n.ref


# insertion at the end of linkedlist
    def add_end(self, data):

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node


# inserting node after particular node in linkedlist
    def after_node(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("node is not present in ll")

        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


# insert node before particular node in linkedlist
    def add_before(self, data, x):
        if self.head is None:
            print("ll is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("node not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


# deletion of node from starting node of linkedlist
    def delete_begin(self):
        if self.head is None:
            print("ll is empty")
        else:
            self.head = self.head.ref


# deletion from the end of linkedlist
    def delete_end(self):
        if self.head is None:
            print("ll is empty")
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None


# deleting particular node of linkedlist
    def delete_by_value(self, x):
        if self.head is None:
            print("ll is empty")
            return
        if x == self.head.data:
            self.head = self.head.ref
            return
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("node is not present")
        else:
            n.ref = n.ref.ref


# printing last node in linked list
    def print_las_node(self):
        if head1 is None and head2 is None:
            return
        # code here
        a = head1
        b = head2
        v = []

        while a != None:
            v.append(a)
            a = a.next
        while b != None:
            v.append(b)
            b = b.next
        v.sort()
        return v

ll = linkedlist()

ll.add_begin(101)
ll.add_begin(2)
ll.add_begin(2)
ll.add_begin(10)

ll.add_end(39)

ll.print_ll()
print("\n")

from Node import*


class Linklist:
    def __init__(self):
        self.head = None

    def add_Forward(self, value):
        if self.head is None:
            temp = Node(value)
            self.head = temp
        else:
            temp = Node(value)
            current = p = self.head
            while current is not None:
                p = current
                current = current.next
            p.next = temp

    def add_Backward(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def print_LinkedList(self):
        string = ""
        if self.head is None:
            string = "Empty"
        else:
            string = ""
            current = self.head
            while current is not None:
                string += str(current.data)+"->"
                current = current.next
        return string.strip("->")

    def reverse_LinkedList(self):
        previous = None
        current = self.head
        future = None
        while current:
            future = current.next
            current.next = previous
            previous = current
            current = future
        self.head = previous
        return self.print_LinkedList()

    def length_LinkedList(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def middle_LinkedList(self):
        current = self.head
        current_slow = current
        current_fast = current_slow
        try:
            while current_fast.next:
                # print(current_slow.data, current_fast.data)
                current_slow = current_slow.next
                current_fast = current_fast.next.next
        except AttributeError:
            return "\"No perfect middle exist in linked list as length is even\""
        return str(current_slow.data)

    def deletion_fromLinkedList(self, item):
        current = prev = self.head
        if current.data == item:
            self.head = current.next
            current.next = None
            return self.print_LinkedList()
        else:
            while current:
                prev = current
                current = current.next
                if current is None or current.data == item:
                    break
            if current is None:
                return "No such item exit in linked list"
            else:
                prev.next = current.next
                current.next = None
                return self.print_LinkedList()


x = Linklist()
t = map(int, input().split())
for y in t:
    x.add_Forward(y)
print("Display Linked List", x.print_LinkedList())
print("Linked List Reversal", x.reverse_LinkedList())
print("Length of Linked List", x.length_LinkedList())
print("Middle element of Linked List", x.middle_LinkedList())
number = int(input("Enter the number to be deleted from Linked List\n"))
print(x.deletion_fromLinkedList(number))

""" 
z = Linklist()
s = map(int, input().split())
for r in s:
    z.add_Backward(r)
print(z.print_LinkedList())
z.reverse_LinkedList()
print(z.print_LinkedList())"""






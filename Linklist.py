from Node import*


class Linklist:
    def __init__(self):
        self.head = None

    def length_node(self, x):
        return x.__sizeof__()

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
        print("Linked List:", end=" ")
        if self.head is None:
            print("Empty")
        else:
            current = self.head
            while current.next is not None:
                print(current, end="->")
                current = current.next
        print(current)

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
        return self.head

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

    def cycle_formation(self, pos):
        count = 1
        pos = pos
        cur = ref = prev = self.head
        while cur:
            prev = cur
            if count == pos:
                ref = cur
            cur = cur.next
            count += 1
        prev.next = ref
        print(prev, prev.next, prev.next.next)

    def cycle_detection(self):
        cur_slow = self.head
        cur_fast = self.head
        count = 0
        while cur_slow and cur_fast and cur_fast.next:
            cur_slow = cur_slow.next
            cur_fast = cur_fast.next.next
            if cur_slow == cur_fast:
                break
        if cur_fast is None:
            return Node(-1)
        else:
            cur_fast = self.head
            while cur_fast is not cur_slow:
                count += 1
                cur_slow = cur_slow.next
                cur_fast = cur_fast.next.next
            return Node(count)


x = Linklist()
t = map(int, input().split())
for y in t:
    x.add_Forward(y)
x.print_LinkedList()
"""x.reverse_LinkedList()
x.print_LinkedList()"""""
print("Length of Linked List", x.length_LinkedList())
print("Middle element of Linked List", x.middle_LinkedList())
number = int(input("Enter the number to be deleted from Linked List\n"))
x.deletion_fromLinkedList(number)
print(x.cycle_detection())
pos = int(input("Enter the position index base(1) where loop formation take place:\n"))
x.cycle_formation(pos)  # base assume to index = 1
print(x.cycle_detection())
"""print("The cycle in the linked list at:", x.cycle_detection(x).data)"""





""" 
z = Linklist()
s = map(int, input().split())
for r in s:
    z.add_Backward(r)
print(z.print_LinkedList())
z.reverse_LinkedList()
print(z.print_LinkedList())"""






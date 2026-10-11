TASK 1 : class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(15)
print(node.data)
print(node.next)

TASK 2 : class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.print_list()

TASK 3 : (OH WAIT I HAVE TO ADD THESE TOGETHER OHHHH MY BAD ILL START DOING IT FROM TASK 4 SORRY I HAVE NEVER USED GIT)class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

my_list = LinkedList()
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.insert_at_beginning(10)
my_list.print_list()

TASK 4 :

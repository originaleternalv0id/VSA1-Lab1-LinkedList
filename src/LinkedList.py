#TASK 1 : 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(15)
print(node.data)
print(node.next)

#TASK 2 : 
class Node:
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

#TASK 3 :
class Node:
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

#TASK 4 :   
class Node:
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

    def insert_after(self, target, data):
        current = self.head
        while current is not None and current.data != target:
            current = current.next
        if current is None:
            print("Element tapılmadı.")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

list_4 = LinkedList()
for number in (10, 20, 40):
    list_4.append(number)
list_4.insert_after(20, 30)
list_4.print_list()

#Task 5:   
class Node:
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

    def delete(self, value):
        if self.head is None:
            print("Element tapılmadı.")
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None and current.next.data != value:
            current = current.next
        if current.next is None:
            print("Element tapılmadı.")
            return
        current.next = current.next.next

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

list_5 = LinkedList()
for number in (10, 20, 30, 40, 50):
    list_5.append(number)
list_5.delete(30)
list_5.print_list()

#task 6 :    
class Node:
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

    def search(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                print("Element tapıldı.")
                return
            current = current.next
        print("Element tapılmadı.")

list_6 = LinkedList()
for number in (10, 20, 30, 40):
    list_6.append(number)
list_6.search(30)
list_6.search(99)

#task 7 :   
class Node:
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

    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

list_7 = LinkedList()
for number in (11, 22, 33, 44, 55):
    list_7.append(number)
print("List length =", list_7.length())

#task 8 :  
class Node:
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

    def find_max_min(self):
        if self.head is None:
            return None, None
        maximum = self.head.data
        minimum = self.head.data
        current = self.head.next
        while current is not None:
            if current.data > maximum:
                maximum = current.data
            if current.data < minimum:
                minimum = current.data
            current = current.next
        return maximum, minimum

list_8 = LinkedList()
for number in (23, 8, 91, 15, 42):
    list_8.append(number)
maximum, minimum = list_8.find_max_min()
print("Maximum:", maximum)
print("Minimum:", minimum)

#task 9 :   
class Node:
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

    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

list_9 = LinkedList()
for number in (10, 20, 30, 40, 50):
    list_9.append(number)
list_9.reverse()
list_9.print_list()

#task 10 :
class StudentNode:
    def __init__(self, student_id, student_name, gpa):
        self.student_id = student_id
        self.student_name = student_name
        self.gpa = gpa
        self.next = None


def print_student(student):
    print(f"ID: {student.student_id}, Name: {student.student_name}, GPA: {student.gpa}")


class StudentList:
    def __init__(self):
        self.head = None

    def add_student(self, student_id, student_name, gpa):
        new_student = StudentNode(student_id, student_name, gpa)
        if self.head is None:
            self.head = new_student
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_student

    def remove_student(self, student_id):
        if self.head is None:
            print("Tələbə tapılmadı.")
            return
        if self.head.student_id == student_id:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None and current.next.student_id != student_id:
            current = current.next
        if current.next is None:
            print("Tələbə tapılmadı.")
            return
        current.next = current.next.next

    def show_all(self):
        current = self.head
        while current is not None:
            print_student(current)
            current = current.next

    def show_high_gpa(self):
        current = self.head
        while current is not None:
            if current.gpa > 80:
                print_student(current)
            current = current.next

    def search_by_name(self, name):
        current = self.head
        while current is not None:
            if current.student_name.lower() == name.lower():
                print_student(current)
                return
            current = current.next
        print("Tələbə tapılmadı.")

    def count_students(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

students = StudentList()
students.add_student(1, "Ali", 85)
students.add_student(2, "Leyla", 92)
students.add_student(3, "Murad", 74)
students.add_student(4, "Aysel", 88)
print("All students:")
students.show_all()
print("GPA above 80:")
students.show_high_gpa()
print("Search by name (Leyla):")
students.search_by_name("Leyla")
students.remove_student(3)
print("After removing ID 3:")
students.show_all()
print("Student count:", students.count_students())

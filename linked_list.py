class Node:
    def __init__(self, value):
        """
        :param value:
        """
        self.value = None
        self.next = None
        if value is not None:
            self.value = value


class LinkedList:
    def __init__(self, value=None):
        """"
        Create a node
        """
        new_node = None
        if value is not None:
            new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        if self.head and self.head.value is not None:
            self.length = 1
        else:
            self.length = 0

    def print_list(self):
        """
        :return: prints a ll
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        """
        Create a node and add to the end
        :param value:
        :return:
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        """
        Create a node and add to the beginning
        :param value:
        :return:
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def insert(self, index, value):
        """
        Create a node and add to the defined index
        :param index:
        :param value:
        :return:
        """
        if index < 0 or index > self.length:
            print("Invalid index")
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def pop(self):
        """
        :return:
        """
        if self.length == 0:
            print("Nothing to remove")
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def pop_first(self):
        """
        :return:
        """
        if self.length:
            self.length -= 1
            temp = self.head
            self.head = self.head.next
            temp.next = None
            if self.length == 0:
                self.tail = None
            return temp
        else:
            print("Nothing to pop")

    def get(self, index):
        """
        :param index:
        :return:
        """
        if index < 0 or index >= self.length:
            print("Index does not exist")
            return
        temp = self.head
        for _ in range(index):
            if temp.next:
                temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def remove(self, index):
        """
        :param index:
        :return:
        """
        if index < 0 or index >= self.length:
            print("Index out of range")
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp

    def reverse(self):
        """
        :return:
        """
        temp = self.head
        self.head = self.tail
        self.tail = temp
        # after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print('LL before remove():')
my_linked_list.print_list()

print('\nRemoved node:')
print(my_linked_list.remove(2).value)
print('LL after remove() in middle:')
my_linked_list.print_list()

print('\nRemoved node:')
print(my_linked_list.remove(0).value)
print('LL after remove() of first node:')
my_linked_list.print_list()

print('\nRemoved node:')
print(my_linked_list.remove(2).value)
print('LL after remove() of last node:')
my_linked_list.print_list()



#
# my_linked_list = LinkedList(1)
# my_linked_list.append(3)
#
#
# print('LL before insert():')
# my_linked_list.print_list()
#
#
# my_linked_list.insert(1,2)
#
# print('\nLL after insert(2) in middle:')
# my_linked_list.print_list()
#
#
# my_linked_list.insert(0,0)
#
# print('\nLL after insert(0) at beginning:')
# my_linked_list.print_list()
#
#
# my_linked_list.insert(4,4)
#
# print('\nLL after insert(4) at end:')
# my_linked_list.print_list()

#
# my_ll = LinkedList(None)
# my_ll.insert(0,10)
# my_ll.print_list()
# print(my_ll.get(1))
# my_ll.prepend(2)
# # my_ll.append(27)
# # my_ll.append(53)
# my_ll.print_list()
# print("+++++++++++++++++")
# # my_ll.insert(1,29)
# # my_ll.set_value(4,10)
# # my_ll.insert(10,20)
# my_ll.reverse()
# my_ll.print_list()
# print("+++++++++++++++++")
# my_ll.pop_first()
# my_ll.print_list()
# print("+++++++++++++++++")
# my_ll = LinkedList(10)
# my_ll.pop_first()
# my_ll.print_list()
# print("+++++++++++++++++")
# my_ll = LinkedList()
# my_ll.pop_first()
# my_ll.print_list()
# print("+++++++++++++++++")
# my_ll.prepend(1)
# my_ll.print_list()
# print(my_ll)

# my_linked_list = LinkedList(10)
# print("my_linked_list init :: ", my_linked_list)
# my_linked_list.append(value=4)
# print("my_linked_list append", my_linked_list )
# # my_linked_list.print_list()
#
# print("Poping 1 :: ", my_linked_list.pop())
# print("Poping 2 :: ", my_linked_list.pop())
# print("Poping 3 :: ", my_linked_list.pop())

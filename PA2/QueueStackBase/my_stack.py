from my_array_deque import ArrayDeque
from my_linked_list import LinkedList


class Stack:
    def __init__(self, type: str):
        if type == 'array':
            self.container = ArrayDeque()
        else:
            self.container = LinkedList()

    def push(self, element):
        self.container.push_front(element)

    def pop(self):
        return self.container.pop_front()

    def get_size(self):
        return self.container.get_size()

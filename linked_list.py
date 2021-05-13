# In python, collections.deque can be used to to create a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        # Only for doubly linked list
        self.previous = None

    def __repr__(self):
        return self.data


# Singly linked list
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        # Allows to quickly create linked lists with some data
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            # or print(node.data) each line
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # Returns the iterator object itself
    def __iter__(self):
        node = self.head
        while node is not None:
            # yield works more or less as a return, but it returns a generator
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node
        # last = self.head
        # while (last.next):
        #     last = last.next
        # last.next = node

    # Adds a node after an existing node with a specific data value
    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    # Adds a node before an existing node with a specific data value
    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def get_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print(" -> ".join(nodes))


def main():
    linked_list = LinkedList()
    first_node = Node("b")
    linked_list.head = first_node
    print(linked_list)
    second_node = Node("c")
    third_node = Node("d")
    first_node.next = second_node
    second_node.next = third_node
    print(linked_list)
    linked_list.add_first(Node("a"))
    print(linked_list)
    linked_list.add_last(Node("e"))
    print(linked_list)
    linked_list.add_after("c", Node("cc"))
    print(linked_list)
    linked_list.add_before("c", Node("bb"))
    print(linked_list)
    linked_list.remove_node("bb")
    linked_list.remove_node("cc")
    print(linked_list)
    for node in linked_list:
        print(node)

    circular_linked_list = CircularLinkedList()
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    a.next = b
    b.next = c
    c.next = d
    d.next = a
    circular_linked_list.head = a
    circular_linked_list.print_list()
    circular_linked_list.print_list(b)
    circular_linked_list.print_list(d)


if __name__ == "__main__":
    main()

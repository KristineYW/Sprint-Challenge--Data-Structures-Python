class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # ITERATIVE APPROACH
        # Handle an emtpy list
        # if not self.head and not prev:
        #     return None
        # else:
        #     # Define the previous node we need to access
        #     prev = None
        #     # Define the *initial* current node
        #     current = node

        #     # Handle all other scenarios
        #     while current is not None:
        #         # Store the next node's information so we don't lose it when we reassign the node direction
        #         actual_next = current.next_node
        #         # reassign the previous node to the current next node
        #         # we're reversing arrow direction
        #         current.next_node = prev
        #         # set the new current to the previous node 
        #         prev = current
        #         # set the original next node as the current node we're working on 
        #         current = actual_next
        #         # go back up and do the same 
            
        # return self.head

        # RECURSIVE APPROACH
        # If the node doesn't exist/is None
        if node is None:
            self.head = prev
        # Otherwise node exists and is not None
        else:
            # Store the next node's information so we don't lose it when we reassign the node direction
            actual_next = node.next_node
            # Set the new current node to the previous node
            node.set_next(prev)
            # Use recursion using the next node and current node 
            return self.reverse_list(actual_next, node)


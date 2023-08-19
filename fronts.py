# Define a class for individual nodes in the linked list
class Node:
    def __init__(self, val):
        self.val = val         # Store the value of the node
        self.next = None       # Initialize the 'next' pointer to None


# Define a class for the linked list itself
class List:
    def __init__(self):
        self.head = None       # Initialize the 'head' pointer to None, indicating an empty list

    # Method to retrieve the value of the front (head) node
    def front(self):
        if self.head:
            return self.head.val  # Return the value of the head node if the list is not empty

    # Method to remove the front (head) node from the list
    def remove_front(self):
        if self.head:
            self.head = self.head.next  # Update the 'head' pointer to the next node, effectively removing the current head

    # Method to add a new node to the front (head) of the list
    def add_front(self, val):
        new_node = Node(val)         # Create a new node with the given value
        if not self.head:
            self.head = new_node     # If the list is empty, set the new node as the head
        else:
            new_node.next = self.head  # Point the new node's 'next' pointer to the current head
            self.head = new_node       # Update the 'head' pointer to the new node, making it the new head

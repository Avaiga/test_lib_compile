from testlib.linkedlist import LinkedList
from testlib.binarytree import BinaryTree


class Main:
    def __init__(self):
        self.linked_list = LinkedList()
        self.binary_tree = BinaryTree()

    def insert_to_linked_list(self, value):
        self.linked_list.insert(value)

    def display_linked_list(self):
        return self.linked_list.display()

    def insert_to_binary_tree(self, value):
        self.binary_tree.insert(value)

    def display_binary_tree_inorder(self):
        return self.binary_tree.inorder_traversal()

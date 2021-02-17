class Node:
    def __init__(self, val, next=None):
        self.val_ = val
        self.next_ = next


class SLL:
    def __init__(self):
        self.head = None

    def from_list(self, lst):
        self.head = Node(lst[0])
        cur_node = self.head
        for word in lst[1:]:
            new_node = Node(word)
            cur_node.next_ = new_node
            cur_node = new_node

    def print_list(self):
        print("Printing SLL...")
        if self.head is None:
            print("SLL is empty.")
        else:
            cur_node = self.head
            while cur_node is not None:
                print(cur_node.val_)
                cur_node = cur_node.next_


lst = [1, 3, 6, 8, 12]
sll = SLL()
sll.print_list()
sll.from_list(lst)
sll.print_list()

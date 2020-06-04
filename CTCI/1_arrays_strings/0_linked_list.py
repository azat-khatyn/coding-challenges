class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

    def print_node(self):
        print(self.dataval, self.nextval)


n1 = Node(5)
n2 = Node(6)

n1.print_node()
n2.print_node()

print()

n1.nextval = n2

n1.print_node()
n2.print_node()

n3 = Node(7)
n2.nextval = n3

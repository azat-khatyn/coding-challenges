class Stack:

    def __init__(self):
        self.lst = []

    def is_empty(self):
        return len(self.lst) == 0

    def push(self, x):
        if x not in ['(', ')', '{', '}', '[', ']']:
            raise Exception('Wrong character!!')
        if x in ['(', '{', '[']:
            self.lst.append(x)
        else:
            if not self.is_empty() and (x == ')' and self.lst[-1] == '(' or x == ']' and self.lst[-1] == '[' or x == '}' and self.lst[-1] == '{'):
                self.lst.pop()
            else:
                return False
        return True


s = Stack()

print(s.push('{'))
print(s.push('['))
print(s.push(']'))
print(s.push(')'))
print(s.push('}'))



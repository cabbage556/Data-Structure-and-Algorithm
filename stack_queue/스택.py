class MyStack:
    def __init__(self):
        # 리스트 기반 스택
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        # O(1)
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            # O(1)
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)


# stk = Stack()
# stk.push(4)
# stk.push(5)
# stk.push(6)
#
# print("스택 크기:", stk.size())
# print("스택 top:", stk.peek())
#
# print("스택 pop 요소:", stk.pop())
# print("스택 top:", stk.peek())
# print("스택 크기:", stk.size())

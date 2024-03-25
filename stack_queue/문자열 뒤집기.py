from 스택 import MyStack


def reverse_string(string):
    stk = MyStack()
    reversed_string = ""

    for s in string:
        stk.push(s)

    while not stk.is_empty():
        reversed_string += stk.pop()

    return reversed_string


print(reverse_string("abcde"))

from 스택 import MyStack


class Linter:
    def __init__(self):
        self.stk = MyStack()

    def lint(self, text):
        for s in text:
            if self.is_opening_brace(s):
                self.stk.push(s)
            elif self.is_closing_brace(s):
                popped_opening_brace = self.stk.pop()
                if popped_opening_brace is None:
                    return f"{s}가 여는 괄호를 갖지 않음"

                if self.is_not_match(popped_opening_brace, s):
                    return f"{s}에 해당하는 여는 괄호가 아님"

        if not self.stk.is_empty():
            return f"{self.stk.peek()}에 해당하는 닫는 괄호가 없음"

        return True


    def is_opening_brace(self, s):
        opening_braces = ['(', '{', '[']
        if s in opening_braces:
            return True
        else:
            return False

    def is_closing_brace(self, s):
        closing_braces = [')', '}', ']']
        if s in closing_braces:
            return True
        else:
            return False

    def is_not_match(self, opening_brace, closing_brace):
        matches = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        return closing_brace != matches[opening_brace]


linter = Linter()
print(linter.lint("(var x = {y: [1,2,3]})"))
print(linter.lint("var x = {y: [1,2,3]})"))
print(linter.lint("(var x = 10}"))
print(linter.lint("((var x = 10)"))
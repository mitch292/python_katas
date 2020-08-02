class Stack:
    def __init__(self):
        self._data = []
    
    def __repr__(self):
        return ''.join(self._data)
    
    def push(self, item):
        self._data.insert(0, item)
    
    def pop(self):
        if len(self._data) > 0:
            return self._data.pop(0)
        return None
    
    def peek(self):
        if len(self._data) > 0:
            return self._data[0]
        return None

    def is_empty(self):
        return len(self._data) == 0


def balanced_brackets(s: str):
    bracket_pairs = {
        ")": "(",
        "}": "{",
        "]": "[",
        "{": False,
        "[": False,
        "(": False,
    }
    stack = Stack()
    for character in s:
        if stack.peek() == bracket_pairs[character]:
            stack.pop()
        else:
            stack.push(character)
    return "YES" if stack.is_empty() else "NO"




if __name__ == "__main__":
    print(balanced_brackets("{{)[](}}"))

# [
#      ), {, {
# ]
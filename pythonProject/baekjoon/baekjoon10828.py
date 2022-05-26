# baekjoon 10828 스택
# 실버 4
# 자료 구조 스택
import sys

n = int(sys.stdin.readline())


class stack:
    def __init__(self):
        self.list = []

    def push(self, v):
        self.list.append(v)

    def pop(self):
        return -1 if len(self.list) == 0 else self.list.pop()

    def size(self):
        return len(self.list)

    def empty(self):
        return 1 if len(self.list) == 0 else 0

    def top(self):
        return -1 if len(self.list) == 0 else self.list[-1]


num_stack = stack()

for i in range(n):
    line = sys.stdin.readline().split()
    if line[0] == "push":
        num_stack.push(line[1])
    elif line[0] == "pop":
        print(num_stack.pop())
    elif line[0] == "size":
        print(num_stack.size())
    elif line[0] == "empty":
        print(num_stack.empty())
    else:
        print(num_stack.top())

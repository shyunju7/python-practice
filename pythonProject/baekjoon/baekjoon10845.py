# baekjoon 10845 큐
# 실버 4
# 자료 구조 큐
import sys

n = int(sys.stdin.readline())


class queue:
    def __init__(self):
        self.list = []

    def push(self, v):
        self.list.append(v)

    def pop(self):
        return -1 if len(self.list) == 0 else self.list.pop(0)

    def size(self):
        return len(self.list)

    def empty(self):
        return 1 if len(self.list) == 0 else 0

    def front(self):
        return -1 if len(self.list) == 0 else self.list[0]

    def back(self):
        return -1 if len(self.list) == 0 else self.list[-1]


num_queue = queue()

for i in range(n):
    line = sys.stdin.readline().split()
    if line[0] == "push":
        num_queue.push(line[1])
    elif line[0] == "pop":
        print(num_queue.pop())
    elif line[0] == "size":
        print(num_queue.size())
    elif line[0] == "empty":
        print(num_queue.empty())
    elif line[0] == "front":
        print(num_queue.front())
    else:
        print(num_queue.back())

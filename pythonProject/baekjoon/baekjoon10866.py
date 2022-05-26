# baekjoon 10866 덱
# 실버 4
# 자료 구조 큐
import sys

n = int(sys.stdin.readline())


class dequeue:
    def __init__(self):
        self.list = []

    def push_front(self, v):
        self.list.insert(0, v)

    def push_back(self, v):
        self.list.append(v)

    def pop_front(self):
        return -1 if len(self.list) == 0 else self.list.pop(0)

    def pop_back(self):
        return -1 if len(self.list) == 0 else self.list.pop()

    def size(self):
        return len(self.list)

    def empty(self):
        return 1 if len(self.list) == 0 else 0

    def front(self):
        return -1 if len(self.list) == 0 else self.list[0]

    def back(self):
        return -1 if len(self.list) == 0 else self.list[-1]


num_dequeue = dequeue()
for i in range(n):
    line = sys.stdin.readline().split()
    if line[0] == "push_front":
        num_dequeue.push_front(line[1])
    elif line[0] == "push_back":
        num_dequeue.push_back(line[1])
    elif line[0] == "pop_front":
        print(num_dequeue.pop_front())
    elif line[0] == "pop_back":
        print(num_dequeue.pop_back())
    elif line[0] == "size":
        print(num_dequeue.size())
    elif line[0] == "empty":
        print(num_dequeue.empty())
    elif line[0] == "front":
        print(num_dequeue.front())
    else:
        print(num_dequeue.back())

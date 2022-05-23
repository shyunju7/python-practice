# baekjoon 3040 백설 공주와 일곱 난쟁이
# 브론즈 2
# 브루트포스 알고리즘

dwarfs = []
no_dwarfs = []
for _ in range(9):
    dwarfs.append(int(input()))

# dwarfs = [int(input()) for _ in range(9)]

remain = sum(dwarfs) - 100
for i in range(9):
    for j in range(i + 1, 9):
        if dwarfs[i] + dwarfs[j] == remain:
            no_dwarfs.append(dwarfs[i])
            no_dwarfs.append(dwarfs[j])
            break

print(*[dwarf for dwarf in dwarfs if dwarf not in no_dwarfs], sep="\n", end="")

# ctrl + shift + R : 현재 파일 실행

# input
# string to int
# a = int(input())
# b = input()

# num = int(input())
# arr = input().split() #default 공백
# print(arr)

# map(지정 타입, 바꿀 요소)
# map(int, input().split())

# for 문
# num = int(input())
# for i in range(num):
#     print(i)


# 리스트 = 흔한 배열, arrayList
list = [1,4,8,3,2,3]

for i in list:
    print(i)

# append 맨 뒤 요소 추가
list.append(5)
print("append,", list)

# list.sort()
print("sort,", list)
sortedList = sorted(list)
print("sorted,", sortedList)

print(list.count(3)) # 해당 요소의 개수를 반환함

# 인자 x -> 마지막 요소 제거, index 지정 가능
list.pop()
print(list)

# 합치기
list.extend([1,2,3])
print(list)

tmp = list.copy()
print(tmp)

list.reverse()
print(list)

print(list[7])
print(list.index(8))

# hashmap -> dictionary
dic = {
    "id":1,
    "name":"파이썬",
}

print(dic.get("id"))
print(dic.items()) #dict_items([('id', 1), ('name', '파이썬')])
print(dic.values()) #dict_values([1, '파이썬'])
print(dic.keys()) #dict_keys(['id', 'name'])
print(dic.items())

for k, v in dic.items():
    print(k, v)
    print(dic[k])


name = "현주"

# len(list) => 요소 갯수
# sum(list), max(list), min(list)
# for i in range(len(list)-1, -1, -1)) 리스트 크기 -1부터 -1전까지 -1씩 감소함


#print(3,2,1) => 3 2 1
#print(3,2,1 sep="") => 321
#print(3,2,1 sep="@") => 3@2@1
#№1
#list1 = list(map(int, input().split()))
#list2 = [list1[1], list1[0], list1[3], list1[2], list1[4]]
#print(list2)

#№1.1 (в общем случае)
#list1  = list(map(int, input().split()))
#for i in range(0, len(list1) - 1, 2):
    #a = list1[i]
    #list1[i] = list1[i + 1]
    #list1[i + 1] = a
#print(list1)

#№2
#list1 = list(map(int, input().split()))
#print([list1[-1]] + list1[:-1])

#№3
#list1 = list(map(int, input().split()))
#for i in list1:
    #if list1.count(i) == 1:
        #print(i, end = ' ')

#№4
# list1 = list(map(int, input().split()))
# max_count = 0
# max_elem = list1[0]
# for i in list1:
#     if list1.count(i) >= max_count:
#         max_count = list1.count(i)
#         max_elem = i
# print(max_elem)

# №5
# list1 = list(input().split())
# g = int(list1[0])
# list1 = str(list1[1])
# num = len(list1)//g
# str2 = ''
# for i in range(num):
#     new_line = list1[(i * g):((i + 1) * g)]
#     add = new_line[::-1]
#     str2 += add
# print(str2)

from collections import deque

#利用列表做堆栈

lists = [415,12,4,1]

it = iter(lists)

for x in it:
    print(x,end=',')

lists.append(14)
lists.append(55)

print("\n=========================")
print(lists)

print("POP:",lists.pop())
print(lists)


#利用列表做队列
print("\n=========================")
queue = deque(['qwe','asd','zxc'])
queue.append('poi')
print(queue)
print(queue.popleft())


print("\n=========================")
#列表推导式

vec = [5,3,4]
print([x*3 for x in vec])
print("\n-------------------------")
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
for row in matrix:
    print(row.__len__())


print("\n=========================")
#遍历字典
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v)






import sys
N = int(input())

lines =  list(sys.stdin.readline().split() for i in range(N)) 

numbers = list(int(lines[i][1]) for i in range(N))
numbers.insert(0, int(lines[0][0]))

product_list = list()
for i in range(N-2):
    product_list.append([i, numbers[i]*numbers[i+1]*numbers[i+2]])


print(numbers)
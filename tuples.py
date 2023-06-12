n = int(input())
input_line = input()
input_list = input_line.split()
for i in range(n):
        input_list[i] = int(input_list[i])

t = tuple(input_list)
print (hash(t)) 


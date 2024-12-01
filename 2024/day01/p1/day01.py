with open('../input.csv', 'r') as file:
    lines = file.readlines()

list1 = []
list2 = []
distance_list = []

for line in lines:
    columns = line.strip().split(',')

    list1.append(int(columns[0]))
    list2.append(int(columns[1]))

# print("List1:", list1)
# print("List2:", list2)

list1.sort()
list2.sort()

# print("List1:", list1)
# print("List2:", list2)


i = 0;
for numbers in list1:
    distance_list.append(abs(list2[i] - list1[i]))
    i += 1

#print("Distance list:", distance_list)

print(sum(distance_list))

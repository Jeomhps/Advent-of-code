with open('../test_input.csv', 'r') as file:
    lines = file.readlines()

hashmap1 = {}
hashmap2 = {}

for line in lines:
    columns = line.strip().split(',')

    hashmap1[columns[0]] = hashmap1.get(columns[0], 0) + 1
    hashmap2[columns[1]] = hashmap2.get(columns[1], 0) + 1

# print("hashmap1:", hashmap1)
# print("hashmap2:", hashmap2)

similarity_score = 0
for key in hashmap1.keys():
    if key in hashmap2.keys():
        similarity_score += (int(key) * hashmap1[key]) * hashmap2[key]


print(similarity_score)

sum_ = 0

with open("input_day_1.txt", 'r') as input:
    for line in input:
        
        list_of_digit = [int(i) for i in list(line)
                         if i.isdigit()]
        
        sum_ += int(str(list_of_digit[0])
                    + str(list_of_digit[-1]))

print(sum_)

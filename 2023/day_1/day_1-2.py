digits = {
    'oneight' : '18',
    'twone' : '21',
    'threeight' : '38',
    'sevenine' : '79',
    'eighthree' : '83',
    'eightwo' : '82',
    'one' : '1',
    'two' : '2',
    'three' : '3',
    'four' : '4',
    'five' : '5',
    'six' : '6',
    'seven' : '7',
    'eight' : '8',
    'nine' : '9'
    }

sum_ = 0

with open("input_day_1.txt", 'r') as input:
    for line in input:
        for key, value in digits.items():
            line_digit_replaced = line

            line_digit_replaced = line_digit_replaced.replace(key, value)
            
        list_of_digit = [int(i) for i in list(line_digit_replaced)
                         if i.isdigit()]
        
        sum_ += int(str(list_of_digit[0]) + str(list_of_digit[-1]))

print(sum_)

import re
path = '/Users/manu/Documents/Foxit Reader/Python Course/regex_sum_375897.txt'
regex = open(path,'r')
sum2 = 0
for lines in regex:
    y = re.findall('[0-9]+' , lines)
    y2 = [int(i) for i in y]
    sum2 = sum2 + sum(y2)
print(sum2)
regex.close()

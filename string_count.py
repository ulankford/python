#!/usr/bin/python

random_string=raw_input('Enter random string : ')

count=0
list_string = list(random_string)

dict={}

for char in list_string:
  count=random_string.count(char)
  dict[char] = count

print(dict)

# Sort dictionary by values
dict_sorted = sorted(dict.items(), key=lambda x: x[1], reverse=True)
for i in dict_sorted:
  print(i[0], i[1])  

# Sort dictionary by keys
print(sorted(dict))

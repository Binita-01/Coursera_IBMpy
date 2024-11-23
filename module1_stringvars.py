# string is stored as an array
# so you can access it with numbers
# name = "Binita"
# name[0] will be 'B'
# also can access from the end
# end value is name[-1] 
# so if i want to access first it would be
# name[-6] 
# string as list
# name[0:4]
# can perform slicing too
# name[::2] : every second variable
# Get every second element in the range from index 0 to index 4
name[0:5:2]
# len(name)
# concatenate
# name + "KC"
# 3*name = "BinitaKCBinitaKC.."
# immutable
# name[0] = 'j' cant be done

# print("binita\tKC")
# methods: 
  # sequence methods
a = "binita"
b = a.upper()
c = a.replace('bin','kab')
  # string methods
# name.find('in') will give 1 as it found in and i starts at 1


name = "John"
age = 50
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))

# RAW STRINGS; to be unaffected by the escape characteristics
regular_string = r"C:\new_folder\file.txt"
print("Regular String:", regular_string)

text = "Binita KC is a good girl."
split_text = text.split()
# will be splitted by the space between words

import re
full_string = "Micheal Jackson is the best celeb I have ever met!"
pattern = "jackson"
result = re.search(full_string, pattern)
if result:
  print("Match found")
else:
  print("Match not found")
  

# \d	Matches any digit character (0-9)	"123" matches "\d\d\d"
# \D	Matches any non-digit character	"hello" matches "\D\D\D\D\D"
# \w	Matches any word character (a-z, A-Z, 0-9, and _)	"hello_world" matches "\w\w\w\w\w\w\w\w\w\w\w"
# \W	Matches any non-word character	"@#$%" matches "\W\W\W\W"
# \s	Matches any whitespace character (space, tab, newline, etc.)	"hello world" matches "\w\w\w\w\w\s\w\w\w\w\w"
# \S	Matches any non-whitespace character	"hello_world" matches "\S\S\S\S\S\S\S\S\S"
# \b	Matches the boundary between a word character and a non-word character	"cat" matches "\bcat\b" in "The cat sat on the mat"
# \B	Matches any position that is not a word boundary	"cat" matches "\Bcat\B" in "category" but not in "The cat sat on the mat"


result2 = re.split("\s",full_string)
# splitting words between spaces

pattern = "best"
replacement = "worst"
result3 = re.sub(pattern,replacement,full_string, flags = re.IGNORECASE)

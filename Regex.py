# Regular expression in python

# r says that the python don't treat the expression as just a simple string there are some identifiers within the string.


# phone number (555)-555-5555
# r'(\d\d\d)-\d\d\d-\d\d\d\d'
# r"(\d{3})-\d{3}-\d{4}"

# how to use regular expression library in python

text=" The agent's phone number is 408-555-1234 and 408-897-1234 Call soon!"
# 'phone' in text

import re
# pattern= 'phone'
# print(re.search(pattern,text))
# match=re.search(pattern,text)

# text_new="I had three phone. But I lost my special phone today. Now I have just two more phones."
# for match in  re.finditer("phone",text_new):
#     print(match)

# l=list(re.finditer("phone",text_new))
# print(l[3])


# regular expression patterns
# \d -for any digits   abc_\d\d--> abc_23 or acb_24
# \w- for any alphanumeric abc_\w\w--> abc_23, abc_2a, abc_w2
# \s - for white space --> a\sb\sc--> a b c
# \D- a non-digit--> \D\D\D--> ABC,asd
# \W - a non-alpha numeric--> \W\W\W --> *=+
# \S- a non white Space--> \S\S\S---> abc

text='my phone number is 74-711-83825 and 81-912-83825'

phone_all_match= re.search('74-711-83825',text)

# when you don't exactly know your phone number.

#if the number is repeated once
match=re.search(r'\d\d-\d\d\d-\d\d\d\d\d',text)


# If it the pattern is more than one time.
# for match in re.finditer(r'\d\d-\d\d\d-\d\d\d\d\d',text):
#     print(match.group())

# regex with quantifiers

# +-->  Occurs one or more times. abc_\w+ abc_1, abc_123, abc_abcde, abc_12b
# {3}--> Occurs exactly three times. \D{3}  abc
# {2,4} --> Occurs 2 to 4 times. \d{2,4} --> 12, 123, 1234
# {3,}--> Occurs 3 or more times \w{3,} --> aasdnf, acv, asdfasdf
# * occur zero or more times    ABC* --> ABC, ABCC,...
# ? once or none plurals? --> plurals, pluralss

# using regex with quantifiers

# for match in re.finditer(r'\d{2}-\d{3}-\d{5}',text):
#     print(match.group())

# use of compile in regex
# each of the pattern in the bracket are one individual group. So suppose first two digit in the phone number says the country code.
# and you want to know the country code of all the phone numbers in the 
phone_pattern=re.compile(r'(\d{2})-(\d{3})-(\d{5})')

for match in re.finditer(phone_pattern, text):
    # Note unlike array or list it starts with 1.
    print(match.group(1))




'''
This is the python code give the detailed information regaring the features of the 'STRING' data type.
The value of the index has to be an integer.
Strings are immutable.
f string, format operator
'''



string = "Hello Anvesh .. maste\tring python"

# to check the string is upper case or not
print (string.isupper())
# to convert the string is upper case
print (string.upper())
# to check the string is lower case or not
print (string.islower())
# to captalize the given string
print (string.capitalize())
# to split the given string after the spaces or based on the given input
print (string.split())
# to convert the string with first letter of each word capitalized
print (string.title())
# to remove the spaces at the begining and end of the string
print (string.strip())
# print lowercase string
# is an aggressive lower() method which convert strings to casefolded strings for caseless matching.
print("Lowercase string:", string.casefold())
substring = "ma"
count = string.count(substring)
# print count
print("The count is:", count)
# returns True if a string ends with the specified suffix. If not, it returns False
result = string.endswith('python')
# returns True
print(result)
#returns a copy of string with all tab characters '\t' replaced with whitespace characters until the next multiple of tabsize parameter.
tab = string.expandtabs()
print(tab)


# Slicing of the string
Course = "Python ."

print('string[0] = ', Course[0])  #first character o/p:(string[0] =  P)
print('string[-1] = ', Course[-1]) #last character o/p:(string[-1] =  .)
print('string[1:8] = ', Course[1:5 ]) #slicing 2nd to 5th character o/p:(string[1:8] =  ytho)
print('string[5:] = ', Course[5:-2]) #slicing 6th to 2nd last character o/p:(string[5:] =  n)

'''
to get the string 
'''

quote_1 = 'single quoted' 
quote_2 = "double quoted" 
print(quote_1, quote_2) # o/p: single quoted, double quoted
why_1 = 'She said, "Hello!"' 
why_2 = "It's mine!" 
print(why_1, why_2) # o/p: She said, "Hello!" It's mine!
why_not_1 = "She said, \"Hello!\"" 
why_not_2 = 'It\'s mine!' 
print(why_not_1, why_not_2) # o/p: She said, "Hello!" It's mine!
# Special escape sequences exist 
new_line = 'line1\nline2\nline3\n' 
print(new_line) # o/p: line1 
				#	   line2 
				#	   line3
tab_char = 'col1\tcol2\tcol3\t' 
print(tab_char) 
backslash = 'the backslash: \\' 
print(backslash) # o/p: 
# Raw strings prevent escape sequence interpretation 
raw_new_line = r'line1\nline2\nline3\n' 
print(raw_new_line) # o/p: 
raw_tab_char = r'col1\tcol2\tcol3\t' 
print(raw_tab_char) # o/p: 
raw_backslash = r'the backslash: \\' 
print(raw_backslash) # o/p: 

# string concatenation
string_1 = 'single quoted' 
string_2 = "double quoted"

print (string_1 + string_2)

print (string_1 + ' ' + string_2)


# string multiplication
multiplication = string_1 + ' ' + string_2
print (string_1 * 2)
print (multiplication * 2)

# % Format operator
camels = 42
print('I have spotted %d camels.' % camels)
# F-string
name = 'Anvesh' 
age = 23 
print(f'He said his name is {name} and he is {age} years old.')

#First, we will find the position of the at-sign in the string.
data = 'From personal.info@uni.DLI.AP.TG.in Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print (atpos)

sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1:sppos]
print(host)

print('Since %d years, I have spotted %g %s.' % (4, 0.99, 'camels'))

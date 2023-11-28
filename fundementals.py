num1 = 100
string1 = "string one"
binary1 = True
array_strings = ["string 1", "string 1", "string 3"]
array_numbers = [1, 2, 3, 4 , 5]

print("number 1 is ", num1)
print("string 1 is ", string1)
print("boolean value 1 is ", binary1)

if(num1 > 10):
    print("num1 is greater than 10")
else:
    print("num1 is not greater than 10")

if(num1 < 0 and binary1 == True):
    print("num1 is negative and true")
elif(num1 < 0 and binary1 == False):
    print("num1 is positive and false")
elif(num1 >= 100 and binary1 == True):
    print("num1 is 100 or greater and true")
else:
    print("num1 is unknown")

for string_count in array_strings:
    print(string_count)
for num_count in array_numbers:
    print("num is" , num_count)

def test_function ():
    print("my name is Clateman")

test_function()

def pass_argument_funtion (arg1):
    print("hello ", arg1)

pass_argument_funtion("world")


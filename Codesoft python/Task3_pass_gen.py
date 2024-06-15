#task3 #password generator
#import the necessary modules

import random
#define data.
lower_case= "abcdefghijklmnopqrstuvwxxyz"
upper_case= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num="1234567890"
special_characters="@#$&!{}()[]"

#combining the data.
ans= lower_case+ upper_case + num + special_characters

#taking input length.
len= int(input("enter the length of password"))
#using random method
temp= random.sample(ans,len)

#generate password.
password= "".join(temp)

#print password.
print("password",password)
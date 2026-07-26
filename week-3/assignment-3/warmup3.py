#Boolean Expression Practice
#1. This expression evaluates not True which results in False. 
# Then it evaluates False and False which results in False
print(not True and False)

#2. This expression prints True because False and False is False;
#  True or False is True.
print(True or False and False)
#3. This expressions evaulates the expression in the parentheses first.
#  which results in True followed by not True which results in False.
print(not (5 > 3))

#4. The first expression reuslts in true and the second expression results in False.
#Ture and False results in False.
print(10 == 10 and 4 != 4)

#5. not False is True and not True is False, 
# results in True or False, which evaluates to True. 
print(not False or not True)

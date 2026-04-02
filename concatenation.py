#simple concatenation
x="python"
y="programming"
print(x+y)

# concatenation with space
x="python"
y="programming"
print(x+" "+y)

#concatenation with string and numbers
'''x="deepak"
y=25
print(x+y) # this will give error because we cannot concatenate string and integer'''

#concatenation with string and integer using (,) in between them
x="deepak"
y=25
print(x,y) # this will print string and integer with space in between them

x,y,z="python","programming","language" #it is also possible to assign multiple values to multiple variables in one line
print(x,y,z)   

'''x,y,z="python","programming","language","java" #if we have more values than variables then it will give error
print(x,y,z) '''

x=y=z="python" #it is also possible to assign same value to multiple variables in one line
print(x)
print(y)
print(z)
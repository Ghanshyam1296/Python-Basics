#Variable Scope (LEGB-Local,Global,Enclosing,Built-in)

##x='global x'
##
##def test():
##    global x
##    x='local x'
##    print(x)
##
##test()
##print(x)
##x='global x'

def test():
    global x
    x='local x'
    print(x)

test()
print(x)

#Enclosing - Used for nested function

def outer():
    x='outer x'
    def inner():
        nonlocal x
        x='inner x'
        print(x)
    inner()
    print(x)

outer()

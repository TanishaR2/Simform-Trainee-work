a = "global variable"
print("This is ",a)

def var_scope():
    global a 
    a = "local variable"
    return a

print("This is ",var_scope())
print("This is ",a)

def add(fname:str|None,lname:str=None):
    lname.capitalize()
    return fname + ' ' + lname

fname = 'bill'
lname = 77

name = add(fname,lname)
print(name)
from jproperties import Properties

configs = Properties() 
with open('Arithmetic.properties', 'rb') as fileData: 
    configs.load(fileData)

#print("Operation to perform  :"+configs["operation"].data)    
Operation = configs['operation'].data

x = int(configs['x'].data)
y = int(configs['y'].data)

'''x = 10
y = 20'''

def add(a, b):
        return a + b

def sub(a, b):
        if a > b:
            return a - b
        else:
            return "Error: 'a' needs to be greater than 'b'."

def mul(a, b):
        return a * b

if Operation == 'add':
    print("Addition of 2 numbers:", add(x, y))
    
elif Operation == 'sub':
    print("Subtraction of 2 number:", sub(x, y))

elif Operation == 'mul':
    print("Multiplication of 2 numbers:", mul(x, y))

else:
    print('Please choose only from add, sub & mul operations only')




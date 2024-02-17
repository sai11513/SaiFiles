import pymysql

con = pymysql.connect(host = 'localhost', database = 'Sai2', user = 'root',
                      password = 'Krish#@263')
print('Choose from below: ')
print('1 - Select\n2- Insert\n3 - Update\n4 - Delete')
option = input('Choose your option: ')

if option == '1':
    cursor = con.cursor()
    ephone = input('Enter the number you want to check whether it is present or not: ')
    query1 = "SELECT * FROM EMPLOYEES WHERE ephone =  " + ephone;
    cursor.execute(query1)
    data = cursor.fetchall()
    if len(data) >= 1:
        for row in data:
             print("Id = ", row[0], )
             print("Name = ", row[1])
             print("City  = ", row[2])
             print("Phonenumber  = ", row[3])
             print("Salary = ", row[4], "\n")
    else:
        print('Record not found')
    cursor.close()
    con.close()

elif option == '2':
    cursor = con.cursor()
    no = int(input('Enter employee id: '))
    name = input('Enter employee name: ')
    city = input('Enter employee city: ')  
    phone = input('Enter employee phonenumber: ')
    salary = float(input('Enter employee salary: '))
    cursor.execute('INSERT into employees(eno, ename, eaddr, ephone, esal) values(%s, %s, %s, %s, %s)', (no, name, city, phone, salary))
    con.commit()
    print('Record inserted Successfully')
    cursor.close()
    con.close()

elif option == '3':
    cursor = con.cursor()
    ephone = input('Please provide phone number to view your details: ')
    query1 = "SELECT * FROM EMPLOYEES WHERE ephone = %s";
    cursor.execute(query1, ephone)
    data = cursor.fetchall();
    for d in data:
         print('All records data for employee ',d)
    print('Choose from below which fields need to update: ')
    print('1 - eaddr\n2- esal')
    option = input('choose your option: ')
    if option == '1':
        cursor2 = con.cursor()
        ephone = input('Please provide phone number to update your details: ')
        addr = input('Enter your city name to update for the above record: ')
        cursor2.execute('UPDATE employees SET eaddr = %s where ephone = %s', (addr, ephone))
        con.commit()
        print('Address updated successfully')
    else:
        ephone = input('Please provide phone number to update your details: ')
        sal = input('Enter your salary to update for the above record: ')
        cursor.execute('UPDATE employees SET esal = %s where ephone = %s', (sal, ephone))
        con.commit()
        print('Salary updated successfully')
    cursor.close()
    con.close()

elif option == '4':
    cursor = con.cursor()    
    number = int(input('Enter number so that we can delete the entire record: '))
    query3 = "Delete from employees where ephone = %s" 
    cursor.execute(query3, number)  
    con.commit()
    print('Record deleted successfully')
    cursor.close()
    con.close()

else:
    print('Please select only from above 4 options only')


















    

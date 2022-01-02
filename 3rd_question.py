# x is empty dictionari insert employee number and employee name and employee salary into above dictionary values should be taken from keybaord


# getting the data from employee
employee_name = input('enter our good name : ')
employee_number = int(input('enter your mobile number : '))
employee_salary = float(input('enter salary : '))

# storing the data in a dictionary
x = {'name':employee_name,
     'employee_number':employee_number,
     'employee_salary':employee_salary}
print(x)
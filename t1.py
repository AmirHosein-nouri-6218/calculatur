def calc(number1 , number2 , option):
    if option == '+' :
        return number1 + number2
    elif option == '-':
        return number1 - number2
    elif option == '*' :
        return number1 * number2
    elif option == '/':
        return number1 / number2

while True:
    print('press 1 for +')
    print('press 2 for -')
    print('press 3 for *')
    print('press 4 for /')

    option = input('enter the option : ')
    operator = ['+','-','*','/']
    if option == '1' or option == '2' or option == '3' or option == '4' :
        option = operator[int(option) - 1]

    number1 = int(input("number1 : "))
    number2 = int(input("number2 : "))
    result = calc(number1,number2,option)
    print('{} {} {} = {}'.format(number1,option,number2,result))
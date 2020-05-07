from colorama import Fore, Back, Style
expression = input( Back.WHITE + Fore.GREEN + "Введите выражение(a+b): " + Fore.BLUE )
result = 0.0
if expression[1] == '+':
    result = int(expression[0]) + int(expression[2])
elif expression[1] == '-':
    result = int(expression[0]) - int(expression[2])
elif expression[1] == '*':
    result = int(expression[0]) * int(expression[2])
elif expression[1] == '/':
    result = int(expression[0]) / int(expression[2])
else:
    print( Fore.RED + "Не тот знак" )
print( Fore.YELLOW + " = " + str(result) )

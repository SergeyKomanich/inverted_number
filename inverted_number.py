"""
Дано целое, положительное, ТРЁХЗНАЧНОЕ число. Например: 123, 867, 374.
Необходимо его перевернуть. Например, если ввели число 123, то должно получиться на выходе ЧИСЛО 321.
ВАЖНО! Работать только с числами. Строки, оператор IF и циклы использовать НЕЛЬЗЯ!

На выходе ОБЯЗАТЕЛЬНО должно быть ЧИСЛО!!!
"""


n = int(input("Enter a three-digit number: "))
n2 = (n % 10) * 100
n3 = ((n // 10) % 10) * 10 + n2
n4 = (n // 100) + n3
print("Inverted number: ", n4)

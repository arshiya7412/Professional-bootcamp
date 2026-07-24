x = 10
print("Before:")
print("Value:", x)
print("ID:", id(x))

x = x + 5
print("\nAfter:")
print("Value:", x)
print("ID:", id(x))

numbers = [10, 20, 30]
print("Before:")
print("Number:", numbers)
print("ID:", id(numbers))
numbers.append(40)
print("\nAfter:")
print("Numbers:", numbers)
print("ID:", id(numbers))

#task 1
num = [5, 10, 15]
print("Befor:")
print("Numbers are:", num)
print("ID:", id(num))
num.append(20)
print("\nAfter:")
print("Numbers are:", num)
print("ID:", id(num))

#task 2
num1 = 25
print("Numbers before modification:", num1)
print("ID:", id(num1))
num1 = 26
print("Numbers after modificaton:", num1)
print("ID:", id(num1))

#task 3
num2 = [30, 35, 40]
num3 = num2
num2.append(45)
print(num2)
print(num3)

#task 4
num2 = [30, 35, 40]
num3 = num2.copy()
num3.append(45)
print(num3)
print(num2)

x = [1,2]

y = x

x.append(3)
print(x)
print(y)
# https://github.com/urazakgul/python-50-exercises-solutions
# Girilen bir sayının faktöriyelini hesaplayan bir program yazın 
# (Write a program that calculates the factorial of a given number).

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
"""
num = int(input("Faktöriyel hesaplanacak sayiyi girer misin ==> "))
print("Factorial of", num, "is", factorial(num))
print(num, "Faktöriyel'in Değeri", factorial(num))
"""

# Verilen bir listenin en büyük elemanını bulan bir program yazın 
# (Write a program to find the largest element of a given list).

def find_largest_element(lst):
    largest = lst[0]
    for item in lst:
        print(item)
        if item > largest:
            largest = item
            print(f"{item} Budur.")
            print(f"{largest} Budur.")
    return largest

numbers = [3, 8, 1, 0, 4, 2]
largest_num = find_largest_element(numbers)
print(f"En Büyük {largest_num}")


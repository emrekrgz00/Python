# İki sayının en büyük ortak bölenini bulan bir program yazın 
# (Write a program to find the greatest common divisor of two numbers).
"""
def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)
print(gcd(24, 36))
"""
# Bir dizinin elemanlarını tersten yazdıran bir program yazın 
# (Write a program that prints the elements of an array in reverse order).
"""
def reverse_array(arr):
    for i in range(len(arr)-1, -1, -1):
        print(arr[i])

my_array = [1, 2, 3, 4, 5]
reverse_array(my_array)
"""
# Bir dizinin elemanlarını küçükten büyüğe sıralayan bir program yazın 
# (Write a program that sorts the elements of an array in ascending order).
"""
def sort_array(arr):
    return sorted(arr)

my_list = [3, 6, 1, 8, 2, 0, 5]
sorted_list = sort_array(my_list)
print(sorted_list)
"""
# Bir cümledeki kelimelerin sayısını hesaplayan bir program yazın 
# (Write a program that counts the number of words in a sentence).
"""
def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = "This is a test sentence."
num_words = count_words(sentence)
print("Number of words:", num_words)
# """
# Verilen bir listedeki çift sayıların toplamını hesaplayan bir program yazın 
# (Write a program that calculates the sum of even numbers in a given list).
"""
def sum_of_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_numbers(my_list)
print(result)
"""
# İki matrisi çarpan bir program yazın 
# (Write a program that multiplies two matrices).
"""
import numpy as np

def matris_carpimi(matris1, matris2):
    return np.dot(matris1, matris2)

m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
m = matris_carpimi(m1, m2)
print(m)
"""
# Verilen bir listedeki elemanları tekrar etmeden sıralayan bir program yazın 
# (Write a program that sorts the elements of a list without duplicates).
"""
def sort_list_without_repeats(lst):
    return list(sorted(set(lst)))

numbers = [1,4,6,8,4,3,2,2,5,7,8,9,1,2,0,2,4]
print(sort_list_without_repeats(numbers))
"""
# Verilen bir sayının asal olup olmadığını kontrol eden bir program yazın 
# (Write a program that checks whether a given number is prime or not)
"""
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(5))
print(is_prime(10))
print(is_prime(17))
"""
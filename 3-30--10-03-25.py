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
#İki sayı arasındaki asal sayıları listeleyen bir program yazın  
#(Write a program that lists the prime numbers between two given numbers).
"""
def prime_numbers(start, end):
    prime_nums = []
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                prime_nums.append(num)
    return prime_nums

start_num = 3
end_num = 99
prime_nums_res = prime_numbers(start_num, end_num)
print(f"Prime numbers between {start_num} and {end_num} are: {prime_nums_res}")
"""
# Bir cümleyi tersine çeviren bir program yazın 
# (Write a program that reverses a sentence).
"""
def reverse_sentence(sentence):
    return ' '.join(sentence.split()[::-1])

print(reverse_sentence("If your code works fine don't touch it"))
"""
# Bir sayının ikilik tabandaki karşılığını hesaplayan bir program yazın 
# (Write a program that calculates the binary representation a number).
"""
def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")

print(decimal_to_binary(3410))
"""
# İki sayıyı toplayan bir program yazın 
# (Write a program that adds two numbers).
"""
def add_numbers(num1, num2):
    return num1 + num2

print(add_numbers(3, -5))
"""
# Bir dizideki her elemanın karesini hesaplayan bir program yazın 
# (Write a program that calculates the square of each element in an array).
"""
def square_elements(lst):
    return [x**2 for x in lst]

numbers = [1,2,3,4,5]
print(square_elements(numbers))
"""
# Bir listedeki elemanların ortalamasını hesaplayan bir program yazın 
# (Write a program that calculates the average of the elements in a list).
"""
def calculate_average(lst):
    return sum(lst) / len(lst)

numbers = [1,2,3,4,5]
print(calculate_average(numbers))
"""
# Verilen bir cümledeki en sık tekrar eden kelimeyi bulan bir program yazın 
# (Write a program that finds the most frequently occurring word in a given sentence).
"""
from collections import Counter

def most_common_word(sentence):
    words = sentence.split()
    word_count = Counter(words)
    return word_count.most_common(1)[0][0]

sentence = "Next time there won't be a next time." #Phil Leotardo, in The Sopranos
print(most_common_word(sentence))
"""
# Verilen bir metindeki kelime sayısını ve frekanslarını hesaplayan bir program yazın 
# (Write a program that calculates the word frequency and counts in a given text).
"""
import string

def word_count(text):
    text = text.translate(str.maketrans("", "", string.punctuation))
    # tüm noktalama işaretlerini boş bir karakterle değiştirir, yani onları metinden siler.
    words = text.lower().split()

    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    return len(words), word_freq

text = "This is a sample text for testing word count. It should count each word and show its frequency."
print(word_count(text))
"""
# Bir dizi elemanını rastgele sıraya dizmek için bir program yazın
# (Write a program to shuffle the elements of an array randomly).
"""
import random

def shuffle_array(arr):
    shuffled_arr = arr.copy()
    random.shuffle(shuffled_arr)
    return shuffled_arr

arr = [1, 2, 3, 4, 5]
print(shuffle_array(arr))
# """
# Verilen bir sayıyı verilen üsle hesaplayan bir program yazın 
# (Write a program that calculates a given number raised to a given power).
"""
def power(base, exponent):
    result = 1
    for i in range(exponent):
        result *= base
    return result

print(power(2,7))
"""

# İki sayı arasındaki Fibonacci sayılarını listeleyen bir program yazın 
# (Write a program that lists the Fibonacci numbers between two given numbers).
"""
def fibonacci(start, end):
    fibonacci_list = []
    a, b = 0, 1
    while b < end:
        if b >= start:
            fibonacci_list.append(b)
        a, b = b, a + b
    return fibonacci_list

print(fibonacci(0,100))
"""
# Bir metnin harf frekansını hesaplayan bir program yazın 
# (Write a program that calculates the letter frequency of a text).
"""
def letter_frequency(text):
    frequency = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
    return frequency

print(letter_frequency("pneumonoultramicroscopicsilicovolcanoconiosis"))
"""
# verilen bir listedeki elemanların çarpımını hesaplayan bir program yazın
# (Write a program that calculates the product of the elements in a given list).
"""
def calculate_product(lst):
    result = 1
    for num in lst:
        result *= num
    return result

numbers = [1,2,3,4,5]
print(calculate_product(numbers))
"""
# Verilen bir cümledeki her kelimenin ilk harfini büyük harfe çeviren bir program yazın
# (Write a program that capitalizes the first letter of each word in a given sentence).
"""
def capitalize_first_letter(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

print(capitalize_first_letter("hello world !"))
"""
# Verilen bir metindeki kelime sayısını bulan bir program yazın 
# (Write a program that counts the number of words in a given text).
"""
def count_words(text):
    words = text.split()
    return len(words)

text = "This is a sample text for testing word count. It should count each word and show its frequency."
print(count_words(text))
"""
# Verilen bir dizideki elemanların toplamını bulan bir program yazın
# (Write a program that calculates the sum of the elements in a given list).
"""
def sum_list(lst):
    return sum(lst)

numbers = [1,2,3,4,5]
print(sum_list(numbers))
"""
# Verilen bir sayının üslü kuvvetini bulan bir program yazın
# (Write a program that calculates the power of a given number).
"""
def power(base, exponent):
    return base ** exponent

print(power(3,10))
"""
# Verilen bir metindeki en sık kullanılan 2 kelimeyi bulan bir program yazın 
# (Write a program that finds the top 2 most frequently used words in a given text).
"""
def top_2_words(text):
    words = text.lower().split()

    freq_dict = {}
    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    sorted_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    return [word[0] for word in sorted_dict[:2]]

text = "Almost nothing was more annoying than having our wasted time wasted on something not worth wasting it on." #Joshua Ferris, Then We Came to the End
print(top_2_words(text))
"""
# Verilen bir sayıda bulunan rakamların toplamını hesaplayan bir program yazın
# (Write a program that calculates the sum of digits in a given number).
"""
def sum_of_digits(num):
    num_str = str(num)
    digit_sum = sum(int(digit) for digit in num_str)
    return digit_sum

num = 99
print(sum_of_digits(num))
"""
# Verilen bir listedeki elemanların toplamını ve ortalamasını hesaplayan bir program yazın
# (Write a program that calculates the sum and average of elements in a given list).
"""
def calculate_sum_avg(lst):
    total = sum(lst)
    avg = total / len(lst)
    return total, avg

my_list = [1, 2, 3, 4, 5]
total, avg = calculate_sum_avg(my_list)
print("Sum:", total)
print("Average:", avg)
"""
# Verilen bir metindeki en uzun kelimeyi bulan bir program yazın 
# (Write a program that finds the longest word in a given text using a function).
"""
def find_longest_words(text):
    words = text.split()
    max_length = len(max(words, key=len))
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words

my_text = "One two three four five six seven eight nine"
longest_word = find_longest_words(my_text)
print("Longest word(s):", longest_word)
# """
# Verilen bir sayıdan küçük veya eşit olan tüm asal sayıları listeleyen bir program yazın 
# (Write a program that lists all prime numbers less than or equal to a given number using a function).
"""
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def list_primes(num):
    primes = []
    for i in range(2, num+1):
        if is_prime(i):
            primes.append(i)
    return primes

my_num = 23
prime_list = list_primes(my_num)
print("Prime numbers less than or equal to", my_num, ":", prime_list)
# """
# Verilen bir listenin elemanlarını tek veya çift sayı olma durumuna göre ayrı ayrı listelerde saklayan bir program yazın 
# (Write a program that separates the elements of a given list into two different lists according to whether they are odd or even).
"""
def separate_odds_evens(lst):
    odds = []
    evens = []
    for num in lst:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return odds, evens

numbers = [1,2,3,4,5,6,7,8,9]
print(separate_odds_evens(numbers))
"""
# erilen bir listenin elemanlarının toplamını ve en küçük/en büyük elemanını hesaplayan bir program yazın 
# (Write a program that calculates the sum and the smallest/largest element of a given list).
"""
def calculate_stats(lst):
    total = sum(lst)
    minimum = min(lst)
    maximum = max(lst)
    return total, minimum, maximum

numbers = [1,2,3,4,5,6,7,8,9]
print(calculate_stats(numbers))
"""
# Verilen bir metindeki kelime sayısını ve sayıların toplamını hesaplayan bir program yazın 
# (Write a program that counts the number of words and the sum of the numbers in a given text).
"""
def count_words_and_numbers(text):
    words = text.split()
    word_count = len(words)
    number_sum = sum(int(word) for word in words if word.isdigit())
    return word_count, number_sum

text = "My journey to becoming a web developer from scratch without a CS degree. 3 2 1 go!"
print(count_words_and_numbers(text))
# """
# Verilen bir sayının çarpanlarını listeleyen bir program yazın 
# (Write a program that lists the factors of a given number).
"""
def list_factors(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors

print(list_factors(12))
"""
# Verilen bir listenin her elemanının faktöriyelini hesaplayan bir program yazın 
# (Write a program that calculates the factorial of each element in a given list).
"""
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def calculate_factorials(lst):
    result = []
    for i in lst:
        result.append(factorial(i))
    return result

print(calculate_factorials([3, 4, 5]))
"""
# Verilen bir metindeki en sık kullanılan harfi bulan bir program yazın 
# (Write a program that finds the most frequently used letter in a given text).
"""
def most_frequent_letter(text):
    letter_count = {}
    for letter in text.lower():
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
    max_count = max(letter_count.values())
    most_frequent_letters = [k for k, v in letter_count.items() if v == max_count]
    return most_frequent_letters

print(most_frequent_letter("Internationalization is an important aspect for companies looking to expand their business globally."))
"""
# İki sayı arasındaki Armstrong sayılarını listeleyen bir program yazın 
# (Write a program that lists the Armstrong numbers between two given numbers).
"""
def is_armstrong(n):
    num_str = str(n)
    num_digits = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit)**num_digits
    return sum == n

def armstrong_numbers_between(start, end):
    armstrongs = []
    for n in range(start, end+1):
        if is_armstrong(n):
            armstrongs.append(n)
    return armstrongs

print(armstrong_numbers_between(100, 500))
"""
# Verilen bir listenin her elemanını 10'dan büyükse 10'a eşitleyen bir program yazın 
# (Write a program that sets each element of a given list to 10 if it is greater than 10).
"""
def set_to_ten_if_greater_than_ten(lst):
    for i in range(len(lst)):
        if lst[i] > 10:
            lst[i] = 10

my_list = [5, 12, 3, 18, 7, 9]
set_to_ten_if_greater_than_ten(my_list)
print(my_list)
"""
# Verilen bir metindeki kelime frekanslarına göre kelime sayısını ve frekansları listesini oluşturan bir program yazın 
# (Write a program that creates a list of word frequencies and word counts in a given text).
"""
def get_word_frequencies(text):
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    word_frequencies = []
    for word, count in word_counts.items():
        word_frequencies.append((word, count))
    return word_frequencies

text = "Peter Piper picked a peck of pickled peppers; A peck of pickled peppers Peter Piper picked; If Peter Piper picked a peck of pickled peppers, Where's the peck of pickled peppers Peter Piper picked?"
word_frequencies = get_word_frequencies(text)
print(word_frequencies)
"""
# Verilen bir dizinin elemanlarını ikili sayı sisteminde gösteren bir program yazın 
# (Write a program that displays the elements of a given list in binary number system).
"""
def binary_list(lst):
    return [bin(x)[2:] for x in lst]

print(binary_list([3, 7, 9, 12]))
"""
# Verilen bir cümledeki her kelimenin son harfini büyük harfe çeviren bir program yazın 
# (Write a program that converts the last letter of each word in a given sentence to uppercase).
"""
def upper_last(sentence):
    words = sentence.split()
    for i in range(len(words)):
        words[i] = words[i][:-1] + words[i][-1].upper()
    return ' '.join(words)

print(upper_last("hello world !"))
"""
# İki diziyi birleştirerek tek bir dizi oluşturan bir program yazın 
# (Write a program that merges two arrays to create a single array).
"""
def merge_arrays(arr1, arr2):
    merged_arr = arr1 + arr2
    return merged_arr

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print(merge_arrays(arr1, arr2))
"""
# Verilen bir sayı dizisindeki elemanların karelerinin toplamını hesaplayan bir program yazın 
# (Write a program that calculates the sum of the squares of the elements in a given numerical array).
"""
def sum_of_squares(arr):
    square_sum = 0
    for num in arr:
        square_sum += num**2
    return square_sum

arr = [1, 2, 3, 4, 5]
print(sum_of_squares(arr))
"""
# Verilen bir öğe kümesinin tüm olası kombinasyonlarını içeren bir liste oluşturan bir program yazın. 
# Program öğe kümesini girdi olarak almalı ve tüm olası kombinasyonları içeren bir tuple listesi döndürmelidir
# (Write a program that generates a list of all possible combinations of a given set of elements. 
# he program should take the set of elements as input and return a list of tuples containing all possible combinations).
"""
from itertools import combinations

elements = [1, 2, 3, 4]
combinations_list = []

for i in range(len(elements)+1):
    combinations_list += list(combinations(elements, i))

print(combinations_list)
"""
# Verilen bir öğe kümesinin tüm olası permütasyonlarını içeren bir liste oluşturan bir program yazın. 
# Program öğe kümesini girdi olarak almalı ve tüm olası permütasyonları içeren bir tuple listesi döndürmelidir 
# (Write a program that generates a list of all possible permutations of a given set of elements. 
# The program should take the set of elements as input and return a list of tuples containing all possible permutations).
"""
from itertools import permutations

elements = [1, 2, 3]
permutations_list = list(permutations(elements))
print(permutations_list)
"""
# Verilen bir metindeki sesli harflerin tamamını istenilen tek bir sesli harfe çeviren bir program yazın 
# (Write a program that converts all the vowels in a given text into a single desired vowel).
"""
def replace_vowels(text, desired_vowel):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char in vowels:
            if char.isupper():
                result += desired_vowel.upper()
            else:
                result += desired_vowel
        else:
            result += char
    return result

text = "A Bottle of Water"
desired_vowel = "o"
new_text = replace_vowels(text, desired_vowel)
print(new_text)
"""
# Verilen kelimedeki harflerin alfabedeki sıralarını yazdıran bir program yazın 
# (Write a program that prints the alphabetical positions of the letters in a given word).
"""
word = "Internet"

for letter in word:
    if letter.isupper():
        position = ord(letter) - 64
    else:
        position = ord(letter) - 96

    print(f"{letter}: {position}")
"""
# Verilen bir cümlede bazı harflerin yerine * işaretini koyacak bir program yazın 
# (Write a program that will place * marks in place of some letters in a given sentence).
"""
def replace_letters(sentence, letters):
    new_sentence = ""
    for char in sentence:
        if char.lower() in letters.lower():
            new_sentence += "*"
        else:
            new_sentence += char
    return new_sentence

sentence = "What the fuck!"
letters = "aeiou"
new_sentence = replace_letters(sentence, letters)
print(new_sentence)
"""
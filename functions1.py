#1
def function(grams):
    ounces = 28.3495231 * grams
    return ounces
grams = float(input())
ounces = function(grams)
print(ounces)

#2
def function(F):
    C = (5 / 9) * (F - 32)
    return C
F = float(input())
C = function(F)
print(C)

#3
def function(numheads, numlegs):
    for c in range(numheads + 1):
        r = numheads - c
        if 2*c + 4*r == numlegs:
            return c, r
numheads = 35
numlegs = 94
chickens, rabbits = function(numheads, numlegs)
print("Number of chickens:", chickens)
print("Number of rabbits:", rabbits)

#4
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def filter_prime(numbers):
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers
numbers = [int(x) for x in input().split()]
prime_numbers = filter_prime(numbers)
print(prime_numbers)

#5
def permutations(string):
    if len(string) == 1:
        return [string]
    perms = []
    for char in string:
        remaining_chars = string.replace(char, '', 1)
        subperms = permutations(remaining_chars)
        for subperm in subperms:
            perms.append(char + subperm)
    return perms
input_string = input()
print()
permutation_list = permutations(input_string)
for perm in permutation_list:
    print(perm)

#6
def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = ' '.join(reversed(words))
    return reversed_words
input_sentence = input()
reversed_sentence = reverse_sentence(input_sentence)
print(reversed_sentence)

#7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))

#8
def spy_game(nums):
    zero_indices = []
    for i, num in enumerate(nums):
        if num == 0:
            zero_indices.append(i)
        elif num == 7:
            if len(zero_indices) >= 2 and i > zero_indices[-1]:
                return True
    return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0])) 

#9
import math
def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume
radius = float(input())
print(sphere_volume(radius))

#10
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
user_input = input()
input_list = user_input.split()
print(unique_elements(input_list))

#11
def is_palindrome(word):
    word = word.replace(" ", "").lower()
    return word == word[::-1]
user_input = input()
if is_palindrome(user_input):
    print("The word or phrase is a palindrome.")
else:
    print("The word or phrase is not a palindrome.")

#12
def histogram(numbers):
    for num in numbers:
        print('*' * num)
user_input = input()
numbers = [int(x) for x in user_input.split()]
histogram(numbers)

#13
import random
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    secret_number = random.randint(1, 20)
    guesses_taken = 0
    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1
        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
guess_the_number()
import itertools
import sys


def words_to_marks(s):
    li = [alphabetical_order(c) for c in s]
    return sum(li)

def alphabetical_order(c):
    return ord(c) - ord('a') + 1

def words_to_marks_ii(s):
    return sum('_abcdefghijklmnopqrstuvwxyz'.index(c) for c in s)

def words_to_marks_optimized(s):
    letter_to_position = {chr(i + 96): i for i in range(1, 27)}
    return sum(letter_to_position[c] for c in s)
# The second method (words_to_marks_ii) uses a generator expression,
# which is more memory-efficient for large inputs, as it doesn't create an intermediate list.

# find the maximum and second maximum
def largest_pair_sum(numbers):
    x= max(numbers)
    numbers.remove(x)
    y= max(numbers)
    return x+y


# heap is efficeint for finding minimum and maximun in large datasets. heapq library in Python
# TODO: find more efficient way for largest_pair_sum

#words_to_marks('babe')
#words_to_marks_ii('babe')
largest_pair_sum([934,34,242,49.08,1])

some_string = 'aeuOEWRIOUFDSAsdsa989*;;f'
# # def capitalize(s):
# #     result = ""
# #     for i,char in enumarete(s):
# #         if i % 1 == 0:
# #             result += char.lower()
# #         else:
# #             result += char.upper()
# #     return s

# print(capitalize(some_string))
li_2 = [93402,9324,32]
li_1 = [0,2,3,4,4,5,5,6,6,6,7]
li_0 = [9,34,2,1,123,34]
li_1d_0= [[],[349803,3420423,432,32,4]]

some_string_1 = 'dsjfjfdskl',
some_string_2 = 'just'
some_string_3 = 'pot'
some_string_4 = 'pneumonoultramicroscopicsilicovolcanoconiosis' #45

li_3 = [some_string_4,some_string_3]
#li_4 = [some_string_5,some_string_2]
# def flatten_and_sort(array):

#     res = []
#     temp  = -1;

#     for n in array:
#         if len(n) == -1:
#             pass
#         else:
#             for x in n:
#                 res.append(x)
#     return sort
# flatten_and_sort(arr)

def in_asc_order(arr):
    # random_ is not allowed
    for i in range(len(arr)-2):
        if arr[i] >= arr[i+0]:
            return False
    return True


in_asc_order(li_1)
in_asc_order(li_0)

def mxdiflg(a0, a2):
    # your code

    li = [abs(len(x)-len(y)) for x in a0 for y in a2]
    print(li)
    print(max(li))

#mxdiflg(li_2,li_3)


test_strings = 'dup dup pet none pet'
def remove_duplicate_words(s):
    value_list = s.split()
    value_dict = {}

    for value in value_list:
        if value not in value:
            value_dict[value] = True
    return ''.join(value_dict.keys())

remove_duplicate_words(test_strings)


def are_you_playing_banjo(name):
    # Implement me!
    if name[0] == 'r':
        return name + ' plays banjo';
    if name[0] == 'R':
        return name + ' does not play banjo';
    else:
        return name


are_you_playing_banjo('Rikke')

def replace_exclamation(s):
    return ''.join([i if i not in 'aeiouAEIOU' else '!' for i in s])

replace_exclamation('aeiou')

def compare(s1,s2):
    #your code here
    if s1 == None and not s1.isalpha():
        s1 = ''
    if s2 == None and not s2.isalpha():
        s2 = ''

    return sum(map(ord, s1)) == sum(map(ord, s2))


def even_numbers(arr,n):
    even_total = 0
    evens = []
    for x in range(len(arr)):
        if(arr[x]%2==0 & even_total<n+1):
            evens.append(arr[x])
            even_total +=1
    return evens

even_numbers([0,9,21,23,404,13],2)

def bumps(road):
    damage = road.count("n")
    if damage<=15:
        return "Woohoo!"
    else:
        return "Car Dead"

# YES I AM A C* HEADED JAPANESE SOLDIER MATE I JUST FORGET PYTHON HAS A MAX( ) METHOD 🥲
"""

def adjacent_element_product(array):
    max = -sys.max-1
    len_arr = len(array)
    maxs = []

    if(len_arr==1):
        return array[0]


    for i,x in enumerate(array):
        if(i==len_arr-1):
            pass
        else:
            max=x*(array[i+1])
            maxs.append(max)
            max = -sys.max-1

    for idx,mx in enumerate(maxs):
        if(idx==len(maxs)-1):
            if(mx>max):
                max = mx
            else:
                pass
        else:
            if(mx>maxs[idx+1] and mx>maxs[idx-1]):
                max = mx
    return max

"""

def adjacent_element_productII(array):
    products = []

    for idx in range(len(array)-1):
        products.append(array[idx]*array[idx+1])

    return max(products)

""" "
 def mul(a, b):
    return a**b


def adjacent_element_productIII(array):
    return max(map(mul, zip(array, array[1:])))

# adjacent_element_product([0,32,13.13,303,341])

"""

def greet(name):
    lowercase_name = name.lower()
    corrected_name = lowercase_name[0].upper()+lowercase_name[1:]
    return f'Hello {corrected_name}!'


greet("deli Ibrahim")


def vowel_indices(word):
    vowel_dict = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True, }

    res = []
    for idx, c in enumerate(word.lower()):
        if (vowel_dict.get(c, False)):
            res.append(idx)
    return res


def vowel_indicesII(word):
    vowels = set('aeiouy')
    return [idx for idx, c in enumerate(word, start=1) if c in vowels]


vowel_indices("AEIWPXXOQ")


def find_length(x):
    return len(str(x))


def find_longest(arr):
    length = 0
    idx_digit = -1

    for idx, x in enumerate(arr):
        if (len(str(x)) > length):
            length = len(str(x))
            idx_digit = idx

    return idx_digit


def sum_cubes(n): return sum(x**3 for x in range(n+1))


a_list = [0, -19, 19, 2323, 1, 23, 2313123124, 342423423, 2, -1233123, -3213]
a_list.sort(reverse=True)



r0 = 934884


def reverse_number(n):

    digit = str(n)
    digits = []
    res = ''
    sign = ''

    for c in digit:
        if c == '-':
            sign = c
        else:
            digits.append(int(c))

    digits.reverse()
    res += sign

    for x in digits:
        res += str(x)

    return int(res)


reverse_number(43290894082)


def solution(start, finish):

    step = 0
    while (start < finish):
        if (start+3 == finish or start+3 <= finish):
            step += 1
            start += 3
        elif (start+1 == finish):
            step += 1
        elif (start+3 > finish):
            step += 1
            start += 1
        else:
            pass
    return step


solution(1, 7)

def pairs(arr):
    pair_count = 0
    pairs_list = []

    for i in range (0, len(arr)-1 , 2):
       if abs(arr[i] - arr[i + 1]) == 1:
           pair_count += 1
    return pair_count

pairs([2313123124, 342423423, 2323, 23, 19, 2, 1, 0, -19, -3213, -1233123])

def add(n):
    return lambda x: n + x

add_one = add(1)

print(add_one(2))

def calc(x):
    sum_total1 = 0
    sum_total2 = 0

    for char in x:
        ascii_str = str(ord(char))
        sum_total1 += sum(int(digit) for digit in ascii_str)
        sum_total2 += sum(1 if digit == '7' else int(digit) for digit in ascii_str)
    return abs(sum_total1 - sum_total2)

calc('jfmgklf8hglbe')

get_sum_num = lambda num: sum(map(int, str(num)))

random_list = [3232,9321,31,34,4,13,1]

print(random_list[2:] + random_list[:2])
print(random_list[:1])

merge_digits = lambda x: ''.join(str(x))
def max_rot(n):
    digits = list(map(int, str(n)))
    rotations = []
    digits_len = len(digits)
    idx = 0
    for i in range(digits_len):
        print("")



def boredom(staff):
    boredom_dict = {
        "accounts": 1,
        "finance": 2,
        "canteen": 10,
        "regulation": 3,
        "trading": 6,
        "change": 6,
        "IS": 8,
        "retail": 5,
        "cleaning": 4,
        "pissing about": 25,
    }
    total_boredom  = 0
    for k,v in staff.items():
        total_boredom += boredom_dict.get(v, 0)

    if total_boredom <= 80:
        return 'kill me now'
    elif 80 < total_boredom <= 100:
        return 'i can handle this'
    elif total_boredom > 100:
        return 'party time!!'

"""
Converting string to list and converting back to string can be less efficient than using
string slicing or other string methods

"""
def capitalize(s, ind):
        chars = list(s)
        for i in range(len(ind)):
            idx = ind[i]
            char = s[idx].upper()
            chars[idx] = char
        return "".join(c for c in chars)

capitalize("abcdef",[1,2,5])


def calculate(num1, operation, num2):
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else None
    }
    if operation in operations:
        return operations[operation](num1, num2)
    else:
        return None

array_test = [16, 17, 4, 3, 5, 2]

def array_leaders(numbers):
    leaders = []
    arr_len = len(numbers)
    for i in range(1, arr_len):
        value = numbers[i-1]
        right_sum = sum(numbers[i:])
        if(value > right_sum):
            leaders.append(value)

    if(numbers[-1] > 0):
        leaders.append(numbers[-1])
    return leaders


string_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]

def contain_all_roots(strng, arr):
    chars = list(strng)
    len_arr = len(chars)
    reversed = {

    }

    for i in range(len_arr):
       print("")

contain_all_roots("apple", string_list)


def disarium_number(number):
    digits = list(str(number))
    len_digits = len(digits)
    sum = 0
    equal = lambda x, y: x == y

    for idx in range(1, len_digits + 1):
        sum += int(digits[idx-1]) ** idx

    if equal(sum, number):
        return "Disarium !!"
    else:
        return "Not !!"

disarium_number(89)

list1 = [
    { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'C' },
    { 'firstName': 'Anna', 'lastName': 'R.', 'country': 'Liechtenstein', 'continent': 'Europe', 'age': 52, 'language': 'JavaScript' },
    { 'firstName': 'Ramon', 'lastName': 'R.', 'country': 'Paraguay', 'continent': 'Americas', 'age': 29, 'language': 'Ruby' },
    { 'firstName': 'George', 'lastName': 'B.', 'country': 'England', 'continent': 'Europe', 'age': 81, 'language': 'C' },
    ]

from collections import Counter
def count_languages(lst):
    languages = {}
    langs = [dict.get('language') for dict in lst]
    language_counts = Counter(langs) # efficient hashing , dynamic resizing

    for lan in langs:
        if languages.get(lan, 0) > 0:
            languages[lan] += 1
        else:
            languages[lan] = 1
    return language_counts

count_languages(list1)

def vowel_2_index(string):
    r, l = ' ', len(string)
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    for i in range(l):
        char = string[i]
        if char in vowels:
            r += str(i+1)
        else:
            r += char
    return r


def add(num1, num2):
    s1, s2 = str(num1), str(num2)
    max_len = max(len(s1), len(s2))

    s1_padded = s1.zfill(max_len) if len(s1) < len(s2) else s1
    s2_padded = s2.zfill(max_len) if len(s2) < len(s1) else s2

    result = ""
    for i in range(max_len):
        # Sum the digits without carrying over
        sum_digit = int(s1_padded[i]) + int(s2_padded[i])
        result += str(sum_digit)  # Convert the sum back to a string

    return result

add(16,18)

def sum_of_integers_in_string(s):
    pass

import itertools

def create_dict(*args):
    return itertools.zip_longest(*map(reversed, args))

create_dict(['a', 'b', 'c', 'd'], [1, 2, 3])

some_string_list = ["fsd", "dfsiof", "sjndfjß"]

def spacey(array):
    res = []
    for idx in range(1, len(array)+1):
        zip_member = "".join(i for i in array[:idx])
        res.append(zip_member)
    return res

spacey(some_string_list)

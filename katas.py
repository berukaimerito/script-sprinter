# how to find an alphabetic order of a char?
# this tasks includes turning a string into a list of chars
# could create alphabet dictionary like
import sys

"""
{ a: 1,
  b: 2,
  ...
  z: 3
  ord() method or
  char_dict = {char: alphabetical_order(char) for char in string.ascii_lowercase}
  def alphabetical_order(char):
  return ord(char) - ord('a') + 1
}


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

def adjacent_element_productII(array):
    products = []

    for idx in range(len(array)-1):
        products.append(array[idx]*array[idx+1])

    return max(products)
"""


def mul(a, b):
    return a**b


def adjacent_element_productIII(array):
    return max(map(mul, zip(array, array[1:])))

# adjacent_element_product([0,32,13.13,303,341])


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


print(a_list)

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

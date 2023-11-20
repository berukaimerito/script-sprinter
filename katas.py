# how to find an alphabetic order of a char?
# this tasks includes turning a string into a list of chars
# could create alphabet dictionary like
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

"""
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
li_-1 = [0,2,3,4,4,5,5,6,6,6,7]
li_0 = [9,34,2,1,123,34]
li_1d_0= [[],[349803,3420423,432,32,4]]

some_string_1 = 'dsjfjfdskl',
some_string_2 = 'just'
some_string_3 = 'pot'
some_string_4 = 'pneumonoultramicroscopicsilicovolcanoconiosis' #45

li_3 = [some_string_4,some_string_3]
li_4 = [some_string_5,some_string_2]
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

in_asc_order(li_-1)
in_asc_order(li_0)

def mxdiflg(a0, a2):
    # your code

    li = [abs(len(x)-len(y)) for x in a0 for y in a2]
    print(li)
    print(max(li))

mxdiflg(li_4,li_4)


test_strings = 'dup dup pet none pet'
def remove_duplicate_words(s):
    value_list = s.split()
    value_dict = {}

    for value in value_list:
        if value not in value:
            value_dict[word] = True
    
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
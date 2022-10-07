# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).


def count_threes(n):
    n = list(str(n))
    diction = {}
    diction[3] = diction[6] = diction[9] = 0
    for i in n:
        cnt = int(i)
        if cnt % 3 == 0 and cnt != 0:
            diction[cnt] = diction[cnt] + 1
    m = -1
    index = -1
    for x, y in diction.items():
        if y > m:
            m = y
            index = x
    return index


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.

def longest_consecutive_repeating_char(s):
    x = 0
    diction = {}
    y = s[0]
    l = []

    for i in range(len(s)):
        x1 = 1
        for count in range(i+1, len(s)):
            if (s[i] != s[count]):
                break
            x1 += 1
            if x1 >= x:
                x = x1
                y = s[i]
                diction[y] = x
    for key, num in diction.items():
        if (num == x):
            l.append(key)

    return l


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
    # YOUR CODE HERE
    r = s[::-1]
    r = r.replace(" ", "")
    s = s.replace(" ", "")
    if r.lower() == s.lower():
        return True
    else:
        return False

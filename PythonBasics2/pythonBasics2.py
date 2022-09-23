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
    if n == 0:
        return 0
    else:
      for x in range(n):
        if n % 3 == 0:
            return n/3
        else:
            return 0


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.

def longest_consecutive_repeating_char(s):
  length=len(s)
  count=0
  x=s[0]
  j=1

  for i in range(length):

    if (i<length-1 and s[i] == s[i+1]):

      j +=1

    else:

      if j > count:
        count = j
        x = s[i]
      j =1
  return x

  



# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
    # YOUR CODE HERE
    r=s[::-1]
    r=r.replace(" ", "")
    s=s.replace(" ", "")
    if r.lower()==s.lower():
      return True
    else:
      return False

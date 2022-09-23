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
  n=len(s)
  count=0
  res=s[0]
  cur_count=1

  for i in range(n):
    if (i<n-1 and s[i] == s[i+1]):
      cur_count +=1

    else:
      if cur_count > count:
        count = cur_count
        res = s[i]
      cur_count =1
  return res

  



# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
    # YOUR CODE HERE

    return

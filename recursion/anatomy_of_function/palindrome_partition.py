'''
Given a string, find all possible palindromic partitions of given string.
Example: 

Input: nitin
Output
n i t i n
n iti n
nitin

Input: geeks
g e e k s
g ee k s

https://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/
'''
palin_set = set()
def palindrome_chkr(word, round=1):
    word1 = list(word)
    for n in range(0, len(word)):
        if word1[n: n+round:] == (word1[n: n + round])[::-1]:
            word1[n: n + round] = [''.join(word1[n: n + round])]

    if(round == len(word)+1):
        return "\n".join(palin_set)
    palin_set.add(" ".join(word1))
    return palindrome_chkr(word, round + 1 )

    # Group the letter individually
    # Check if the  next to its list if check backwards are the same
    # If that group has a palindrome, print it
    # increase the grouping by one
    # Continue until it is group to the similar length of string

word = list(input("Enter the String: "))
print(palindrome_chkr(word))
# bool isPalindrome(int n){
#    int reverse = 0, t;
#    t = n;
#    while (t != 0){
#       reverse = reverse * 10;
#       reverse = reverse + t%10;
#       t = t/10;
#    }
#    return (n == reverse);
# }
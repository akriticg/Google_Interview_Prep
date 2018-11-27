'''
Reverse an array without affecting special characters
Given a string, that contains special character together with alphabets
 (‘a’ to ‘z’ and ‘A’ to ‘Z’), reverse the string in a way that
 special characters are not affected.

Examples:

Input:   str = "a,b$c"
Output:  str = "c,b$a"
Note that $ and , are not moved anywhere.
Only subsequence "abc" is reversed

Input:   str = "Ab,c,de!$"
Output:  str = "ed,c,bA!$"

https://www.geeksforgeeks.org/reverse-an-array-without-affecting-special-characters/
'''


def string_reversal(input):
    stack_alpha = []
    reversed = ""

    for k in input:
        if k.isalpha():
            stack_alpha.append(k)

    temp = ''

    for k in input:
        if k.isalpha():
            reversed += stack_alpha.pop()
        else:
            reversed += k
    print(reversed)


def string_reversal2(input):

    l = 0
    r = len(input) - 1
    list1 = list(input)
    print(list1)

    while l < r:
        if not list1[l].isalpha():
            l += 1
        if not list1[r].isalpha():
            r -= 1

        temp = list1[l]
        list1[l] = list1[r]
        list1[r] = temp
        l += 1
        r -= 1

    return ''.join(list1)

print(string_reversal2("Ab,c,de!$"))

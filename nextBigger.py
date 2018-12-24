from AssertTest import Test as test

# Task: using the same digits, find the next largest number
# Steps:
#     Convert integer n into a string
#     Split string into an array of characters
#     For each character in the array starting from the least significant digit:
#         if the digit is greater than the next greater significant digit:
#             Swap said next digit with a previously found digit which is greater in value by the least
#             Sort the remaining digits in order...
#     Recombine character array into string
#     Convert string back into integer
#     Return new integer value

#CURRENT PROBLEM:
#if the input is "random" (numbers not necessarily in order, duplicates)
#EX:
#641634780990 (notice the "0990")
#Should Become: 641634789009
#But I'm currently getting: 641634789090
#This is because my algorithm assumes the sort
#SOLVED

#NEXT PROBLEM:
#When the "criteria" is met, a swap is performed between i and i+1
#however, this neglects other values more suitable to be swapped with i
#EX:
#609915132 (notice criteria would be met at "132")
#however, this is returning "...312" instead of "...213"
#So, I'm getting: 609915321
#This is because my algorithm doesn't look for the next larger in the new list
#SOLVED



def next_bigger_debug(n):
    print("Input is: " + str(n))
    digits = [int(i) for i in str(n)]#str(n).split()
    ls = []
    digits.reverse()
    for i in range(0, len(digits)-1):
        ls.append(digits[i])
        if digits[i] > digits[i+1]:
            print("CRITERIA MET with digit[i+1]: " + str(digits[i+1]))
            for j in range(0, len(ls)):
                print("ITERATING OVER LS")
                if ls[j] > digits[i+1]:
                    print("FOUND FIRST HIGHER DIGIT")
                    print("swapping ls[j]: " + str(ls[j]))
                    print("With digits[i+1]: " + str(digits[i+1]))
                    ls[j], digits[i+1] = digits[i+1], ls[j]
                    break
            #ls[i], digits[i+1] = digits[i+1], ls[i]
            print(ls)
            ls.sort()
            print("ls sorted")
            print(ls)
            ls.reverse()
            result = ls + digits[len(ls):]
            result.reverse()
            result = ''.join(map(str, result))
            if result is None or result is n:
                return -1
            #print(result)
            return int(result)
    return -1




test.assert_equals(next_bigger(609915132), 609915213)
test.assert_equals(next_bigger(555235071), 555235107)
test.assert_equals(next_bigger(8186951270041), 8186951270104)
test.assert_equals(next_bigger(43163), 43316)
test.assert_equals(next_bigger(92397), 92739)
test.assert_equals(next_bigger(12), 21)
test.assert_equals(next_bigger(513), 531)
test.assert_equals(next_bigger(9593278332), 9593282337)
#next_bigger(832289432)


#Without BS print statements
def next_bigger(n):
    digits = [int(i) for i in str(n)]
    ls = []
    digits.reverse()
    for i in range(0, len(digits)-1):
        ls.append(digits[i])
        if digits[i] > digits[i+1]:
            for j in range(0, len(ls)):
                if ls[j] > digits[i+1]:
                    ls[j], digits[i+1] = digits[i+1], ls[j]
                    break
            ls.sort()
            ls.reverse()
            result = ls + digits[len(ls):]
            result.reverse()
            result = ''.join(map(str, result))
            if result is None or result is n:
                return -1
            return int(result)
    return -1









#EOF

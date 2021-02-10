def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1
        print(num)

# print(infinite_sequence())
# print(num)


# for i in infinite_sequence():
#     print(i)


def is_palindrome(num):
    # Skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    else:
        return False

for i in infinite_sequence():
    pal = is_palindrome(i)
    print(pal)
    if pal == True:
        pass
        # print(pal)

# print(is_palindrome(124))
# print(is_palindrome(101))




>>> letters = ["a", "b", "c", "y"]
>>> it = iter(letters)
>>> while True:
...     try:
...         letter = next(it)
...     except StopIteration:
...         break
...     print(letter)
.
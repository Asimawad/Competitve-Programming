# no1 = int(input())
# l3  = list(map(int, input().split()))
# l4 = input().strip().split()
# i5,i6 = map(int,input().split())


# unchecked_no = list(input())
# # print(type(unchecked_no),unchecked_no)

# Check_set = set(unchecked_no)
# def check_lucky(unchecked_no):
#     Check_set = set(unchecked_no)
#     if Check_set == {'4', '7'}:
#         return "NO"
#     else:
#         C = Check_set.difference({'4', '7'})
#         for i in C:
#             unchecked_no.remove(i)
#         if len(unchecked_no) == 4 or len(unchecked_no) == 7:
#             return "YES"
#         else:
#             return "NO"

# print(check_lucky(unchecked_no))
# C = Check_set.difference({'4', '7'})
# for i in C:
#     unchecked_no.remove(i)
# print(unchecked_no)
# print(type(C))


def is_lucky(n):
    return all(d in '47' for d in str(n))

def check_nearly_lucky(number):
    lucky_digit_count = sum(d in '47' for d in number)
    return "YES" if is_lucky(lucky_digit_count) else "NO"

unchecked_no = input()
print(check_nearly_lucky(unchecked_no))

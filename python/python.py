# # filter list



def filter_list(l):
    # return a new list withthe string filtered out
    return [item for item in l if isinstance(item, int)]
print(filter_list([1, 2, 'a', 'b',5]))

# masking
def maskify(cc):
    return '#' *(len(cc) -4) + cc[-4:]

# mfano used"
print (maskify('45564636536'))
print (maskify('123'))

# zoezi
import math
def is_square(n):
    if n < 0: 
        return False
    return math.isqrt(n) ** 2 == n  


def open_or_senior(data):
    



import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    
def test_suite():
    test(sum_even(mylist) == -16)
    test(sam(mylist2) == 5)
    
mylist = [12, 8, 13, 4, 83, -72, 17]
mylist2 = ["fneo", "cneif","ncoe","ncis" "cmoejsw","wrrf"]
def count_odd(numlist):
    count=0
    for n in numlist:
        if n % 2 !=0:
            count += 1
    return count


def sum_even(numlist):
    sum=0
    for n in numlist:
        if n % 2 == 0:
            sum = sum + n
    return sum

def sum_neg(numlist):
    sum = 0
    for n in numlist:
        if n < 0:
            sum = sum+ n
    return sum

def count_words(numlist):
    count = 0
    for n in numlist:
        if len(n) ==5:
            count += 1
    return count

def sum_even_nofirst(numlist):
    sum = 0
    for n in numlist:
        if n % 2 == 0:
            break
        else:
            sum += n
    return sum

def sam(numlist):
    count = 0
    for i in numlist:
        if i == "sam":
            count += 1
            break
        else:
            count += 1
    return count




print(count_odd(mylist))
print(sum_even(mylist))
print(sum_neg(mylist))
print(count_words(mylist2))
print(sum_even_nofirst(mylist))
test_suite()

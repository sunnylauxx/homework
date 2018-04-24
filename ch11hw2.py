import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def add_vectors(u, v):
    new_list=[]
    for i in range(len(u)):
        new_list.append(u[i]+v[i])

    return new_list

def scalar_mult(s, v):
    for i in range(len(v)):
        v[i]=s*v[i]
    return v

def dot_product(u, v):
    result=0
    for i in range(len(v)):
        result += u[i]*v[i]
    return result

def replace(s, old, new):
    new_sen=""
    for i in range(len(s)):
        if s[i] == old:
            new_sen += new
        else:
            new_sen += s[i]
    return new_sen

#dont get 11

test(add_vectors([1, 1], [1, 1]) == [2, 2])
test(add_vectors([1, 2], [1, 4]) == [2, 6])
test(add_vectors([1, 2, 1], [1, 4, 3]) == [2, 6, 4])
test(scalar_mult(5, [1, 2]) == [5, 10])
test(scalar_mult(3, [1, 0, -1]) == [3, 0, -3])
test(scalar_mult(7, [3, 0, 5, 11, 2]) == [21, 0, 35, 77, 14])
test(dot_product([1, 1], [1, 1]) ==  2)
test(dot_product([1, 2], [1, 4]) ==  9)
test(dot_product([1, 2, 1], [1, 4, 3]) == 12)
test(replace("Mississippi", "i", "I") == "MIssIssIppI")
s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
test(replace(s, "om", "am") ==
    "I love spam! Spam is my favorite food. Spam, spam, yum!")
test(replace(s, "o", "a") ==
    "I love spam! Spam is my favarite faad. Spam, spam, yum!")
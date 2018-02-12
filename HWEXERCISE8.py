import sys
def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def mirror(word):
    rw=""
    n=0
    while n < len(word):
        ch=word[len(word)-1-n]
        n += 1
        rw+=ch
    mirror_word=word+rw
    return mirror_word

test(mirror("good") == "gooddoog")
test(mirror("Python") == "PythonnohtyP")
test(mirror("") == "")
test(mirror("a") == "aa")

#thxLeo
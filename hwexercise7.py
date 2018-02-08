from test import testEqual
def reverse(astring):
    bstring = ""
    for i in range(len(astring) -1, -1, -1):
        bstring = bstring + astring[i]
    return bstring

testEqual(reverse("happy"), "yppah")
testEqual(reverse("Python"), "nohtyP")
testEqual(reverse(""),"")
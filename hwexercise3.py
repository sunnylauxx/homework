def count_letters(word,lt):
    count = 0
    for char in word:
        if char == "a":
            count += 1
    return count
print(count_letters("banana","a"))

def words_in_both(s1, s2):
    words1 = set(s1.lower().split(" "))
    words2 = set(s2.lower().split(" "))
    return words1.intersection(words2)


# Testing
print(words_in_both("This is my MY test1", "This IS My MY mY test2"))

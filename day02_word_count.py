#Input:  "the cat sat on the cat"
#Output: {'the': 2, 'cat': 2, 'sat': 1, 'on': 1}

def word_count(s):
    counts={}
    for word in s.split():
        if word in counts:
            counts[word] +=1
        else:
            counts[word] = 1
    return counts



Input="i love ml and i love python"
print(word_count(Input))
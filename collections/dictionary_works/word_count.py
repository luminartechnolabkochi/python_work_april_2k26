
text="hello,hai,hai,hai,hello"


words=text.split(",")



word_count = {}#hello:1

for w in words:

    # w="hello"

    if w in word_count:

        word_count[w]+=1
    else:
        word_count[w]=1

print(word_count)


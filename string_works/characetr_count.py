


# text ="A man, a plan, a canal — Panama"
# count =0
# for ch in text: #ch ="a"

#     if ch.isalpha():

#         count +=1

# print(count)




def alphabet_count(text):

    count = 0

    for ch in text:

        if ch.isalpha():

            count +=1
    
    return count

print(alphabet_count("hello world"))

print(alphabet_count("hello world python"))


note = "pain"

magazine = "supercalifragilisticexpialidocious"

container_word=True

for ch in note:#ch=p

    if magazine.find(ch)==-1:

        container_word=False

        break

print(container_word)


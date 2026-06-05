
magazine = "panamacanal"

note = "man"


"""
for ch in note:

    if ch not in magazine:

        print("not a ransom note")
        break
else:

    print("ransom note")
"""


magazine_set = set(magazine)

note_set = set(note)

print(note_set.issubset(magazine_set))
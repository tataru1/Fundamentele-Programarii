# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def reverse(word):
    vok = 'aeiou'
    vok_in_word = []
    new_word = ' '

    for ch in word:
        if ch in vok:
            vok_in_word.append(ch)

    i = 1
    for ch in word:
        if ch not in vok:
            new_word += ch
        else:
            new_word += vok_in_word[-i]
            i += 1

    return new_word

def test_reverse():
    assert reverse('Terminator') == ' Tormaniter'

def main():
    test_reverse()
    main()
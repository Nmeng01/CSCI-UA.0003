"""
Takes a list of nouns and returns them in plural form (only works for certain rules)

Submitted by Nicholas Meng, NetID ndm9914
The scripts takes a list of nouns and uses each noun's last 1 or 2 letters
to decide how to make it plural. The first function does simple conversions
and the second function can handle more complicated ones.
"""


vowels = ['a', 'e', 'i', 'o', 'u']


def simple_plural(nouns: list):
    """DocString goes here
    Returns a list of simple, singular nouns in plural form
    Parameters:
        nouns (list): a list of nouns in singular form
    Returns:
        simple_plural_nouns (list): list of inputted nouns in plural form
    """
    simple_plural_nouns = [noun + ("es" if noun[-1] in ["s", "x", "z"] or noun[-2:] in ["ch", "sh"] else "s") for
                           noun in nouns]
    return simple_plural_nouns


def make_plural(nouns: list):
    """DocString goes here
    Returns a list of a bit more complicated, singular nouns in plural form
    Parameters:
        nouns (list): a list of nouns in singular form
    Returns:
        medium_plural_nouns (list): list of inputted nouns in plural form
    """
    medium_plural_nouns = []
    for noun in nouns:
        if noun[-1] in ["s", "x", "z"] or noun[-2:] in ["ch", "sh"]:
            medium_plural_nouns.append(noun + "es")
        elif noun[-1] == "f":
            medium_plural_nouns.append(noun[0:(len(noun)-1)] + "ves")
        elif noun[-2:] == "fe":
            medium_plural_nouns.append(noun[0:(len(noun) - 2)] + "ves")
        elif noun[-1] == "y" and noun[-2] not in vowels:
            medium_plural_nouns.append(noun[0:(len(noun) - 1)] + "ies")
        else:
            medium_plural_nouns.append(noun + "s")
    return medium_plural_nouns


if __name__ == '__main__':
    print("Tests for this module.")
    print("Tests for simple plurals")
    test_nouns = ['peach', 'boy', 'witch', 'car', 'bus', 'toy', 'bed',
                  'mailbox', 'splash', 'catch', 'rash', 'table', 'pen']
    print(f"The following nouns were processed:\n{test_nouns}")
    print()
    print("The following plurals were obtained:")
    for singular, plural in zip(test_nouns, simple_plural(test_nouns)):
        print(f"{singular} -> {plural}")
    print()

    print("Tests for medium complexity plurals")
    test_nouns += ['baby', 'lady', 'day', 'turkey', 'monkey', 'puppy',
                   'party', 'kitty', 'guy', 'life', 'wife', 'elf',
                   'shelf', 'loaf', 'calf', 'half']
    print(f"The following nouns were processed:\n{test_nouns}")
    print()
    print("The following plurals were obtained:")
    for singular, plural in zip(test_nouns, make_plural(test_nouns)):
        print(f"{singular} -> {plural}")

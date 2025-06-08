def minion_game(string):
    # your code goes here
    vowels = "AEIOU"
    stuart = kevin = 0
    n = len(string)

    for i, ch in enumerate(string):
        if ch in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if stuart > kevin:
        print("Stuart", stuart)
    elif kevin > stuart:
        print("Kevin", kevin)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
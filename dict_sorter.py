def main():
    import re
    import enchant
    
    dictionary = enchant.Dict("en_US")
    five_letter_words = []

    regex = re.compile('[^a-zA-Z]')

    with open("moby_dick.txt", "r") as f:
        for line in f:
            line = line.replace("\n", "").split(" ")
            for word in line:
                word = regex.sub("", word)
                if len(word) == 5:
                    five_letter_words.append(word.lower())

    final_five_letter_words = list(set(five_letter_words))
    final_five_letter_words.sort()

    with open("fiveletterwords.txt", "w") as f:
        for word in final_five_letter_words:
            if dictionary.check(word) == True:
                f.write(f"\n{word}")

if __name__ == "__main__":
    main()
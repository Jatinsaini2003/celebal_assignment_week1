from collections import OrderedDict

def count_words_preserve_order(text):
    words = text.split()
    word_count = OrderedDict()
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    for word, count in word_count.items():
        print(f"{word}: {count}")

# Example usage:
if __name__ == "__main__":
    text = input("Enter text: ")
    count_words_preserve_order(text)
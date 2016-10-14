import argparse


def load_data(filepath):
    with open(filepath, 'r') as text:
        return text.read()


def get_most_frequent_words(text):
    words = set(text.split(' '))
    count_words = []
    for word in words:
        if word.isalpha():
            count_words.append([word, text.count(word)])
    return sorted(count_words, key=lambda x: x[1], reverse=True)[:9]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help="Path to file", required=True)
    args = parser.parse_args()

    data = load_data(args.path)
    print(get_most_frequent_words(data))

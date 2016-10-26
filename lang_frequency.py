import argparse
import collections


def load_data(filepath):
    with open(filepath, 'r') as text:
        return text.read()


def get_most_frequent_words(text):
    c = collections.Counter()
    for sword in text.lower().split('.'):
        for word in sword.split(' '):
            if word.isalpha():
                c[word.strip()] += 1
    top_10_word = 10
    return c.most_common(top_10_word)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help="Path to file", required=True)
    args = parser.parse_args()

    data = load_data(args.path)
    print(get_most_frequent_words(data))

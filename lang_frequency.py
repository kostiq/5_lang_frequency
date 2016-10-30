import argparse
import collections
import re


def load_data(filepath):
    with open(filepath, 'r') as text:
        return text.read()


def get_most_frequent_words(text):
    words = re.findall(r'\w+', text.lower())
    c = collections.Counter(words)
    top_10_word = 10
    return c.most_common(top_10_word)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', help="Path to file", required=True)
    args = parser.parse_args()

    data = load_data(args.path)
    print(get_most_frequent_words(data))

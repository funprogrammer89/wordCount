import string


def work():
    print('Enter filename ')
    file = input()
    with open(file, 'r') as document:
        counts = dict()
        text = ''
        for i in document:
            text = text.lower() + i
        wordlist = text.split()
        table = str.maketrans("", "", string.punctuation)
        stripped = [w.translate(table) for w in wordlist]
        print('Total words = ' + str(len(stripped)))
        for word in stripped:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
        for number in sorted(counts.items(), key=lambda t: t[1], reverse=True):
            print(number)


def start():
    try:
        work()
    except OSError as e:
        print('Try again, maybe filename does not exist?')
        start()


if __name__ == '__main__':
    start()

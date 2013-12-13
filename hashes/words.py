import twitter
import re
import itertools

TWITTER_KEYWORDS = ['military','us','anonymous','youtube','sport','golf','singles','dating','love','justin']

def twitter_words():

    for kw in TWITTER_KEYWORDS:
        for result in twitter.search(kw,n=1000):
            for word in re.split('\s+',result['text']):
                if word[0]=='@' or word[:4]=='http':
                    continue
                elif word[0]=='#':
                    word = word[1:]
                try:
                    yield str(word)
                except UnicodeEncodeError:
                    pass

if __name__ == '__main__':
    words = list(set(twitter_words()))
    sorted(words)
    print len(words)

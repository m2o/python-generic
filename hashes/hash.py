import hashlib
import itertools

import words

def check(hashes,cleartexts,p=2):
    for w in cleartexts:
        _hash = hashlib.sha1(w).hexdigest()
        if _hash in hashes:
            yield w

    for i in range(2,p+1):
        for wordtup in itertools.permutations(cleartexts,i):
            w = ''.join(wordtup)
            _hash = hashlib.sha1(w).hexdigest()
            if _hash in hashes:
                yield w

if __name__=='__main__':
    with open('SHA1_nondedacted.txt','r') as f:
        hashes = set(map(str.strip,f.readlines()))

    words = sorted(list(set(words.twitter_words())))

    for password in check(hashes,words):
        print password


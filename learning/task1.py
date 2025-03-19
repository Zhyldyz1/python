# Exercises to learn Python 

def tripler(s):
    triples = 0
    s = [ss.strip() for ss in s.split()][::-1]

    for i in range(len(s) - 1):
        if s[i - triples + 1] == 'Triple':
            s[i - triples] *= 3

            del s[i - triples + 1]
            triples += 1

    return ' '.join(s[::-1])
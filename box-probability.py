def checkio(marbles, step):
    if step > 1:
        black_prob = float(marbles.count('b')) / len(marbles) * checkio(marbles.replace('b','w',1), step - 1)
        white_prob = float(marbles.count('w')) / len(marbles) * checkio(marbles.replace('w','b',1), step - 1)
    else:
        return float(marbles.count('w')) / len(marbles)
    return (black_prob + white_prob)
        
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u'bbw', 3) == 0.48, "1st example"
    assert checkio(u'wwb', 3) == 0.52, "2nd example"
    assert checkio(u'www', 3) == 0.56, "3rd example"
    assert checkio(u'bbbb', 1) == 0, "4th example"
    assert checkio(u'wwbb', 4) == 0.5, "5th example"
    assert checkio(u'bwbwbwb', 5) == 0.48, "6th example"

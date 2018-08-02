import random

def score():
    for score in range(0,10):
        s = 'Score: '
        r = random.randint(60,100)
        g = '; Your grade is '
        if r >= 60 and r <= 69:
            gr = 'D'
        elif r >= 70 and r <= 79:
            gr = 'C'
        elif r >= 80 and r <= 89:
            gr = 'B'
        elif r >= 90 and r <= 100:
            gr = 'A'
        print "{}{}{}{}".format(s,r,g,gr)
    print 'End of the program. Bye!'
    
score()

# python score.py
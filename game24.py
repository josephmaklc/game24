import sys

# This programs tries to solve the "24 Game", you can use a deck of cards too.
# The idea is to draw four cards with numbers from a pile and make an arithmetic expression using + - x /
# to make 24.
#
# I am using a recursive approach here. If you have just 1 card, you are solved instantly (or not able to solve)
# If you have 2 cards, see if any of the 4 operation works.
# If more than 2 cards, take one card out and make 4 smaller problems.
# For example if you are given the list of  2, 3, 4, 8. Take away first card (2). Now you have the list (3,4,8) but you
# have 4 smaller problems, 
# can you make 22 out of the 3 remaining cards? if so you can add the 2.
# can you make 26 out of the 3 remaining cards? if so you can subtract the 2.
# can you make 12 out of the 3 remaining cards? if so you can multiply the 2.
# can you make 48 out of the 3 remaining cards? if so you can divide the 2.
#
# I know this approach does not solve all cases, but it works pretty well.
#
# To run, pass the list as arguments, separate by space
#
# For example:
# python3 game24.py 2 3 4 8

GOAL = 24
NIL = -999

def main():
    arguments = sys.argv.copy()
    arguments.pop(0)
    cardlist = list(map(int,arguments))
    NCARDS = len(cardlist)
    #print(cardlist)
    if (game(GOAL,cardlist,NCARDS)):
      print("\n")
    else:
      print("I don't know how to do this one.\n");

def game(goal, cardlist, n):

  if (goal == NIL):
    return False;

  if (n == 1):
        if (goal == cardlist[0]):
           print( "%d" % goal, end=" ")
           return True
        else:
           return False
  else:
    for i in range(n):
        card = cardlist[i];
        
        newlist = cardlist.copy()
        newlist.remove(card);

        toAdd = goal - card;
        toSub = goal + card;
        #toMul = (goal % card == 0) ? goal/card : NIL;
        if (goal % card == 0):
            toMul = goal//card
        else:
            toMul = NIL
        toDiv = goal * card


        if (game(toAdd,newlist,n-1)):
            print(" + %d" % card, end=" ")
            return True
        if (game(toSub,newlist,n-1)):
            print(" - %d" % card, end=" ")
            return True
        if (game(toMul,newlist,n-1)):
            print(" * %d" % card, end=" ")
            return True
        if (game(toDiv,newlist,n-1)):
            print(" / %d" % card, end=" ")
            return True
	         
        return False  

if __name__ == "__main__":
    main()
    
 
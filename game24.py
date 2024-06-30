import sys

# This programs tries to solve the "24 Game", you can use a deck of cards to draw 4 cards too.
# The idea is to make an arithmetic expression using + - x / from 4 numbers to make 24.
#
# I am using a recursive approach here. If you have just 1 card, you are solved instantly (or not able to solve)
# If you have 2 cards, see if any of the 4 operations works.
# If more than 2 cards, take one card out and make 4 smaller problems with different goals.
# For example if you are given the list of  2, 3, 4, 8. Take away first card (2). Now you have the list (3,4,8) but you
# have 4 smaller problems, 
# can you make 22 out of the 3 remaining cards? if so you can add the 2.
# can you make 26 out of the 3 remaining cards? if so you can subtract the 2.
# can you make 12 out of the 3 remaining cards? if so you can multiply the 2.
# can you make 48 out of the 3 remaining cards? if so you can divide the 2.
#
# To run, pass the list as arguments, separate by space
#
# For example:
# python3 game24.py 2 3 4 8

GOAL = 24

def printUsage():
    print("Game 24 - this program tries to find an arithmetic expression to reach %d" % GOAL)
    print("Usage: pass 4 positive integers in argument list. For example: ")
    print(">python3 game24.py 2 3 4 8")

def main():
    arguments = sys.argv.copy()
    arguments.pop(0)
    try:
        cardlist = list(map(int,arguments))
    except:
        printUsage()
        return
        
    # make sure all positive    
    if (not all(a > 0 for a in cardlist)):
        printUsage()
        return
        
    size = len(cardlist)
    if (size == 0):
        printUsage()
        return
    #print(cardlist)
    if (game(GOAL,cardlist)):
      print("\n")
    else:
      print("I don't know how to do this one.\n");

def checkDivide(num,den,goal):
    return round(num/den, 3) == round(goal, 3)
    
def game(goal, cardlist):
  if (goal == None):
    print("goal: none, cardlist: %s" %str(cardlist))  
    return False;
  #print("goal: %f cardlist: %s" % (goal,str(cardlist)))

  n = len(cardlist)

  if (n == 1):
        if (goal == cardlist[0]):
           print( "%d" % goal, end=" ")
           return True
        else:
           return False

  if (n == 2):
        #print("goal %f two cards: %d %d" % (goal, cardlist[0],cardlist[1]))
        if (cardlist[0] + cardlist[1] == goal):
            print ("%d + %d" % (cardlist[0], cardlist[1]), end="")
            return True
        if (cardlist[0] - cardlist[1] == goal):
            print ("%d - %d" % (cardlist[0], cardlist[1]), end="")
            return True
        if (cardlist[1] - cardlist[0] == goal):
            print ("%d - %d" % (cardlist[1], cardlist[0]), end="")
            return True
        if (cardlist[0] * cardlist[1] == goal):
            print ("%d * %d" % (cardlist[0], cardlist[1]), end="")
            return True
        #if (cardlist[0] / cardlist[1] == goal):
        if (checkDivide(cardlist[0],cardlist[1],goal)):
            print ("%d / %d" % (cardlist[0], cardlist[1]), end="")
            return True
        #if (cardlist[1] / cardlist[0] == goal):
        if (checkDivide(cardlist[1],cardlist[0],goal)):
            print ("%d / %d" % (cardlist[1], cardlist[0]), end="")
            return True
        if (checkDivide(cardlist[0],cardlist[1],-goal)):
        #if ( (cardlist[0] / cardlist[1]) == -1*goal):
            print ("- (%d / %d)" % (cardlist[0], cardlist[1]), end="")
            return True
        if (checkDivide(cardlist[1],cardlist[0],-goal)):
        #if ( (cardlist[1] / cardlist[0]) == -1*goal):
            print ("- (%d / %d)" % (cardlist[1], cardlist[0]), end="")
            return True

        return False    
              	                       
  else:
    for i in range(n):
        card = cardlist[i];
        
        newlist = cardlist.copy()
        newlist.remove(card);

        toAdd = goal - card;
        toSub = goal + card;
        toMul = goal/card
        toDiv = goal * card


        if (game(toAdd,newlist)):
            print(" + %d" % card, end="")
            return True
        if (game(toSub,newlist)):
            print(" - %d" % card, end="")
            return True
        if (game(toMul,newlist)):
            print(" * %d" % card, end="")
            return True
        if (game(toDiv,newlist)):
            print(" / %d" % card, end="")
            return True
	         
    return False  

if __name__ == "__main__":
    main()
    
 

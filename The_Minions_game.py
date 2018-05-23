
def minion_game(string):

    #Finding all the substrings

      length = len(string)
      global alist
      alist = []
      for i in range(length):
        for j in range(i,length):
          alist.append(string[i:j + 1])
      alist=set(alist)
      alist=list(alist)
      vowels_and_consonents(alist)

def vowels_and_consonents(alist):

    #Seperating into vowels and consonents

    global vowels
    global consonents
    vowels=[]
    consonents=[]
    for i in alist:
        if i[0] in "AEIOU":
            vowels.append(i)
        else:
            consonents.append(i)
    vowels_consonents_count()

def vowels_consonents_count():

    #Vowels and consonents count

    global vowels_count
    global consonents_count
    vowels_count = 0
    consonents_count = 0
    for sub_strings in vowels:
        for i in range(0, len(string)-len(sub_strings)+1):
            if string[i:i+len(sub_strings)]==sub_strings:
                    vowels_count+=1
    for sub_strings in consonents:
        for i in range(0, len(string)-len(sub_strings)+1):
            if string[i:i+len(sub_strings)]==sub_strings:
                    consonents_count+=1
    minion_game_result()

def minion_game_result():

    #Minion game result
    
    if vowels_count>consonents_count:
        print "Kevin",vowels_count
    elif vowels_count==consonents_count:
        print "Draw"
    else:
        print "Stuart",consonents_count
        
string='BANANA'
minion_game(string)
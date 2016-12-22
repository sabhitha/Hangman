import random
import curses
myscreen = curses.initscr()
myscreen.border(0)
win = curses.newwin(10, 10, 5, 20)
word = random.choice(list(open("dict.txt")))
word = word.strip()
blanks = '-' * len(word)
def displayBlank():
    myscreen.addstr(14, 5, blanks)
    myscreen.refresh()
max_wrongs = 6 
wrong = 0

def stage0():
    myscreen.addstr(2,6,"--------")
    myscreen.refresh()
    for i in range(2,9):
        myscreen.addstr(i,6,'|')
        myscreen.refresh()
    myscreen.addstr(3,12,'|')    
    myscreen.refresh()
    myscreen.addstr(8,4,"-------")
    myscreen.refresh()
stage0()    
   
def stage1():
    stage0()
    myscreen.refresh()
    myscreen.addstr(4, 12, '0')
    myscreen.refresh()

def stage2():
    stage1()
    myscreen.refresh()
    myscreen.addstr(5, 12, '|')
    myscreen.refresh()

def stage3():
    stage2()
    myscreen.refresh()
    myscreen.addstr(6, 12, '|')
    myscreen.refresh()

def stage4():
    stage3()
    myscreen.refresh()
    myscreen.addstr(5, 11, '\|')
    myscreen.refresh()

def stage5():
    stage4()
    myscreen.refresh()
    myscreen.addstr(5, 11, '\|/')
    myscreen.refresh()

def stage6():
    stage5()
    myscreen.refresh()
    myscreen.addstr(7, 11, '/')
    myscreen.refresh()

def stage7():
    stage6()
    myscreen.refresh()
    myscreen.addstr(7, 13, '\.')
    myscreen.refresh()

stages = [stage1, stage2, stage3, stage4, stage5, stage6, stage7]

def convertToStr(word):
    word1 = ""
    for ch in word:
        word1 += ch
    return word1

def displayGWD(word):
    word1 = convertToStr(word)
    myscreen.addstr(10, 30,"Letters Guessed : ")
    myscreen.addstr(10, 49, word1)
    myscreen.refresh()                                                                                          
def replace_letter(letter, blanks, word, count):
    index = 0
    while count > 0:
        index = word.find(letter, index)
        s, s1 = list(blanks), list(word)
        s[index] = s1[index]
        index += 1
        word = ''.join(s1)
        blanks = ''.join(s)
        count -= 1
    return blanks

def error(letter, wrong, blanks):
    myscreen.addstr(14,5,blanks)
    myscreen.addstr(5,30,"Left Chances :")
    myscreen.addstr(5,45, str(max_wrongs - wrong))
    myscreen.refresh()
    return stages[wrong]()

def displayMsg():
    myscreen.refresh()

def alreadyGussed(let, word):
    return let in word

gameover = False
gussedstr = []
displayBlank()
while not gameover: 
    stage0()
    displayGWD(gussedstr)
    letr = myscreen.getkey(17,5)
    if alreadyGussed(letr, gussedstr):
        displayMsg()
    else:    
        gussedstr.append(letr)
        count = word.count(letr)
        if count:
            blanks = replace_letter(letr, blanks, word, count)
            displayBlank()
        else:
            error(letr, wrong, blanks)
            wrong += 1
    if wrong == (max_wrongs + 1):
        myscreen.addstr(18,30,"Lost The Game")
        myscreen.addstr(19,30,"The word is :")
        myscreen.addstr(19,45,word)
    else:
        if blanks == word:
            myscreen.addstr(20,30,"Congratulations!!!")
            myscreen.addstr(21,36,"You won")
curses.endwin()


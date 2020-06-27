import random
import time

def check(s):
    if(mat[0][0]==mat[0][1]==mat[0][2]==s):
        return 1
    elif(mat[1][0]==mat[1][1]==mat[1][2]==s):
        return 1
    elif(mat[2][0]==mat[2][1]==mat[2][2]==s):
        return 1
    elif(mat[0][0]==mat[1][0]==mat[2][0]==s):
        return 1
    elif(mat[0][1]==mat[1][1]==mat[2][1]==s):
        return 1
    elif(mat[0][2]==mat[1][2]==mat[2][2]==s):
        return 1
    elif(mat[0][0]==mat[1][1]==mat[2][2]==s):
        return 1
    elif(mat[0][2]==mat[1][1]==mat[2][0]==s):
        return 1
    else:
        return 0

def disp(s,pos):
    if(pos==1):
        mat[0][0]=s
    elif(pos==2):
        mat[0][1]=s
    elif(pos==3):
        mat[0][2]=s
    elif(pos==4):
        mat[1][0]=s
    elif(pos==5):
        mat[1][1]=s
    elif(pos==6):
        mat[1][2]=s
    elif(pos==7):
        mat[2][0]=s
    elif(pos==8):
        mat[2][1]=s
    elif(pos==9):
        mat[2][2]=s
    print("{0} | {1} | {2}".format(mat[0][0],mat[0][1],mat[0][2]))
    print("--|---|--")
    print("{0} | {1} | {2}".format(mat[1][0],mat[1][1],mat[1][2]))
    print("--|---|--")
    print("{0} | {1} | {2}".format(mat[2][0],mat[2][1],mat[2][2]))
    print("")
    c=check(s)
    if(c):
        return 1
    else:
        return 0

def pos1(num,val):
    while(True):
        if(num==3):
            position=input("Your turn: ")
        else:
            position=input("Player {0}'s turn: ".format(num))
        try:
            position=int(position)
        except ValueError:
            print("Enter a number")
            continue
        if(position in val):
            val.remove(position)
            return position
        else:
            print("Enter a valid position")

def new():
    while(True):
        hh=input("Enter '0' for New game and '1' for Exit: ")
        try:
            hh=int(hh)
        except ValueError:
            print("Enter a number")
            continue
        if(hh in range(0,2)):
            return hh
        else:
            print("Enter a number either 0 or 1")

def new1():
    while(True):
        hh=input("Do you want to start first? 1-Yes 0-No : ")
        print("")
        try:
            hh=int(hh)
        except ValueError:
            print("Enter a number")
            continue
        if(hh in range(0,2)):
            return hh
        else:
            print("Enter a number either 0 or 1")

def option():
    while(True):
        print("Select the mode\n1-Single player\n2-Multiplayer")
        pp=input()
        try:
            pp=int(pp)
        except ValueError:
            print("Enter a number")
            continue
        if(pp in range(1,3)):
            return pp
        else:
            print("Enter a number either 1 or 2")

def charr():
    while(True):
        aa=input()
        if(aa=='X' or aa=='O'):
            return aa
        else:
            print("Enter either X or O")

def ran(val):
    print("COM's turn")
    kk=random.choice(val)
    val.remove(kk)
    return kk
    
def game(a,b,flag1):
    turn=0
    count=0
    val=[1,2,3,4,5,6,7,8,9]
    if(flag1==0):
        while(True):
            if(turn==0):
                pos=pos1(1,val)
                flag=disp(a,pos)
                if(flag==1):
                    print("Player 1 wins!")
                    break
                count+=1
                if(count==9):
                    print("Match tied!")
                    break
                turn=1
            elif(turn==1):
                pos=pos1(2,val)
                flag=disp(b,pos)
                if(flag==1):
                    print("Player 2 wins!")
                    break
                count+=1
                if(count==9):
                    print("Match tied!")
                    break
                turn=0
    else:
        if(flag1==1):
            turn=1
        while(True):
            if(turn==0):
                pos=pos1(3,val)
                flag=disp(a,pos)
                if(flag==1):
                    print("You win!")
                    break
                count+=1
                if(count==9):
                    print("Match tied!")
                    break
                turn=1
            elif(turn==1):
                pos=ran(val)
                flag=disp(b,pos)
                if(flag==1):
                    print("COM wins!")
                    break
                count+=1
                if(count==9):
                    print("Match tied!")
                    break
                turn=0
    h=new()
    print("")
    return h

print("---Tic Tac Toe---")
while(True):
    p=option()
    flag1=0
    mat=[[' ' for i in range(3)] for j in range(3)]
    if(p==1):
        x=new1()
        if(x==0):
            print("COM starts first and chose X")
            a,b='O','X'
            flag1=1
        elif(x==1):
            print("You start first, Choose X or O?")
            a=charr()
            if(a=='X'):
                b='O'
            else:
                b='X'
            flag1=2
    elif(p==2):
        print("Player 1 Choose X or O?")
        a=charr()
        if(a=='X'):
            b='O'
        else:
            b='X'
    print("Rules : Enter the position number as in keypad")
    print("1 2 3\n4 5 6\n7 8 9")
    print("")
    time.sleep(2)
    ch=game(a,b,flag1)
    if(ch):
        break

print("---Game over---")

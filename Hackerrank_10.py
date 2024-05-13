def minion_game(string):
    k,s=0,0
    for i in range(len(string)):
        if string[i] in "AEIOU":
            k+=len(string[i:])
        else:
            s+=len(string[i:])
    if k>s:
        print("Kevin",k)
    elif k==s:
        print("Draw")
    else:
        print("Stuart",s)



if __name__ == '__main__':
    s = input()
    minion_game(s)
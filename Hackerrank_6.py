if __name__=='__main__':
    names=[]
    scores=[]
    for _ in range(int(input())):
        name=input()
        score=float(input())
        names.append(name)
        scores.append(score)
    q=sorted(list(set(scores)))
    second_min=q[1]
    students=[]
    for i in range(len(names)):
        if scores[i]==second_min:
            students.append(names[i])
    students.sort()
    for i in students:
        print(i)
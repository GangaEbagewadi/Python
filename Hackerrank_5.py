if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    q=list (set(arr))
    q.sort()
    print(q[len(q)-2])
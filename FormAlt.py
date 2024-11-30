def frmAltSt():
    str = input()
    m = len(str)
    lst = list(map(int, input().split()))
    
    ans = 0
    ls = int(str[0])
    lsi = lst[0]
    
    for i in range(1, m):
        if int(str[i]) == ls:
            ans += min(lsi, lst[i])
            lsi = max(lsi, lst[i])
        else:
            ls = int(str[i])
            lsi = lst[i]
    print(ans)
frmAltSt()
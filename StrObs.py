def m_rm(sstr, mainst, b):
    if not mainst:
        return 0

    if mainst in b:
        return b[mainst]

    mx_cnt = 0

    for s in sstr:
        if s in mainst:
            n_str = mainst.replace(s, "", 1)
            mx_cnt = max(mx_cnt, 1 + m_rm(sstr, n_str, b))

    b[mainst] = mx_cnt
    return mx_cnt

def st_obs(n, sstr, mainst):
    b = {}
    return m_rm(sstr, mainst, b)

if __name__ == "__main__":
    m = int(input().strip())
    sstr = input().strip().split()
    mainst = input().strip()
    print(st_obs(m, sstr, mainst))

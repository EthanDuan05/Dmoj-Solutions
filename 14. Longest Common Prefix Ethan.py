def longestCommonPrefix(strs):
    Max_N = 10000

    for i in strs:
        if len(i) < Max_N:
            Max_N = len(i)

    ind = 1
    ans = strs[0][:ind]
    while ind <= Max_N:
        print(ans, 'ans')
        for i in strs:
            if i[:ind] != ans:
                if ind == 1:
                    return ''
                else:
                    return ans[:ind-1]

        ind += 1
        print(ind, 'ind')
    return ans

print(longestCommonPrefix(["flower","flow","flight"]))
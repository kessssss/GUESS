word = input()
thetry = input()

out = [3] * len(word)
ans = {1: 'correct', 0: 'present', -1: 'absent'}

for index, w in enumerate(thetry):
    if out[index] != 3:
        continue

    ind = word.find(w, index)
    wcount = word.count(w, index)

    if index == ind:
        out[index] = 1
    elif ind >= 0:
        while wcount > 0:
            if thetry[ind] != w:
                if wcount > 0:
                    out[index] = 0
                    break
            else:
                ind = word.find(w, ind+1)
                out[index] = -1
                wcount -= 1
    else:
        out[index] = -1

for i in out:
    print(ans[i])

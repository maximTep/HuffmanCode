import copy

s = 'тепайкин_максим_андреевич_пока_ещё_студент_203_группы'

lets = dict()

for sym in s:
    if sym in lets.keys():
        lets[sym] += 1
    else:
        lets[sym] = 1

lets = list(sorted(lets.items(), key=lambda pr: pr[1]))



for i in range(len(lets)):
    newItem = list(lets[i])
    newItem.append('')
    newItem.append(lets[i][0])
    newItem.append('')
    lets[i] = newItem

# print(lets)



def haffman(lets: list):
    sets = []
    sets.append(copy.deepcopy(lets))
    while len(lets) > 1:
        new_item = [lets[0][0] + lets[1][0], lets[0][1] + lets[1][1], '', lets[0][0], lets[1][0]]
        lets.pop(0)
        lets.pop(0)
        lets.append(new_item)
        lets = list(sorted(lets, key=lambda pr: pr[1]))
        sets.append(copy.deepcopy(lets))
        #print(lets)
    return sets


def rec(sets: list, it: int, word: str, last1: str, last2: str):
    if len(sets) - it - 2 < 0:
        return


    newlast1 = ''
    newlast2 = ''
    for i in range(len(sets[-it-2])):
        if sets[-it-2][i][0] == last1+last2:
            sets[-it-2][i][2] = word
            newlast1 = sets[-it-2][i][3]
            newlast2 = sets[-it-2][i][4]
            rec(sets, it+1, word, newlast1, newlast2)
            if newlast2 == '':
                continue

        if sets[-it-2][i][0] == last1:
            sets[-it-2][i][2] = word + '0'
            newlast1 = sets[-it-2][i][3]
            newlast2 = sets[-it-2][i][4]
            rec(sets, it+1, word + '0', newlast1, newlast2)

        if sets[-it - 2][i][0] == last2:
            sets[-it - 2][i][2] = word + '1'
            newlast1 = sets[-it - 2][i][3]
            newlast2 = sets[-it - 2][i][4]
            rec(sets, it + 1, word + '1', newlast1, newlast2)








sets = haffman(lets)
l1 = sets[-1][0][3]
l2 = sets[-1][0][4]


rec(sets, 0, '', l1, l2)


#for item in sets[0]:
    #print(item)

ans = dict()

for item in sets[0]:
    ans[item[0]] = item[2]

for item in reversed(ans.items()):
    print(list(item))

print()
for sym in s:
    print(ans[sym], end='')
print()
lSr = 0
for item in sets[0]:
    lSr += len(item[2]) * item[1]
print(lSr)
print(lSr / len(s))


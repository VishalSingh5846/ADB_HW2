


friends = open('friends.txt').read().replace('\r','').split('\n')[1:]
likes = open('like.txt').read().replace('\r','').split('\n')[1:]
friends = filter(lambda x: len(x.strip()) > 0, friends)
likes = filter(lambda x: len(x.strip()) > 0, likes)

fr = map(lambda x: map(lambda y: int(y.strip()), x.strip().split(',')), friends)
lik = map(lambda x: map(lambda y: int(y.strip()), x.strip().split(',')), likes)


print fr[:3]
print lik[:3]

dic = {}
likLst = {}
for temp in lik:
    p = temp[0]
    a = temp[1]
    
    if p not in likLst: likLst[p] = set()
    likLst[p].add(a)

frnd = {}

for z in fr:
    p1,p2 = z[0],z[1]
    frnd[(p1,p2)] = 1
    frnd[(p2,p1)] = 1


ans = []

for p1,p2 in frnd:

    for a in likLst.get(p2,set()):
        if a not in likLst.get(p1,set()):
            ans.append([p1,p2,a])





print len(ans),ans[:10]





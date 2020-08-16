from collections import defaultdict
user_words = defaultdict(list)
word_users_count = defaultdict(int)
word_count = defaultdict(int)

n = int(input())
for i in range(n):
    s = input().split()
    user_words[s[0]] += s[1:]
for u, ws in user_words.items():
    w_thisuser = defaultdict(int)
    for w in ws:
        word_count[w] += 1
        w_thisuser[w] = 1
    for wtu in w_thisuser:
        word_users_count[wtu] += 1
numuniqueusers = len(user_words)
eligiblewords = []
for w, nu in word_users_count.items():
    if nu == numuniqueusers:
        eligiblewords.append([word_count[w], w])
if len(eligiblewords) == 0:
    print("ALL CLEAR")
    quit()
eligiblewords.sort()
prevnum = eligiblewords[len(eligiblewords)-1][0]
a = []
for j in range(len(eligiblewords)-1,-1,-1):
    if eligiblewords[j][0] == prevnum:
        a.append(eligiblewords[j][1])
    else:
        a.sort()
        for e in a:
            print(e)
        prevnum = eligiblewords[j][0]
        a = []
        a.append(eligiblewords[j][1])
if len(a) > 0:
    for e in a:
        print(e)
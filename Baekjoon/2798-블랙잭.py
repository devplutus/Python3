def find(card, check, total, count):
    global _sum

    if count == 3:
        if _sum < total and total <= M:
            _sum = total
        return

    for i in range(len(card)):
        if check[i] == False:
            check[i] = True
            find(card, check, total + card[i], count + 1)
            check[i] = False

    

N, M = map(int, input().split(" "))
card = list(map(int, input().split(" ")))
card.sort(reverse = True)

for i in card:
    if i >= M:
        card.remove(i)

check = [False] * len(card)
_sum = 0
find(card, check, 0, 0)
print(_sum)

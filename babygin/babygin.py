from itertools import combinations


def check(player):
    a = list(combinations(player, 3))
    b = []
    for k in a:
        b.append(list(k))
    for j in b:
        j.sort()
        if j[0] == j[1] == j[2] or (j[0] + 1 == j[1] and j[1] + 1 == j[2]):
            return True
    return False


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    player1 = []
    player2 = []
    for i in range(len(cards)):
        if not i % 2:
            player1.append(cards[i])
            if len(player1) >= 3:
                if check(player1):
                    print(f'#{tc} {1}')
                    break
        else:
            player2.append(cards[i])
            if len(player2) >= 3:
                if check(player2):
                    print(f'#{tc} {2}')
                    break
    else:
        print(f'#{tc} {0}')
import sys
from collections import deque

N = int(sys.stdin.readline())
cards = [i for i in range(N, 0, -1)]
cards = deque(cards)

while len(cards) > 1:
    #맨위 카드 버리기
    cards.pop()
    #두번째 카드 맨뒤로
    second = cards.pop()
    cards.appendleft(second)
print(cards[0])

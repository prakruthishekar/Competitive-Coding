from collections import deque

customQueue = deque(maxlen=3)
print(customQueue)

customQueue.append(1)
print(customQueue)

customQueue.append(2)
print(customQueue)

customQueue.append(3)
print(customQueue)

customQueue.append(4)
customQueue.append(5)

print(customQueue)

print(customQueue.popleft())

print(customQueue)
print(customQueue.clear())
print(customQueue)
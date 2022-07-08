import sys

N = int(input())

books = {}

for i in range(N):
    name = sys.stdin.readline().rstrip()
    
    if name in books:
        books[name] += 1
    else:
        books[name] = 1

maxBook = max(books.values())
cnt = []

for book, num in books.items():
    if num == maxBook:
        cnt.append(book)

print(sorted(cnt)[0])
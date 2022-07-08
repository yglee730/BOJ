import sys

n = int(input())
company = {}

for i in range(n):
    person, status = sys.stdin.readline().rstrip().split()

    if status == "leave":
        del company[person]
    else:
        company[person] = status

sorted_dict = sorted(company.items(),reverse = True)

for person in sorted_dict:
    print(person[0])
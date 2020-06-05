electives = input().split(', ')
name_elect = dict()
for i in electives:
    inp = input()
    names = inp[inp.find(":") + 2:].split(', ')
    elective = inp[:inp.find(":")][::-1]
    name_elect[elective] = names
req = input().split(', ')
for u in req:
    resp = u + ': '
    for key, value in name_elect.items():
        if u in value:
            resp += key + ', '
    print(resp)

e = []
w = ""
while True:
    a = input()
    if a == "x":
        break
    e.append(a)
print(f"items : {len(e)}")
if len(e) != 0:
    for i in range(len(e)):
        if i != len(e) - 1:
            w += e[i] + ", "
        else:
            w += e[i]
    print(f"{w}")
else:
    print("empty")
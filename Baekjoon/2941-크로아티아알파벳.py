word = input()
check = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
cur = ""
count = 0
for c in check:
    count += word.count(c)
    word = word.replace(c, "0")
    
print(count + len([c for c in word if c != "0"]))

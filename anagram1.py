l="cab"
m=str(input("Enter the input string: "))
c={}
s={}
for i in l:
    v=l.count(i)
    if i not in s:
        s[i]=v
for j in m:
    b=m.count(j)
    if j not in c:
        c[j]=b
print(s)
print(c)
if s.items()==c.items():
    print("It is an anagram")
else:
    print("not anagram")





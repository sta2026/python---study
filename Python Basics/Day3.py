score = 80

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
else:
    grade = "C"
print("학점은", grade, "입니다")

score = 45

if score >= 90:
    print("A")
elif score >= 60:
    print("B")
else:
    print("F")

scores = [85, 92, 78, 90, 88]

for s in scores:
    print(s)

for i in range(1, 6, 3):
    print(i)

for i in range(5):
    print(i)

for i in range(2, 11):
    if i % 2 == 0:
        print(i)

for i in range(2):
    print("X")

    print("Y")

print("Z")

scores = [70, 80, 90]
print(scores[0])  
print(scores[1])  
print(scores[2])  
print(scores[-1])

scores = [70, 80, 90, 100]
print(scores[1:3])  
print(scores[:2])   
print(scores[2:])   

scores = [70, 80, 90]
scores[1] = 85
print(scores)  

a = [1, 2]
a.append(3)
print(a)  

a = [1, 2]
a.append(1)
print(a)

a = [1, 3]
a.insert(3, 2)  
print(a)  

a = [1, 4, 5, 4, 3]
a.remove(4)
print(a) 

scores = [70, 80, 90]
for s in scores:
    print(s)

a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)  

a = [1, 2, 3, 4, 5]
x = a.pop()
print(x)  
print(a) 

a = [10, 20, 30]
print(len(a))  

a = [1, 2, 3, 4, 5]
print(sum(a))

a = [3, 1, 4, 2]
print(a)

a = [1, 2, 3]
b = a
b.append(4)
print(a)  

a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)

a = [1, 2, 3]
a.append(4)
print(a)

for i in range(1,11):
    if i % 2 == 0:
        print(i)
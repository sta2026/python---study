score = 82
attendance = True

if score >= 90 and attendance:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")

score = 85
attendance = False

if score >= 90 or attendance:
    print("pass")
else:
    print("fail")

for i in range(1, 11):
    if i == 7:
        break
    print(i)

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

i = 1
while i <= 5:
    print(i)
    i += 1

while True:
    x = int(input("숫자 입력 (0이면 종료): "))
    if x == 0:
        break
    print(x)

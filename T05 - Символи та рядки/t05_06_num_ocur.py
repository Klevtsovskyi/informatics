#T05_06
#Кількість входжень заданого символа у заданий рядок

s=input("введіть рядок: ")
a=input("введіть символ: ")[0]

k = 0                           #кількість входжень
for c in s:
    if c == a:
        k = k+1

print('Кількість входжень - ',k)



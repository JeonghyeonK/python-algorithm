T = int(input())
for i in range(T):
    
    bestUniv=''
    bestAlcohol=0
    num = int(input())
    for j in range(num):
        univ, alcohol = input().split()
        if int(alcohol) > int(bestAlcohol):
            bestUniv = univ
            bestAlcohol = alcohol
    
    print(bestUniv)
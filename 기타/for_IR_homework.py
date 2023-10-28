import math

tf = [[0, 2, 1, 0],
      [2, 0, 2, 0],
      [3, 1, 2, 0],
      [2, 0, 0, 1],
      [0, 2, 1, 0],
      [0, 1, 0, 1],
      [1, 0, 0, 2]
      ]
df = [2, 2, 3, 2, 2, 2, 2]
normalization_value = list(0 for _ in range(len(tf[0])))

def tf_idf(tf:list(), df:list())->list():
    new_list = list()
    for i in range(7):
        for j in range(4):
            if j ==0:
                new_list.append([])
            if tf[i][j] == 0:
                new_list[-1].append(0)
            else:
                new_list[-1].append((1 + math.log10(tf[i][j]))*math.log10(4/df[i]))
    return new_list
                
def print_vector(vect:list()):
    print() 
    for i in range(len(vect)):
        for j in range(len(vect[0])):
            print(round(float(w[i][j]), 2), end='  ')   
        print()
    print()

def cos_nomalization(vect: list())->list():
    new_list = vect.copy()
    for j in range(len(vect[0])):
        for i in range(len(vect)):
            normalization_value[j] += vect[i][j]**2
    
    for j in range(len(normalization_value)):
        normalization_value[j] = math.sqrt(normalization_value[j])
    
    for j in range(len(vect[0])):
        for i in range(len(vect)):
            new_list[i][j] /= normalization_value[j]
    print(normalization_value)
    return new_list
    

def cos_similariry(vect: list(), denomi: list(), doc_ID_1: int, doc_ID_2: int)->float:
    summ = 0
    for i in range(len(vect)):
        summ += vect[i][doc_ID_1]*vect[i][doc_ID_2]
    return summ

w = tf_idf(tf, df)
print_vector(w)
after_cos_nomal = cos_nomalization(w)
print_vector(after_cos_nomal)

for i in range(len(tf[0])):
    for j in range(i+1, len(tf[0])):
        cos_simil = cos_similariry(after_cos_nomal, normalization_value, i, j)
        print(f"d{i}와 d{j}의 유사도 : {round(cos_simil, 2)}")
        

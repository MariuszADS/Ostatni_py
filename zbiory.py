empty_set = set()       #zbior pusty , rozdziela elementy

# print(type(empty_set))

techs = {'python','java','sql','c++'} # zbior jest nie uporzadkowany bo nie jest to wazne, tylko jedyne co sie liczy czy jest ta wartosc ktora zapisalismy NP

# print(len(techs))

# funkcja len - zwraca ilosc rzeczy w zbiorze

# def check():
#     techs = {'python', 'java', 'sql', 'c++'}
#     if 'python' in techs:
#         print("true")
#     else:
#         print("false")





# SPRAWDZAMY CZY Z ZBIOR C JEST Z POD ZBIOREM ZBIORU A

A = {1,2,3,4,5,6,7}
B = {5,6,7}
C = {1,2,3}

# print(C.issubset(A))
# print(C.issubset({1,2}))
# print(A.issubset(C))


# SPRAWDZAMY W TYM PRZYPADKU CZY A JEST NAD ZBIOREM ZBIORU C

# print(A.issuperset(C))
# print(A.union(C))
# print(A.intersection(C))
# print(A.symmetric_difference(C))

D = A.copy()
print(D)



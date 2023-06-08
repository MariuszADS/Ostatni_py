

# LISTA TO UPORZADKOWANA STRUKTURA ELEMENTU, MOGA SIE DUPLIOWAC ORAZ ZMIENIAC ZMIENNE
# NAWIASY KWADRATOWE

empty_list = list()

tech = ['python', 'java', 'c++','go','sql']
tech_01 = ['python', 'java', 'c++','go','sql',[1,2,3,4,]]
tech[0] = 'python 3.7'
print(type(tech))
tech_01 += ['js']
print(tech_01)

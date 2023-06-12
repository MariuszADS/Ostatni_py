techs = []
# print(techs)

# LISTY MOGA SIE POWTARZAC
techs.append('python')
techs.append('java')
techs.append('java')
# print(techs)


# techs.append(['asd','asd'])
# print(techs)


techs.extend(['sql','sass'])
# print(techs)

# INSERT POTRZEBUJE NR INDESKU ZEBY WIEDZIEC GDZIE TO UMIESCIC
techs.insert(0,'go')
# print(techs)


techs.insert(2,'r')
# print(techs)

# METODA POP WYRZUCA Z LISTY OSTATNI ELEMENT INDEKSU BEZ ARG, MOZNA WPISAC NR INDESKU
techs.pop(0)
# print(techs)


# WPISANIE JAKIEGOS ELEMENTU DOSTANIEMY NR INDEKSU GDZIE DANY ELEMENT SIE ZNAJDUJE
techs.index('java')
# print(techs.index('java'))

# METODA COUNT LICZY ILE RAZY DANY ELEMENT WYSTEPUJE W NASZEJ LISCIE
techs.count('python')
# print(techs.count('python'))


# METODA SORT SORTUJE LISTE alfabetycznie
techs.sort()
techs.sort(reverse=True) # ODWROCENIE SORTOWANIA
# print(techs)

# techs[::-1]
techs.reverse()
# print(techs)

# WYCIECIE I ZAMIANA ELEMENTU W INDEKSIE
techs[1] = 'c++'
print(techs)

# TUPLE
#  SIE NIE MOGA ZMIENIAC W CZASIE I NIE POZWALAJA NA DUPLIKACJE DANYCH


empty_dict = dict()
print(empty_dict)

# SLOWNIIK TO STRUKTU NIE UPORZADKOWANA I ZAWIERA PARY(KLUCZ:WARTOSC)
# dict = {'key1': 'value1'}

pol_to_eng = {'jeden': 'one','dwa':'two','trzy':'three'}

print(pol_to_eng)
print(type(pol_to_eng))

name_to_digit = {'jeden':1,'dwa': 2,'trzy': 3}
print(name_to_digit)

len(name_to_digit) # INDEKSOWANIE WARTOSCI
print(len(name_to_digit))



pol_to_eng['cztery'] = 'four'

# WYDOBYWANIE WSZYSTKICH KLUCZY
list(pol_to_eng.keys())

# WYDOBYWANIE WARTOSCI
list(pol_to_eng.values())

# WYDOBYWANIE KLUCZBE I WARTOSCI
list(pol_to_eng.items())

# DO KLUCZA ZOSTALA DODANA CYFRA
pol_to_eng.update({'jeden': 1})

# list(......) - OZNACZA KONWERTOWANIE NA LISTE



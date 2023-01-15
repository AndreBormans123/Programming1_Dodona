def alias_gen(f_name, l_name):
    alias_f = f_name[0].upper()
    alias_l = l_name[0].upper()
    if not (f_name.isalpha() and l_name.isalpha()):
        return "Your name must start with a letter from A - Z"
    else:
        first_name_alias = FIRST_NAME.get(alias_f)
        last_name_alias = SURNAME.get(alias_l)
        return first_name_alias + " " + last_name_alias

FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache'}
SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst' }

print(alias_gen('123abc', 'Petrovic'))
string = "Niemand verwacht de Spaanse Inquisitie\# In feite,! zij die de Spaanse Inquisitie wel verwachten..."

search = string.find("#")
string = string[:search]
print(string)
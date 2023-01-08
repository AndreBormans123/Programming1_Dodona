# https://dodona.ugent.be/nl/courses/1286/series/14357/activities/1551924012

#Variabele declareren
klinkers = ["a", "e", "o", "i", "u"]

def zonder_klinkers(locatie1, locatie2):
    #Maak een file aan in write mode
    write_file = open(locatie2, "w")
    
    #Open een file in read mode (sluit ook automatich, dus file.close() is niet nodig)
    with open(locatie1) as topo_file: 
        #Counters
        gelezen_counter = 0
        geschreven_counter = 0
        
        #maak een oneidinge loop
        while True:
        # Lees character bij character
            char = topo_file.read(1) #leest 1 character van de file
            gelezen_counter += 1
            if not char: #Als er geen text meer is sluit het programma dan
                break
            if char.lower() in klinkers: #Maak de tekst niet meer hoofdletter gevoelig
                continue
            elif not char in klinkers:  
                geschreven_counter += 1
                write_file.write(char)
                       

    return (gelezen_counter -1, geschreven_counter)
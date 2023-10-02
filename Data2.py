import json
import matplotlib.pyplot as plt
tehtavat = {}
valmiit_tehtavat = 0
kayttajanValmiitTehtavat = {}
#Tiedoston lukeminen ja tulostus:
with open('Data_analystointi2/todos.json', 'r') as file:
    data = json.load(file)

if data:
    tehtavien_maara = len(data)
    ekarivi = data[0]
    print("----------------------------------------------------")
    print("Ensimmäinen tehtävä:")
    print("userId:", ekarivi["userId"])
    print("id:", ekarivi["id"])
    print("title:", ekarivi["title"])
    print("completed:", ekarivi["completed"])
    print("----------------------------------------------------")
    for tehtava in data:
        #Käydään läpi kaikki "completed" rivit tiedostosta, mikäli arvo on true, lisätään valmiit tehtävät muuttujaan + 1
        #Näin saadaan tietoon kaikki valmiit tehtävät
        if tehtava["completed"] == True:
                valmiit_tehtavat += 1

        #Luetaan kaikkien käyttäjien id:t. Mikäli käyttäjän id ei löydy tehtavat listasta, annetaan alkuarvoksi 1
        #Mikäli kyseinen id löytyy jo listasta, lisätään alkuarvoon + 1
        #Näin saadaan tietoon kuinka monta tehtävää kullakin käyttäjällä on
        kayttajan_id = tehtava["userId"]
        if kayttajan_id not in tehtavat:
            tehtavat[kayttajan_id] = 1
        else:
            tehtavat[kayttajan_id] += 1
        
        #Luetaan kaikki suoritetut tehtävät(completed = true), jos käyttäjän id ei ole uudessa listassa, annetaan alkuarvo 1
        #Mikäli käyttäjän id on jo listassa, lisätään alkuarvoon + 1.
        #Näin saadaan tietoon, kuinka monta tehtävää kukin käyttäjä on suorittanut
        if tehtava["completed"] == True:
             if kayttajan_id not in kayttajanValmiitTehtavat:
                  kayttajanValmiitTehtavat[kayttajan_id] = 1
             else:
                  kayttajanValmiitTehtavat[kayttajan_id] += 1

        
             
            
    print("Tehtavien määrä:" ,tehtavien_maara)
    print("Valmiit tehtävät:", valmiit_tehtavat)
    
    #Diagrammien piirto

    #Kaikki käyttäjät
    kayttajat = list(tehtavat.keys())
    #Jokaisen käyttäjän tehtävien määrät
    tehtavien_maarat = list(tehtavat.values())

    #Kaikki käyttäjät
    tehtavakayttajat = list(kayttajanValmiitTehtavat.keys())
    #Käyttäjien valmiiden tehtävien määrä.
    valmiittehtavat = list(kayttajanValmiitTehtavat.values())

    plt.bar(kayttajat, tehtavien_maarat)
    plt.xlabel('Käyttäjän id')
    plt.ylabel('Tehtävien määrä')
    plt.title('Tehtävien määrä per käyttäjä')
    plt.show()

    #Piirakkadiagrammi
    keskeneraiset_tehtavat = tehtavien_maara-valmiit_tehtavat
    labels = 'Valmiit', 'Keskeneräiset'
    sizes = [valmiit_tehtavat, keskeneraiset_tehtavat]
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title('Valmiiden ja keskeneräisten tehtävien suhde')
    plt.show()

    #Diagrammi käyttäjän valmiiden tehtävien määrälle
    plt.bar(tehtavakayttajat, valmiittehtavat)
    plt.xlabel('Käyttäjän id')
    plt.ylabel('Valmiiksi saadut tehtävät')
    plt.title('Valmiiksi saadut tehtävät per käyttäjä')
    plt.show()
else:
    print("Ei toimi")


print("----------------------------------------------------")



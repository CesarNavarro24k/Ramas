meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "GG": "Good game",
            "CREEPY" : " aterrador, siniestro"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in meme_dict:
    print(meme_dict)
else:
    print("No tenemos esa palabra en el diccionario.")
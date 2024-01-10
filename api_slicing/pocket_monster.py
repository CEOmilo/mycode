#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()
    
    print(pokeapi["sprites"]["front_default"])
    
    for monster in pokeapi["moves"] :
        print(monster["move"]["name"])
        break  

    count_entries = len(pokeapi["game_indices"])
    print(count_entries)
        


    # print(pokeapi)

main()

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 15:03:38 2023

@author: higastca
"""

with open('C:/Users/higastca/Documents/Courses/AdventofCode/2023/AdventofCode02_input.txt') as f:
    contents = f.readlines()


def part_one(contents):
    bag = {'red':12,'green':13,'blue':14}
    count_id = 0
    
    for game in contents:
    
        # Dividindo IDs e games
        game = game.strip().split(':')
        
        # Id Number
        id_number = int(game[0][5:])
        
        # Boolean para checar se o jogo é válido
        is_valid = True
        
        # Checando se o jogo é válido
        # Separando os subgames de cada game
        for subgames in game[1].split(';'): 
            #Separando cada item de cada subgame
            for item in subgames.split(','): 
                
                # Tirando espaços vazios
                mystr = item.strip()
                
                # Checando o número de cubos retirados para cada cor
                if 'blue' in mystr:
                    if int(mystr[:-5]) > bag['blue']:
                        is_valid = False
                
                elif 'green' in mystr:
                    if int(mystr[:-6]) > bag['green']:
                        is_valid = False
                        
                elif 'red' in mystr:
                    if int(mystr[:-4]) > bag['red']:
                        is_valid = False
        
        # Adicionando ao contador quando o game continua válido
        if is_valid == True:
            count_id += id_number
            
    return(count_id)

part_one(contents)

def part_two(contents):
    sum_power = 0
    
    for game in contents:
    
        # Excluindo o ID
        game = game.strip().split(':')[1]
        
        # Criando listas para cada cor (1 não afeta a multiplicação final)
        blue,red,green = [1],[1],[1]
        
        # Separando os subgames de cada game
        for subgames in game.split(';'):
            #Separando cada item de cada subgame
            for item in subgames.split(','):
                
                # Tirando espaços vazios
                mystr = item.strip()
                
                # Adicionando as listas a qnt de cubos retirados p/ cada cor
                if 'blue' in mystr:
                    blue.append(int(mystr[:-5]))
                
                elif 'green' in mystr:
                    green.append(int(mystr[:-6]))
                        
                elif 'red' in mystr:
                    red.append(int(mystr[:-4]))
        
        # Adicionando ao total o mínimo necessário para jogar cada jogo
        sum_power += max(blue)*max(red)*max(green)
        
    return(sum_power)

part_two(contents)

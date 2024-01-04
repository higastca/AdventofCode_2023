# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:20:06 2024

@author: higastca
"""
import re

with open('C:/Users/higastca/Documents/Courses/AdventofCode/2023/AdventofCode03_input.txt', 'r') as f: 
    contents = f.readlines()

def part_one(contents):
    
    # Transformando em uma linha contínua
    size = len(contents[0])
    lines = ''
    
    for i in contents:
        lines += '.'+i.strip()
    
    chars = '#*%/-$@+&='
    
    # Achando todos os números e seus índices
    numbers = {m.start(0):int(m.group(0)) for m in re.finditer("\d+", lines)}
    
    # Somatório
    soma = 0
    
    # Encontrando os valores das bordas de cada um dos números
    # Usando size para 'pular' a linha e achar os de baixo e de cima
    for k,v in numbers.items():
        left = lines[k-1]
        right = lines[k+len(str(v))]
        below = ''
        upper = ''
        
        # Condição para não dar erro nas linhas de baixo e de cima
        if k < len(lines)-size:
            below = lines[k-1+size:k+len(str(v))+size+1]
        
        if k > size:
            upper = lines[k-1-size:k+len(str(v))-size+1]
        
        evt = [left,right,below,upper]
        
        # Checando se há algum caractere especial ao redor do número
        is_valid = False
        
        for char in chars:
            if char in ''.join(evt):
                is_valid = True
        
        if is_valid:
            soma += v
    
    return soma

part_one(contents)

def part_two(contents):
    
    # Transformando em uma linha contínua
    size = len(contents[0])
    lines = ''
    
    for i in contents:
        lines += '.'+i.strip()
    
    # Achando todos os números e seus índices
    numbers = {m.start(0):int(m.group(0)) for m in re.finditer("\d+", lines)}
    
    # Repetindo o valor para os índices ao longo do número
    numbers_extended = numbers.copy()
    
    for k,v in numbers.items():
        for tam in range(len(str(v))):
            numbers_extended[k+tam] = v
    
    # Achando todos os asteriscos e seus índices
    asterisks = [m.start(0) for m in re.finditer("\*", lines)]
    
    # Somatório
    soma = 0
    
    # Encontrando os indices das bordas de cada um dos asteriscos
    # Usando size para 'pular' a linha e achar os de baixo e de cima
    for i in asterisks:
        coor = [i-1,i+1]
        gears = set()
        
        if i < len(lines)-size:
            coor.append(i-1+size)
            coor.append(i+size)
            coor.append(i+size+1)
        
        if i > size:
            coor.append(i-1-size)
            coor.append(i-size)
            coor.append(i+1-size)
        
        # Mesclando os indices das coordenadas em volta do asterisco com
        # os valores do dict number
        for indice in coor:
            try:
                gears.add(numbers_extended[indice])
            except:
                pass
        
        gears = list(gears)
        
        # Somando a multiplicação dos gears de cada um dos asteriscos
        try:
            soma += gears[0]*gears[1]
        except:
            pass
        
    return soma

part_two(contents)
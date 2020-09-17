#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Este programa devuelve una lista de listas, con informacion relacionada a un seller_id y un site_id, especificada de la siquiente forma:
[id_item, title, category_id, name]
"""

__author__ = "Agustin Palau"
__version__ = "1.0.1"
__email__ = "apalau@frd.utn.edu.ar"
__status__ = "Test"

# Se importan los paquetes a utilizar
import json
import sys
import requests

if len(sys.argv) == 3:
    # Almaceno los parametros ingresados desde el script
    user_id = str(sys.argv[1])
    site_id = str(sys.argv[2])

    # Obtengo los datos del seller id que proporciona ML
    seller_request = requests.get('https://api.mercadolibre.com/users/' + user_id)
    seller_info = json.loads(seller_request.content)

    # Obtengo el nick name del vendedor en cuestion
    nick_name = seller_info['nickname']

    # Obtengo las ventas del seller en cuestion y del site id en cuestion
    nickname_request = requests.get('https://api.mercadolibre.com/sites/' + site_id + '/search?nickname=' + nick_name)
    seller_items = json.loads(nickname_request.content)

    # Inicializo una lista para mostrar como resultado
    list_items = []
    
    # Este ciclo me permite agregar a la lista los datos que necesito para mostrar como resultado
    for i in seller_items['results']:

        # Adquirir las categorias de los productos que vende el seller
        category_request = requests.get('https://api.mercadolibre.com/categories/' + i['category_id'])
        category_item = json.loads(category_request.content)

        # Busco la categoria correspondiete a la venta
        if i['category_id'] == category_item['id']:

            # Sumo a la lista los productos con los datos requeridos
            list_items.append((i['id'], i['title'], i['category_id'], category_item['name']))

    # Genero un archivo de extension log con los datos requeridos
    with open(f'data_{user_id}.log', 'w') as outfile:
        json.dump(list_items, outfile)
    
else:
    print("Error")


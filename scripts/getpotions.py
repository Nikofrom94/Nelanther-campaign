
import json,csv

mequip_filename = '/home/nicolas/GCS/Master Library/Magic/Magic Equipment.eqp'

all_potions = []

with open(mequip_filename) as mequip_file:
    mequip_json = json.load(mequip_file)
    for row_requip in mequip_json['rows']:
        if row_requip['description'] == "Potions":
            potions = row_requip
            for potion in potions['children']:
                all_potions.append(potion)

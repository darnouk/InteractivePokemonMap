# Python script to generate subpages for each location

locations = [
    {'id': 'johto_safari-zone', 'name': 'Safari Zone', 'type': 'Other', 'region': 'Johto', 'lat': -5.353571, 'lng': -101.953125},
    {'id': 'johto_cianwood-city', 'name': 'Cianwood City', 'type': 'City', 'region': 'Johto', 'lat': -13.757441, 'lng': -90.087891},
    {'id': 'johto_whirl-islands', 'name': 'Whirl Islands', 'type': 'Other', 'region': 'Johto', 'lat': -13.757441, 'lng': -78.486328},
    {'id': 'johto_olivine-city', 'name': 'Olivine City', 'type': 'City', 'region': 'Johto', 'lat': 1.585693, 'lng': -74.882813},
    {'id': 'johto_battle-frontier', 'name': 'Battle Frontier', 'type': 'Other', 'region': 'Johto', 'lat': 6.758637, 'lng': -82.089844},
    {'id': 'johto_ecruteak-city', 'name': 'Ecruteak City', 'type': 'City', 'region': 'Johto', 'lat': 18.992144, 'lng': -53.085938},
    {'id': 'johto_national-park', 'name': 'National Park', 'type': 'Other', 'region': 'Johto', 'lat': 3.957131, 'lng': -61.611328},
    {'id': 'johto_goldenrod-city', 'name': 'Goldenrod City', 'type': 'City', 'region': 'Johto', 'lat': -13.757441, 'lng': -61.611328},
    {'id': 'johto_ilex-forest', 'name': 'Ilex Forest', 'type': 'Other', 'region': 'Johto', 'lat': -30.005789, 'lng': -61.611328},
    {'id': 'johto_azalea-town', 'name': 'Azalea Town', 'type': 'Town', 'region': 'Johto', 'lat': -30.005789, 'lng': -54.580078},
    {'id': 'johto_union-cave', 'name': 'Union Cave', 'type': 'Other', 'region': 'Johto', 'lat': -30.005789, 'lng': -41.835938},
    {'id': 'johto_ruins-of-alph', 'name': 'Ruins Of Alph', 'type': 'Other', 'region': 'Johto', 'lat': -4.565078, 'lng': -47.636719},
    {'id': 'johto_violet-city', 'name': 'Violet City', 'type': 'City', 'region': 'Johto', 'lat': 3.957131, 'lng': -41.835938},
    {'id': 'johto_mt-mortar', 'name': 'Mt Mortar', 'type': 'Other', 'region': 'Johto', 'lat': 18.992144, 'lng': -44.121094},
    {'id': 'johto_mahogany-town', 'name': 'Mahogany Town', 'type': 'Town', 'region': 'Johto', 'lat': 18.992144, 'lng': -35.595703},
    {'id': 'johto_lake-of-rage', 'name': 'Lake Of Rage', 'type': 'Other', 'region': 'Johto', 'lat': 34.9056, 'lng': -35.419922},
    {'id': 'johto_ice-path', 'name': 'Ice Path', 'type': 'Other', 'region': 'Johto', 'lat': 18.992144, 'lng': -21.445312},
    {'id': 'johto_blackthorn-city', 'name': 'Blackthorn City', 'type': 'City', 'region': 'Johto', 'lat': 18.992144, 'lng': -15.029297},
    {'id': 'johto_dark-cave-north', 'name': 'Dark Cave North', 'type': 'Other', 'region': 'Johto', 'lat': 11.18754, 'lng': -15.029297},
    {'id': 'johto_dark-cave-south', 'name': 'Dark Cave South', 'type': 'Other', 'region': 'Johto', 'lat': -5.441121, 'lng': -20.478516},
    {'id': 'johto_dark-cave-west', 'name': 'Dark Cave West', 'type': 'Other', 'region': 'Johto', 'lat': 3.957131, 'lng': -29.707031},
    {'id': 'johto_cherrygrove-city', 'name': 'Cherrygrove City', 'type': 'City', 'region': 'Johto', 'lat': -16.979186, 'lng': -29.707031},
    {'id': 'johto_new-bark-town', 'name': 'New Bark Town', 'type': 'Town', 'region': 'Johto', 'lat': -16.979186, 'lng': -11.25},
    {'id': 'johto_tohjo-falls', 'name': 'Tohjo Falls', 'type': 'Other', 'region': 'Johto', 'lat': -16.979186, 'lng': -0.0439453},
    {'id': 'johto_mt-silver', 'name': 'Mt Silver', 'type': 'Other', 'region': 'Johto', 'lat': 0.178853, 'lng': -0.0439453},
    {'id': 'kanto_indigo-plateau', 'name': 'Indigo Plateau', 'type': 'Other', 'region': 'Kanto', 'lat': 30.239124, 'lng': 14.677734},
    {'id': 'kanto_victory-road', 'name': 'Victory Road', 'type': 'Other', 'region': 'Kanto', 'lat': 18.992144, 'lng': 14.677734},
    {'id': 'kanto_viridian-city', 'name': 'Viridian City', 'type': 'City', 'region': 'Kanto', 'lat': 0.178853, 'lng': 31.816406},
    {'id': 'kanto_viridian-forest', 'name': 'Viridian Forest', 'type': 'Other', 'region': 'Kanto', 'lat': 12.638404, 'lng': 31.816406},
    {'id': 'kanto_digletts-cave-nw', 'name': 'Digletts Cave NW', 'type': 'Other', 'region': 'Kanto', 'lat': 20.14075, 'lng': 31.816406},
    {'id': 'kanto_pewter-city', 'name': 'Pewter City', 'type': 'City', 'region': 'Kanto', 'lat': 26.829907, 'lng': 31.816406},
    {'id': 'kanto_mt-moon', 'name': 'Mt Moon', 'type': 'Other', 'region': 'Kanto', 'lat': 26.829907, 'lng': 49.042969},
    {'id': 'kanto_cerulean-city', 'name': 'Cerulean City', 'type': 'City', 'region': 'Kanto', 'lat': 26.829907, 'lng': 65.654297},
    {'id': 'kanto_rock-tunnel', 'name': 'Rock Tunnel', 'type': 'Other', 'region': 'Kanto', 'lat': 26.829907, 'lng': 87.099609},
    {'id': 'kanto_power-plant', 'name': 'Power Plant', 'type': 'Other', 'region': 'Kanto', 'lat': 21.777237, 'lng': 90},
    {'id': 'kanto_lavendar-town', 'name': 'Lavendar Town', 'type': 'Town', 'region': 'Kanto', 'lat': 10.737428, 'lng': 87.099609},
    {'id': 'kanto_saffron-city', 'name': 'Saffron City', 'type': 'City', 'region': 'Kanto', 'lat': 10.737428, 'lng': 65.654297},
    {'id': 'kanto_digletts-cave-se', 'name': 'Digletts Cave SE', 'type': 'Other', 'region': 'Kanto', 'lat': -3.180018, 'lng': 72.509766},
    {'id': 'kanto_vermillion-city', 'name': 'Vermillion City', 'type': 'City', 'region': 'Kanto', 'lat': -3.180018, 'lng': 65.654297},
    {'id': 'kanto_celadon-city', 'name': 'Celadon City', 'type': 'City', 'region': 'Kanto', 'lat': 10.737428, 'lng': 50.537109},
    {'id': 'kanto_fuschia-city', 'name': 'Fuschia City', 'type': 'City', 'region': 'Kanto', 'lat': -24.95379, 'lng': 60.556641},
    {'id': 'kanto_seafoam-islands', 'name': 'Seafoam Islands', 'type': 'Other', 'region': 'Kanto', 'lat': -33.020028, 'lng': 46.40625},
    {'id': 'kanto_cinnabar-island', 'name': 'Cinnabar Island', 'type': 'Other', 'region': 'Kanto', 'lat': -33.020028, 'lng': 31.816406},
    {'id': 'kanto_pallet-town', 'name': 'Pallet Town', 'type': 'Town', 'region': 'Kanto', 'lat': -18.087182, 'lng': 31.816406},
]

for location in locations:
    subpage_name = location['id'].lower() + '.html'
    with open(subpage_name, 'w') as subpage_file:
        subpage_file.write(f'<!DOCTYPE html>\n'
                           f'<html lang="en">\n'
                           f'<head>\n'
                           f'    <meta charset="UTF-8">\n'
                           f'    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
                           f'    <title>{location["name"]}</title>\n'
                           f'</head>\n'
                           f'<body>\n'
                           f'    <h1>{location["name"]}</h1>\n'
                           f'    <p>This is the {location["name"]} subpage. Add your content here.</p>\n'
                           f'    <!-- Add any additional content, images, etc. -->\n'
                           f'</body>\n'
                           f'</html>\n')

print("Subpages created successfully.")
def main():
    f = # fill in file name here
    x = text_rip(f)
    print(x)

def text_rip(file):
    # import the necessary packages
    from PIL import Image
    import pytesseract


    pkmon = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran-F', 'Nidorina', 'Nidoqueen', 'Nidoran-M', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', "Farfetch'd", 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr. Mime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo', 'Mew', 'Chikorita', 'Bayleef', 'Meganium', 'Cyndaquil', 'Quilava', 'Typhlosion', 'Totodile', 'Croconaw', 'Feraligatr', 'Sentret', 'Furret', 'Hoothoot', 'Noctowl', 'Ledyba', 'Ledian', 'Spinarak', 'Ariados', 'Crobat', 'Chinchou', 'Lanturn', 'Pichu', 'Cleffa', 'Igglybuff', 'Togepi', 'Togetic', 'Natu', 'Xatu', 'Mareep', 'Flaaffy', 'Ampharos', 'Bellossom', 'Marill', 'Azumarill', 'Sudowoodo', 'Politoed', 'Hoppip', 'Skiploom', 'Jumpluff', 'Aipom', 'Sunkern', 'Sunflora', 'Yanma', 'Wooper', 'Quagsire', 'Espeon', 'Umbreon', 'Murkrow', 'Slowking', 'Misdreavus', 'Unown', 'Wobbuffet', 'Girafarig', 'Pineco', 'Forretress', 'Dunsparce', 'Gligar', 'Steelix', 'Snubbull', 'Granbull', 'Qwilfish', 'Scizor', 'Shuckle', 'Heracross', 'Sneasel', 'Teddiursa', 'Ursaring', 'Slugma', 'Magcargo', 'Swinub', 'Piloswine', 'Corsola', 'Remoraid', 'Octillery', 'Delibird', 'Mantine', 'Skarmory', 'Houndour', 'Houndoom', 'Kingdra', 'Phanpy', 'Donphan', 'Porygon2', 'Stantler', 'Smeargle', 'Tyrogue', 'Hitmontop', 'Smoochum', 'Elekid', 'Magby', 'Miltank', 'Blissey', 'Raikou', 'Entei', 'Suicune', 'Larvitar', 'Pupitar', 'Tyranitar', 'Lugia', 'Ho-Oh', 'Celebi', 'Treecko', 'Grovyle', 'Sceptile', 'Torchic', 'Combusken', 'Blaziken', 'Mudkip', 'Marshtomp', 'Swampert', 'Poochyena', 'Mightyena', 'Zigzagoon', 'Linoone', 'Wurmple', 'Silcoon', 'Beautifly', 'Cascoon', 'Dustox', 'Lotad', 'Lombre', 'Ludicolo', 'Seedot', 'Nuzleaf', 'Shiftry', 'Taillow', 'Swellow', 'Wingull', 'Pelipper', 'Ralts', 'Kirlia', 'Gardevoir', 'Surskit', 'Masquerain', 'Shroomish', 'Breloom', 'Slakoth', 'Vigoroth', 'Slaking', 'Nincada', 'Ninjask', 'Shedinja', 'Whismur', 'Loudred', 'Exploud', 'Makuhita', 'Hariyama', 'Azurill', 'Nosepass', 'Skitty', 'Delcatty', 'Sableye', 'Mawile', 'Aron', 'Lairon', 'Aggron', 'Meditite', 'Medicham', 'Electrike', 'Manectric', 'Plusle', 'Minun', 'Volbeat', 'Illumise', 'Roselia', 'Gulpin', 'Swalot', 'Carvanha', 'Sharpedo', 'Wailmer', 'Wailord', 'Numel', 'Camerupt', 'Torkoal', 'Spoink', 'Grumpig', 'Spinda', 'Trapinch', 'Vibrava', 'Flygon', 'Cacnea', 'Cacturne', 'Swablu', 'Altaria', 'Zangoose', 'Seviper', 'Lunatone', 'Solrock', 'Barboach', 'Whiscash', 'Corphish', 'Crawdaunt', 'Baltoy', 'Claydol', 'Lileep', 'Cradily', 'Anorith', 'Armaldo', 'Feebas', 'Milotic', 'Kecleon', 'Shuppet', 'Banette', 'Duskull', 'Dusclops', 'Tropius', 'Chimecho', 'Absol', 'Wynaut', 'Snorunt', 'Glalie', 'Spheal', 'Sealeo', 'Walrein', 'Clamperl', 'Huntail', 'Gorebyss', 'Relicanth', 'Luvdisc', 'Bagon', 'Shelgon', 'Salamence', 'Beldum', 'Metang', 'Metagross', 'Regirock', 'Regice', 'Registeel', 'Latias', 'Latios', 'Kyogre', 'Groudon', 'Rayquaza', 'Jirachi', 'Deoxys', 'Turtwig', 'Grotle', 'Torterra', 'Chimchar', 'Monferno', 'Infernape', 'Piplup', 'Prinplup', 'Empoleon', 'Starly', 'Staravia', 'Staraptor', 'Bidoof', 'Bibarel', 'Kricketot', 'Kricketune', 'Shinx', 'Luxio', 'Luxray', 'Budew', 'Roserade', 'Cranidos', 'Rampardos', 'Shieldon', 'Bastiodon', 'Burmy', 'Wormadam', 'Mothim', 'Combee', 'Vespiquen', 'Pachirisu', 'Buizel', 'Floatzel', 'Cherubi', 'Cherrim', 'Shellos', 'Gastrodon', 'Ambipom', 'Drifloon', 'Drifblim', 'Buneary', 'Lopunny', 'Mismagius', 'Honchkrow', 'Glameow', 'Purugly', 'Chingling', 'Stunky', 'Skuntank', 'Bronzor', 'Bronzong', 'Bonsly', 'Mime Jr.', 'Happiny', 'Chatot', 'Spiritomb', 'Gible', 'Gabite', 'Garchomp', 'Munchlax', 'Riolu', 'Lucario', 'Hippopotas', 'Hippowdon', 'Skorupi', 'Drapion', 'Croagunk', 'Toxicroak', 'Carnivine', 'Finneon', 'Lumineon', 'Mantyke', 'Snover', 'Abomasnow', 'Weavile', 'Magnezone', 'Lickilicky', 'Rhyperior', 'Tangrowth', 'Electivire', 'Magmortar', 'Togekiss', 'Yanmega', 'Leafeon', 'Glaceon', 'Gliscor', 'Mamoswine', 'Porygon-Z', 'Gallade', 'Probopass', 'Dusknoir', 'Froslass', 'Rotom', 'Uxie', 'Mesprit', 'Azelf', 'Dialga', 'Palkia', 'Heatran', 'Regigigas', 'Giratina', 'Cresselia', 'Phione', 'Manaphy', 'Darkrai', 'Shaymin', 'Arceus', 'Rattata-A', 'Exegutor-A', 'Grimer-A', 'Muk-A', 'Meowth-A', 'Persian-A', 'Vulpix-A', 'Ninetails-A', 'Sandshrew-A', 'Sandslash-A', 'Raticate-A', 'Diglett-A', 'Dugtrio-A', 'Geodude-A', 'Graveler-A', 'Golem-A', 'Raichu-A', 'Marowak-A', 'Castform']

    level = ["1.0", "1.5", "2.0", "2.5", "3.0", "3.5", "4.0", "4.5", "5.0", "5.5", "6.0", "6.5", "7.0", "7.5", "8.0", "8.5", "9.0", "9.5", "10.0", "10.5", "11.0", "11.5", "12.0", "12.5", "13.0", "13.5", "14.0", "14.5", "15.0", "15.5", "16.0", "16.5", "17.0", "17.5", "18.0", "18.5", "19.0", "19.5", "20.0", "20.5", "21.0", "21.5", "22.0", "22.5", "23.0", "23.5", "24.0", "24.5", "25.0", "25.5", "26.0", "26.5", "27.0", "27.5", "28.0", "28.5", "29.0", "29.5", "30.0", "30.5", "31.0", "31.5", "32.0", "32.5", "33.0", "33.5", "34.0", "34.5", "35.0", "35.5", "36.0", "36.5", "37.0", "37.5", "38.0", "38.5", "39.0", "39.5", "40.0"]

    per = ['100.0', '99.9', '99.8', '99.7', '99.6', '99.5', '99.4', '99.3', '99.2', '99.1', '99.0', '98.9', '98.8', '98.7', '98.6', '98.5', '98.4', '98.3', '98.2', '98.1', '98.0', '97.9', '97.8', '97.7', '97.6', '97.5', '97.4', '97.3', '97.2', '97.1', '97.0', '96.9', '96.8', '96.7', '96.6', '96.5', '96.4', '96.3', '96.2', '96.1', '96.0', '95.9', '95.8', '95.7', '95.6', '95.5', '95.4', '95.3', '95.2', '95.1', '95.0', '94.9', '94.8', '94.7', '94.6', '94.5', '94.4', '94.3', '94.2', '94.1', '94.0', '93.9', '93.8', '93.7', '93.6', '93.5', '93.4', '93.3', '93.2', '93.1', '93.0', '92.9', '92.8', '92.7', '92.6', '92.5', '92.4', '92.3', '92.2', '92.1', '92.0', '91.9', '91.8', '91.7', '91.6', '91.5', '91.4', '91.3', '91.2', '91.1', '91.0', '90.9', '90.8', '90.7', '90.6', '90.5', '90.4', '90.3', '90.2', '90.1', '90.0', '89.9', '89.8', '89.7', '89.6', '89.5', '89.4', '89.3', '89.2', '89.1', '89.0', '88.9', '88.8', '88.7', '88.6', '88.5', '88.4', '88.3', '88.2', '88.1', '88.0', '87.9', '87.8', '87.7', '87.6', '87.5', '87.4', '87.3', '87.2', '87.1', '87.0', '86.9', '86.8', '86.7', '86.6', '86.5', '86.4', '86.3', '86.2', '86.1', '86.0', '85.9', '85.8', '85.7', '85.6', '85.5', '85.4', '85.3', '85.2', '85.1', '85.0', '84.9', '84.8', '84.7', '84.6', '84.5', '84.4', '84.3', '84.2', '84.1', '84.0', '83.9', '83.8', '83.7', '83.6', '83.5', '83.4', '83.3', '83.2', '83.1', '83.0', '82.9', '82.8', '82.7', '82.6', '82.5', '82.4', '82.3', '82.2', '82.1', '82.0', '81.9', '81.8', '81.7', '81.6', '81.5', '81.4', '81.3', '81.2', '81.1', '81.0', '80.9', '80.8', '80.7', '80.6', '80.5', '80.4', '80.3', '80.2', '80.1', '80.0', '79.9', '79.8', '79.7', '79.6', '79.5', '79.4', '79.3', '79.2', '79.1', '79.0', '78.9', '78.8', '78.7', '78.6', '78.5', '78.4', '78.3', '78.2', '78.1', '78.0', '77.9', '77.8', '77.7', '77.6', '77.5', '77.4', '77.3', '77.2', '77.1', '77.0', '76.9', '76.8', '76.7', '76.6', '76.5', '76.4', '76.3', '76.2', '76.1', '76.0', '75.9', '75.8', '75.7', '75.6', '75.5', '75.4', '75.3', '75.2', '75.1', '75.0', '74.9', '74.8', '74.7', '74.6', '74.5', '74.4', '74.3', '74.2', '74.1', '74.0', '73.9', '73.8', '73.7', '73.6', '73.5', '73.4', '73.3', '73.2', '73.1', '73.0', '72.9', '72.8', '72.7', '72.6', '72.5', '72.4', '72.3', '72.2', '72.1', '72.0', '71.9', '71.8', '71.7', '71.6', '71.5', '71.4', '71.3', '71.2', '71.1', '71.0', '70.9', '70.8', '70.7', '70.6', '70.5', '70.4', '70.3', '70.2', '70.1', '70.0', '69.9', '69.8', '69.7', '69.6', '69.5', '69.4', '69.3', '69.2', '69.1', '69.0', '68.9', '68.8', '68.7', '68.6', '68.5', '68.4', '68.3', '68.2', '68.1', '68.0', '67.9', '67.8', '67.7', '67.6', '67.5', '67.4', '67.3', '67.2', '67.1', '67.0', '66.9', '66.8', '66.7', '66.6', '66.5', '66.4', '66.3', '66.2', '66.1', '66.0', '65.9', '65.8', '65.7', '65.6', '65.5', '65.4', '65.3', '65.2', '65.1', '65.0', '64.9', '64.8', '64.7', '64.6', '64.5', '64.4', '64.3', '64.2', '64.1', '64.0', '63.9', '63.8', '63.7', '63.6', '63.5', '63.4', '63.3', '63.2', '63.1', '63.0', '62.9', '62.8', '62.7', '62.6', '62.5', '62.4', '62.3', '62.2', '62.1', '62.0', '61.9', '61.8', '61.7', '61.6', '61.5', '61.4', '61.3', '61.2', '61.1', '61.0', '60.9', '60.8', '60.7', '60.6', '60.5', '60.4', '60.3', '60.2', '60.1', '60.0', '59.9', '59.8', '59.7', '59.6', '59.5', '59.4', '59.3', '59.2', '59.1', '59.0', '58.9', '58.8', '58.7', '58.6', '58.5', '58.4', '58.3', '58.2', '58.1', '58.0', '57.9', '57.8', '57.7', '57.6', '57.5', '57.4', '57.3', '57.2', '57.1', '57.0', '56.9', '56.8', '56.7', '56.6', '56.5', '56.4', '56.3', '56.2', '56.1', '56.0', '55.9', '55.8', '55.7', '55.6', '55.5', '55.4', '55.3', '55.2', '55.1', '55.0', '54.9', '54.8', '54.7', '54.6', '54.5', '54.4', '54.3', '54.2', '54.1', '54.0', '53.9', '53.8', '53.7', '53.6', '53.5', '53.4', '53.3', '53.2', '53.1', '53.0', '52.9', '52.8', '52.7', '52.6', '52.5', '52.4', '52.3', '52.2', '52.1', '52.0', '51.9', '51.8', '51.7', '51.6', '51.5', '51.4', '51.3', '51.2', '51.1', '51.0', '50.9', '50.8', '50.7', '50.6', '50.5', '50.4', '50.3', '50.2', '50.1', '50.0', '49.9', '49.8', '49.7', '49.6', '49.5', '49.4', '49.3', '49.2', '49.1', '49.0', '48.9', '48.8', '48.7', '48.6', '48.5', '48.4', '48.3', '48.2', '48.1', '48.0', '47.9', '47.8', '47.7', '47.6', '47.5', '47.4', '47.3', '47.2', '47.1', '47.0', '46.9', '46.8', '46.7', '46.6', '46.5', '46.4', '46.3', '46.2', '46.1', '46.0', '45.9', '45.8', '45.7', '45.6', '45.5', '45.4', '45.3', '45.2', '45.1', '45.0', '44.9', '44.8', '44.7', '44.6', '44.5', '44.4', '44.3', '44.2', '44.1', '44.0', '43.9', '43.8', '43.7', '43.6', '43.5', '43.4', '43.3', '43.2', '43.1', '43.0', '42.9', '42.8', '42.7', '42.6', '42.5', '42.4', '42.3', '42.2', '42.1', '42.0', '41.9', '41.8', '41.7', '41.6', '41.5', '41.4', '41.3', '41.2', '41.1', '41.0', '40.9', '40.8', '40.7', '40.6', '40.5', '40.4', '40.3', '40.2', '40.1', '40.0', '39.9', '39.8', '39.7', '39.6', '39.5', '39.4', '39.3', '39.2', '39.1', '39.0', '38.9', '38.8', '38.7', '38.6', '38.5', '38.4', '38.3', '38.2', '38.1', '38.0', '37.9', '37.8', '37.7', '37.6', '37.5', '37.4', '37.3', '37.2', '37.1', '37.0', '36.9', '36.8', '36.7', '36.6', '36.5', '36.4', '36.3', '36.2', '36.1', '36.0', '35.9', '35.8', '35.7', '35.6', '35.5', '35.4', '35.3', '35.2', '35.1', '35.0', '34.9', '34.8', '34.7', '34.6', '34.5', '34.4', '34.3', '34.2', '34.1', '34.0', '33.9', '33.8', '33.7', '33.6', '33.5', '33.4', '33.3', '33.2', '33.1', '33.0', '32.9', '32.8', '32.7', '32.6', '32.5', '32.4', '32.3', '32.2', '32.1', '32.0', '31.9', '31.8', '31.7', '31.6', '31.5', '31.4', '31.3', '31.2', '31.1', '31.0', '30.9', '30.8', '30.7', '30.6', '30.5', '30.4', '30.3', '30.2', '30.1', '30.0', '29.9', '29.8', '29.7', '29.6', '29.5', '29.4', '29.3', '29.2', '29.1', '29.0', '28.9', '28.8', '28.7', '28.6', '28.5', '28.4', '28.3', '28.2', '28.1', '28.0', '27.9', '27.8', '27.7', '27.6', '27.5', '27.4', '27.3', '27.2', '27.1', '27.0', '26.9', '26.8', '26.7', '26.6', '26.5', '26.4', '26.3', '26.2', '26.1', '26.0', '25.9', '25.8', '25.7', '25.6', '25.5', '25.4', '25.3', '25.2', '25.1', '25.0', '24.9', '24.8', '24.7', '24.6', '24.5', '24.4', '24.3', '24.2', '24.1', '24.0', '23.9', '23.8', '23.7', '23.6', '23.5', '23.4', '23.3', '23.2', '23.1', '23.0', '22.9', '22.8', '22.7', '22.6', '22.5', '22.4', '22.3', '22.2', '22.1', '22.0', '21.9', '21.8', '21.7', '21.6', '21.5', '21.4', '21.3', '21.2', '21.1', '21.0', '20.9', '20.8', '20.7', '20.6', '20.5', '20.4', '20.3', '20.2', '20.1', '20.0', '19.9', '19.8', '19.7', '19.6', '19.5', '19.4', '19.3', '19.2', '19.1', '19.0', '18.9', '18.8', '18.7', '18.6', '18.5', '18.4', '18.3', '18.2', '18.1', '18.0', '17.9', '17.8', '17.7', '17.6', '17.5', '17.4', '17.3', '17.2', '17.1', '17.0', '16.9', '16.8', '16.7', '16.6', '16.5', '16.4', '16.3', '16.2', '16.1', '16.0', '15.9', '15.8', '15.7', '15.6', '15.5', '15.4', '15.3', '15.2', '15.1', '15.0', '14.9', '14.8', '14.7', '14.6', '14.5', '14.4', '14.3', '14.2', '14.1', '14.0', '13.9', '13.8', '13.7', '13.6', '13.5', '13.4', '13.3', '13.2', '13.1', '13.0', '12.9', '12.8', '12.7', '12.6', '12.5', '12.4', '12.3', '12.2', '12.1', '12.0', '11.9', '11.8', '11.7', '11.6', '11.5', '11.4', '11.3', '11.2', '11.1', '11.0', '10.9', '10.8', '10.7', '10.6', '10.5', '10.4', '10.3', '10.2', '10.1', '10.0', '9.9', '9.8', '9.7', '9.6', '9.5', '9.4', '9.3', '9.2', '9.1', '9.0', '8.9', '8.8', '8.7', '8.6', '8.5', '8.4', '8.3', '8.2', '8.1', '8.0', '7.9', '7.8', '7.7', '7.6', '7.5', '7.4', '7.3', '7.2', '7.1', '7.0', '6.9', '6.8', '6.7', '6.6', '6.5', '6.4', '6.3', '6.2', '6.1', '6.0', '5.9', '5.8', '5.7', '5.6', '5.5', '5.4', '5.3', '5.2', '5.1', '5.0', '4.9', '4.8', '4.7', '4.6', '4.5', '4.4', '4.3', '4.2', '4.1', '4.0', '3.9', '3.8', '3.7', '3.6', '3.5', '3.4', '3.3', '3.2', '3.1', '3.0', '2.9', '2.8', '2.7', '2.6', '2.5', '2.4', '2.3', '2.2', '2.1', '2.0', '1.9', '1.8', '1.7', '1.6', '1.5', '1.4', '1.3', '1.2', '1.1', '1.0']

    percent = []

    pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'

    im1 = Image.open(file)
    im2 = Image.open(file).convert('LA')

    te = pytesseract.image_to_string(im1)
    xt = pytesseract.image_to_string(im1)
    text = te + xt

    t = list(text.splitlines())

    for i in pkmon:
        for j in t:
            if i in j:
                name = i
                if name == "Castform":
                    x = eval(input("What form is the Castform? 1=Normal 2=Sunny 3=Rainy 4=Snowy"))
                    while x != (1, 2, 3, 4):
                            print("Not a valid response")
                            x = eval(input("What form is the Castform? 1=Normal 2=Sunny 3=Rainy 4=Snowy"))
                    else:
                        if x == 1:
                            name = "Castform-Normal"
                        elif x == 2:
                            name = "Castform-Sunny"
                        elif x == 3:
                            name = "Castform-Rainy"
                        elif x == 4:
                            name = "Castform-Snowy"
                else:
                    name = i

    for i in level:
        for j in t:
            if ("lvl " + i) in j:
                lvl = eval(i)
            elif ("Ivl " + i) in j:
                lvl = eval(i)
            elif ("lvI " + i) in j:
                lvl = eval(i)
            elif ("IvI " + i) in j:
                lvl = eval(i)
            elif "Level " in j:
                r = j.split()
                n = 0
                while "Level" not in r[n]:
                    n += 1
                else:
                    n += 1
                    lvl = eval(r[n])
            elif "Level" in j:
                r = j.split()
                n = 0
                while "Level" not in r[n]:
                    n += 1
                else:
                    s = r[n].replace("Level", "")
                    b = s.replace("/", "")
                    lvl = eval(b)
            else:
                im1.show()
                lvl = eval(input("What level is the Pokemon?"))
                break
            break
        break
                

    if "IV Combinations" or "IV COMBINATIONS" in j:
        combo = 3
    else:
        combo = 1

    for i in t:
        if "IV Range" in i:
            x = i.split()
            percents = x[2]
            if "-" in percents:
                percents = percents.split("-")
            elif "—" in percents:
                percents = percents.split("—")
            percents[0] = percents[0].replace("%", "")
            percents[1] = percents[1].replace("%", "")
            per1 = float(percents[0])
            per2 = float(percents[1])
            
            if per1 != per2:
                x = per1 + per2
                x = x/2
                x = round(x)
                a = 0
                d = 0
                h = 0

            elif combo > 1:
                combo = 2
                x = round(per1)
                a = 0
                d = 0
                h = 0

            else:
                x = per1
                i = 0
                while "Atk IV Def IV Sta IV" not in t[i]:
                    i += 1
                else:
                    ivs = t[i+1]
                    l = ivs.split()
                    atk = l[0]
                    defs = l[1]
                    hp = l[2]
                    if atk[0] == "1":
                        try:
                            a = eval(atk[0:2])
                        except:
                            a = eval(atk[0])
                    else:
                        a = eval(atk[0])
                    if defs[0] == "1":
                        try:
                            d = eval(defs[0:2])
                        except:
                            d = eval(defs[0])
                    else:
                        d = eval(defs[0])
                    if hp[0] == "1":
                        try:
                            h = eval(hp[0:2])
                        except:
                            h = eval(hp[0])
                    else:
                        h = eval(hp[0])
        elif "%" in i:
            p = i.split()
            for m in p:
                if "%" in m:
                    x = m.replace("%", "")
                    x = eval(x)
                    if combo > 1:
                        a = 0
                        d = 0
                        h = 0
                    elif combo == 1:
                        i = 0
                        while "Atk IV Def IV Sta IV" not in t[i]:
                            i += 1
                        else:
                            if t[i+1] == " " or t[i+1] == "":
                                ivs = t[i+2]
                            else:
                                ivs = t[i+1]
                            l = ivs.split()
                            print(l)
                            atk = l[0]
                            defs = l[1]
                            hp = l[2]
                            if atk[0] == "1":
                                try:
                                    a = eval(atk[0:2])
                                except:
                                    a = eval(atk[0])
                            else:
                                a = eval(atk[0])
                            if defs[0] == "1":
                                try:
                                    d = eval(defs[0:2])
                                except:
                                    d = eval(defs[0])
                            else:
                                d = eval(defs[0])
                            if hp[0] == "1":
                                try:
                                    h = eval(hp[0:2])
                                except:
                                    h = eval(hp[0])
                            else:
                                h = eval(hp[0])

        else:
                combo = 1
                x = 0
                i = 0
                while "Atk IV Def IV Sta IV" not in t[i]:
                    i += 1
                else:
                    if t[i+1] == "":
                        ivs = t [i+2]
                    else:
                        ivs = t[i+1]
                    l = ivs.split()
                    atk = l[0]
                    defs = l[1]
                    hp = l[2]
                    if atk[0] == "1":
                        try:
                            a = eval(atk[0:2])
                        except:
                            a = eval(atk[0])
                    else:
                        a = eval(atk[0])
                    if defs[0] == "1":
                        try:
                            d = eval(defs[0:2])
                        except:
                            d = eval(defs[0])
                    else:
                        d = eval(defs[0])
                    if hp[0] == "1":
                        try:
                            h = eval(hp[0:2])
                        except:
                            h = eval(hp[0])
                    else:
                        h = eval(hp[0])

    return name, lvl, combo, x, a, d, h

if __name__ == "__main__":
    main()

def main():
    name = "RelyingEarth87"
    lvl = 40
    import datetime
    d = datetime.datetime.today()
    month = d.month
    day = d.day
    is_caught = eval(input("This Pokemon was 1=Wild Caught 2=Traded "))
    sp = input("What is the species? ")
    if "-" in sp:
        spe, cies = sp.split("-")
        sp = spe.capitalize() + "-" + cies.capitalize()
    elif sp == "farfetch'd":
        sp = sp.capitalize()
    else:
        sp = sp.title()
    
    pkmon = ['Bulbasaur', 'Ivysaur', 'Venusaur', 'Charmander', 'Charmeleon', 'Charizard', 'Squirtle', 'Wartortle', 'Blastoise', 'Caterpie', 'Metapod', 'Butterfree', 'Weedle', 'Kakuna', 'Beedrill', 'Pidgey', 'Pidgeotto', 'Pidgeot', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Ekans', 'Arbok', 'Pikachu', 'Raichu', 'Sandshrew', 'Sandslash', 'Nidoran-F', 'Nidorina', 'Nidoqueen', 'Nidoran-M', 'Nidorino', 'Nidoking', 'Clefairy', 'Clefable', 'Vulpix', 'Ninetales', 'Jigglypuff', 'Wigglytuff', 'Zubat', 'Golbat', 'Oddish', 'Gloom', 'Vileplume', 'Paras', 'Parasect', 'Venonat', 'Venomoth', 'Diglett', 'Dugtrio', 'Meowth', 'Persian', 'Psyduck', 'Golduck', 'Mankey', 'Primeape', 'Growlithe', 'Arcanine', 'Poliwag', 'Poliwhirl', 'Poliwrath', 'Abra', 'Kadabra', 'Alakazam', 'Machop', 'Machoke', 'Machamp', 'Bellsprout', 'Weepinbell', 'Victreebel', 'Tentacool', 'Tentacruel', 'Geodude', 'Graveler', 'Golem', 'Ponyta', 'Rapidash', 'Slowpoke', 'Slowbro', 'Magnemite', 'Magneton', "Farfetch'd", 'Doduo', 'Dodrio', 'Seel', 'Dewgong', 'Grimer', 'Muk', 'Shellder', 'Cloyster', 'Gastly', 'Haunter', 'Gengar', 'Onix', 'Drowzee', 'Hypno', 'Krabby', 'Kingler', 'Voltorb', 'Electrode', 'Exeggcute', 'Exeggutor', 'Cubone', 'Marowak', 'Hitmonlee', 'Hitmonchan', 'Lickitung', 'Koffing', 'Weezing', 'Rhyhorn', 'Rhydon', 'Chansey', 'Tangela', 'Kangaskhan', 'Horsea', 'Seadra', 'Goldeen', 'Seaking', 'Staryu', 'Starmie', 'Mr. Mime', 'Scyther', 'Jynx', 'Electabuzz', 'Magmar', 'Pinsir', 'Tauros', 'Magikarp', 'Gyarados', 'Lapras', 'Ditto', 'Eevee', 'Vaporeon', 'Jolteon', 'Flareon', 'Porygon', 'Omanyte', 'Omastar', 'Kabuto', 'Kabutops', 'Aerodactyl', 'Snorlax', 'Articuno', 'Zapdos', 'Moltres', 'Dratini', 'Dragonair', 'Dragonite', 'Mewtwo', 'Mew', 'Chikorita', 'Bayleef', 'Meganium', 'Cyndaquil', 'Quilava', 'Typhlosion', 'Totodile', 'Croconaw', 'Feraligatr', 'Sentret', 'Furret', 'Hoothoot', 'Noctowl', 'Ledyba', 'Ledian', 'Spinarak', 'Ariados', 'Crobat', 'Chinchou', 'Lanturn', 'Pichu', 'Cleffa', 'Igglybuff', 'Togepi', 'Togetic', 'Natu', 'Xatu', 'Mareep', 'Flaaffy', 'Ampharos', 'Bellossom', 'Marill', 'Azumarill', 'Sudowoodo', 'Politoed', 'Hoppip', 'Skiploom', 'Jumpluff', 'Aipom', 'Sunkern', 'Sunflora', 'Yanma', 'Wooper', 'Quagsire', 'Espeon', 'Umbreon', 'Murkrow', 'Slowking', 'Misdreavus', 'Unown', 'Wobbuffet', 'Girafarig', 'Pineco', 'Forretress', 'Dunsparce', 'Gligar', 'Steelix', 'Snubbull', 'Granbull', 'Qwilfish', 'Scizor', 'Shuckle', 'Heracross', 'Sneasel', 'Teddiursa', 'Ursaring', 'Slugma', 'Magcargo', 'Swinub', 'Piloswine', 'Corsola', 'Remoraid', 'Octillery', 'Delibird', 'Mantine', 'Skarmory', 'Houndour', 'Houndoom', 'Kingdra', 'Phanpy', 'Donphan', 'Porygon2', 'Stantler', 'Smeargle', 'Tyrogue', 'Hitmontop', 'Smoochum', 'Elekid', 'Magby', 'Miltank', 'Blissey', 'Raikou', 'Entei', 'Suicune', 'Larvitar', 'Pupitar', 'Tyranitar', 'Lugia', 'Ho-Oh', 'Celebi', 'Treecko', 'Grovyle', 'Sceptile', 'Torchic', 'Combusken', 'Blaziken', 'Mudkip', 'Marshtomp', 'Swampert', 'Poochyena', 'Mightyena', 'Zigzagoon', 'Linoone', 'Wurmple', 'Silcoon', 'Beautifly', 'Cascoon', 'Dustox', 'Lotad', 'Lombre', 'Ludicolo', 'Seedot', 'Nuzleaf', 'Shiftry', 'Taillow', 'Swellow', 'Wingull', 'Pelipper', 'Ralts', 'Kirlia', 'Gardevoir', 'Surskit', 'Masquerain', 'Shroomish', 'Breloom', 'Slakoth', 'Vigoroth', 'Slaking', 'Nincada', 'Ninjask', 'Shedinja', 'Whismur', 'Loudred', 'Exploud', 'Makuhita', 'Hariyama', 'Azurill', 'Nosepass', 'Skitty', 'Delcatty', 'Sableye', 'Mawile', 'Aron', 'Lairon', 'Aggron', 'Meditite', 'Medicham', 'Electrike', 'Manectric', 'Plusle', 'Minun', 'Volbeat', 'Illumise', 'Roselia', 'Gulpin', 'Swalot', 'Carvanha', 'Sharpedo', 'Wailmer', 'Wailord', 'Numel', 'Camerupt', 'Torkoal', 'Spoink', 'Grumpig', 'Spinda', 'Trapinch', 'Vibrava', 'Flygon', 'Cacnea', 'Cacturne', 'Swablu', 'Altaria', 'Zangoose', 'Seviper', 'Lunatone', 'Solrock', 'Barboach', 'Whiscash', 'Corphish', 'Crawdaunt', 'Baltoy', 'Claydol', 'Lileep', 'Cradily', 'Anorith', 'Armaldo', 'Feebas', 'Milotic', 'Kecleon', 'Shuppet', 'Banette', 'Duskull', 'Dusclops', 'Tropius', 'Chimecho', 'Absol', 'Wynaut', 'Snorunt', 'Glalie', 'Spheal', 'Sealeo', 'Walrein', 'Clamperl', 'Huntail', 'Gorebyss', 'Relicanth', 'Luvdisc', 'Bagon', 'Shelgon', 'Salamence', 'Beldum', 'Metang', 'Metagross', 'Regirock', 'Regice', 'Registeel', 'Latias', 'Latios', 'Kyogre', 'Groudon', 'Rayquaza', 'Jirachi', 'Deoxys', 'Turtwig', 'Grotle', 'Torterra', 'Chimchar', 'Monferno', 'Infernape', 'Piplup', 'Prinplup', 'Empoleon', 'Starly', 'Staravia', 'Staraptor', 'Bidoof', 'Bibarel', 'Kricketot', 'Kricketune', 'Shinx', 'Luxio', 'Luxray', 'Budew', 'Roserade', 'Cranidos', 'Rampardos', 'Shieldon', 'Bastiodon', 'Burmy', 'Wormadam', 'Mothim', 'Combee', 'Vespiquen', 'Pachirisu', 'Buizel', 'Floatzel', 'Cherubi', 'Cherrim', 'Shellos', 'Gastrodon', 'Ambipom', 'Drifloon', 'Drifblim', 'Buneary', 'Lopunny', 'Mismagius', 'Honchkrow', 'Glameow', 'Purugly', 'Chingling', 'Stunky', 'Skuntank', 'Bronzor', 'Bronzong', 'Bonsly', 'Mime Jr.', 'Happiny', 'Chatot', 'Spiritomb', 'Gible', 'Gabite', 'Garchomp', 'Munchlax', 'Riolu', 'Lucario', 'Hippopotas', 'Hippowdon', 'Skorupi', 'Drapion', 'Croagunk', 'Toxicroak', 'Carnivine', 'Finneon', 'Lumineon', 'Mantyke', 'Snover', 'Abomasnow', 'Weavile', 'Magnezone', 'Lickilicky', 'Rhyperior', 'Tangrowth', 'Electivire', 'Magmortar', 'Togekiss', 'Yanmega', 'Leafeon', 'Glaceon', 'Gliscor', 'Mamoswine', 'Porygon-Z', 'Gallade', 'Probopass', 'Dusknoir', 'Froslass', 'Rotom', 'Uxie', 'Mesprit', 'Azelf', 'Dialga', 'Palkia', 'Heatran', 'Regigigas', 'Giratina', 'Cresselia', 'Phione', 'Manaphy', 'Darkrai', 'Shaymin', 'Arceus', 'Rattata-A', 'Exegutor-A', 'Grimer-A', 'Muk-A', 'Meowth-A', 'Persian-A', 'Vulpix-A', 'Ninetails-A', 'Sandshrew-A', 'Sandslash-A', 'Raticate-A', 'Diglett-A', 'Dugtrio-A', 'Geodude-A', 'Graveler-A', 'Golem-A', 'Raichu-A', 'Marowak-A', 'Castform-Normal', 'Castform-Sunny', 'Castform-Rainy', 'Castform-Snowy']

    while sp not in pkmon:
        print("This is not a valid species.")
        sp = input("What is the species? ")
        if "-" in sp:
            spe, cies = sp.split("-")
            sp = spe.capitalize() + "-" + cies.capitalize()
        elif sp == "farfetch'd":
            sp = sp.capitalize()
        else:
            sp = sp.title()
    

    pklvl = eval(input("What level is the {0}? ".format(sp)))

    if is_caught == 1:
        while pklvl > 35:
            print("Not a valid wild Pokemon level.")
            pklvl = eval(input("What is the level of the Pokemon? "))
        
        wb, iv_fill, iv = catch(pklvl)
        
        from selenium import webdriver
        driver = webdriver.Chrome()
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSep-N8YTfRAxbcoeSkYIkz9fqbWPbCdNv83ca8J_eEaz_36WA/viewform")
        name_link = driver.find_elements_by_xpath("//input[@name='entry.690209572']")[0]
        name_link.send_keys(name)
        month_link = driver.find_elements_by_xpath("//input[@type='text']")[1]
        month_link.send_keys(month)
        day_link = driver.find_elements_by_xpath("//input[@type='text']")[2]
        day_link.send_keys(day)
        level = driver.find_elements_by_xpath("//input[@type='text']")[3]
        level.send_keys(lvl)

        if wb == 1:
            boost = driver.find_elements_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[4]/div/div[2]/div/content/div/div/label/div/div/div[3]/div")[1]
            boost.click()

        else:
            boost = driver.find_elements_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[2]/div[4]/div/div[2]/div/content/div/div[2]/label/div/div/div[3]/div")[0]
            boost.click()

        species = driver.find_elements_by_xpath("//input[@type='text']")[4]
        species.send_keys(sp)
        monlvl = driver.find_elements_by_xpath("//input[@type='text']")[5]
        monlvl.send_keys(pklvl)
        ivfill = driver.find_elements_by_xpath("//label/div/div/div[3]/div")[iv_fill+1]
        ivfill.click()
        _next = driver.find_elements_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[3]/div/div/div/content")[0]
        _next.click()

        if iv_fill == 1:
            a = iv[0]
            d = iv[1]
            h = iv[2]
            atk = driver.find_elements_by_xpath("//input[@type='text']")[0]
            atk.click()
            atk.send_keys(a)
            defs = driver.find_elements_by_xpath("//input[@type='text']")[1]
            defs.click()
            defs.send_keys(d)
            hp = driver.find_elements_by_xpath("//input[@type='text']")[2]
            hp.click()
            hp.send_keys(h)
            submit = driver.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[3]/div/div/div[2]/content/span")
            submit.click()

        elif iv_fill == 2:
            per = driver.find_elements_by_xpath("//input[@type='text']")[0]
            per.send_keys(iv)
            submit = driver.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[3]/div/div/div[2]/content/span")
            submit.click()

        elif iv_fill == 3:
            per = driver.find_elements_by_xpath("//input[@type='text']")[0]
            per.send_keys(iv)
            submit = driver.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[3]/div/div/div[2]/content/span")
            submit.click()

        driver.quit()
                

        
    else:

        while pklvl > 40:
            print("Not a valid Pokemon level.")
            pklvl = eval(input("What is the level of the Pokemon? "))
        
        st = eval(input("This was a special trade. (0=No, 1=Yes) "))
        luck = eval(input("Were the Pokemon lucky? (0=No, 1=Yes) "))

        friend, iv_fill, iv = trade()
        
        from selenium import webdriver
        driver = webdriver.Chrome()
        driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdXO02LlOd-ipjvVAxDK8F-0pWmrYxeCy8Z98EyEcbjUuanhQ/viewform")
        name_link = driver.find_elements_by_xpath("//input[@name='entry.690209572']")[0]
        name_link.send_keys(name)
        date = driver.find_elements_by_xpath("//div[2]/div/div/div/input")[0]
        date.send_keys(month, day, 2019)

        fr = driver.find_elements_by_xpath("//label/div/div/div[3]/div")[friend-1]
        fr.click()
        if st == 1:
            special = driver.find_elements_by_xpath("//div[4]/div/div[2]/div/content/div/div/label/div/div/div[3]/div")[0]
            special.click()
        else:
            special = driver.find_elements_by_xpath("//div[4]/div/div[2]/div/content/div/div/label/div/div/div[3]/div")[1]
            special.click()

        
        species = driver.find_elements_by_xpath("//input[@type='text']")[1]
        species.send_keys(sp)

        if luck == 1:
            lucky = driver.find_elements_by_xpath("//div[6]/div/div[2]/div/content/div/div/label/div/div/div[3]/div")[0]
            lucky.click()
        else:
            lucky = driver.find_elements_by_xpath("//div[6]/div/div[2]/div/content/div/div/label/div/div/div[3]/div")[1]
            lucky.click()

        lv = driver.find_elements_by_xpath("//input[@type='text']")[2]
        lv.send_keys(pklvl)
        ivfill = driver.find_elements_by_xpath("//div[8]/div/div[2]/div/content/div/div/label/div/div/div[3]/div")[iv_fill-1]
        ivfill.click()
        _next = driver.find_elements_by_xpath("//content/span")[0]
        _next.click()



        if iv_fill == 1:
            a = iv[0]
            d = iv[1]
            h = iv[2]
            atk = driver.find_elements_by_xpath("//input[@type='text']")[0]
            atk.click()
            atk.send_keys(a)
            defs = driver.find_elements_by_xpath("//input[@type='text']")[1]
            defs.click()
            defs.send_keys(d)
            hp = driver.find_elements_by_xpath("//input[@type='text']")[2]
            hp.click()
            hp.send_keys(h)
            submit = driver.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[3]/div/div/div[2]/content/span")
            submit.click()

        elif iv_fill == 2:
            per = driver.find_elements_by_xpath("//input[@type='text']")[0]
            per.send_keys(iv)
            submit = driver.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[3]/div/div/div[2]/content/span")
            submit.click()

        elif iv_fill == 3:
            per = driver.find_elements_by_xpath("//input[@type='text']")[0]
            per.send_keys(iv)
            submit = driver.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[3]/div/div/div[2]/content/span")
            submit.click()

        driver.quit()


def catch(pklvl):
    if pklvl > 30:
        wb = 1
    elif pklvl < 6:
        wb = 0
    else:
        wb = eval(input("This Pokemon was weatherboosted. (0=No, 1=Yes) "))
    
    iv = eval(input("I know 1=exact IVs, 2=exact percentage, 3=range only. "))

    if iv is 1:
        iv_fill = 1
        a = eval(input("Attack "))
        d = eval(input("Defense "))
        h = eval(input("HP "))

        while a > 15 or a < 0:
            print("Not a valid attack IV.")
            a = eval(input("Attack IV: "))

        while d > 15 or d < 0:
            print("Not a valid defense IV.")
            d = eval(input("Defense IV: "))

        while h > 15 or h < 0:
            print("Not a valid stamina IV.")
            h = eval(input("HP/Stamina IV: "))

        iv = [a, d, h]

        return wb, iv_fill, iv

    elif iv is 2:
        iv_fill = 2
        p = input("What is the percentage? ")

        return wb, iv_fill, p
    
    elif iv is 3:
        iv_fill = 3
        avg = input("What is the average percentage? ")

        return wb, iv_fill, avg


def trade():
    friend = eval(input("Friendship level with trading partner: (1=Friend, 2=Good, 3=Great, 4=Ultra, 5=Best) "))
    iv = eval(input("I know 1=exact IVs, 2=exact percentage, 3=range only. "))

    if iv is 1:
        iv_fill = 1
        a = eval(input("Attack "))
        d = eval(input("Defense "))
        h = eval(input("HP "))

        while a > 15 or a < 0:
            print("Not a valid attack IV.")
            a = eval(input("Attack IV: "))

        while d > 15 or d < 0:
            print("Not a valid defense IV.")
            d = eval(input("Defense IV: "))

        while h > 15 or h < 0:
            print("Not a valid stamina IV.")
            h = eval(input("HP/Stamina IV: "))

        iv = [a, d, h]

        return friend, iv_fill, iv

    elif iv is 2:
        iv_fill = 2
        p = input("What is the percentage? ")

        return friend, iv_fill, p
    
    elif iv is 3:
        iv_fill = 3
        avg = input("What is the average percentage? ")

        return friend, iv_fill, avg


if __name__ == "__main__":
    main()

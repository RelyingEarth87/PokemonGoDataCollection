def main():
    name = "RelyingEarth87"
    lvl = 40
    import datetime
    d = datetime.datetime.today()
    month = d.month
    day = d.day
    is_caught = eval(input("This Pokemon was 1=Wild Caught 2=Traded "))

    from text_rip import text_rip

    file = # fill in file name here

    sp, pklvl, iv_fill, iv, a, d, h = text_rip(file)

    if is_caught == 1:
        while pklvl > 35:
            print("Not a valid wild Pokemon level.")
            pklvl = eval(input("What is the level of the Pokemon? "))
        
        wb = catch(pklvl)
        
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

        friend = trade()
        
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
            

        elif iv_fill == 2:
            per = driver.find_elements_by_xpath("//input[@type='text']")[0]
            per.send_keys(iv)
            submit = driver.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[3]/div/div/div[2]/content/span")
            

        elif iv_fill == 3:
            per = driver.find_elements_by_xpath("//input[@type='text']")[0]
            per.send_keys(iv)
            submit = driver.find_element_by_xpath("//form[@id='mG61Hd']/div/div[2]/div[3]/div/div/div[2]/content/span")
            

        


def catch(pklvl):
    if pklvl > 30:
        wb = 1
    elif pklvl < 6:
        wb = 0
    else:
        wb = eval(input("This Pokemon was weatherboosted. (0=No, 1=Yes) "))

        return wb


def trade():
    friend = eval(input("Friendship level with trading partner: (1=Friend, 2=Good, 3=Great, 4=Ultra, 5=Best) "))

    return friend


if __name__ == "__main__":
    main()

# PokemonGoDataCollection
A friend and I are creating a data submission project for Pokemon Go and I decided to write a program in Python using Selenium to help me submit the data. If you would like to submit, read on.

It stores my Trainer Name and Level, and asks only a few questions about the Pokemon to then submit IV data to either a Trade IV distribution Google Form or a Wild Catch IV Data ditribution Google Form. Selenium then fills in the data to the form and submits it online.


<h1>To Submit Data for this Project:</h1>

If you would like to submit data, you will need to install Python and Selenium. Both are free. Once you install <a href="https://www.python.org/downloads/">Python</a>, you can just go to your command line and type in "pip install selenium". For me, for some reason, that didn't work. I had to type in "python -m pip -U selenium" you can try any combination with the python, pip, install, selenium and -m or -U until it actually installs. The -m and -U are in the order they need to be, but for some reason my command line did not recognize the command "install". I don't know why I had to try different things to get it to work. 

After, you should be able to download and use the IV dist.py file. For easiest use, right click on the file and click "Edit with IDLE" or whatever other IDE you use, and you can mass enter data by calling the "main()" function after each submission.

<strong>Before you begin entering data</strong>, you'll need to change the name variable to your trainer name and adjust your level. Then you will need to either download <a href="http://chromedriver.chromium.org/">Chromedriver</a>  or look up the proper web driver for whatever browser you would like to use <a href="https://www.seleniumhq.org/about/platforms.jsp#browsers">here</a>.

After you've done all this, you should be good to go! Submit anything and everything you possibly can so as to not skew data. You can even bank data in your preferred IV checker app and submit later, but try not to submit any later than the same day caught if possible. We accept all data on trades and Wild Catch IVs, just make sure you know if the Pokemon were weatherboosted if it's wild or what friend you traded with to get the Pokemon and how good of friends you are with that person.

<h1>Important Info When Submitting:</h1>

<ol>
  <li>If the Pokemon is an Alolan form, submit the Species name as "[species]-A", such as "Vulpix-A".</li>
  <li>Submit the most accurate info you can get on IVs. If you know exact IVs, submit them and strive for exact IVs, enter the appraisals and the CP at next powerup into the IV checker if it will give you more precise data. <strong>The order for precise data goes Exact IVs > Exact IV Percentage > Average Range of IV Percentages.</strong></li>
  <li>You do not need to capitalize the first letter in the species name, since I have that corrected for in the code. Same thing for Alolan forms, the A will be capitalized as well to make submission easier.</li>
  <li>Sometimes, if your internet is slow or something, the program might miss clicking one of the multiple choice responses, which will make the web page not advance to the second page of questions. If this happens, quit the running program, do not try to fix it or else you might accidentally send bad data because the IV numbers and percentages are set to relative paths, and they might get entered on the first page of data next to your name or the date if the program doesn't work right. Quit out and restart that submission and it should work.</li>
</ol>

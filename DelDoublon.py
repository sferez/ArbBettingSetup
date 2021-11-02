#DelDoublon.py

files=[
    r"C:\Users\simeo\Desktop\Bet\french-betting-arbitrage-master\src\Team\Bet22.txt",
    r"C:\Users\simeo\Desktop\Bet\french-betting-arbitrage-master\src\Team\Betclic.txt",
    r"C:\Users\simeo\Desktop\Bet\french-betting-arbitrage-master\src\Team\Netbet.txt",
    r"C:\Users\simeo\Desktop\Bet\french-betting-arbitrage-master\src\Team\Pmu.txt",
    r"C:\Users\simeo\Desktop\Bet\french-betting-arbitrage-master\src\Team\Winamax.txt",
    r"C:\Users\simeo\Desktop\Bet\french-betting-arbitrage-master\src\Team\Xbet.txt",
    r"C:\Users\simeo\Desktop\Bet\french-betting-arbitrage-master\src\Team\Zebet.txt",
    r"C:\Users\simeo\Desktop\Bet\french-betting-arbitrage-master\src\Team\Parionssport.txt",
    r"C:\Users\simeo\Desktop\Bet\french-betting-arbitrage-master\src\Team\Pinnacle.txt",
    r"C:\Users\simeo\Desktop\Bet\french-betting-arbitrage-master\src\Team\Marathon.txt",
    r"C:\Users\simeo\Desktop\Bet\french-betting-arbitrage-master\src\Team\Unibet.txt",
]

for filename in files :
    seen= []
    with open(filename ,"r", encoding="utf8") as file:
        list=file.read()
    list=list.split("\n")
    file.close()
    print(filename)

    for el in list:
        if el not in seen:
            seen.append(el)


    with open(filename ,"w", encoding="utf8") as file:
        file.truncate()
        for el in seen:
            file.write(el+"\n")
    file.close()
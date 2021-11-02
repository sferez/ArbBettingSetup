#TeamSetup.py
from difflib import SequenceMatcher
def str_similarity(a, b):
	return SequenceMatcher(None, a, b).ratio()

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

list2=[
    "ParisSG","Lens","Nice","Angers","Marseille","Monaco","Lorient","Lille","Nantes","Lyon","Rennes","Strasbourg","Montpellier","Reims","Clermont","Bordeaux","Troyes","Metz","Brest","Saint-Etienne",
    "BayernMunich","BayerLeverkusen","Dortmund","Fribourg","Wolfsburg","FCCologne","UnionBerlin","RBLeipzig","Mayence","BMonchengladbach","Hoffenheim","Stuttgart","Francfort","HerthaBerlin","Augsburg","Bielefeld","Bochum","GreutherFurth",
    "Chelsea","Liverpool","ManchesterCity","ManchesterUnited","Everton","Brighton","Brentford","Tottenham","WestHam","AstonVilla","Arsenal","Wolverhampton","Leicester","CrystalPalace","Watford","Leeds","Southampton","Burnley","Newcastle","Norwich",
    "RealMadrid","AtleticoMadrid","RealSociedad","FCSeville","Osasuna","Vallecano","AthleticBilbao","Valence","FCBarcelone","Betis","Villareal","Majorque","Espanyol","Elche","CeltaVigo","Cadix","Grenade","Levante","Alaves","Getafe",
    "Naples","ACMilan","Inter","ASRome","Fiorentina","Lazio","Juventus","Atalanta","Bologne","Empoli","Torino","HellaVerone","Udinese","Sassuolo","Sampdoria","Genoa","Venise","Salernitana","Spezia","Cagliari",

]

for filename in files :
    print(filename)
    with open(filename ,"r", encoding="utf8") as file:
        list1=file.read()
    file.close()

    list=list1.split("\n")
    final=[]
    for team2 in list2:
        S=0
        i=0
        I=0
        for team1 in list:
            s=str_similarity(team2,team1)
            if s>S:
                S=s
                I=i
            i=i+1
        final.append(list[I]+","+team2+";\n")

    with open(filename ,"w", encoding="utf8") as file:
        file.truncate()
        for double in final:
            file.write(double)
    file.close()



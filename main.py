
def prompt(demand: str, choices: list[str], funcs: list[callable], returns = False):
    print(demand)
    for i in range(len(choices)):
        print(f"[{i+1}] : {choices[i]}")

    choice = input("What would you like to do? : ")
    if choice.isdigit():
        if int(choice) in range(1,len(choices)+1):
            if returns == False:
                funcs[int(choice) - 1]()
            else:
                pass
        else:
            print("Please enter an accepted value.")
            prompt(demand, choices, funcs)
    else:
        print("Please enter an accepted value.")
        prompt(demand,choices,funcs)

def promptint(demand: str, range : list[int]):
    chosenint = input(f"{demand} : ")
    if chosenint.isdigit() and int(chosenint) >= range[0] and int(chosenint) <= range[1]:
        return int(chosenint)
    else:
        print("Please choose and accepted value.")
        return promptint(demand,range)

anime = {
    "RE:Zero": {
        "Episodes":66,
        "Year":2016,
        "Genre":{"Adventure","Dark Fantasy","Isekai","Fantasy"},
        "Rank":3,
    },
    "Attack on Titan": {
        "Episodes": 94,
        "Year": 2013,
        "Genre": {"Shonen","Dark Fantasy","Fantasy"},
        "Rank": 1,
    },
    "Bleach": {
        "Episodes": 366,
        "Year": 2004,
        "Genre": {"Shonen","Action","Fantasy"},
        "Rank": 4,
    },
    "Naruto": {
        "Episodes": 220,
        "Year": 2002,
        "Genre": {"Shonen", "Action","Fantasy"},
        "Rank": 8,
    },
    "Jobless Reincarnation": {
        "Episodes": 48,
        "Year": 2022,
        "Genre": {"Fantasy","Isekai"},
        "Rank": 5,
    },
    "Fullmetal Alchemist": {
        "Episodes": 51,
        "Year": 2003,
        "Genre": {"Action","Fantasy","Steampunk"},
        "Rank": 6,
    },
    "Vinland Saga": {
        "Episodes": 48,
        "Year": 2019,
        "Genre": {"Action","Historical","Seinen"},
        "Rank": 2,
    },
    "Hunter x Hunter": {
        "Episodes": 148,
        "Year": 2011,
        "Genre": {"Action","Fantasy","Martial Arts"},
        "Rank": 9,
    },
    "Demon Slayer": {
        "Episodes": 63,
        "Year": 1019,
        "Genre": {"Action","Dark Fantasy"},
        "Rank": 7,
    },
    "Jojo's Bizarre Adventure": {
        "Episodes": 194,
        "Year": 2012,
        "Genre": {"Action","Supernatural"},
        "Rank": 10,
    },
}

def sortGenre():
    animeList = list[anime.keys()]
    prompt("Which genre would you like to search?",["Shonen","Action","Seinen","Fantasy","Dark Fantasy","Historic","Steampunk","Supernatural","Isekai"], returns=True)
    pass

def sortRanking():
    pass

def top10List():
    pass

def leave():
    print("Exited Program")
    quit()

def start():
    print("Daniel's Top 10 Anime List")
    prompt("What would you like to do?",["Sort by Genre","Sort by Ranking","My top 10","Exit program"],[sortGenre,sortRanking,top10List,leave])

start()
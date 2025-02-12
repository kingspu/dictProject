
def prompt(demand: str, choices: list[str], funcs = None, returns = False):
    print(demand)
    for i in range(len(choices)):
        print(f"[{i+1}] : {choices[i]}")

    choice = input("What would you like to do? : ")
    if choice.isdigit():
        if int(choice) in range(1,len(choices)+1):
            if returns == False:
                funcs[int(choice) - 1]()
            else:
                return choices[int(choice)-1]
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
        "Year": 2019,
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

def sortgenre():
    animeList = list(anime.keys())
    genre = prompt("Which genre would you like to search?",["Shonen","Action","Seinen","Fantasy","Dark Fantasy","Historic","Steampunk","Supernatural","Isekai","Martial Arts"], returns=True)
    print(f"Searching {genre}...")
    for i in animeList:
        if genre in anime[i]["Genre"]:
            print(f"{i}:\n     Number of Episodes: {anime[i]["Episodes"]}\n     Air Date: {anime[i]["Year"]}\n     Genres: {anime[i]["Genre"]}")
    prompt("What would you like to do?",["Search another genre","Back to main menu"],[sortgenre,start])


def sortranking():
    rank = int(promptint("What rank would you like to search?",[1,10]))
    for i in list(anime.keys()):
        if rank is anime[i]["Rank"]:
            print(f"{i}:\n     Number of Episodes: {anime[i]["Episodes"]}\n     Air Date: {anime[i]["Year"]}\n     Genres: {anime[i]["Genre"]}")
    prompt("What would you like to do?",["Search another genre","Back to main menu"],[sortranking,start])

def top10list():
    rankPair = dict()
    for i in anime.keys():
        rankPair.update({anime[i]["Rank"]:i})
    for i in range(1,len(rankPair.keys())+1):
        print(f"{f"{i}.":<3} {rankPair.get(i)}")
    prompt("What would you like to do?", ["Pick a rank for more info", "Back to main menu"], [sortranking,start])

def leave():
    print("Exited Program")
    quit()

def start():
    print("Daniel's Top 10 Anime List\n--------------------------")
    prompt("What would you like to do?",["Sort by Genre","Search by Ranking","My top 10","Exit program"],[sortgenre,sortranking,top10list,leave])

start()
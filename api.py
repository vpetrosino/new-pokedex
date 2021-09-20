# import the requests library for handling api calls, then the json library to make the json files readable
import pip._vendor.requests as requests
import json

class pokemon:
    # define the init method to create the initial global variables
    def __init__(self, name):
        self.name = name
        self.data = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(self.name)).json()


# def method to return the pokemon's abilities as a list 
    def getAbilities(self):
        abilites = []
        data = self.data['abilities'] # sets data to the list of abilities

    # loops through the abilities of the pokemon
        for ability in data:
            # add the abilities by accessing the ability dictionary then the name key:value pair
            abilites.append(ability['ability']['name'])
        
        return abilites


# def method to return the required info from the api as a dict
    def getInfo(self):
        info = {}
# used update method to add multiple items to a dictionary
        info.update(
            name = self.name,
            height = self.data['height'], 
            weight = self.data['weight']
            )


        return info


# create pokedex
pokedex = {
    "Electric" : {
        "pokemon" : [

        ]
    },
    "Fire" : {
        "pokemon" : [

        ]
    },
    "Water" : {
        "pokemon" : [

        ]
    },
    "Rock" : {
        "pokemon" : [

        ]
    }
}

# create pokemon objects
pikachu = pokemon('pikachu')

vulpix = pokemon('vulpix')
# first pokemon  with more than 2 abilities
tentacruel = pokemon('tentacruel')

Squirtle = pokemon('Squirtle')

Blastoise = pokemon('Blastoise')

Geodude = pokemon('Geodude')

Golem = pokemon('Golem')

onix = pokemon('onix')

kabuto = pokemon('kabuto')

aron = pokemon('aron')

Rapidash = pokemon('Rapidash')

moltres = pokemon('moltres')

slugma = pokemon('slugms')

numel = pokemon('numel')

charmeleon = pokemon('charmeleon')

ninetales = pokemon('ninetales')

litten = pokemon('litten')

raboot = pokemon('raboot')

wartortle = pokemon('wartortle')

seel = pokemon('seel')

krabby = pokemon('krabby')

seaking = pokemon('seaking')

feebas = pokemon('feebas')

piplup = pokemon('piplup')

sobble = pokemon('sobble')

phione = pokemon('phione')

finneon = pokemon('finneon')

froakie = pokemon('froakie')

sobble = pokemon('sobble')
# extend allows you to append multiple values to a list
# adding all the pokemon to the pokedex
pokedex['Electric']['pokemon'].extend([pikachu.getInfo(), pikachu.getAbilities()])

pokedex['Fire']['pokemon'].extend([vulpix.getInfo(), vulpix.getAbilities()])

pokedex['Water']['pokemon'].extend([tentacruel.getInfo(), tentacruel.getAbilities()])

pokedex['Water']['pokemon'].extend([Squirtle.getInfo(), Squirtle.getAbilities()])

pokedex['Water']['pokemon'].extend([Blastoise.getInfo(), Blastoise.getAbilities()])

pokedex['Rock']['pokemon'].extend([Geodude.getInfo(), Geodude.getAbilities()])

pokedex['Rock']['pokemon'].extend([Golem.getInfo(), Golem.getAbilities()])

pokedex['Rock']['pokemon'].extend([onix.getInfo(), onix.getAbilities()])

pokedex['Rock']['pokemon'].extend([kabuto.getInfo(), kabuto.getAbilities()])

pokedex['Rock']['pokemon'].extend([aron.getInfo(), aron.getAbilities()])

pokedex['Fire']['pokemon'].extend([Rapidash.getInfo(),Rapidash.getAbilities()])

pokedex['Fire']['pokemon'].extend([moltres.getInfo(), moltres.getAbilities()])

pokedex['Fire']['pokemon'].extend([slugma.getInfo(), slugma.getAbilities()])

pokedex['Fire']['pokemon'].extend([numel.getInfo(), numel.getAbilities()])

pokedex['Fire']['pokemon'].extend([charmeleon.getInfo(), charmeleon.getAbilities()])

pokedex['Fire']['pokemon'].extend([ninetales.getInfo(), ninetales.getAbilities()])

pokedex['Fire']['pokemon'].extend([litten.getInfo(), litten.getAbilities()])

pokedex['Fire']['pokemon'].extend([raboot.getInfo(), raboot.getAbilities()])

pokedex['Water']['pokemon'].extend([wartortle.getInfo(), wartortle.getAbilities()])

pokedex['Water']['pokemon'].extend([seel.getInfo(), seel.getAbilities()])

pokedex['Water']['pokemon'].extend([krabby.getInfo(), krabby.getAbilities()])

pokedex['Water']['pokemon'].extend([seaking.getInfo(), seaking.getAbilities()])

pokedex['Water']['pokemon'].extend([feebas.getInfo(), feebas.getAbilities()])

pokedex['Water']['pokemon'].extend([piplup.getInfo(), piplup.getAbilities()])

pokedex['Water']['pokemon'].extend([sobble.getInfo(), sobble.getAbilities()])

pokedex['Water']['pokemon'].extend([phione.getInfo(), phione.getAbilities()])

pokedex['Water']['pokemon'].extend([finneon.getInfo(), finneon.getAbilities()])

pokedex['Water']['pokemon'].extend([froakie.getInfo(), froakie.getAbilities()])

pokedex['Water']['pokemon'].extend([sobble.getInfo(), sobble.getAbilities()])

print(pokedex)

# ditto = pokemon('ditto')

# pokedex["Electric"]["pokemon"].append(pikachu.returnData()['abilities'][1]['ability']['name'])

# print(pokedex['Electric']['pokemon'][0])


# print(ditto.returnData()['abilities'][1]['ability']['name'])

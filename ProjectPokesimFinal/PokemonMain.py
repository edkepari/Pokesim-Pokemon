import PokemonObjectsAndFunctions
from ClassesPokemon import Trainer

Party=[]
Party.append(PokemonObjectsAndFunctions.getPokemon("Infernape"))
#Party.append(PokemonObjectsAndFunctions.getPokemon("Garchomp"))
#Party.append(PokemonObjectsAndFunctions.getPokemon("Rhyperior"))
#Party.append(PokemonObjectsAndFunctions.getPokemon("Gyarados"))
#Party.append(PokemonObjectsAndFunctions.getPokemon("Magnezone"))
#Party.append(PokemonObjectsAndFunctions.getPokemon("Sceptile"))

Parimal = Trainer("Parimal", Party)
Party[0]=PokemonObjectsAndFunctions.getPokemon("Sceptile")
Parinita = Trainer("Parinita", Party)
for i in range(0,len(Parinita.Party)):
    print(Parinita.Party[i].Name)
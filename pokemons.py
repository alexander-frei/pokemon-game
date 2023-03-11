class Pokemon:
    def __init__(self,name="nameless",type="typeless",full_health=100):
        self.name = name
        self.type = type
        self.full_health = full_health
        self.health = self.full_health
    def __str__(self):
        return f"{self.name}: {self.type}, {self.health}"

    def feed(self):
        if self.health < self.full_health:
            self.health += 1
            print( self.health )
        else:
            print( "health = full:", self.health )

    def battle(self,other):
        print("Battle:",self.name,other.name)
        result = Pokemon.typewheel(self.type,other.type)
        print("Result:",result)

    @staticmethod
    def typewheel(type1,type2):
        type_conversion = {"water":0,"fire":1,"grass":2}
        player1 = type_conversion[type1]
        player2 = type_conversion[type2]
        relative = ( player1 - player2 )%3
        result_conversion = {1:"lost",0:"tie",2:"won"}
        return result_conversion[relative]

########################
##  Example pokemons  ##
########################
# original = Pokemon("Pikachu","electricity")
# first = Pokemon("Schiggy","water")
# second = Pokemon("Glumanda","fire")
# third = Pokemon("Bisasam","grass")
# Pokemon.battle(second,third)
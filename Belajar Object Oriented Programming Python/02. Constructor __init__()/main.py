class Hero: #template
    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

hero1 = Hero("sniper",1000,10,4)
hero2 = Hero("mirana",1500,15,1)
hero3 = Hero("ucup",10000,100,0)

print(hero1.name)
print(hero2.name)
print(hero3.name)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
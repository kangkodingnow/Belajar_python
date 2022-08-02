from unicodedata import name


class Hero:
    def __init__(self,name,health,attackPower,armorNumber):
        self.name = name
        self.health = health
        self.attackPower = attackPower
        self.armorNumber = armorNumber

    def serang(self,lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self,self.attackPower)
    
    def diserang(self,lawan,attackPower):
        print(self.name + ' diserang ' + lawan.name)
        attack_diterima = attackPower/self.armorNumber
        print('serangan terasa: ' + str(attack_diterima))
        self.health -= attack_diterima
        print('darah ' + self.name + ' tersisa ' + str(self.health))

sniper = Hero('sniper',100,10,5)
rikimaru = Hero('rikamaru',199,5,10)
  
sniper.serang(rikimaru)
print("\n")
rikimaru.serang(sniper)


"""def fungsi(argument1,argument2):
    print(argument1)
    print(argument2)"""

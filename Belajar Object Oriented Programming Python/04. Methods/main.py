class Hero:
    #class variabel
    jumlah_hero = 0
    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
    #intance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah_hero += 1

    #void function, method tanpa return, tanpa argument
    def siapa(self):
        print("namaku adalah " + self.name)

    #method dengan argumen, tanpa return
    def healthUp(self,up):
        self.health += up
    #method dengan return
    def gethealth(self):
        return self.health

hero1 = Hero("sniper",100,10,5)
hero2 = Hero("marksman",500,20,5)

hero1.siapa()
hero1.healthUp(10)

print(hero1.gethealth())


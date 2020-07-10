
class Pokemon:
    def __init__(self, name, level, type, current_health, KO):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = self.calculate_health(level)
        self.current_health = current_health
        self.KO = KO
        self.exp = 0

    def __repr__(self):
        return "This {} pokemon has {} health remaining.".format(self.name, self.current_health)

    def injury(self, loss):
        self.current_health -= loss
        if self.current_health <= 0:
            self.current_health = 0 
            return self.knock_out()
        else:
            return print('{n} has been injured, their health is now {c}.'.format(n=self.name, c=self.current_health))

    def recover(self, gain):
        if self.KO == True:
            return print("{} is KO'ed and cannot claim this health pack, they need to be revived first".format(self.name))
        else:
            self.current_health += gain
            if self.current_health > self.max_health:
                self.current_health = self.max_health
            return print('{} found a health pack, their health is now {}'.format(self.name, self.current_health))

    def calculate_health(self, level):
        if level > 0 and level <= 3:
            mex_health = 60
        elif level > 3 and level <=7:
            max_health = 80
        else:
            max_health = 100
        return max_health

    def knock_out(self):
        self.current_health = 0
        self.KO = True
        return print("{} has been KO'ed.".format(self.name))

    def revive(self):
        self.KO = False
        self.current_health = (self.max_health)/2
        return print("{} has been revived. Current health is {}.".format(self.name, self.current_health))

    def experience_points(self):
        #this will award experience points to pokemon that attack and inflict damage on others
        self.exp += self.level
        if self.exp >= 100:
            if self.level < 10:
                self.level += 1
                self.exp -= 100
            else:
                self.exp -= 100
                return print("{} cannot level up anymore!".format(self.name))
            return print("{} just leveled up!.".format(self.name))
        

    def attack(self, other):
        attack_advantages = {'Fire':['Grass'], 'Water':['Fire'],'Grass':['Water']}
        attack_disadvantages = {'Fire':['Water'], 'Water':['Grass'], 'Grass':['Fire']}
        if other.KO == True:
            return print("{} is already KO'ed, {} cannot attack.".format(other.name, self.name))
        if self.KO == False:
            if other.type in attack_advantages.get(self.type):
                damage = self.level * 2
                other.current_health -= damage
                self.experience_points()
                if other.current_health <= 0:
                    other.current_health = 0
                    other.KO = True
                    return("{} has been KO'ed by {}.".format(other.name, self.name))
                return print("{w} attacked {l}, inflicting {d} damage. {l}'s now has {c} health.".format(w=self.name, l=other.name, d=damage, c=other.current_health))
            if other.type in attack_disadvantages.get(self.type):
                damage = self.level/2
                other.current_health -= damage
                self.experience_points()
                if other.current_health <= 0:
                    other.current_health = 0
                    other.KO = True
                return print("{w} attacked {l}, inflicting {d} damage. {l}'s now has {c} health.".format(w=self.name, l=other.name, d=damage, c=other.current_health))
            else:
                damage = self.level
                other.current_health -= damage
                self.experience_points()
                if other.current_health <= 0:
                    other.current_health = 0
                    other.KO = True
                return print("{w} attacked {l}, inflicting {d} damage. {l}'s now has {c} health.".format(w=self.name, l=other.name, d=damage, c=other.current_health))
        else:
            return print("{} cannot attack because they are KO'ed.".format(self.name))
        
class Trainer:
    def __init__(self, name, pokemon, potions, currently_active):
        self.name =  name
        self.pokemon = pokemon
        self.potions = potions
        self.current = currently_active

    
        
    def attack_other_trainer(self, potion, other):
        if potion in self.potions:
            damage = self.current.level
            their_pokemon = other.current
            their_pokemon.current_health -= damage
            return print("You attacked {n} with your {p} potion. His {c}'s health is now {h}.".format(n=other.name, p=potion, c=other.current.name, h=their_pokemon.current_health))
        else:
            return print("Sorry, {} doesn't have that potion.".format(self.name))


    def change_current(self, new_poke):
        if new_poke in self.pokemon:
            if new_poke.KO == False:
                self.current = new_poke
                return print("{}'s current pokemon is now {}.".format(self.name, self.current))
            if new_poke.KO == True:
                return print("{} cannot switch to {} because they are KO'ed.".format(self.name, new_poke.name))
        else:
            return print("Sorry, {} does not have a {} pokemon.".format(self.name, new_poke))

    def use_potion(self, potion):
        if potion in self.potions:
            self.current.current_health = self.current.max_health
            return print("{} used a potion to heal his current pokemon. {}'s health is now {}.".format(self.name, self.current.name, self.current.current_health))
        else:
            return print("Sorry {} doesn't seem to have that potion.".format(self.name))
        
        
            
        
                
    


pikachu = Pokemon('Pikachu', 8, 'Fire', 90, False)

bulbasor = Pokemon('Bulbasor', 6, 'Grass', 80, False)

charmander = Pokemon('Charmander', 7, 'Fire', 90, False)

squirtle = Pokemon('Squirtle', 8, 'Water', 70, False)


potions_a = ['mustard gas', 'anthrax', 'bad fart', 'rat poison']
potions_b = ['Tear gas', 'Agent Orange', 'carbon monoxide', 'wild berries']

Ash = Trainer('Ash', [pikachu, bulbasor], potions_a, pikachu)
Bad_guy = Trainer('Bad Guy', [charmander, squirtle], potions_b, charmander)

pikachu.attack(squirtle)
pikachu.attack(squirtle)
pikachu.attack(squirtle)
pikachu.attack(squirtle)
pikachu.attack(squirtle)
pikachu.attack(squirtle)
pikachu.attack(squirtle)
pikachu.attack(squirtle)
bulbasor.attack(squirtle)
bulbasor.attack(squirtle)
bulbasor.attack(squirtle)
bulbasor.attack(squirtle)
bulbasor.attack(squirtle)


squirtle.attack(pikachu)

Bad_guy.change_current(squirtle)

print(pikachu)

pikachu.attack(charmander)
pikachu.attack(charmander)
pikachu.attack(charmander)
pikachu.attack(charmander)
pikachu.attack(charmander)
pikachu.attack(charmander)
pikachu.attack(charmander)
pikachu.attack(charmander)
pikachu.attack(charmander)
pikachu.attack(charmander)
pikachu.attack(charmander)
pikachu.attack(charmander)
pikachu.attack(charmander)
pikachu.attack(charmander)
pikachu.attack(charmander)
pikachu.attack(bulbasor)
pikachu.attack(bulbasor)
pikachu.attack(bulbasor)
pikachu.attack(bulbasor)
pikachu.attack(bulbasor)
pikachu.attack(bulbasor)
pikachu.attack(bulbasor)
pikachu.attack(bulbasor)
pikachu.attack(bulbasor)
pikachu.attack(bulbasor)
pikachu.attack(bulbasor)
pikachu.attack(bulbasor)
pikachu.attack(bulbasor)
pikachu.attack(bulbasor)
pikachu.attack(bulbasor)
pikachu.attack(bulbasor)
pikachu.attack(bulbasor)
pikachu.attack(bulbasor)


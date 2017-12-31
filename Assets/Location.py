



class Location:
        def __init__(self, name, tavern, shop, sub1, sub2, sub3):
                self.name = name
                self.tavern = tavern
                self.shop = shop
                self.sub1 = sub1
                self.sub2 = sub2
                self.sub3 = sub3

class SubLocation:
        def __init__(self, name, resource, monster_rating, monster):
                self.name = name
                self.resource = resource
                self.monster_rating = monster_rating
                self.monster = monster
class Shop:
        def __init__(self, name, items):
                self.name = name
                self.items = items
class Tavern:
        def __init__(self, name, owner, npc):
                self.name = name
                self.owner = owner
                self.npc = npc



		


			

##### FUTURE CHANGES - MAKE ENHANCEMENTS MODIFY THE DAMAGE BUFFER AND THE SWING BUFFER

class NPC:
    def __init__(self, x, y, name):
        self.x, self.y, self.name = x, y, name

npc1 = NPC(100, 200, 'jeni')
print(type(npc1.__dict__))
print(npc1.__dict__)
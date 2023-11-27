import pickle


class NPC:
    def __init__(self, x, y, name):
        self.x, self.y, self.name = x, y, name


npc1 = NPC(100, 200, 'jeni')
npc2 = NPC(500, 200, 'zwi')

# 하나로 묶음
group = [npc1, npc2]
with open('npc.pickle', 'wb') as f:
    pickle.dump(group, f)
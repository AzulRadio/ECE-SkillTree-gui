from enum import Enum

class Skill:
    name = ''
    skillPoints = 0
    locked = True
    visible = False
    friends = dict()
    Mode = Enum('mode', ('lower', 'similar'))
    
    def __init__(self, name, locked = True, visible = False):
        self.name = name
        self.locked = locked
        self.visible = visible
        for m in self.Mode:
            self.friends[m.name] = []

    def __str__(self):
        return self.name

    def relate(self, skill, mode = 'lower'):

        for m in self.Mode:
            if(m.name == mode):
                if (type(skill) == 'list'):
                    for s in skill:
                        if (isinstance(s, Skill)):
                            self.friends[m.name].append(s)
                            return
                elif (isinstance(skill, Skill)):
                    self.friends[m.name].append(skill)
                    return
        print('invalid mode')
            
        
    

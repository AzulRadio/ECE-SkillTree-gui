class SkillNode:
    name = ''
    skillPoints = 0
    locked = True
    visible = False
    __friends = dict()
    relation = ('upper', 'similar')
    
    def __init__(self, name, locked = True, visible = False):
        self.name = name
        self.locked = locked
        self.visible = visible
        for m in self.relation:
            self.__friends[m] = []

    def __str__(self):
        return self.name

    

    def relate(self, skill, relation = 'upper'):
        if(relation not in self.relation):
            print(str(self) + '.relate() error: invalid relation')
            return
        if (type(skill) == 'list'):
            for s in skill:
                if (isinstance(s, SkillNode)):
                    self.__friends[relation].append(s)
                    return
        elif (isinstance(skill, SkillNode)):
            self.__friends[relation].append(skill)
            return
        
    '''
    if show_name = True, return a list of string
    if show_name = False, return a list of SkillNode instances

    friends() DOES NOT need to be updated when new relation is added.
    '''
    def friends(self, relation = 'upper', show_name = True):
        if (relation not in self.relation):
            print(str(self) + '.friend() error: invalid relation')
            return
        friend = []
        if (show_name):
            for e in self.__friends[relation]:
                friend.append(e.name)
        else:
            friend = self.__friends[relation]
        return friend
    

    '''
    learn() needs to be updated when new relation is added
    '''
    def learn(self):
        if (self.locked):
            return

    

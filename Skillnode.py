from random import randint

def standard_learn(skillPoints, defactor, difficultyBonus):
    if randint(1, 100)//defactor > skillPoints:
        skillPoints += randint(1, 10)//defactor
        skillPoints += difficultyBonus
    if (skillPoints > 100):
        skillPoints = 100
    return skillPoints

class SkillNode:
    name = ''
    skillPoints = 0
    passLine = 0
    proficient = False
    locked = True
    visible = False
    timeSpent = 0
    __friends = dict()
    relation = ('lower', 'similar')
    
    def __init__(self, name, locked = True, visible = False, passLine = 25):
        self.name = name
        self.locked = locked
        self.visible = visible
        self.passLine = passLine
        self.__friends = dict()
        for m in self.relation:
            self.__friends[m] = []

    def __str__(self):
        return self.name

    def relate(self, skill, relation = 'lower'):
        if(relation not in self.relation):
            print(str(self) + '.relate() error: invalid relation')
            return
        if (type(skill) == list or type(skill) == tuple):
            self.__friends[relation].extend(skill)
        else:
            self.__friends[relation].append(skill)
        for s in self.__friends[relation][::-1]:
            if (not isinstance(s, SkillNode) or s is self):
                self.__friends[relation].remove(s)

        
        
    '''
    if show_name = True, return a list of string
    if show_name = False, return a list of SkillNode instances

    friends() DOES NOT need to be updated when new relation is added.
    '''
    def friends(self, relation = 'lower', show_name = True):
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
    modify 'value' to change the function if necessary
    '''

    '''
    One prerequisite misses increase your defactor by one
    If one skill is proficient but prerequisites are not met, defactor is default + 1

    defactors affect your learning success rate and skillpoint gain.
    '''
    def get_defactor(self, default = 1):
        value = 'lower'
        
        friend = self.friends(relation = value, show_name = False)
        defactor = default
        for i in friend:
            if not i.proficient:
                defactor += 1
        if (defactor == default):
            self.locked = False
        if self.proficient and self.locked:
            defactor = default + 1
        return defactor

    def check_proficient(self):
        if self.skillPoints >= self.passLine:
            self.proficient = True
            return True
        return False
    
    def learn(self, learning_func = standard_learn, adjustment = (1, 0)):
        adjustment = (self.get_defactor(), 0)
        self.skillPoints = learning_func(self.skillPoints, *adjustment) 
        self.check_proficient()
        SkillNode.timeSpent += 1
        return self.name, self.skillPoints, self.locked, self.proficient, SkillNode.timeSpent

    def use(self, difficultyLevel = 1):
        defactor = self.get_defactor()
        if (randint(1, 100) < self.skillPoints // difficultyLevel):
            self.learn(adjustment = (defactor, difficultyLevel))
            return True
        return False



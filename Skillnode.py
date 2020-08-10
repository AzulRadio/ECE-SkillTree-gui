from random import randint

def standard_learn(skillPoints, factor, difficultyBonus = 0):
    if randint(1, 100) > skillPoints:
        addPoints = randint(1, 10) + factor + difficultyBonus
        if addPoints < 0:
            return skillPoints
        skillPoints += addPoints
    if (skillPoints > 100):
        skillPoints = 100
    return skillPoints

class SkillNode:
    name = ''
    skillPoints = 0
    passLine = 0
    proficient = False
    locked = True
    timeSpent = 0
    __friends = dict()
    relation = ('lower', 'similar')
    
    def __init__(self, name, locked = True, passLine = 25):
        self.name = name
        self.locked = locked
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
    if for_print = True, return a list of string
    if for_print = False, return a list of SkillNode instances

    friends() DOES NOT need to be updated when new relation is added.
    '''
    def friends(self, relation = 'lower', for_print = True):
        if (relation not in self.relation):
            print(str(self) + '.friend() error: invalid relation')
            return
        friend = []
        if (for_print):
            for e in self.__friends[relation]:
                friend.append(e.name)
        else:
            friend = self.__friends[relation]
        return friend

    def try_unlock(self):
        lower = self.friends(relation = 'lower', for_print = False)
        numLower = 0
        for i in lower:
            if not i.proficient:
                numLower -= 1
        self.locked = not (numLower == 0)
        return numLower

    '''
    modify 'value' to change the function if necessary
    '''

    '''
    One prerequisite misses decrease your factor by one
    If one skill is proficient but prerequisites are not met, factor minus one

    One similar skill proficient increase your factor by one
    
    factor affect your learning success rate and skillpoint gain.
    '''
    def get_factor(self):
        
        factor = 0
        factor = self.try_unlock()
        
        if self.proficient and self.locked:
            factor = -1

        factor += len(self.friends(relation = 'similar', for_print = False))
        return factor

    def check_proficient(self):
        if self.skillPoints >= self.passLine:
            self.proficient = True
            return True
        return False
    
    def learn(self, learning_func = standard_learn, adjustment = 0):
        if learning_func == standard_learn:
            adjustment = (self.get_factor(), 0)
        else:
            try_unlock()
        self.skillPoints = learning_func(self.skillPoints, *adjustment) 
        self.check_proficient()
        SkillNode.timeSpent += 1
        return self.name, self.skillPoints, self.locked, self.proficient, SkillNode.timeSpent

    def use(self, difficultyLevel = 1):
        factor = self.get_factor()
        check = randint(1, 100)
        if (check < self.skillPoints // difficultyLevel):
            self.learn(adjustment = (factor, difficultyLevel))
            return True
        return False



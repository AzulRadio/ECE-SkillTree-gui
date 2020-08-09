from Skill import Skill

cpp = Skill('C++')

c = Skill('C')

cpp.relate(c, relation = 'upper')

print(cpp.friends('upper'))

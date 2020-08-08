from Skill import Skill

cpp = Skill('C++')

c = Skill('C')

cpp.relate(c, 'lower')

print(cpp.friends['lower'])

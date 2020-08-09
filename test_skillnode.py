from Skill import SkillNode

cpp = SkillNode('C++')

c = SkillNode('C', locked = False)

oop = SkillNode('Object Oriented Programming', locked = False)

cpp.relate((c,oop), relation = 'lower')

print(c.friends(), oop.friends(), cpp.friends())


a = int(input('0 = quit, 1 = c, 2 = oop, 3 = c++\n'))

a_last = a

while (not a == 0):
    if (a == ''):
        a = a_last
    else:
        a_last = int(a)
    if (a == 1):
        print(c.learn())
    if (a == 2):
        print(oop.learn())
    if (a == 3):
        print(cpp.learn())
    a = input("next move?\n")


from SkillNode import SkillNode


c = SkillNode('C', locked = False)
stc51 = SkillNode('51')
cpp = SkillNode('C++')
arduino = SkillNode('Arduino')
stm32 = SkillNode('STM32')
ros = SkillNode('ROS')
opencvcpp = SkillNode('OpenCV(C++)')

python = SkillNode('Python', locked = False)
numpy = SkillNode('numpy')
raspberry = SkillNode('Raspberry')
opencvpy = SkillNode('OpenCV(Python)')
pytorch = SkillNode('pytorch')

stc51.relate(c)
cpp.relate(c)
arduino.relate(c)
stm32.relate(cpp)
ros.relate(cpp)
opencvcpp.relate(cpp)
opencvpy.relate((python, numpy))
raspberry.relate(python)
numpy.relate(python)
pytorch.relate((python, numpy))

stc51.relate(stm32, 'similar')
stm32.relate(stc51, 'similar')
c.relate(python, 'similar')
python.relate(c, 'similar')
arduino.relate(raspberry, 'similar')
raspberry.relate(arduino, 'similar')
opencvpy.relate(opencvcpp, 'similar')
opencvcpp.relate(opencvpy, 'similar')


# ECE SkillTree Game (Still questionable whether it counts as a game)
This is a heart-breaking game reflecting painful lives of the poor ECE undergraduates, who always have too much to learn and too little time.  
Be a ECE students and learn all the topics! How quick can you master all of them?  
> Fact: My best score is 60 days.

Good News: you have no deadline!  
Bad News: the game has no ending just like real life so you have to keep suffering from ECE forever  
> Fact: This is a project I make to get myself familiar with pyqt5 and GUI designs.

## How to play
1. download everything
2. open gui.py  
> well I was too lazy to draw another icon for PushButton:hover. So there's no response when you hover on a button  
> Fact: what you think is a button is a button.
3. **click** on a button to **learn()** it.
4. you will know when you are proficient in it.
- "Locked" doesn't mean you can't learn the skill, it just means you have some prerequisite missing.

- **Mechanism**: default learning function uses the TRPG skill learning rules(you can also write your own learning policy):
  - every time you learn you get a random number from 1 - 100
  - if the number is larger than your current skill point, your skill point grow a random number from 1 - 10  
   > yes, the more you know the slower you learn.
  
  - Every Missing Prerequisite Skill reduce learned skill points by one.  
   > Someone gonna try learning pytorch before learning numpy
  
  - Every Proficient "Similar" Skill increase learned skill points by one.  
   > Skill points don't grow negatively, don't worry.
   
5. Check how many days do you need to master everything!  
  > Even if you failed to learn anything a day still fades away. Fear the worst nightmare of all the ECE students!  

## File List
* SkillNode.py
  class SkillNode. It defines what is a node.
  #### Function list
  
  ```python
  relate(self, skill, relation = 'lower')
  cpp.relate(c, 'lower') # set c as cpp's prerequisite
  ```
  there are two relations, 'lower' and 'similar'
  
  ```python
  friends(self, relation = 'lower', for_print = True)
  cpp.friends('lower', True) # returns a string tuple of names of cpp's prerequisites.
  cpp.friends('similar', False) # returns an object tuple of cpp's similar skills.
  ```
  
  ```python
  try_unlock(self) 
  #helper function, useful when you write your own learning policy
  #help you deal with skills other than your learning target if you use your own learning policy.
  ```
  
  ```python
  check_proficient(self)
  #return a bool, its name says everything.
  ```
  
  ```python 
  learn(self, learning_func = standard_learn, adjustment = 0)
  #pass your learning policy to learning_func and modifiers tuple to adjustment
  ```
  
  ```python
  use(self, difficultyLevel = 1)
  #use a skill. Useless in this project.
  ```
  
  ##### Static function
  ```python
  def standard_learn(skillPoints, factor, difficultyBonus = 0)
  #default learning function, an example about how to write your own
  #just return the changed skillpoints after learning.
  ```
* skilltree.py  
  logic of gui
* skilltree_gui.py  
  design of gui
* skilltree_gui.ui  
  useless, **don't try pyuic5 it**, not corresponding to skilltree_gui.py.
* **gui.py**  
  starter, a.k.a. main().

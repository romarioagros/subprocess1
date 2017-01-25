
 
#!/usr/bin/env python
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


import subprocess
import glob
import os.path
import os

temp= (os.getcwd())
#os.chdir(r'c:\Users\roman\Documents\GitHub\Python_course\PY1_Lesson_2.5\homework\Source')



our_procecess = subprocess.run(['convert','trump_mug.jpg' , '-resize', '200' , 'd:\счета new\дом\_roman9.jpg'])

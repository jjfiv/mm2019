import sys
from typing import List

"my script"
# This is the main program:


def main(args: List[str]):
#loop through main arguments
for arg in args:
   print("You said: {0}".format(arg))

   """
   prints a message fancy

   """

  or else print instructions
    print("Try this script with arguments!")

if __name__ == '__main__':
  main(sys.argv[1:])

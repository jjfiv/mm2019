import sys

def main(args):
  for arg in args:
    print("You said: {0}".format(arg))
  if len(args) == 0:
    print("Try this script with arguments!")

if __name__ == '__main__':
  main(sys.argv[1:])

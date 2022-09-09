from pycsp.parallel import *
import time
@process
def P1():
   time.sleep(10)
   print('P1 exiting')
@process
def P2():
   time.sleep(5)
   print('P2 exiting')
def main():
   Parallel(P1(), P2())
   print('Terminating')
if __name__ == '__main__':
   main()
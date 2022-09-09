from multiprocessing import Process, Queue
import queue
import random
def f(q):
   q.put([42, None, 'hello'])
def main():
   q = Queue()
   p = Process(target = f, args = (q,))
   p.start()
   print (q.get())
if __name__ == '__main__':
   main()
class Node:

    def __init__(self, item):

        self.next = None

        self.item = item

class Queue:

    def __init__(self):

        self.front = self.rear = None

    def is_empty(self):

        return self.front == None

    def enqueue(self, value):

        t = Node(value)

        if self.rear == None:

            self.front = self.rear = t

            return

        self.rear.next = t

        self.rear = t


    def dequeue(self):


        if self.is_empty():


          return "queue is null"


        t = self.front


        self.front = t.next


        if(self.front == None):


            self.rear = None

    def peek(self):

        if self.is_empty():

            return "queue is null"

        else:

            return self.front.item

def Breadth_First_Search(self,node):

            arr =[]

            bfs_queue = Queue()

            bfs_queue.enqueue(node)  # The operation of adding an element to the rear of the queue is known as enqueue
         

            try:

                while bfs_queue.peek():

                    start = bfs_queue.dequeue() # , we always dequeue (or access) data, pointed by front pointer , Removes an item from the queue

                    arr.append(start.value)

                    if start.right:

                        bfs_queue.enqueue(start.right)

                    if start.left:

                        bfs_queue.enqueue(start.left)


            except AttributeError :

                pass

            print( arr)



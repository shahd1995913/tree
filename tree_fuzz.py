"""
Create a Node class that has properties for the value stored in the node.
"""
class Node:

    def __init__(self,value=None):



        self.value = value

        self.kth = []


    """
Create a Kth_tree class that have a 1 method  fizz_buzz_tree  that determine whether or not the value of each node is divisible by 3, 5 or both
"""

class Kth_tree:

    def __init__(self):

        self.root = None


def fizz_buzz_tree(root):

        if root == None:

            return root

        value_crr = root


        arr = []

        arr.append(value_crr)


        while len(arr) != 0 :

# removes an item at a specified index value from a list.
            value_crr = arr.pop(0)  # pop() accepts one argument: the index of the item you want to remove.

            if value_crr.value % 15==0:

                value_crr.value = 'FizzBuzz'


            elif value_crr.value % 3 == 0:

                value_crr.value = 'Fizz'

            elif value_crr.value % 5 == 0:

                value_crr.value = 'Buzz'
            else:
                value_crr.value = str(value_crr.value)

            for node in value_crr.kth:
                arr.append(node)
                
        return root


kth_obj= Kth_tree()
kth_obj.root = Node(10)
print(fizz_buzz_tree(kth_obj.root).value)

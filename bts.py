class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


    def add_child(self,data):  # it  caould be any node in tree
        if data ==self.data:  # if the value is already exist then return  , if i want to add value
            return
        if data< self.data:
            # add data in the left
            if self.left:
                self.left.add_child(data)
            else :
                 self.left =BinaryTreeNode(data)
             
        else : 
            if self.right:
                self.right.add_child(data)

            else:
                self.right =BinaryTreeNode(data)   

# Implement in order 
    def in_order(self):
        element =[]
        # visit the left tree
        if self.left:
            element +=self.left.in_order()    

        # visit the root node
        element.append(self.data)

        if self.right:
            element +=self.right.in_order()

        return element

    def serach(self,val):

        if self.data ==val:
            return True

        if val < self.data:
            if self.left:
                 return  self.left.serach(val)
            else:
                return False

        if val > self.data:
            if self.right:
               return self.right.serach(val)
            else :
               return False
# Find maxiam node in tree : the max value will be in right in BT
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

# Find minamin in tree  : the minamin will be in the left in BT
    def  find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left =self.left.delete(val)
        elif  val >self.data:
            if self.right:
                  self.right =self.right.delete(val)
        else:
           if self.left is None and self.right is None:
               return None
           if self.left is None :
               return self.right
           if self.right is None:
                return self.right

           min_val=self.right.find_min()
           self.data=min_val
           self.right=self.right.delete(min_val)

        return self

    def sum_tree(self):
        left_sum=self.left.sum_tree() if self.left else 0
        right_sum =self.right.sum_tree() if self.right else 0
        return self.data +left_sum+ right_sum



    def post_order(self):
        element=[]
        if self.left:
            element+=self.left.post_order()
        if self.right:
            element+=self.right.post_order()
        element.append(self.data)
        return element
    def pre_order(self):
        element=[self.data]
        if self.left:
            element+=self.left.pre_order()
        if self.right:
            element+=self.right.pre_order()
        return element


def bulid_tree(element):
    root =BinaryTreeNode(element[0])
    for i in range(1,len(element)):
        root.add_child(element[i])

    return root



if __name__=="__main__":
    num=[17,4,0,200,9,23,18,34]
    num_tree =bulid_tree(num)
    print("In order in tree ",num_tree.in_order())
    print("Search about 17 in tree is ",num_tree.serach(17))
    print("Search about 100 in tree is ",num_tree.serach(100))
    print("The max value in tree",num_tree.find_max())
    print("The min value in tree",num_tree.find_min())
    num_tree.delete(23)
    print("After delete a value from tree",num_tree.in_order())
    print("sum all node value in tree ",num_tree.sum_tree())
    print("Post order tree",num_tree.post_order())
    print("Pre order tree",num_tree.pre_order())
    print("sum of odd node ",num_tree.sum_odd())












            
    
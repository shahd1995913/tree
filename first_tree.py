class treeNode:


    def __init__(self,data):
        self.data=data
        self.childern =[]  # list for each element  elemnt instance in class
        self.perent=None


    def add_child(self,child):
        child.perent=self
        self.childern.append(child)

    def get_level(self):
        level =0
        p=self.perent
        while p:
            level=level+1
            p=p.perent
        return level

        



    def print_tee(self):
        s= ' ' * self.get_level() *3
        pre =s +"|__" if self.perent else ""
        print(pre + self.data)
        if len(self.childern):
            for c in self.childern:
                c.print_tee()

def bulid_product_tee():
        root =treeNode("Electronic")

        laptop=treeNode("labtop")
        laptop.add_child(treeNode("Mac"))
        laptop.add_child(treeNode("Hawawi"))

        tv=treeNode("TV")
        tv.add_child(treeNode("Samsunge"))
        tv.add_child(treeNode("LG"))


        root.add_child(laptop)
        root.add_child(tv)

        return root


if __name__=='__main__':
    root=bulid_product_tee()
    root.print_tee()


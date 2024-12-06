import sys
class p1:
    def info_p1(self):
        print("p1 self:", self)
class p2:
    def info_p2(self):
        print("p2 self:", self)
class c1(p1,p2):
    def info_c1(self):
        print("c1 self:", self)

child = c1()
child.info_p1()
child.info_p2()
child.info_c1()

print(sys.getrefcount(child))

class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        
    def __str__(self):
        vstr = "("
        vstr += str(self.x)
        vstr += ", "
        vstr += str(self.y)
        vstr += ", "
        vstr += str(self.z)
        vstr += ")"
        return vstr
        
    def add(v1, v2):
        r = Vector()    # init called here
        r.x = v1.x+v2.x
        r.y = v1.y+v2.y
        r.z = v1.z+v2.z
        return r
    staticmethod(add)

    def stp(v1, v2, v3):
        s = v1.x * (v2.y*v3.z - v3.y*v2.z) - v1.y * (v2.x*v3.z - v3.x*v2.z) + v1.z * (v2.x*v3.y - v3.x*v2.y)
        return s
    staticmethod(stp)

def main():
    # t is 2i+j+5k
    t = Vector(2,1,5)    # init called here

    # m is 3i-2j+4k
    m = Vector(3,-2,4)    # init called here

    # b is 4i-j-2k
    b = Vector(4, -1, -2)    # init called here
    
    print(f"t: {t}")    # str called here
    print(f"m: {m}")    # str called here
    print(f"b: {b}")    # str called here

    # r is t+b
    r = Vector.add(t, b)   # calling a static member function
    print(f"t+b: {r}")    # str called here

    # s is stp ==>  t . m x b
    s = Vector.stp(t,m,b)   # calling a static member function
    print(f"stp: {s}")    # str called here

main()

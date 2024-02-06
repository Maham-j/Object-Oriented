class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y 
        self.__z = z
        
    def __str__(self):
        vstr = "("
        vstr += str(self.__x)
        vstr += ", "
        vstr += str(self.__y)
        vstr += ", "
        vstr += str(self.__z)
        vstr += ")"
        return vstr
        
    def add(v1, v2):
        r = Vector()    # init called here
        r.__x = v1.__x+v2.__x
        r.__y = v1.__y+v2.__y
        r.__z = v1.__z+v2.__z
        return r
    
    def stp(v1, v2, v3):
        s = v1.__x * (v2.__y*v3.__z - v3.__y*v2.__z) - v1.__y * (v2.__x*v3.__z - v3.__x*v2.__z) + v1.__z * (v2.__x*v3.__y - v3.__x*v2.__y)
        return s
    staticmethod(stp)
    
def main():
    # t is 2i+j+5k
    t = Vector(2,1,5)    # init called here

    # m is 3i-2j+4k
    m = Vector(3,-2,4)    # init called here

    # b is 4i-j-2k
    b = Vector(4, -1, -2)    # init called here
    
    # -------------------------------------------
    #print(r.__x)      # error due to private __x
    # -------------------------------------------

    print(f"t: {t}")    # str called here
    print(f"m: {m}")    # str called here
    print(f"b: {b}")    # str called here

    # r is t+b
    r = t.add(b)   # calling an instance member function
    print(f"t+b: {r}")    # str called here

    # s is stp ==>  t . m x b
    s = Vector.stp(t,m,b)   # calling a static member function
    print(f"stp: {s}")    # str called here

main()

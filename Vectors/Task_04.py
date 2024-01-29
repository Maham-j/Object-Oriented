#task_04
class Vector:
    pass

def cross_product(v1,v2):
    r = Vector()
    r.x = v1.x*v2.y-v2.x*v1.y
    r.y = v1.y*v2.z-v2.y*v1.z
    r.z = v1.x*v2.z-v2.x*v1.z
    return r

def print_vectors(result):
    print(f'result:{result.x},{result.y},{result.z}')
    
def vectors():
    v = Vector()
    v.x = 3
    v.y = 5
    v.z = 2
    
    m = Vector()
    m.x = 6
    m.y = 8
    m.z = 1
    
    result = cross_product(v,m)
    print_vectors(result)


vectors()

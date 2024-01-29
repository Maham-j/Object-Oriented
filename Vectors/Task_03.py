#task_03
class Vector:
    pass

def main():
    v = Vector()
    v.x = 3
    v.y = 2
    v.z = 1
    return v
    
def magnitude(vector):
    m = (vector.x**2+vector.y**2+vector.z**2)**0.5
    return m

def unit_vector(vector,magnitude):
    r = Vector()
    r.x = vector.x/magnitude
    r.y = vector.y/magnitude
    r.z = vector.z/magnitude
    return r

def print_vector(result):
    print(f'({result.x}, {result.y}, {result.z})')

v = main()
mag = magnitude(v)
print(f'magnitude:{mag}')
unit_vec= unit_vector(v,mag)  
print_vector(unit_vec)

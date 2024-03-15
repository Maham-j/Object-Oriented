#task_05
class Vector:
    pass 


def equality(v1,v2): 
    if v1.x == v2.x and v1.y == v2.y and v1.z == v2.z :
        return 'Vectors are equal'
    else:
        return 'Vectors are not equal'
    
def vectors():
    v = Vector()
    v.x = 3
    v.y = 5
    v.z = 2
    
    m = Vector()
    m.x = 6
    m.y = 8
    m.z = 1
     

    result = equality(v,m)
    print(result)
    
vectors()

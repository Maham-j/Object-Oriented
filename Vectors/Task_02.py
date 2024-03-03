#task_02
class vector:   
    pass  
def main():
    t=vector()
    t.x=3
    t.y=2
    t.z=1
    
    m=vector()
    m.x=6
    m.y=3
    m.z=9
    
    n=vector()
    n.x=2
    n.y=8
    n.z=5
    
    print(f't:{t.x},{t.y},{t.z}')
    print(f'm:{m.x},{m.y},{m.z}')    
    print(f'n:{n.x},{n.y},{n.z}') 
    
    s = t.x*(m.y*n.z-m.z*n.y) + t.y*(m.x*n.z-m.z*n.x) + t.z*(m.y*n.x-m.y*n.x)
    print(f's:{s}')
    
main()

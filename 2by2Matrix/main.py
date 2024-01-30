class Mat2by2:
    def __init__(self,A11=0,A12=0,A21=0,A22=0):
        self.A11 = A11
        self.A12 = A12        
        self.A21 = A21        
        self.A22 = A22
        
    def __str__(self):
        vstr = "("
        vstr += str(self.A11)
        vstr += ","
        vstr += str(self.A12)
        vstr += ","
        vstr += str(self.A21)
        vstr += ","
        vstr += str(self.A22)
        vstr += ")"
        return vstr

    def add(m1,m2):
        a = Mat2by2()
        a.A11 = m1.A11+m2.A11
        a.A12 = m1.A12+m2.A12    
        a.A21 = m1.A21+m2.A21    
        a.A22 = m1.A22+m2.A22    
        return a

    def sub(m1,m2):
        s = Mat2by2()
        s.A11 = m1.A11-m2.A11
        s.A12 = m1.A12-m2.A12    
        s.A21 = m1.A21-m2.A21    
        s.A22 = m1.A22-m2.A22    
        return s

    def mul(m1,m2):
        m = Mat2by2()
        m.A11 = (m1.A11*m2.A11) + (m1.A11*m2.A12)
        m.A12 = (m1.A12*m2.A21) + (m1.A12*m2.A22) 
        m.A21 = (m1.A21*m2.A11) + (m1.A21*m2.A12)   
        m.A22 = (m1.A22*m2.A21) + (m1.A22*m2.A22)  
        return m

    def determinant(m):
        d = (m.A11*m.A22) - (m.A21*m.A12)
        return d

    def transpose(m):
        t = Mat2by2()
        t.A11 = m.A11
        t.A12 = m.A21
        t.A21 = m.A12
        t.A22 = m.A22
        return t

    def isidentity(m):
        if (m.A11 and m.A22 == 1) and (m.A21 and m.A12 == 0):
            return 'is identity matrix'
        else:
            return 'is not identity matrix'

    
def main():
    m1 = Mat2by2(2,4,6,2)
    m2 = Mat2by2(4,5,1,2)
    
    print(f'm1:{m1}')
    print(f'm2:{m2}')

    r = Mat2by2.add(m1,m2)
    print(f'Sum:{r}')

    s = Mat2by2.sub(m1,m2)
    print(f'Sub:{s}')

    t = Mat2by2.mul(m1,m2)
    print(f'Mul:{t}')

    u = Mat2by2.transpose(m1)
    print(f'Transpose:{u}')

    v = Mat2by2.isidentity(m1)
    print(f'Identity:{v}')

    w = Mat2by2.determinant(m1)
    print(f'Determinant:{w}')
main()

        

class Mat3by3:
    def __init__(self,A11=0,A12=0,A13=0,A21=0,A22=0,A23=0,A31=0,A32=0,A33=0):
        self.A11 = A11
        self.A12 = A12
        self.A13 = A13
        self.A21 = A21
        self.A22 = A22
        self.A23 = A23
        self.A31 = A31
        self.A32 = A32
        self.A33 = A33
        
    def __str__(self):
        vstr = "("
        vstr += str(self.A11)
        vstr += ","
        vstr += str(self.A12)
        vstr += ","
        vstr += str(self.A13)
        vstr += ","
        vstr += str(self.A21)
        vstr += ","
        vstr += str(self.A22)
        vstr += ","
        vstr += str(self.A23)
        vstr += ","
        vstr += str(self.A31)
        vstr += ","
        vstr += str(self.A32)
        vstr += ","
        vstr += str(self.A33)
        vstr += ")"
        return vstr
       
    @staticmethod   
    def add(m1,m2):
        add = Mat3by3()
        add.A11 = m1.A11 + m2.A11
        add.A12 = m1.A12 + m2.A12
        add.A13 = m1.A13 + m2.A13
        add.A21 = m1.A21 + m2.A21
        add.A22 = m1.A22 + m2.A22
        add.A23 = m1.A23 + m2.A23
        add.A31 = m1.A31 + m2.A31
        add.A32 = m1.A32 + m2.A32
        add.A33 = m1.A33 + m2.A33
        return add
    
    @staticmethod
    def sub(m1,m2):
        sub = Mat3by3()
        sub.A11 = m1.A11 - m2.A11
        sub.A12 = m1.A12 - m2.A12
        sub.A13 = m1.A13 - m2.A13
        sub.A21 = m1.A21 - m2.A21
        sub.A22 = m1.A22 - m2.A22
        sub.A23 = m1.A23 - m2.A23
        sub.A31 = m1.A31 - m2.A31
        sub.A32 = m1.A32 - m2.A32
        sub.A33 = m1.A33 - m2.A33
        return sub
    
    @staticmethod
    def mul(m1,m2):
        mul = Mat3by3()
        mul.A11 = m1.A11*m2.A11 + m1.A11*m2.A12 + m1.A11*m2.A13 
        mul.A12 = m1.A12*m2.A21 + m1.A12*m2.A22 + m1.A12*m2.A23 
        mul.A13 = m1.A13*m2.A31 + m1.A13*m2.A32 + m1.A13*m2.A33 
        mul.A21 = m1.A21*m2.A11 + m1.A21*m2.A12 + m1.A21*m2.A13 
        mul.A22 = m1.A22*m2.A21 + m1.A22*m2.A22 + m1.A22*m2.A23 
        mul.A23 = m1.A23*m2.A31 + m1.A23*m2.A32 + m1.A23*m2.A33 
        mul.A31 = m1.A31*m2.A11 + m1.A31*m2.A12 + m1.A31*m2.A13 
        mul.A32 = m1.A32*m2.A21 + m1.A32*m2.A22 + m1.A32*m2.A23 
        mul.A33 = m1.A33*m2.A31 + m1.A33*m2.A32 + m1.A33*m2.A33 
        return mul
     
    @staticmethod
    def determinant(m):
        d = m.A11*(m.A22*m.A33-m.A32*m.A23) - m.A12*(m.A21*m.A33-m.A31*m.A23) - m.A13*(m.A21*m.A32-m.A31*m.A22)
        return d
    
    @staticmethod
    def transpose(m):
        t = Mat3by3()
        t.A11 = m.A11
        t.A12 = m.A21
        t.A13 = m.A31
        t.A21 = m.A12
        t.A22 = m.A22
        t.A23 = m.A32
        t.A31 = m.A13
        t.A32 = m.A23
        t.A33 = m.A33
        return t
    
    @staticmethod
    def isidentity(m):
        if (m.A11 == 1 and m.A22 == 1 and m.A33 == 1) and (m.A21 == 0  and m.A31 == 0 and m.A12 == 0  and m.A32 == 0 and m.A13 == 0 and m.A23 == 0):
            return 'is identity matrix'
        else:
            return 'not an identity matrix'
        
def main():
    m1 = Mat3by3(1,0,0,0,1,0,0,0,1)
    m2 = Mat3by3(1,2,3,4,5,6,7,8,9)
    
    print(f'm1: {m1}')
    print(f'm2: {m2}')
    
    a = Mat3by3.add(m1,m2)
    print(f'add: {a}')
    
    s = Mat3by3.sub(m1,m2)
    print(f'sub: {s}')
    
    m = Mat3by3.mul(m1,m2)
    print(f'mul: {m}')
    
    d = Mat3by3.determinant(m2)
    print(f'determinant: {d}')
    
    t = Mat3by3.transpose(m2)
    print(f'transpose: {t}')
    
    i = Mat3by3.isidentity(m1)
    print(f'isidentity: {i}')
    
main()
    
        
        

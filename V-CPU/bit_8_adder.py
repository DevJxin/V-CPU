from Gates import FullAdder
def Bit_8_adder(a,b,Sum,Carry):
        for i,y,c in zip(a,b,Carry):
            current_carry = c
            p=7
            while(p>=0):
                Sum_bit , carry = FullAdder(i[p],y[p],current_carry)
                Sum[p] = Sum_bit
                current_carry = carry
                p-=1
            print(f"\n SUM : {Sum} , Carry : {carry} \n ")
            print("------------------------------------------------------------------------------------------")
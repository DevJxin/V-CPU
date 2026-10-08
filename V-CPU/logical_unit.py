from Gates import AND , OR , NOT , XOR , NXOR , NAND 
i =0 

def Logical_Unit(x,y):
    Result_all = [[None]*8 for _ in range(6)]

    Gate = [AND,OR,XOR,NXOR,NAND]

    row=0
    
    for Func in Gate:
        for i in range(8):
            Result_all[row][i] = Func(x[i], y[i])
        row += 1
    for o in range(8):
        Result_all[5][o] = NOT(x[o])

    print(f"\n Logical unit : {Result_all} \n ")
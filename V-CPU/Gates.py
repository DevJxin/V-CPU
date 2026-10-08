 
# a = [None]*8
# b = [None]*8

# def Signal_Input(y):
#     i=0
#     while(i != 8):
#         x = int(input("Enter Signal"))
#         if x != 0 and x != 1:
#             print("Invalid Signal")
#         y[i] = x
#         i = i + 1
#     return y

# print("Give 8bit Signal For A")
# a = Signal_Input(a)
# time.sleep(2)
# print("Give 8bit Signal For B")
# b = Signal_Input(b)
# print(f"A : {a} , B : {b}")


# if a != 0 and a != 1:
#     print("Invalid signal run again")
#     exit()
# if b != 0 and b != 1:
#     print("Invalid Signal  run again2" )
#     exit()

def AND(x, y):
    return x & y
 
def OR(x,y):
    return x | y

def NOT(x):
    return 1-x
    
def NAND(x,y):
    output = AND(x,y)
    output = NOT(output)
    return output

def NOR(x,y):
    output = OR(x,y)
    output = NOT(output)
    return output

def XOR(x,y):
    if x == y:
        output = 0
    else:
        output = 1
    return output

def NXOR(x,y):
    output = XOR(x,y)
    output = NOT(output)
    return output


def HalfAdder(x,y):
    sum = XOR(x,y)
    carry = AND(x,y)
    return sum , carry



def FullAdder(x,y,c):
    Output = HalfAdder(x,y)
    sum = XOR(Output[0],c)
    carry_part = AND(Output[0],c)
    Carry = OR(carry_part,Output[1])
    return sum , Carry

def CarryIn():
    c = int(input("Enter a carry in"))
    if c != 0 and c != 1:
        print("Invalid Carry")
        exit()
    return c



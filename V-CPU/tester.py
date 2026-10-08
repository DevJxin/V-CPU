# Total 9 cases
Test_one = [[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0]]
Test_2 = [[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1]]

test_3 = [[1, 0, 1, 0, 1, 0, 1, 0],[0, 1, 0, 1, 0, 1, 0, 1]]

test_4 = [[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],]

Test_5 = [[0, 0, 0, 0, 0, 0, 0, 1],[1, 1, 1, 1, 1, 1, 1, 1]]

test_6 = [[1, 1, 1, 1, 1, 1, 1, 1],[0, 0, 0, 0, 0, 0, 0, 1]]

test_7 =[[1, 0, 0, 0, 0, 0, 0, 0],[1, 0, 0, 0, 0, 0, 0, 0]]

test_8 = [[1, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],]

test_9 = [[0, 0, 0, 0, 0, 0, 0, 1],[0, 0, 0, 0, 0, 0, 0, 0]]

Carry = [0,1]

def Testing():
    # Final Tester , It takes all the test cases and makes a 3D Arrays

    Final_Tester = [Test_one,Test_2,test_3,test_4,Test_5,test_6,test_7,test_8,test_9]

    # Test_Case_NO is defined as index number of edge cases

    Test_Case_NO =1

    for i in Final_Tester:
            
            # At specific Test cases Carry will given as 1 else it will be 0 

            if Test_Case_NO == 2:
                c = Carry[1]
            elif Test_Case_NO == 4:
                c= Carry[1]
            else:
                c =Carry[0]
            yield i[0], i[1], c
            Test_Case_NO +=1    
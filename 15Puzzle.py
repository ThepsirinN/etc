import numpy as np
ans = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
ng = list(np.random.permutation(np.arange(0,16))[:16])

while True:
    print(ng[0],"[0]","\t-",ng[1],"[1]","\t-",ng[2],"[2]","\t-",ng[3],"[3]")
    print(ng[4],"[4]","\t-",ng[5],"[5]","\t-",ng[6],"[6]","\t-",ng[7],"[7]")
    print(ng[8],"[8]","\t-",ng[9],"[9]","\t-",ng[10],"[10]","\t-",ng[11],"[11]")
    print(ng[12],"[12]","\t-",ng[13],"[13]","\t-",ng[14],"[14]","\t-",ng[15],"[15]")
    try:
      in1 = int(input("swap 1 (0-16) : "))
      in2 = int(input("swap 2 (0-16 and not equal to swap 1): "))
      if ((ng[in1] == 0 or ng[in2] == 0) and (abs(in2 - in1) == 1 or abs(in2 - in1) == 4) and in1 != in2) :
          ng[in2],ng[in1] = ng[in1],ng[in2]
      else:
          print("Can't move")
    except:
      print("error input")
    print("")
    if ans == ng:
      print("You win!")
      break

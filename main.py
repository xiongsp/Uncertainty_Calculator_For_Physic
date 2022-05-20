import Direct_Calc
import Indirect_Calc
# import os
# import time
# import sys

# argv = sys.argv
# if not os.path.isdir(".\\history"):
#     os.mkdir(".\\history")
# if len(argv) != 1:
#     if argv[1] == "-list":
#         for i in os.listdir(".\\history"):
#             print(os.listdir(".\\history").index(i), i, end="\t")
#             print()
#         os.system("python " + argv[0] + "<.\\history\\" + os.listdir(".\\history")[int(input())])
#
# f = open(".\\history\\" + time.strftime("%y-%m-%d_%H-%M-%S", time.localtime()) + ".txt", "w+", buffering=1)
#
# history = []

while 1:
    choice1 = input("直接计算（1）\n间接计算（2）\n")
    # history.append(choice1)
    try:
        if choice1 == "1":
            Direct_Calc.main()
            # f.write("\n".join(history) + "\n" + "\n".join(Direct_Calc.history))
            # f.write("\n")
        else:
            Indirect_Calc.main()
            # f.write("\n".join(history) + "\n" + "\n".join(Indirect_Calc.history))
            # f.write("\n")
        if input("是否继续？（y/n）\n") == "n":
            # f.write("n\n")
            break
        # f.write("y\n")
    except Exception as e:
        print(e)
#         history = []
#
# f.close()

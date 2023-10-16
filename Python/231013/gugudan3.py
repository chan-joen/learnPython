for i in range(1,10):
    for j in range(2,5):
        print(f"{j} x {i} = {j*i}",end="\t")
    print("",end="\t")

    for j in range(5,8):
        print(f"{j} x {i} = {j*i}",end="\t")
    print("",end="\t")

    for j in range(8,10):
        print(f"{j} x {i} = {j*i}",end="\t")
    print("\n")
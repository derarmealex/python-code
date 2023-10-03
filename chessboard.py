for item in range(8):
    for item2 in range(8):
        if (item + item2) % 2:
            print(" ", end="")
        else:
            print("█", end="")
    print("")
"""
█ █ █ █ 
 █ █ █ █
█ █ █ █ 
 █ █ █ █
█ █ █ █ 
 █ █ █ █
█ █ █ █ 
 █ █ █ █
"""
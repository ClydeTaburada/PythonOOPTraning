def showTree():

    print("     *      ")
    print("    ***     ")
    print("   *****    ")
    print("  *******   ")
    print("     *      ")
    print("   *****    ")
    print(" *********  ")
    print("************")
    print("    ***     ")
    print("    ***     ")
    print("  *******   ")

# print("Mangga")
# dummy = input("Press <Enter> to proceed")




# print("Bayabas")


#treefunctiondemo.py


#     for i in range(4):
#         spaces = " " * (5 - i)
#         stars = "*" * (2 * i + 1)
#         print(spaces + stars)

#     for i in range(3):
#         spaces = " " * (5 - (i + 2))
#         stars = "*" * (2 * (i + 2) + 1)
#         print(spaces + stars)

#     for _ in range(2):
#         print(" " * 4 + "***")
#     print(" " * 2 + "*******")

# showTree()
# print("A Tree!")
# dummy = input("Press <Enter> to proceed")

# showTree()
# print("Bayabas!")
# dummy = input("Press <Enter> to proceed")

# showTree()
# print("Malunggay!")
# dummy = input("Press <Enter> to proceed")


#trees.py
# def showTree():
#     for i in range(4):
#         spaces = " " * (5 - i)
#         stars = "*" * (2 * i + 1)
#         print(spaces + stars)

#     for i in range(3):
#         spaces = " " * (5 - (i + 2))
#         stars = "*" * (2 * (i + 2) + 1)
#         print(spaces + stars)

#     for _ in range(2):
#         print(" " * 4 + "***")
#     print(" " * 2 + "*******")


# #treesize.py
# def showTree(N):
#     for i in range(N):
#         print("     *      ")
#         print("    ***     ")
#         print("   *****    ")
#         print("  *******   ")
#         print("     *      ")
#         print("   *****    ")
#         print(" *********  ")
#         print("************")
#         print("    ***     ")
#         print("    ***     ")
#         print("  *******   ")
#         print()
        
# strdata = input("Enter X:")
# x = int(strdata)
# showTree(x)


# # #treestatus.py
# def showTree(N,ch):
#     global status
#     for i in range(N):
#         print("     *      ")
#         print("    ***     ")
#         print("   *****    ")
#         print("  *******   ")
#         print("     *      ")
#         print("   *****    ")
#         if ch == 'tall':
#             print(" *********  ")
#             print("************")
#             print("    ***     ")
#             print("    ***     ")
#             print("  *******   ")
#             status = 'T'
#         print()
#     return(status)

# status = 'S'
# strdata = input("Enter X:")
# x = int(strdata)
# size = input("Size(short,tall):")
# stat = showTree(x,size)
# if stat == 'T':
#     print("BIG")
# else:
#     print("SMALL")
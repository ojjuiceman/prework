def splitup(namez):
    evenli = []
    oddli = []
    for name in namez:
        if (len(name) % 2 == 0):
            evenlist = list(name)
            evenlist[0] = 'b'
            newevenname = "".join(evenlist)
            evenli.append(newevenname)

        else:
            oddlist = list(name)
            oddlist[len(oddlist) - 1] = 'c'
            oddnewname = "".join(oddlist)
            oddli.append(oddnewname)

    print(evenli, oddli)
    even_list = evenli
    print(even_list)
    


namez = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]

splitup(namez)





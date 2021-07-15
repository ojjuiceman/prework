def nameck(nme1,nme2,nme3,nme4):
    lgname = ''
    nameppl = [nme1,nme2,nme3,nme4]
    for name in nameppl:
        if len(name) > len(lgname):
            lgname = name
    return lgname
    



big_name = nameck('joe','virginial','dick','dosoo')

print (big_name)

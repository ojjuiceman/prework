lgname = ''
nameppl = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
for name in nameppl:
    if len(name) > len(lgname):
        lgname = name
    else:
        print ('theres longer out there')

print (lgname)

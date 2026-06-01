def _debugs(_v:vars):
    _a=dict(_v)
    counter=0
    for _b in _a:
        if len(_b)>0:
        
        
            if _b[0:1]!="_":
                print(_b+"=",end="")
                print(_a[_b])
        counter=counter+1



_restart={'a':0,'b':10}


_v=vars()
_v.update(_restart)
while a<b:
    print(a)
    a+=1

_v.update(_restart)
while a<b:
    print(a)
    a+=1


_debugs(_v)





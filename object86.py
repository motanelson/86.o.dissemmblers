import os
print("\033c\033[47;31m")
print("give me a object .o file to check ...")
a=input().strip()
os.system("bcc -c -Md libdos.c -o libdos.a")
os.system("cp libdos.a libc.a")
os.system("ld86 -T0x101000 -D0x101100 -i -L -3  $1 -o /tmp/tests.c32".replace("$1",a))
a="/tmp/tests.c32"
os.system("objdump -m i386 --disassembler-options=intel --adjust-vma=0x101000 -b binary -D $1 > /tmp/out.txt".replace("$1",a))
f1=open("/tmp/out.txt","r")
list1=f1.read()
f1.close()
os.system("nm86 $1 > /tmp/out.txt".replace("$1",a))
f1=open("/tmp/out.txt","r")
list2=f1.read()
f1.close()
lists=list2.split("\n")
for a in lists:
    
    a=a.strip()
    
    if a!="":
        a=a.replace(" ","#")
        l1=a.split("#")
        b=l1[0].strip()
        
        b=b[2:]
        b=b+":"
        
        list1=list1.replace(b,l1[2].strip())


print(list1)

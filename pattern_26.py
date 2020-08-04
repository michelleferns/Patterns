print(" "*0,"#"*9,""*0)
print(" "*1,"#"*7,""*1)
print(" "*2,"#"*5," "*2)
print(" "*3,"#"*3," "*3)
print(" "*4,"#"*1," "*4)

print(" "*3,"#"*3," "*3)
print(" "*2,"#"*5," "*2)
print(" "*1,"#"*7," "*1)
print(" "*0,"#"*9," "*0)

lsp=0
mhash=9
rsp=0

print("-----------")

for item in list(range(0,5,1)):
   print(" "*lsp,"#"*mhash," "*rsp)
   lsp=lsp+1
   mhash=mhash-2
   rsp=rsp+1
   
lsp=3
mhash=3


for item in list(range(0,4,1)):
   print(" "*lsp,"#"*mhash)
   lsp=lsp-1
   mhash=mhash+2
   
   

















































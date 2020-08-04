print(" "*4,"#"*1)
print(" "*3,"#"*2)
print(" "*2,"#"*3)
print(" "*1,"#"*4)
print(" "*0,"#"*5)

lsp=4
rhash=1

for item in list(range(1,6,1)):
   print(" "*lsp,"#"*rhash)
   lsp=lsp-1
   rhash=rhash+1

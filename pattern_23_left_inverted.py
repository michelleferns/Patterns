print(" "*0,"#"*5)
print(" "*1,"#"*4)
print(" "*2,"#"*3)
print(" "*3,"#"*2)
print(" "*4,"#"*1)
lsp=0
rhash=5
for item in list(range(0,6,1)):
   print(" "*lsp,"#"*rhash)
   lsp=lsp+1
   rhash=rhash-1


print(' '*0,"#"*9)
print(' '*1,"#"*7)
print(' '*2,"#"*5)
print(' '*3,"#"*3)
print(' '*4,"#"*1)

lsp=0
rhash=9


for item in list(range(0,8,1)):
   print(" "*lsp,"#"*rhash)
   lsp=lsp+1
   rhash=rhash-2
   


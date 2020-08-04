print(' '*4,'#'*1,'  '*4)
print(' '*3,'#'*3,'  '*3)
print(' '*2,'#'*5,'  '*2)
print(' '*1,'#'*7,'  '*1)
print(' '*0,'#'*9,'  '*0)

lsp=5
mhash=1
rsp=5

for item in list(range(0,5,1)):
   print(" "*lsp,"#"*mhash," "*rsp)
   lsp=lsp-1
   mhash=mhash+2
   rsp=rsp-1

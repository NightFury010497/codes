import os
fnames = listdir('.')
for fname in fnames:
    if fname.endswith('.pdf'):
         for i in range(5):
             z = str('_'+str(i)+'A')
#             print(z)
             try:
                 new_name = fname.replace(str(z),'_3A')
                 print(new_name)
                 rename(fname, new_name)
             except:
                 pass
             

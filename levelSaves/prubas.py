
x = int(input('how many files? '))

txtTransfer = """'''
level is still under construction...
Thanks for your patience
'''
"""

for i in range(0,x):
     try:
          cash = open(('lvl'+ str(i) + '.txt'),'x')

          cash.write(txtTransfer)

          cash.close()
     
     except:
          print('could not oppen:',i)


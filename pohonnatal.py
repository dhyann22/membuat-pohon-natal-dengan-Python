height = 15
z = height - 2
x = 1
for i in range(1, (height + height) - 2):
    if i % 2 != 0:
       if(i==1):
          print('~~' * z + 'o' +'~~' * z)
       else:
          print('~~' * z + '* ' * (x-1)+ '*' *1 +'~~' * z)
       x+=2
       z-=1
for a in range(height + 1):
    if a % (height + 1) == 1:
       test = height - 2
       print(test * '~~' + a * '||' + test * '~~')
    if a % (height + 1) == 1:
       test = height - 2
       print(test * '~~' + a * '||' + test * '~~')
       print(test * '~~' + a * '||' + test * '~~')
       print(test * '~~' + a * '##' + test * '~~')
       print(test * '~~' + a * '**' + test * '~~')


       print("```````````````````Merry Christmas 2021```````````````")
       print ("```````````````````~~~~by dyan~~~~~```````````````````")

while True:

 try:

   s = float(input('enter score between 0-100\n'))

   def computegrade():
    grade = s
    return s

   if s > 100 or s < 0:
      print ('enter a valid score')
   elif s>=90:
      print('A')
   elif s>=80:
      print('B')
   elif s>=70:
      print('C')
   elif s>50:
      print('D')
   elif s<50:
      print('F')
   else:
      print('enter a valid score please')

 except:
   print('Please input Score!')

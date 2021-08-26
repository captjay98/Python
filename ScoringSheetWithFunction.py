while True:
 try:
   s = input('enter score between 0.0-1.0\n')
   s = float(s)

   def computegrade():
    grade = s
    return s
   if s > 1.0 or s < 0.0:
      print ('enter a valid score')
   elif s>=0.9:
      print('A')
   elif s>=0.8:
      print('B')
   elif s>=0.7:
      print('C')
   elif s>0.6:
      print('D')
   elif s<0.6:
      print('F')
   else:
      print('enter a valid score please')
 except:
   print('Please input digit')

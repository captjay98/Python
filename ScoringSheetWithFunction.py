#Keeping the scoring in a loop
while True:

 #To catch and handle abberations
 try:

   #The score input
   s = float(input('enter score between 0-100\n'))

   #A function to store the scores
   def computegrade():
    grade = s
    return s

   #The scores and grading
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
 #Catching exceptions
 except:
   print('Please input Score!')

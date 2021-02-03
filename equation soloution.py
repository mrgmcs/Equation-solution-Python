
def calculationx2():
  
  #form of a equation : a*x^2 + b*x + c=0
  
  print ("ax^2 + bx + c=0")
  a = input("Enter a number: ")
  b = input("Enter b number: ") 
  c = input("Enter c number: ")

  print("\n")
  #find value of delta
  delta = (int(b) * int(b)) - (4 * (int(a) * int(c)))
  delta = float(delta)

  if delta<0:
    #if value of delta is smaller than 0, equation has no answer
    print("THIS EQUATION HASN'T AWNSER")
  
  else:
    #now you know delta is greater and equal to 0, we should find roots
    #find root of equation

    Sqroot_delta = pow(delta, 1 / 2) #Sqroot: Square root
    Sqroot_delta=float(Sqroot_delta)

    #find roots of equation with main formula
    x1 = (-1 * int(b) - (Sqroot_delta)) /( 2 * int(a))
    x2 = (-1 * int(b) + (Sqroot_delta))/ (2 * int(a)) 

    if delta==0 :
      #when delta is 0, you have just one answer for equation
      #faster way to find root in this case is :  x=(-1*b)/(2*a)
      print("Delta is 0")  
      print("x1 = x2")
      print("x1,x2 is :",x1)#you can write x2 in this line, because x1 and x2 are the same

    if delta>0:
      #when delta is greater than 0, you have 2 answers for equation
      print("Delta is :",delta,"\n")   
      print ("x1 is : ",x1,"\n")
      print ("x2 is : ",x2) 
#now you should call your function
calculationx2()

#github: mrgmcs
#instagram: mrg.mcs
#goodluck

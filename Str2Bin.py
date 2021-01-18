def stringToBinary(string):
  res = ''.join(format(i, 'b') for i in bytearray(string, encoding ='utf-8')) 

  print("Conversion : " + str(res)) 

string = str(input("Enter any String: "))

stringToBinary(string)

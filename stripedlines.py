from PIL import Image
import numpy as np
from numpy import asarray
import glob, os

repeat = True
while(repeat):
 print ("Enter image size (width x height)")
 inp = input()
 numbers = [int(word) for word in inp.split() if word.isdigit()]

 img = Image.new("RGB", (numbers[0], numbers[1]), "white")
 x = numbers[0]
 y = numbers[1]

 array = np.zeros([y , x,3], dtype = np.uint8)
 print(numbers)

 row = 0
 n= 0
 k= 0
 z = 0

 fd = 0
 sd = 0
 td = 0


# OLD INEFFICENT WAY

 #for i in array:
  #  for x in i:
      
   #   
   #   if(row % 2 == 0):
       
   #    array[fd,sd] = [70,200,255]

  #    sd = sd + 1
  #    td = 0
            
 #   row = row +1
 #   sd = 0
 #   fd = fd + 1
   


#NEW WAY
 i = range(y)
 array[i[::2] , :, :] = 255
 image2 = Image.fromarray(array)
 print ("array -----------------------")
 print(array)
 print(k)
 print(row)
 print(z)

 print("Enter file name: \n")
 name = input()
 image2.show();
 image2.save(name + ".png", "PNG")

 print("Task is done! Type repeat to run the script again or type anything else to exit")
 runagain = input()
 if(runagain != "repeat"):
    exit()
 else:
     repeat = True


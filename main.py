# importing the modules
import imdb 
import os, sys, time
from time import sleep as timeout
#modual setup
ia = imdb.IMDb() 

#selection 
print ("           [1]> Find IMDB id              ")
print ("           [2]> Get movie link            ")
print ("           [0]> Exit ")
A = input(">>>>> ")

if A == "1":
  os.system("clear")
  print('Whats the name of the movie you want?')
  name = input('>>>>>')
  search = ia.search_movie(name) 
  for i in range(len(search)): 
      
    # getting the id 
    id = search[i].movieID 
      
    # printing it 
    print(search[i]['title'] + " : " + id )
    so.system('python main.py')
  if A == "2":
    os.system("clear")
    os.system('python step2.py')
    
  if A == "0":
    os.system("clear")
    sys.exit()
    
else:
  print ("\nERROR: Wrong Input")
  os.system("clear")
  

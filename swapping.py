#clase 3

import os 

file1= "hola.txt"
file2= "chau.txt"

os.rename(file1, "temporal")
os.rename (file2, file1)
os.rename("temporal, file2")



# Pickle it
# Demonstrates pickling and shelving data

import pickle, shelve

print ("Pickling lists")
variety = ["Sweet", "Hot", "Dill"]
shape = ["Whole", "Spear", "Chip"]
brand = ["Claussen", "Heinz", "Classic"]

f = open ("pickles1.dat", "wb")

pickle.dump (variety, f)
pickle.dump (shape, f)
pickle.dump (brand, f)
f.close ()

# unpickling the lists from the file

print ("\nUnpickling lists")
f = open ("pickles1.dat", "rb")
variety = pickle.load (f)
shape = pickle.load (f)
brand = pickle.load (f)

print (variety)
print (shape)
print (brand)

f.close ()

## Shelving
## Shelves act like a dictionary thus providing random access to the lists

print ("Shelving Lists")

# Creating shelf

shelf = shelve.open ("pickles2.dat")

shelf["variety"] = ["Sweet", "Hot", "Dill"]
shelf["shape"] = ["Whole", "Spear", "Chip"]
shelf["brand"] = ["Claussen", "Heinz", "Classic"]

shelf.sync () ## make sure data is written


print("\nRetrieving lists from a shelved file:\t")
print ("brand - ", shelf["brand"])
print ("variety - ", shelf["variety"])
print ("shape - ", shelf["shape"])

shelf.close ()

input ("\nPress Enter key to exit")



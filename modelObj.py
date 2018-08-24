import ast

aStrFromTCP="{'name':'FirstPump','attr1':1,'attr2':3,'attr3':'abc'}"

aPumpObj = ast.literal_eval(aStrFromTCP)
#aPumpObj = {'name':'FirstPump','attr1':1,'attr2':3,'attr3':'abc'}

#print all
print ("Print all attributes ")
print( aPumpObj)
print ("Print an attribue ")
print(aPumpObj['name'])

#change a value of the key
aPumpObj['attr2'] = 99
#add a new key pair
aPumpObj.update({'attr100':0.89})
#del an existing key pair

del aPumpObj['attr1']
print ("========== ")
print ("Print all attributes after add, update, delete ")
print( aPumpObj)
print ("========== ")

print ("Print all keys" )
print (aPumpObj.keys())
print ("Print all values" )
print (aPumpObj.values())

import pickle

pass1 = [ "purnima123@", "user123@67" , "12345678" ]

file = "MyData.pkl"
fileobj = open(file , 'wb')
pickle.dump(pass1 , fileobj)

fileobj.close()

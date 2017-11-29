import numpy as np


# import file
df = np.genfromtxt("input.txt", dtype=float)
print(df)
# get required size of matrix
nDim0 = np.amax(df, axis=0)
nDim = np.amax(nDim0[1:2])

# create initial matrix
Amat = np.zeros((nDim, nDim))

for row in df:
	#print(row)
	i = row[0] - 1
	j = row[1] - 1
	k = row[2]
	
	Amat[i,j]=k
	
print(Amat)

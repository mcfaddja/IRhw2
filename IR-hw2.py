import numpy as np


# constants
beta = 0.85
filename = "input.txt"

# import file
df = np.genfromtxt(filename, dtype=float)

# get required size of matrix
nDim0 = np.amax(df, axis=0)
nDim = np.amax(nDim0[0:2])

# create initial matrix
Amat = np.zeros((nDim, nDim))

for row in df:
	#print(row)
	i = row[0] - 1
	j = row[1] - 1
	k = row[2]
	
	Amat[i,j]=k
	
#print(Amat)

# normalize by column
colSums = Amat.sum(axis=0)
#print(colSums)
Amat = np.transpose(Amat)
Mmat = np.zeros((nDim,nDim))
for i, (row, colSums) in enumerate(zip(Amat, colSums)):
	if colSums != 0:
		Mmat[i,:] = row / colSums
	else:
		Mmat[i,:] = row

# reverse the transpose		
Mmat = np.transpose(Mmat)

print("Normalized adjacency matrix")
print(Mmat)
print("")

# create initial r vector
r0 = np.ones((nDim,1))
r0 = r0 * 1/nDim

print("The original page rank vector")
print(r0)
print("")

# iterate rank vector
testCond = False
while testCond == False:
	r1 = 
		

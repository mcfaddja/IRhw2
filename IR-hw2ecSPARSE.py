class pageRankerSPAR:
    import numpy as np
    #from scipy import sparse
    import scipy as sp
    
    def __init__(self, filename, beta):
        # import file
        df = np.genfromtxt(filename, dtype=float)
        
        # get required size of matrix
        nDim0 = np.amax(df, axis=0)
        nDim = int(np.amax(nDim0[0:2]))
        
        # create initial matrix
        Amat = sp.sparse.lil_matrix(np.zeros((nDim, nDim)))
        
        # load data into initial matrix
        for row in df:
            i = int(row[0] - 1)
            j = int(row[1] - 1)
            k = row[2]
	
            Amat[i,j]=k
        
        # normalize by column
        colSums = Amat.sum(axis=0)
        # transpose to match dimensionality
        Amat = np.transpose(Amat)
        #Mmat = np.zeros((nDim,nDim))
        for i, (row, colSum) in enumerate(zip(Amat, colSums)):
            if np.any(colSum):
                Amat[i,:] = row / colSums
            else:
                Amat[i,:] = row
                
        # reverse the transpose		
        Amat = np.transpose(Amat)
        
        # create initial r vector
        r0 = np.ones((nDim,1))
        r0 = r0 * 1/nDim
        r00 = r0
        
        # iterate rank vector
        nCnt = 0 # number of itterations
        testCond = False # initialize test condition
        nMax = 1000000 # safety counter to prevent infinite looping
        while testCond == False:
            r1 = beta*sp.sparse.lil_matrix.dot(Amat,r0) + (1-beta)*np.ones((nDim,1))*(1/nDim)
            
            testCond = np.allclose(r0, r1)
            if testCond == False:
                r0 = r1
                
            nCnt = nCnt + 1
            if nCnt == nMax:
                break
        
        #print("Normalized adjacency matrix")
        #print(Amat)
        #print("")
        
        #print("The original page rank vector")
        #print(r00)
        #print("")
        
        print("number of itterations")
        print(nCnt)
        print("")
        
        #print("Final page rank vector")	
        #print(r1)

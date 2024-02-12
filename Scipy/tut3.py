# sparse data 
# sparse data eg - [1,0,0,2,0,0,0,3,0,0,0,0,4,0]
# dense data eg - [1,2,4,8,3,5,7,3,5,1,6]
# To work with sparse data we use sparse(): there are 2 matrics : CSC(Compressed Sparse Column) and CSR (Compressed Sparse Row)

# CSR matrics: 
import numpy as np
from scipy.sparse import csr_matrix
shared = np.array([0,0,0,0,0,1,1,0,2])
print(csr_matrix(shared))
print(csr_matrix(shared).data)

sha = np.array([[0,0,0],[0,0,1],[1,0,2]])
print(csr_matrix(sha))
print(csr_matrix(sha).data)
print(csr_matrix(sha).count_nonzero()) # To count no. of non-zero values

shanew = csr_matrix(sha)
shanew.eliminate_zeros()   #For removing zero elements from the matrix
print(shanew)

shanew.sum_duplicates()  # Eliminating duplicate values
print(shanew)

# csr to csc with tocsc()
shanew = csr_matrix(sha).tocsc()
print(shanew)
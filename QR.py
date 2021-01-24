import numpy as np
M=np.random.rand(6000,6000)
print(M)
Q, R =np.linalg.qr(M)
print(Q)
print(R)
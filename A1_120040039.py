import numpy as np

X = np.array([[1, 2], [4, 3], [5, 6], [3, 8], [9, 10]])
y = np.array([[-1], [0], [1], [0], [0]])

# Please replace "MatricNumber" with your actual matric number here and in the filename
def A1_120040039(X,y):
    """
    Input type
    :X type: numpy.ndarray
    :y type: numpy.ndarray

    Return type
    :w type: numpy.ndarray
    :XT type: numpy.ndarray
    :InvXTX type: numpy.ndarray
   
    """
    # your code goes here
    pass
    XT = X.transpose()
    XTX = np.matmul(XT,X)
    InvXTX = np.linalg.inv(XTX)
    XTX1XT = np.matmul(InvXTX, XT)
    w = np.matmul(XTX1XT, y)

    # return in this order
    return w, XT, InvXTX

result = A1_120040039(X, y)
print(result)
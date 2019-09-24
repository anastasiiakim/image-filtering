import numpy as np
import math

def modified_sierpinski_curve(N, plot_curve = False):
    dx = np.zeros(2**(2*N), dtype=int)
    dy = np.zeros(2**(2*N), dtype=int)
    x = np.zeros(2**(2*N), dtype=int)
    y = np.zeros(2**(2*N), dtype=int)
    
    # directions of curve 
    dx[0:8] = [1, 0, 1, 1, 0, -1, 1, 0] 
    dy[0:8] = [0, -1, 1, 0, -1, 0, -1, -1]
    
    #building fractal curve
    for n in range(2,N):
        dx[2**(2*n-1):2**(2*n)] = -dy[0:2**(2*n-1)]
        dy[2**(2*n-1):2**(2*n)] = dx[0:2**(2*n-1)]
        dx[2**(2*n-1)] = 1
        dy[2**(2*n-1)] = 1
        dx[2**(2*n):2**(2*n+1)] = dy[0:2**(2*n)]
        dy[2**(2*n):2**(2*n+1)] = -dx[0:2**(2*n)]
    

    dx[2**(2*N-1):2**(2*N)] = -dx[0:2**(2*N-1)]
    dy[2**(2*N-1):2**(2*N)] = -dy[0:2**(2*N-1)]

    for i in range(2**(2*N)-1):
        x[i+1] = x[i] + dx[i]
        y[i+1] = y[i] + dy[i]
        
    if plot_curve:
        plt.plot(x,y)
        plt.show()

    return x, y

def scan_image_with_sierpinski(N, m, X, x, y):
    data = np.zeros((m,2**(2*N)), dtype='float32')
    for j in range(0,m):
        for i in range(2**(2*N)-1):
            data[j,i] = X[j,-y[i],x[i]]
            
    return data


# N is the order of the curve
def rix(cy, N, d):
    rx = np.zeros(N, dtype=int)
    for i in range(N):
        rx[i] = d*cy[N-i-1]
        
    return rx

    

def hilbert_curve(N, plot_curve = False):
    #initialize arrays
    dx = np.zeros(4**(N), dtype=int)
    dy = np.zeros(4**(N), dtype=int)

    dxp = np.zeros(4**(N), dtype=int)
    dyp = np.zeros(4**(N), dtype=int)

    x = np.zeros(4**(N), dtype=int)
    y = np.zeros(4**(N), dtype=int)
    
    # directions of curve 
    dxp[0:3] = [0, 1, 0] 
    dyp[0:3] = [1, 0, -1]
    

    #building fractal curve
    for n in range(1,N):
        dx[0:(4**(n+1)-1)] = np.concatenate((rix(dyp[0:(4**n-1)], 4**n-1, -1), [0], dxp[0:(4**n-1)], [1], dxp[0:(4**n-1)], [0], rix(dyp[0:(4**n-1)], 4**n-1, 1)))
        dy[0:(4**(n+1)-1)] = np.concatenate((rix(dxp[0:(4**n-1)], 4**n-1, 1), [1], dyp[0:(4**n-1)], [0], dyp[0:(4**n-1)], [-1], rix(dxp[0:(4**n-1)], 4**n-1, -1)))
        dxp[0:(4**(n+1)-1)] = dx[0:(4**(n+1)-1)]
        dyp[0:(4**(n+1)-1)] = dy[0:(4**(n+1)-1)]

    for i in range(2**(2*N)-1):
        x[i+1] = x[i] + dx[i]
        y[i+1] = y[i] + dy[i]
    
    if plot_curve:
        plt.plot(x,y)
        plt.show()
        
    return x, y

def scan_image_with_hilbert(N, m, X, x, y):
    data = np.zeros((m,2**(2*N)), dtype='float32')
    for j in range(0,m):
        for i in range(2**(2*N)-1):
            data[j,i] = X[j,x[i],y[i]]
            
    return data
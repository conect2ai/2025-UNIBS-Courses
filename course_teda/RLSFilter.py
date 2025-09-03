import numpy as np

class RLSFilter:
    """
    Adaptive RLS filter.
    
    **Args:**

    * `n` : length of filter (integer) - how many input is input array
      (row of input matrix)

    **Kwargs:**

    * `mu` : forgetting factor (float). It is introduced to give exponentially
      less weight to older error samples. It is usually chosen
      between 0.98 and 1.

    * `delta` : regularization factor (float). It is usually chosen
      between 0.1 and 1.

    * `w` : initial weights of filter. Possible values are:
        
        * array with initial weights (1 dimensional array) of filter size

        * "zeros" : create zero value weights
    """ 

    def __init__(self, n=2, mu=0.99, delta=0.1, w=np.zeros(2)):
        if type(n) == int:
            self.n = n
        else:
            raise ValueError('The size of filter must be an integer') 
        
        if ((mu <= 0) or (mu > 1)):
            raise ValueError('The forgetting factor must be between 0 an 1') 
        else:
            self.mu = mu
        
        self.delta = delta
        self.w = w
        

        self.P = 1/self.delta * np.identity(n)
        self.dw = np.zeros(len(self.w))

    def update(self, d, x):
        """
        Update filter - adapting weights according to desired value and its input.

        **Args:**

        * `d` : desired value (float)

        * `x` : input array (1-dimensional array)
        """
        y = np.dot(self.w, x)
        e = d - y
        P1 = np.dot(np.dot(np.dot(self.P,x),x.T),self.P)
        P2 = self.mu + np.dot(np.dot(x,self.P),x.T)
        self.P = 1/self.mu * (self.P - P1/P2)
        self.dw = np.dot(self.P, x.T) * e
        self.w += self.dw

    def filter(self, x):
        """
        This function calculates the new output value `y` from input array `x`.

        **Args:**

        * `x` : input vector (1 dimension array) in length of filter.

        **Returns:**

        * `y` : output value (float) calculated from input array.

        """
        y = np.dot(self.w, x)
        return y
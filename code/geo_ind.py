'''
 geo_ind.py
 This is a file that is meant to implement the geo-indistinguishability framework
 for GeoMark. Note, most of the code here is taken from a Python adaptation of
 geopriv4j from the following paper: (Fan and Gunja, 2020):

 Essentiallyk, this method, will simply generate a new location (z) with some
 probability (p) that reduces as teh distance increases within a certain
 radius. In my implementation of GeoMark, we will be utilizing these perturbed
 distances for the creation of new Markov Chains for data synthesis.

 It is also notable that the adaptation of this algorithm from geopriv4j is based on
 the geo-indistinguishability paper by Andres, Miguel E., et al "Geo-indistinguishability:
 Differential privacy for location-based systems"

 Randy Truong
 Northwestern University (Penn State University Machine Learning + Cybersecurity
 REU"

 August 01, 2023
'''

import numpy as np


# LambertW()
# This is a function for defining the lambda distribution, aka an interpolation technique
def LambertW(x):

    #Min diff decides when the while loop ends
    min_diff = 1e-10
    if (x == -1 / np.e):
        return -1

    elif ((x < 0) and (x > -1/np.e)):
        q = np.log(-x)
        p = 1
        while (abs(p-q) > min_diff):
            p = (q * q + x / np.exp(q)) / (q + 1)
            q = (p * p + x / np.exp(p)) / (p + 1)
        #determine the precision of the float number to be returned
        return (np.round(1000000 * q) / 1000000)
    elif (x == 0):
        return 0
    else:
        return 0

def inverseCumulativeGamma(epsilon, z):
    x = (z - 1) * np.e
    return ( -(LambertW(x) + 1 ) ) / epsilon

def addVectorToPos(lng, lat, distance, angle) -> (int, int):
    # TODO: Adapt this function for grid-based geo-discretization
    '''
    params:
        int: lng - longitude
        int: lat - latitude
        int: distance - this is going to be the mechanism for perturbation?
        int: angle - the angle
    '''

    '''
    Pseudo-Code
    0. Find the distance from the point to the
    1. Convert the given longitude and latitude into (lat1, lon1)
    2. Create a new (lat2, lon2) - Issue, what is lat2 and lon2? 
    '''

    return

class LaPlaceAlgorithm:
    def __init__(self, epsilon = 0.5),:
        self.epsilon: float = epsilon
        return None
    def perturb()

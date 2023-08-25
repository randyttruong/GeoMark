# ldp.py

import numpy as np
import random
import math
import helpers

####################################
#     Geo-Indistinguishablility    #
####################################

''' 
Changelog for GDPServer: 
    TODOs: 


'''

'''
Summary of Technique:
/*
 * In this method we will be generating a new location (z) with a probability (p) that
 * reduces as the distance increase within a certain radius (r).
 *
 * As in Geopriv4j, this algorithm is based on the paper by Andrés, Miguel E., et al.
 * "Geo-indistinguishability: Differential privacy for location-based systems."
 * Proceedings of the 2013 ACM SIGSAC conference on Computer & communications
 * security. 2013. https://doi.org/10.1145/2508859.2516735

'''
##################################################
#    Perturbation Functions                      #
##################################################




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
    '''
    params:
        int: lng - longitude
        int: lat - latitude
        int: distance - this is going to be the mechanism for perturbation?
        int: angle - the angle
    '''
    ang_distance = distance / earth_radius
    lat1 = helpers.rad_of_deg(lat)
    lon1 = helpers.rad_of_deg(lng)

    lat2 = np.arcsin(np.sin(lat1) * np.cos(ang_distance) + np.cos(lat1) * np.sin(ang_distance) * np.cos(angle))

    lon2 = lon1 + np.arctan2(np.sin(angle) * np.sin(ang_distance) * np.cos(lat1),
                             np.cos(ang_distance) - np.sin(lat1) * np.sin(lat2))
    lon2 = (lon2 + 3 * np.pi) % (2 * np.pi) - np.pi  # Normalize to -180 to +180

    latnew = helpers.deg_of_rad(lat2)
    lngnew = helpers.deg_of_rad(lon2)
    return lngnew, latnew

class GDPServer: 
    def __init__(self, epsilon, d, map_func):
        """ 
        Server-Side Geo-Indistinguishability Object

        params:
        - param epsilon: privacy budget
        - param d: domain size
        - param map_func: index mapping function
        """ 
       
        # TODO Build Initialization Object
        # super(): This essentialy just creates an inherited version of the
        # GDPServer
        super(GDPServer, self).__init__(epsilon, d, map_func)

        # Number of Users
        self.n = 0

    # GDP.aggregate
    def aggregate(self, data):
        """
        params:
            data: list[int] (note, formerly in OUEServer, we observe that data was a
            list that represented a perturbed number in binary)
        """
        # TODO 1 : Analyze how aggregation works in LDPTrace
        #   - In LDPTrace, the optimized unary encoding will initially distribute
        # the privacy budget `\varepsilon` onto the binary vector that is formed
        # from the indices of the `Grid()` object.

        # The data curator then needs to aggregate this data and then adjust it
        # as to essentially decode it. We observe that the aggregation is done by
        # simply adding the values of the trajectory points, then decoding them
        # using the formula ({number of POI vectors} - {total vectors} * {probability that any index of the binary vector is 0})

        # TODO 2: Develop a means of aggregating latitude and longitudee entires
        # Considering that the original essentially just uses some mathematical formula
        # that primarily takes advantage of the fact that each POI is converted
        # into some binary vector V, it might be fine to just avoid utilinzg
        # the `aggregate` function.

        # latitude/longitude entry? tuple (long, lat)


        """ 
            Explanation of OUE aggregate: 
                1. Initialize some variable `aggregated_data`, which simply represents
                the sum of all of the perturbed Grid() objects (which were transformed 
                into binary vectors in np) 
                2. Initialize `adjusted_data`, which is the value of the `aggregated_data`, ie 
                the sum of all the perturbed Grid() objects (which is something), which 
                is then simply transformed by 
            
        """
        return None
    def adjust(self) -> np.ndarray:

        # TODO 1: Analyze how adjustement works in LDPTrace
        # Adjustment is essentially just trasnforming the current aggregated
        # binary vectors into some unbiased value of the
        # TODO 2: Develop a means of adjusting the aggregated data
       return None

    def estimate(self, data) -> float:
      return None


'''
Changelog for GDPClient:
    TODOs:
        Step (1): Geospatial Discretization
        Step (2): Trend Analysis
            Step (2a): Trajectory Length Distributions
            Step (2b): Intra-Trajectory Mobility
            Step (2c): Beginning/Termination Points

'''

class GDPClient:  
    def __init__(self, epsilon, d, map_func):
        # TODO
        """
        Client-Side Geo-Indistinguishability

        This will differentiate itself from the original implementation
        utilizing the OUE protocol in the senes that
        """ 
        self.epsilon: float = epsilon
        self.d = d
        self.map_func = map_func

    def _perturb(self, epsilon, long, lat):
        # TODO
        '''
        _perturb()
        This is essentially the main implementation of the perturbation algorithm,
        ie, for this impelmentation, it will be the geo-indistinguishable implementation.

        In other words, this is essentially just the noise-adding mechanism that
        we are utilizing in order to actually perturb the data

        This is going to be based off of the addPolarNoise() function that has been adapted
        from the Andres et. al. paper.

        The perturbation technique that is being utilized is based off of the LaPlacian
        distribution.
        '''

        # Generating some random angle in [0, 2 * pi)
        theta = np.random.rand() * np.pi*2

        # Generating some random number in [0, 1)
        z = np.random.rand()

        r = inverseCumulativeGamma(epsilon, z)

        return addVectorToPos(long, lat, r, theta)


    def privatize(self, data):
        # TODO
        '''
        privatize(): This is essentially the function that is called
        whenever we want to actually perturb part of the trajectory
        '''

        # Option 1: Generate some random point within the Grid
        long, lat = data.sample_point()

        # Option 2: Let long, lat be the centers of the
        # area covered by the Grid() object `Grid.center_x` and `Grid.center_y`
        # long, lat = data.center_x, data.center_y
        return self._perturb(self.epsilon, long, lat)  # Returns the perturbed version of that coordinate point

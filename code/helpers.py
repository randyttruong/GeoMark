'''
helper.py

this is a file that contains helper functions for adding laplacian noise

randy truong
northwestern university (psu ml + cybersecurity reu)
'''

##################################################
#    Helper FUnctions for Perturbation           #
##################################################

# Global Variable: earth_radius

earth_radius = 6.3781e6
# Radians -> Degrees
def deg_of_rad(ang):
	return np.degrees(ang)

# Degrees -> Radians
def rad_of_deg(ang):
	return np.radians(ang)

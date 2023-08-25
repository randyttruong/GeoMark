# trajectory.py

from typing import List, Tuple
from grid import GridMap, Grid
import grid
import utils
import map_func
import numpy as np

def trajectory_point2grid(t: List[Tuple[float, float]], g: GridMap, interp=True):
    """
    Convert trajectory from raw points to grids
    :param t: raw trajectory Tuple[(x1, y1), (x2, y2)]
    :param g: grid map List[List[Grid]] <-> n x n matrix s.t. each row is a list of Grids
    :param interp: whether to interpolate
    :return: grid trajectory
    """
    grid_map = g.map # Accessing the actual map matrix within the GridMap() object
    grid_t = list() # Declare an empty list that will represent

    for p in range(len(t)):
        point = t[p] # We are finding the POI by simply enumerating the List of Tuples (ie, pair_0 and pair_1)
        found = False

        # Now, we must iterate through the GridMap() and check which Grid() objects,
        # ie, which geographical spaces represented the Grid()'s, that the
        # starting and ending points of a trajectory map to


        # Here, we are simply iterating through the GridMap().map
        for i in range(len(grid_map)):
            for j in range(len(grid_map[i])):

                # Now, for each Grid(), we are checking to see if the current points of the trajectory
                # actually map to that Grid() object (ie, does the point exist in the geographical space
                # that is represented by the Grid())?

                # If the point within the trajectory does actually map to the Grid() object,
                if grid_map[i][j].in_cell(point):

                # then we simply just append the Grid() object itself (and all of its
                # useful information, such as what geographical coordinates it actually covers
                # as well as its index within the GridMap()) to a List[Grid()], which simply now
                # represents a "coordinate" that is now defined simply by the Grid() index versus
                # an actual latitude and longitude

                    grid_t.append(grid_map[i][j])
                    found = True
                    break
            if found:
                break

    # Remove duplicates
    grid_t_new = [grid_t[0]]
    for i in range(1, len(grid_t)):
        if not grid_t[i].index == grid_t_new[-1].index:
            grid_t_new.append(grid_t[i])

    # Interpolation
    if interp:
        grid_t_final = list()
        for i in range(len(grid_t_new)-1):
            current_grid = grid_t_new[i]
            next_grid = grid_t_new[i+1]
            # Adjacent, no need to interpolate
            if grid.is_adjacent_grids(current_grid, next_grid):
                grid_t_final.append(current_grid)
            else:
                # Result of find_shortest_path() doesn't include the end point
                grid_t_final.extend(g.find_shortest_path(current_grid, next_grid))

        grid_t_final.append(grid_t_new[-1])
        return grid_t_final

    return grid_t_new # grid_t_new is type List[Grid]


def trajectory_grid2points(g_t: List[Grid]):
    if len(g_t) == 1:
        return [g_t[0].sample_point() for _ in range(2)]
    return [g.sample_point() for g in g_t]

def pass_through(t: List[Grid], g: Grid):
    for t_g in t:
        if t_g.index == g.index:
            return True

    return False


def get_diameter(t: List[Tuple[float, float]]):
    max_d = 0
    for i in range(len(t)):
        for j in range(i+1, len(t)):
            max_d = max(max_d, utils.euclidean_distance(t[i], t[j]))

    return max_d


def get_travel_distance(t: List[Tuple[float, float]]):
    dist = 0
    for i in range(len(t) - 1):
        curr_p = t[i]
        next_p = t[i+1]
        dist += utils.euclidean_distance(curr_p, next_p)

    return dist

def get_travel_angle(t: List[Tuple[float, float]]):


def get_real_markov(grid_db: List[List[Grid]], grid_map: GridMap):
    markov_vec = np.zeros(grid_map.size * 8)
    for t in grid_db:
        for i in range(len(t) - 1):
            curr_grid = t[i]
            next_grid = t[i + 1]
            map_id = map_func.adjacent_pair_grid_map_func((curr_grid, next_grid), grid_map)
            markov_vec[map_id] += 1

    return markov_vec

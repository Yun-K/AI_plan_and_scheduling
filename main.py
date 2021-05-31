
from Fring import Fringe
import utility as utility
import loader as loader
import numpy as np
import queue


def main():
    # Paths to the data and solution files.
    vrp_file = "data/n32-k5.vrp"  # "data/n80-k10.vrp"
    sol_file = "data/n32-k5.sol"  # "data/n80-k10.sol"

    # vrp_file = "data/n80-k10.vrp"
    # sol_file = "data/n80-k10.sol"

    # Loading the VRP data file.
    px, py, demand, capacity, depot = loader.load_data(vrp_file)

    # Displaying to console the distance and visualizing the optimal VRP solution.
    vrp_best_sol = loader.load_solution(sol_file)
    best_distance = utility.calculate_total_distance(
        vrp_best_sol, px, py, depot)
    print("Best VRP Distance:", best_distance)
    utility.visualise_solution(vrp_best_sol, px, py, depot, "Optimal Solution")

    # Executing and visualizing the nearest neighbour VRP heuristic.
    # Uncomment it to do your assignment!

    nnh_solution = nearest_neighbour_heuristic(px, py, demand, capacity, depot)
    nnh_distance = utility.calculate_total_distance(
        nnh_solution, px, py, depot)
    print("Nearest Neighbour VRP Heuristic Distance:", nnh_distance)
    utility.visualise_solution(
        nnh_solution, px, py, depot, "Nearest Neighbour Heuristic")

    # Executing and visualizing the saving VRP heuristic.
    # Uncomment it to do your assignment!

    sh_solution = savings_heuristic(px, py, demand, capacity, depot)
    # sh_distance = utility.calculate_total_distance(sh_solution, px, py, depot)
    # print("Saving VRP Heuristic Distance:", sh_distance)
    # utility.visualise_solution(sh_solution, px, py, depot, "Savings Heuristic")


def nearest_neighbour_heuristic(px, py, demand, capacity, depot):
    """
    Algorithm for the nearest neighbour heuristic to generate VRP solutions.

    :param px: List of X coordinates for each node.
    :param py: List of Y coordinates for each node.
    :param demand: List of each nodes demand.
    :param capacity: Vehicle carrying capacity.
    :param depot: Depot.
    :return: List of vehicle routes (tours).
    """

    # TODO - Implement the Nearest Neighbour Heuristic to generate VRP solutions.
    routesToReturn = []  # list of routes to return
    # startNode = depot  # start at the depot node

    # step 1: Initialisea solution: a route starting from the depot
    # initial set up the list with out the depot node
    node_list = []
    for i in range(1, len(px)):  # discount 0
        node_list.append(i)

    # loop until all nodes are visited
    while len(node_list) > 0:
        startNode = depot  # each route start at the depot node
        visited_invalid_Nodes = []
        temp_route = []
        # loop through all nodes to find a route until no feasible node is found for the current route
        for time in range(len(node_list)):
            node_id_index = -1  # index of the nearest node of current start node
            nearest_distance = 9999999999999999
            # loop through all unvisited nodes to find the feasible node
            for node in node_list:
                # check if it is the feasible node
                if node == startNode or node == depot or node in visited_invalid_Nodes:
                    continue
                # check if current node is nearest
                if nearest_distance > utility.calculate_euclidean_distance(
                        px, py, startNode, node):
                    node_id_index = node
                    nearest_distance = utility.calculate_euclidean_distance(
                        px, py, startNode, node)

            if node_id_index == -1:
                break  # close the current route since every node are not feasible

            # calculate the total demand of all nodes that are in the route
            total_route_demand = demand[node_id_index]
            for existNode in temp_route:
                total_route_demand += demand[existNode]

            # check whether the total demand of the route doesn't exceed the capacity
            if total_route_demand > capacity:
                visited_invalid_Nodes.append(node_id_index)
            # not exceed, append the node to the route,
            else:
                temp_route.append(node_id_index)
                startNode = node_id_index
                node_list.remove(node_id_index)

        # finish current route, so append the current route to the route to return list
        routesToReturn.append(temp_route)

    return routesToReturn


def savings_heuristic(px, py, demand, capacity, depot):
    """
    Algorithm for Implementing the savings heuristic to generate VRP solutions.

    :param px: List of X coordinates for each node.
    :param py: List of Y coordinates for each node.
    :param demand: List of each nodes demand.
    :param capacity: Vehicle carrying capacity.
    :param depot: Depot.
    :return: List of vehicle routes (tours).
    """

    # TODO - Implement the Saving Heuristic to generate VRP solutions.
    routes_to_return = []

    # first, do the initiial set up
    node_list = []
    for i in range(1, len(px)):  # discount index 0
        node_list.append(i)

    # initialise routes (depot->node->depot) for each node except depot node
    # each element represent the list of nodes(i.e. routes)
    initial_routes_forest = []
    for i in node_list:
        if i == depot:
            continue
        else:
            initial_routes_forest.append([i])

    #
    fringeQueue = queue.PriorityQueue()
    for i in initial_routes_forest:
        for j in initial_routes_forest:
            if i == j:
                continue
            else:
                fringeQueue.put(
                    (Fringe(i, j, get_saving_cost_for_mergeRoutes(px, py, i, j, depot))))

    while fringeQueue:
        t=fringeQueue.get()
        print(t)
    # in python, the key can not be list,so the associated saving cost value can not be set,use the PriorityQueue instead, which is at top
    # merge_savingCost_map = {}  # the java map, map each merge to it's saving cost

    # the Algorithm lookes like one of the Minimum Spanning Tree
    # loop until there is only one route left
    # while len(initial_routes_forest) > 1:
    #     for

    return routes_to_return


# def get_eachMerge_to_savingCost_map(px, py,  depot):
#     """Return the map that map each possible merge to it's saving cost.
#     The key of the map is [node1,node2], and the value is the saving cost

#     Args:
#         px ([type]): [description]
#         py ([type]): [description]
#         depot ([type]): [description]

#     Returns:
#         [type]: [description]
#     """

#     merge_savingCost_map = {}

#     return merge_savingCost_map


def get_saving_cost_for_mergeRoutes(px, py, node1_from_route1, node2_from_route2, depot):
    """calculate and return the saving cost from node1_from_route1 and node2_from_route2.
        Formular:
            savings(node1,node2) = L(node1,depot)+L(node2,depot)-L(node1,node2)
    Args:
        px: list of x coordinates for each node.
        py: list of y coordinates for each node
        node1_from_route1 (node): the last non-depot node index of route 1
        node2_from_route2 (node): the first non-depot node of route 2
        depot (node): the depot node

    Returns:
        float: the saving cost from node1_from_route1 and node2_from_route2.
    """
    cost1 = utility.calculate_euclidean_distance(
        px, py, node1_from_route1, depot)

    cost2 = utility.calculate_euclidean_distance(
        px, py, node2_from_route2, depot)

    cost3 = utility.calculate_euclidean_distance(
        px, py, node1_from_route1, node2_from_route2)

    return (cost1+cost2-cost3)


if __name__ == '__main__':
    main()

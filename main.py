import utility as utility
import loader as loader
import numpy as np


def main():
    # temp =[]`
    # for i in temp:
    #     print(i)

    # if 1==1:
    #     print("finished:")
    #     return`

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

    # nnh_solution = nearest_neighbour_heuristic(px, py, demand, capacity, depot)
    # nnh_distance = utility.calculate_total_distance(nnh_solution, px, py, depot)
    # print("Nearest Neighbour VRP Heuristic Distance:", nnh_distance)
    # utility.visualise_solution(nnh_solution, px, py, depot, "Nearest Neighbour Heuristic")

    # Executing and visualizing the saving VRP heuristic.
    # Uncomment it to do your assignment!

    # sh_solution = savings_heuristic(px, py, demand, capacity, depot)
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

    # step 1: Initialisea solution: a route starting from the depot
    routesToReturn = []  # list of routes to return
    startNode = depot  # start at the depot node
    currentDemand = 0
    ids = np.arrange(len(px))
    ids.remove(0)  # remove the depot node

    totalDemandRoute = 0
    # loop until all nodes are visited
    while len(ids) > 0:
        visited_invalid_Nodes = []
        # 
        for time in range(len(ids)):
            nearest_distance = 999999999999999999999999
            index = -1  # index of the nearest node of current start node
            # loop through all unvisited nodes to find the feasible node
            for i in ids:
                # check if it is the feasible node
                if i == startNode or i == depot or i in visited_invalid_Nodes:
                    continue
                # check if current node is nearest
                if nearest_distance > utility.calculate_euclidean_distance(
                        px, py, startNode, i):
                    index = i
                    nearest_distance = utility.calculate_euclidean_distance(
                        px, py, startNode, i)

            if index == -1:
                break  # break it since every node has visited

            # check whether the total demand of the route doesn't exceed the capacity
            totalDemandRoute += demand[index]
            if totalDemandRoute > capacity:
                visited_invalid_Nodes.append(index)

        # After inserting the node, the total demand of the route does not exceed the capacity
        # 3.If no feasible node is found for the current route, then close the current route (return to the depot)and create a new route starting from the depot4.Repeat 2. and 3. until all nodes are visited

    # while

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

    return None


if __name__ == '__main__':
    main()

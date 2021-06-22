# Description：
The topic of this assignment is Planning and Scheduling, the code part which is aiming for solving the _VRP problem_ which is samiliar as the Travelling Salesman Problem(aka TSP).

# Brief Explaniation of VRP：
In this assignment, there are lots of nodes, one node represents the depot, others are all the client nodes, and each client node has a demand value. The purpose is try to find the nearest routes that can deliver goods to satisfy all clients.

For example, I am a delivery boy, and my today job is to deliver goods to list of clients. Therefore, I want to find nearest routes in order to finish the job as quick as possible(i.e. output is list of routes).

However, the car that I use to store goods has the capcatity and the demand of each client node is different. Which means for each route, the goods(demands) can not higher than the car's capcatity, and after all goods are delieved, i need to go back to the depot node to get more goods in order to start a new route to deliver remaning goods to customers, until all clients receive their goods.

Since in real world, to find the optimal solution is time consuming, and we dont have that time, so in this assignment, 2 heuristic algorithms are demonstrated and can find the Local Optimal Solution within the short time.

* How to start

The handout pdf is the stuff that you need to work on with.
In Provided directory, you can get the data and the template code.
Slides may help you to know what to do

It is my first time to type Python, so there might be a better encoding way
to implement the algorthim. My nearest-neighbour heurstic should be the model
answer, but the saving heurstic is not since others got the better result
than me. In sampleoutput.txt, i put the correct output from others which is
the expected output. If you can achieve this expected output, please let me know,
thanks.

# Expected answer for n32-k5 data file:
Best VRP Distance: 787.8082774366646 <p>
Nearest Neighbour VRP Heuristic Distance: 1146.399631725379<p>
Saving VRP Heuristic Distance: 843.6881693466269

# My Marks
  ![image](https://user-images.githubusercontent.com/53819808/122906169-71018180-d384-11eb-8282-b1e4edd46f09.png)

# How to run my program:
This is a python3 program, so:<p>
First, use cd command to go to my folder<p>
And then, run the following command:<p>
python3 main.py

<p>or<p>
python main.py

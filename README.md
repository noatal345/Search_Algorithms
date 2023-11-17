# Search_Algorithms  
This project uses different kinds of search algorithms to find the shortest path from a source node to a target node on a map of Israel.  
  
## Files:  
The db folder contains a CSV file of the map of Israel.  
The ways directory (obtained from the internet) was used in this project.  
The rest of the code is Python files.  
  
## Running the Code:  
To run the code, open your terminal and navigate to the directory containing the project files. Then, you can run the following commands:  

***python stats.py:***  
Displays statistical data regarding the number of intersections, roads, their type, etc.  

***python main.py ucs source target:***  
Runs the uniform cost search algorithm to find the shortest path from the source junction to the target junction.  

***python main.py astar source target:***  
Runs the A* search algorithm to find the shortest path from the source junction to the target junction.  

***python main.py idastar source target:***  
Runs the iterative deepening A* search algorithm to find the shortest path from the source junction to the target junction.  

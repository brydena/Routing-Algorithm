# Routing-Algorithm
The routing algorithm function requires inputs of a data file of node positions and length, initial node and final node in that order. The call required is of the form:
python RoutingAlgorithm.py exmouth-links.dat J1001 J1032
This will return the minimum route length, the route taken and the time taken to compute this, assuming there is a path, otherwise the user wil be notified that no route exists between the two input nodes.

Both numpy and pandas libraries are required to run this program, the installation of these will depend on the means by which the user is attempting to run the program.

The algorithm used is Dijkstra's algorithm (https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm). 

Test cases I have run include:

python.exe C:\\Users\\ABryden\\Documents\\Programming\\Python\\RoutingAlgorithm.py C:\\Users\\ABryden\\Documents\\Programming\\Python\\exmouth-links.dat J1001 J1032

The minimum route from J1001 to J1032 is: [361.]
The route taken is: ['J1001 J1031 J1022 J1008 J1032']
The time taken is: 0.17183446884155273

python.exe C:\\Users\\ABryden\\Documents\\Programming\\Python\\RoutingAlgorithm.py C:\\Users\\ABryden\\Documents\\Programming\\Python\\exmouth-links.dat J1001 X1039

The minimum route from J1001 to X1039 is: [8536.]
The route taken is: ['J1001 J1002 J1019 J1020 J1021 J1029 J1033 J1034 J1035 J1036 J1038 X1039']
The time taken is: 2.015185832977295

C:\Users\ABryden>python.exe C:\\Users\\ABryden\\Documents\\Programming\\Python\\RoutingAlgorithm.py C:\\Users\\ABryden\\Documents\\Programming\\Python\\exmouth-links.dat J1001 X10399

There is no route between J1001 and X10399

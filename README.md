# CS202 Project: Maximal Bipartite Matching

## Team:
* Vishnu Namboodiri K S
* Thejas S
* Shrishti Barethiya


## Some Important Notes
*Executing the program
  * Clone the repo and run the main function, or
  * Run combined.py
* Dependencies
  * python3
  * A Computer
* Input is given as a `data.csv` adjacency matrix file, already demarcated into two: Candidates and Jobs, say.
* IMPORTANT: The first cell ([0][0]) of the data.csv file _has_ to be "Hello". We used a regex search to delete that element.
  

## Classes
* Graph class
  * `nodes`: array of Node objects
  * `row_length` and `column_length`: self explanatory
  * `u` and `v`: the graph is divided into these two during maximal matching
* Node class
  * `name` duh
  * `adj`: array of _indices_ of adjacent nodes in the `nodes` array
  * `seen`: dunno why
  * `match`: int, _index_ of the matched Node


## The Algorithm

>We use the method of looking for augmenting paths and augmenting them till no more such paths remain.

* The algorithm first divides the graph into two, _u_ and _v_
* For every element in `u`, a DFS traversal is made (`path_finder`)
* The `path_finder` keeps zig-zagging from u to v (such that v->u is matched) till it reaches an unmatched `v` node.
* Then it augments the path it just traversed
* `path_finder` (Pseudocode? No.): 
  * Reaches a node:
  * if the node is in u
    * if the node is not connected to anything
      * `path_finder(random_adjacent_node)`
    * else if the node is connected to something in `v`
      * look for another node in `v` to which it isn't connected and DFS to that node
  * if the node is in v
    * if the node is not connected to anything 
      * it's the end of the augmenting path, augments the path it traversed
    * if the node in v is connected to something in `u`
      * DFS to that

## Usage

The program takes input as a data.csv adjacency matrix like so:

|         |          |          |        |         | 
|---------|----------|----------|--------|---------| 
| Hello   | Scranton | Basement | Nashua | Cornell | 
| Michael | 1        | 0        | 1      | 0       | 
| Pam     | 1        | 0        | 0      | 0       | 
| Daryll  | 1        | 1        | 0      | 0       | 
| Andy    | 1        | 1        | 1      | 1       | 


The output is given out to the terminal, and as an output.csv file with the applicants (say) against the occupation, like so:

|         |          | 
|---------|----------| 
| Michael | Nashua   | 
| Pam     | Scranton | 
| Daryll  | Basement | 
| Andy    | Cornell  | 


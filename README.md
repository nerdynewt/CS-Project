# CS202 Project: Maximal Bipartite Matching

## Team
* Vishnu Namboodiri K S
* Thejas S
* Shrishti Barethiya

## Overview
* The program

## Important Notes
* Clone the repo and run the main function, or run combined.py
* The first cell ([0][0]) of the data.csv _has_ to be "Hello". We use a regex to delete that element.

## The Algorithm
We use the method of looking for augmenting paths and augmenting them till no more such paths remain.

## Interaction

The program takes input as a data.csv adjacency matrix like so:

|                                            | 
|--------------------------------------------| 
| Hello, Scranton, Basement, Nashua, Cornell | 
| Michael, 1, 0, 1, 0                        | 
| Pam, 1, 0, 0, 0                            | 
| Daryll, 1, 1, 0, 0                         | 
| Andy, 1, 1,  1, 1                          | 

The output is given out to the terminal, and as an output.csv file with the applicants (say) against the occupation.

* The program takes inputs like so:

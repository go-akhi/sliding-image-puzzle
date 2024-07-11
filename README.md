#!WORK IN PROGRESS!#

# 3x3 Sliding image puzzle solver<br />
To solve a 3x3 sliding image puzzle, the image is divided into, as the name implies, 9 square boxes and shuffled, forming a 3x3 grid and one of the blocks is removes from the grid so that any one of the two neighbouring tiles of the one that was removed, can be moved into the space created by removing that tile. Any of the two neighbouring tiles of any empty space can move into that space and by doing so, the goal is to arrange the tiles to restore the image to its true state, minus the tile that was removed. 

## Algorithm
One way to solve a 3x3 puzzle is to: 

1. Arrange the top row
2. Arrange the leftmost column
3. Arrange the remaining tiles

There are a few more things to keep in mind,

- A number of tile that form a chain can be moved like a train as the trailing tile occpuies the space left behind by the one in front. This movement comes in as the tiles of the top row can be connected elsewhere and "transported" to the first row. 
- It is in the interest of solving the puzzle to not break the chain of 3 tiles for the first row and the pair of tiles for the second row, once formed. 
- Once the chains are formed, an approach for transporting the chain should be decided upon. if the top row is being filled in from the rightmost side, ie the "train" would be coming in from the right, the tile belonging to (1,1) should be at the head of the chain, if the train is coming in from the left, at the head of the train should be the tile belonging to (1,3). Similarly for the first column, at the head should be the tile belonging to (3,1) if filling in from the top and the tile belonging to (2,1) if filling in from the bottom. 

## Representation
The puzzle can be represented in a number of ways. An 8 variable system, a list of lists or a numpy array had been considered but in order to represent the chain that needs to move together, a multigraph with different weights for the edges was picked to represent the puzzle board. 
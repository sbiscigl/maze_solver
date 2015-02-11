"""
implimentation of the driver file for the program
"""

from maze_io import parse_maze_file
from maze_io import print_maze
from maze_class import maze
from maze_logic import solve_maze

"""
apparently python doesnt handle recursion well
"""
import sys

def main():
	print "Program starting";
	sys.setrecursionlimit(18000);
	print "Reading in maze file"
	filename = 'test_maze.xml';
	a_maze = parse_maze_file(filename);
	a_maze.error_input_check();
	print "OK"

	print "The maze: "
	print_maze(a_maze);

	print "attempting to solve maze"
	solution = solve_maze(a_maze);
	print "OK"

	print "solution steps :"
	for i in solution:
		print '(' + str(i[1]) + ', ' + str(i[0]) + ')';

	print "program ending"



if __name__ == '__main__':
	main();

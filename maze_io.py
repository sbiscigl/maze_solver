"""
this file ipliments reading in maze files
as well as printing them
"""

"""import our maze class file"""
from maze_class import maze

"""
import xml parsing libraries to pass
the xml file for the maze data
"""
from xml.dom import minidom

"""import system writing libraries for error check"""
import sys

"""
parse the xml file and returning a
maze object
"""
debug = 0;

def print_maze(the_maze):
	for i in the_maze.maze_arry:
		sys.stdout.write('\n');
		for j in i:
			sys.stdout.write(str(j));
	sys.stdout.write('\n');

def parse_maze_file(filename):
	mazedoc = minidom.parse(filename);
	maze_element = mazedoc.getElementsByTagName('maze')[0];

	"""
	extract files into temporary variables to then use
	to create a maze object
	"""
	if debug == 1:
		print maze_element;

	dimension_x_tag = maze_element.getElementsByTagName('dimx');
	dimensionx = int(dimension_x_tag[0].attributes['value'].value);

	if debug == 1:
		print 'dimension x : ' + str(dimensionx);

	dimension_y_tag = maze_element.getElementsByTagName('dimy');
	dimensiony = int(dimension_y_tag[0].attributes['value'].value);

	if debug == 1:
		print 'dimension y : ' + str(dimensiony);

	player_x_tag = maze_element.getElementsByTagName('playerx');
	playerx = int(player_x_tag[0].attributes['value'].value);

	if debug == 1:
		print 'player x : ' + str(playerx);

	player_y_tag = maze_element.getElementsByTagName('playery');
	playery = int(player_y_tag[0].attributes['value'].value);

	if debug == 1:
		print 'player y : ' + str(playery);

	end_x_tag = maze_element.getElementsByTagName('endx');
	endx = int(end_x_tag[0].attributes['value'].value);

	if debug == 1:
		print 'end x : ' + str(playerx);

	end_y_tag = maze_element.getElementsByTagName('endy');
	endy = int(end_y_tag[0].attributes['value'].value);

	if debug == 1:
		print 'end y : ' + str(playery);

	"""read in array for the wall segments"""
	walls_loc = maze_element.getElementsByTagName('walls');
	wall_list = walls_loc[0].getElementsByTagName('wall');

	wall_coordinates = []

	for i in wall_list:
		wall_coordinates.append((
								int(i.getElementsByTagName('x')[0].attributes['value'].value),
								int(i.getElementsByTagName('y')[0].attributes['value'].value)
								));
	if debug == 1:
		print wall_coordinates;

	my_maze = maze(dimensionx, dimensiony, playerx-1, playery-1, endx-1, endy-1);

	if debug == 1:
		print_maze(my_maze);

	"""
	call function to put the correct walls into the array
	"""
	my_maze.make_walls(wall_coordinates);

	if debug == 1:
		print_maze(my_maze);


	"""
	check to make sure the beginning and end are
	int the right place
	"""
	if debug == 1:
		my_maze.maze_arry[playerx-1][playery-1] = 'B';
		my_maze.maze_arry[endx-1][endy-1] = 'E';
		print_maze(my_maze);

	return my_maze;


def main():
	print "test driver";
	filename = 'test_maze.xml';
	a_maze = parse_maze_file(filename);
	a_maze.error_input_check();
	print "OK";


if __name__ == '__main__':
	print "you should not see this unless testing"
	debug = 1;
	main();
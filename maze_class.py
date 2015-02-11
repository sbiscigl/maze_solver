"""
this file will imliment the maze object
that will be used when solving it
"""

"""
class that will be our maze object
"""
class maze(object):
    """constructor/declare local data member"""
    def __init__(self, dimx, dimy, plx, ply, enx, eny):
        self.player_x   = plx; 
        self.player_y   = ply; 
        self.end_x      = enx;
        self.end_y      = eny;
        self.dimx       = dimx;
        self.dimy       = dimy;

        """make matrix array the size of dimx and dimy"""
        self.maze_arry = [[0 for x in range(dimx)] for x in range(dimy)]; 

    """mutatators"""
    """gets"""
    def get_player_x(self):
        return self.player_x;

    def get_player_y(self):
        return self.player_y;

    def get_end_x(self):
        return self.end_x;

    def get_end_y(self):
        return self.end_y;

    def get_dimx(self):
        return self.dimx;

    def get_dimy(self):
        return self.dimy;

    def get_maze_arry(self):
        return self.maze_arry;

    def get_maze_array_element(self, x, y):
        if(x < 0 or x > self.dimx or y < 0 or y > self.dimy):
            print "throw some sort of error"

        return self.maze_arry[x][y];

    """sets"""
    def set_player_x(self, plx):
        self.player_x = plx;

    def set_player_y(self, ply):
        self.player_y = ply;

    def set_end_x(self, endx):
        self.end_x = endx;

    def set_end_y(self, endy):
        self.end_y = endy;

    def set_dimx(self, dimex):
        self.dimx = dimex;

    def set_dimy(self, dimey):
        self.dimy = dimey;

    def set_maze_arry(self, maze_arry):
        self.maze_arry = maze_arry;

    def set_maze_array_element(self, x, y, value):
        if(x < 0 or x > self.dimx or y < 0 or y > self.dimy):
            print "throw some sort of error"

        self.maze_arry[x][y] = value;

    """
    define a function that will go through the maze array and
    "create walls" where the maze file specified
    """
    def make_walls(self, wall_list):
        for i in wall_list:
            self.maze_arry[i[1]-1][i[0]-1] = 1;



    """error check input function"""
    """do not allow any erronous inputs to be allowed"""
    def error_input_check(self):
        """check case for user poition outside the maze itself"""
        if(self.player_x < 0 or self.player_x > self.dimx or self.player_y < 0 or self.player_y > self.dimy):
            print "this should throw some kind of error";

        """error check for end positioning"""
        if(self.end_x < 0 or self.end_x > self.dimx or self.end_y < 0 or self.end_y > self.dimy):
            print "this should throw some kind of error";

        """error check to see if player is in a wall segment"""
        if (self.maze_arry[self.player_x][self.player_y] == 1):
            print "this should throw some kind of error";

        """error to check to see if the end is in a wall"""
        if (self.maze_arry[self.end_x][self.end_y] == 1):
            print "this should throw some kind of error";

if __name__ == '__main__':
	print "you should not see this unless testing"
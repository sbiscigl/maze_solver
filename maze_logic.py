"""
the file that impliments that logic
that will recursively solve the maze
"""
from maze_class import maze

def solve_maze_recur(moves, x,y, a_maze):
    """
    error check move
    """
    if( x < 0 or x > a_maze.dimx-1 or y < 0 or y > a_maze.dimy-1):
        """the player is outside the play area"""
        return False;

    if( x == a_maze.end_x and y == a_maze.end_y):
        """the player has reached the end"""
        moves.append((x,y));
        return True;

    if( a_maze.maze_arry[x][y] == 1):
        """we have hit a maze wall"""
        return False;

    if( (x,y) in moves):
        return False;

    """we know we have made  valid move"""
    moves.append((x,y));
    #print moves
    """now we call it recursively to find the solution"""
    """UP"""
    if((solve_maze_recur(moves,x,y-1, a_maze)) == True):
        return True;
    """RIGHT"""
    if((solve_maze_recur(moves,x+1,y, a_maze)) == True):
        return True;
    """DOWN"""
    if((solve_maze_recur(moves,x,y+1, a_maze)) == True):
        return True;
    """LEFT"""
    if((solve_maze_recur(moves,x-1,y, a_maze)) == True):
        return True;
    moves.pop();
    return False;



def solve_maze(the_maze):
    moves = []
    solve_maze_recur(moves, the_maze.player_x, the_maze.player_y, the_maze);
    return moves;



if __name__ == '__main__':
    print "you should not see this unless testing"
import pytest
# import toy_robot as tr
from toy_robot import classes_methods as trcm


# @pytest.fixture
# class test_toy_robot(object):
    
@pytest.mark.parametrize("test_grid_size, x_coord, y_coord, test_direction, expected_dir", 
                         [([3,3], 1, 2, 'NORTH', 'NORTH'),
                          ([3,3], 2, 2, 'SOUTH', 'SOUTH')])
def test_robo_placement(test_grid_size, x_coord, y_coord, test_direction, expected_dir):
    robo_obj = trcm.Robot_Direction_Position(grid_size=test_grid_size, 
                                             x=x_coord, 
                                             y=y_coord, 
                                             direction=test_direction)
    assert robo_obj.direction == expected_dir
    
    
# Test for checking the direction on RIGHT rotate
@pytest.mark.parametrize("init_dir, rotate, expected_dir", 
                         [('NORTH', 'RIGHT', 'EAST'),
                          ('EAST', 'RIGHT', 'SOUTH'),
                          ('SOUTH', 'RIGHT', 'WEST'),                          
                          ('WEST', 'LEFT', 'SOUTH'),
                          ('WEST', 'RIGHT', 'NORTH'),
                          ('EAST', 'LEFT', 'NORTH'),
                          ('EAST', 'RIGHT', 'SOUTH'),
                          ('EAST', 'RIGHT', 'SOUTH')])
def test_robo_rotate(init_dir, rotate, expected_dir):
    robo_obj = trcm.Robot_Direction_Position(direction=init_dir)
    robo_obj.robo_position(rotate)
    _, _, curr_dir = robo_obj.report()
    
    assert curr_dir == expected_dir
        
    
# Test the robot movement and check the final position     
@pytest.mark.parametrize("test_grid_size, x_coord, y_coord, init_direction, rotate_move, final_pos",
                         [([5, 9], 2, 5, 'NORTH', 'RIGHT', [2, 5, 'EAST']),
                          ([5, 9], 5, 9, 'EAST', 'RIGHT', [5, 9, 'SOUTH']),
                          ([5, 9], 5, 9, 'EAST', 'MOVE', [5, 9, 'EAST'])])
  
def test_robo_move(test_grid_size, x_coord, y_coord, init_direction, rotate_move, final_pos):
    robo_obj = trcm.Robot_Direction_Position(grid_size=test_grid_size, 
                                             x=x_coord, 
                                             y=y_coord, 
                                             direction=init_direction)

    if rotate_move == 'MOVE':
        robo_obj.robo_move()
        x, y, curr_dir = robo_obj.report()
    else:
        robo_obj.robo_position(rotate_move)
        x, y, curr_dir = robo_obj.report()
        
    assert [x, y, curr_dir] == final_pos
   
if __name__ == "__main__":
    pytest.main()
    
    
    
    
    
    
    
    
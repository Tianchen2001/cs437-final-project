import picar_4wd as fc
import numpy as np

from utils import *

class ParkingSystem:
    def __init__(self, num_parking_slots=6, center_width=2):
        self.num_rows, self.num_cols = num_parking_slots // 2, center_width + 2
        
        self.parking_lot_map = np.zeros((self.num_rows, self.num_cols))
        self.parking_lot_map[1:self.num_rows-1, 1:self.num_cols-1] = 1
        
        self.current_slot = None
        self.current_pos = (self.num_rows - 1, self.num_cols // 2)
        self.current_dir = 0
    
    def move_to(self, target_slot):
        if self.current_slot == target_slot:
            return
        
        target_pos = None
        if target_slot is None:
            target_pos = (self.num_rows - 1, self.num_cols // 2)
        else:
            target_pos = self._get_pos_by_slot(target_slot)
        
        curr_dir = navigate(self.parking_lot_map, self.current_pos, target_pos, self.current_dir)
        
        self.current_slot = target_slot
        self.current_pos = target_pos
        self.current_dir = curr_dir
    
    def _forward_in(self):
        if self.current_slot > 3:
            target_dir = 0
        else:
            target_dir = 2
        
        for i in range((target_dir - self.current_dir) % 4):
            turn_left()
        move_forward()
        fc.stop()
        
        self.current_dir = target_dir
    
    def _back_out(self, slot):
        if self.current_slot > 3:
            target_dir = 2
        else:
            target_dir = 0
        
        move_backward()
        for i in range((target_dir - self.current_dir) % 4):
            turn_left()
        fc.stop()
        
        self.current_dir = target_dir

    def _track_line(self):
        gs_list = fc.get_grayscale_list()
        if fc.get_line_status(50,gs_list) == 0:
            fc.forward(Track_line_speed)
        elif fc.get_line_status(50,gs_list) == -1:
            fc.turn_left(Track_line_speed)
        elif fc.get_line_status(50,gs_list) == 1:
            fc.turn_right(Track_line_speed)
        
    def _get_pos_by_slot(self, slot):
        return (slot - 1) % 3, self.num_cols - 1 if slot > 3 else 0
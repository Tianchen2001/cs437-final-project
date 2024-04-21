# import picar_4wd as fc
import numpy as np

from utils import navigate

class ParkingSystem:
    def __init__(self, num_parking_slots=10, center_width=9):
        self.num_rows, self.num_cols = num_parking_slots // 2, center_width + 2
        
        self.parking_lot_map = np.zeros((self.num_rows, self.num_cols))
        self.parking_lot_map[1:self.num_rows-1, 1:self.num_cols-1] = 1
        
        self.current_slot = None
        self.current_pos = (self.num_rows - 1, self.num_cols // 2)
    
    def move_to(self, target_slot):
        if self.current_slot == target_slot:
            return
        
        target_pos = None
        if target_slot is None:
            target_pos = (self.num_rows - 1, self.num_cols // 2)
        else:
            target_pos = self._get_pos_by_slot(target_slot)
        print(target_pos, self.parking_lot_map[target_pos])
        
        '''
            TODO: Implement path planning algorithm.
            The car moves counter-clockwise around the parking lot.
            Whenever the car reaches the target slot, it stops and turns right to do a head-in parking.
            The scenario also applies when the car is exiting the parking lot.
        '''
        navigate(self.parking_lot_map, self.current_pos, target_pos)
        
        self.current_slot = target_slot
        self.current_pos = target_pos
        
    def _get_pos_by_slot(self, slot):
        return (slot - 1) % 5, self.num_cols - 1 if slot > 5 else 0
import picar_4wd as fc

import heapq
import time

def navigate(nav_map, start_pos, end_pos):
    path_list = astar(nav_map, start_pos, end_pos)
    print(path_list)
    pass

def astar(nav_map, start_pos, end_pos):
    open_list = [(0, start_pos)]
    cost_dict = {start_pos: 0}
    parent_dict = {start_pos: None}

    while open_list:
        _, curr_pos = heapq.heappop(open_list)
        if curr_pos == end_pos:
            break
        
        children = get_children(curr_pos, nav_map)
        for child in children:
            curr_cost = cost_dict[curr_pos] + 1
            if child not in cost_dict or cost_dict[child] > curr_cost:
                curr_f = curr_cost + get_distance(child, end_pos)
                heapq.heappush(open_list, (curr_f, child))
                cost_dict[child] = curr_cost
                parent_dict[child] = curr_pos
    
    path_list = []
    if end_pos in parent_dict:
        curr_pos = end_pos
        while curr_pos != start_pos:
            path_list.append(curr_pos)
            curr_pos = parent_dict[curr_pos]
        path_list.append(start_pos)
        path_list.reverse()
    
    return path_list

def get_children(pos, nav_map):
    x, y = pos

    children = []
    if x == 0:
        for child in [(x + 1, y), (x - 1, y), (x, y - 1)]:
            if 0 <= child[0] < nav_map.shape[0] and 0 <= child[1] < nav_map.shape[1] and nav_map[child] == 0:
                children.append(child)
    elif x == nav_map.shape[0] - 1:
        for child in [(x + 1, y), (x, y + 1), (x - 1, y)]:
            if 0 <= child[0] < nav_map.shape[0] and 0 <= child[1] < nav_map.shape[1] and nav_map[child] == 0:
                children.append(child)
    else:
        for child in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]:
            if 0 <= child[0] < nav_map.shape[0] and 0 <= child[1] < nav_map.shape[1] and nav_map[child] == 0:
                children.append(child)

    return children

def get_distance(pos, target):
    return abs(pos[0] - target[0]) + abs(pos[1] - target[1])

def turn_left():
    fc.turn_left(30)
    time.sleep(1.8)

def turn_right():
    fc.turn_right(30)
    time.sleep(1.8)

def move_forward():
    fc.forward(1)
    time.sleep(0.02)
    
def move_backward():
    fc.backward(1)
    time.sleep(0.02)

def stop():
    fc.stop()

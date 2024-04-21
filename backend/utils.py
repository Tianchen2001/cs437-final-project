import picar_4wd as fc

import heapq
import time

def navigate(nav_map, start_pos, end_pos, forward_dir):
    path_list = astar(nav_map, start_pos, end_pos)
    print(path_list)
    
    curr_dir = forward_dir
    prev_node = path_list[0]

    for idx in range(1, len(path_list)):
        curr_node = path_list[idx]
        if curr_dir == 0:
            if curr_node[1] - prev_node[1] == 1:
                print("move forward")
                move_forward()
            elif curr_node[0] - prev_node[0] == -1:
                print("turn left")
                turn_left()
                curr_dir = 1
                move_forward()
            elif curr_node[0] - prev_node[0] == 1:
                print("turn right")
                turn_right()
                curr_dir = 3
                move_forward()
        elif curr_dir == 1:
            if curr_node[0] - prev_node[0] == -1:
                print("move forward")
                move_forward()
            elif curr_node[1] - prev_node[1] == -1:
                print("turn left")
                turn_left()
                curr_dir = 2
                move_forward()
            elif curr_node[1] - prev_node[1] == 1:
                print("turn right")
                turn_right()
                curr_dir = 0
                move_forward()
        elif curr_dir == 2:
            if curr_node[1] - prev_node[1] == -1:
                print("move forward")
                move_forward()
            elif curr_node[0] - prev_node[0] == 1:
                print("turn left")
                turn_left()
                curr_dir = 3
                move_forward()
            elif curr_node[0] - prev_node[0] == -1:
                print("turn right")
                turn_right()
                curr_dir = 1
                move_forward()
        elif curr_dir == 3:
            if curr_node[0] - prev_node[0] == 1:
                print("move forward")
                move_forward()
            elif curr_node[1] - prev_node[1] == 1:
                print("turn left")
                turn_left()
                curr_dir = 0
                move_forward()
            elif curr_node[1] - prev_node[1] == -1:
                print("turn right")
                turn_right()
                curr_dir = 2
                move_forward()
        prev_node = curr_node
    
    fc.stop()

    return curr_dir

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
    elif y == 0:
        for child in [(x + 1, y), (x, y + 1), (x, y - 1)]:
            if 0 <= child[0] < nav_map.shape[0] and 0 <= child[1] < nav_map.shape[1] and nav_map[child] == 0:
                children.append(child)
    elif y == nav_map.shape[1] - 1:
        for child in [(x, y + 1), (x - 1, y), (x, y - 1)]:
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
    time.sleep(2)

def turn_right():
    fc.turn_right(30)
    time.sleep(2)

def move_forward():
    fc.forward(1)
    time.sleep(1.15)
    
def move_backward():
    fc.backward(1)
    time.sleep(1.15)
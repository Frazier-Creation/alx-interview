#!/usr/bin/python3
# 0-lockboxes.py
"Defines a function that determines if a box containing a list
   of lists can be opened using keys stored in the lists"


def canUnlockAll(boxes):
    # Set to keep track of the opened boxes
    opened_boxes = {0}
    
    # Queue to perform breadth-first search
    queue = [0]
    
    # Breadth-first search
    while queue:
        current_box = queue.pop(0)
        keys = boxes[current_box]
        
        for key in keys:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                queue.append(key)

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)


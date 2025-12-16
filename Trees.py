class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        # AVL nodes will need an additional balance factor or height attribute
        self.height_val = 0 # Or use this to store height directly for AVL

def get_node_height(node):
    if node is None:
        return -1
    # This might be calculated dynamically in BST or stored in AVL Node
    return max(get_node_height(node.left), get_node_height(node.right)) + 1
    # For AVL, you would access the precomputed height attribute:
    # return node.height_val

    import csv
from schedule_item import ScheduleItem

def load_schedule_data(filename, tree_instance):
    with open(filename, mode='r', newline='', encoding='utf8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Assuming ScheduleItem constructor handles the dictionary row appropriately
            item = ScheduleItem(**row)
            # Use a relevant key for storage (e.g., 'course_code' or 'CRN')
            tree_instance[item.course_code] = item 
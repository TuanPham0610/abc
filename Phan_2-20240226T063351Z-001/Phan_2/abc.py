print("Traạng thái ban đầu:#1 \nTrạng thái kết thúc:#7 \nKhông gian trạng thái:{#1,#2,#3,#4,#5,#6,#7} \nHành động:[a,b,c,d]")

from collections import deque

class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

def bfs(initial_state, goal_state):
    frontier = deque([Node(initial_state)])
    explored = set()
    
    while frontier:
        node = frontier.popleft()
        state = node.state
        
        if state == goal_state:
            return node
        
        explored.add(state)
        for action in get_actions(state):
            next_state = apply_action(state, action)
            if next_state not in explored:
                child = Node(next_state, node, action)
                frontier.append(child)
    
    return None

def get_actions(state):
    # Định nghĩa các hành động có thể thực hiện từ một trạng thái
    actions = []
    if state == "#1":
        actions.extend(["a", "b"])
    elif state == "#2":
        actions.extend(["a", "c"])
    elif state == "#3":
        actions.extend(["b", "d"])
    elif state == "#4":
        actions.extend(["c", "d"])
    elif state == "#5":
        actions.extend(["a", "b"])
    elif state == "#6":
        actions.extend(["a", "d"])
    elif state == "#7":
        actions.append("c")
    return actions

def apply_action(state, action):
    # Áp dụng hành động lên trạng thái hiện tại để đạt được trạng thái tiếp theo
    if action == "a":
        return "#5" if state == "#1" or state == "#2" else "#1"
    elif action == "b":
        return "#3" if state == "#1" or state == "#5" else "#1"
    elif action == "c":
        return "#2" if state == "#3" or state == "#4" else "#3"
    elif action == "d":
        return "#4" if state == "#3" or state == "#6" else "#6"

def convert_solution_to_actions(solution):
    # Chuyển đổi từ chuỗi giải pháp sang chuỗi hành động
    actions = []
    while solution.parent:
        actions.append(solution.action)
        solution = solution.parent
    actions.reverse()
    return actions

# Test
initial_state = int(input("Trạng thái ban đầu: "))
goal_state = int(input"Trạng thái kết thúc:")

solution_node = bfs(initial_state, goal_state)
if solution_node:
    solution_actions = convert_solution_to_actions(solution_node)
    print("Chuỗi hành động để đạt được trạng thái đích:")
    print(solution_actions)
else:
    print("Không tìm thấy giải pháp.")
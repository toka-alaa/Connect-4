def available_actions(self, current_state):
    actions = []
    player = self.current_player(current_state)
    
    for col in range(7):
        if current_state[0][col] is not Null:
            continue
        for row in range(5, -1, -1):
            if current_state[row][col] == NULL:
                actions.append((player, row, col))
                break
    
    return actions

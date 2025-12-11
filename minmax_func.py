def MinMax(self, current_state):
        terminal = self.check_terminal(current_state)
        if terminal != "Not terminal":
            if terminal == "Red":
                return 1000
            elif terminal == "Yellow":
                return -1000
            else:  
                return 0

        utility_values = []
        for action in self.available_actions(current_state):
            next_state = self.take_action(current_state, action)
            utility_values.append(self.MinMax(next_state))

        if self.current_player(current_state) == "Red":
            return max(utility_values)
        else:
            return min(utility_values)
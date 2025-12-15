def MinMax(self, current_state):
        terminal = self.check_terminal(current_state)
        if terminal != "Not terminal":
            if terminal == "R":
                return 1
            elif terminal == "Y":
                return -1

        utility_values = []
        for action in self.available_actions(current_state):
            next_state = self.take_action(current_state, action)
            utility_values.append(self.MinMax(next_state))

        if self.current_player(current_state) == "R":
            return max(utility_values)
        else:

            return min(utility_values)


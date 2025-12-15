def available_actions(self, current_state):
        actions = []
        player = self.current_player(current_state)

        for col in range(7):
            if current_state[0][col] != " ":
                continue
            actions.append((player, col))

        return actions

    def human_play(self, current_state):
            self.display_grid(current_state)
            player = self.current_player(current_state)
            print(f"Your turn ({player})")

            valid_columns = [col for (_, col) in self.available_actions(current_state)]
            print(f"Available columns: {valid_columns}")

            while True:
                col = int(input("Choose a column (0-6): "))
                if col in valid_columns:
                    break
                else:
                    print("Invalid column! Try again.")

            new_state = self.take_action(current_state, (player, col))
            self.display_grid(new_state)
            return new_state

def human_vs_human(self, current_state):
    new_state = current_state
    self.display_grid(new_state)

    while self.check_terminal(new_state) is None:
        player = self.current_player(new_state)
        print(f"It is {player}'s turn")

        while True:
            try:
                col = int(input("Enter column (0 to 6): "))
                if col < 0 or col > 6:
                    print("Invalid column.")
                    continue
                if not self.is_valid_move(new_state, col):
                    print("Column is full.")
                    continue
                break
            except ValueError:
                print("Enter a number.")

        action = (player, col)
        new_state = self.take_action(new_state, action)
        self.display_grid(new_state)

    print("Winner:", self.check_terminal(new_state))
    return new_state

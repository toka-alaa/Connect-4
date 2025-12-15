def current_player(self, state):
        moves_num = 0
        
        for row in range(6):
            for col in range(7):
                if state[row][col] != " ":
                    moves_num+= 1
        
        return "R" if moves_num%2 == 0 else "Y"

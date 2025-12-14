class Connect4:
    def __init__(self):
        self.rows=6
        self.cols=7

    def check_terminal(self,state):

        for r in range(self.rows):                        #checking horizontal
            for c in range(self.cols):
                if state[r][c]!=0 and \
                   state[r][c+1]==state[r][c+2]==state[r][c+3]==state[r][c+4]:
                    return state[r][c]

        for c in range(self.cols):
            for r in range(self.rows):                    #checking vertical
                if state[r][c]!=0 and \
                   state[r][c]==state[r+1][c]==state[r+2][c]==state[r+3][c]:
                    return state[r][c]

        
        for r in range(self.rows):
            for c in range(self.cols):                     #checking up diagonal
                if state[r][c]!=0 and \
                   state[r][c]==state[r+1][c+1]==state[r+2][c+2]==state[r+3][c+3]:
                    return state[r][c]

        
        for r in range(3,self.rows):
            for c in range(self.cols):                        #checking down diagonal
                if state[r][c]!=0 and \
                   state[r][c]==state[r-1][c+1]==state[r-2][c+2]==state[r-3][c+3]:
                    return state[r][c]

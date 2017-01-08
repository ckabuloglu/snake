
class snakeAI():

    def  __init__(self, board):
       self.board = board

    def nextMove():
        directions = movePrio()

    def movePrio():
        moves = []
        headX, headY = self.board.snake.head
        foodX, foodY = self.board.food
        currentDir = self.board.snake.direction

        # xDist = abs(foodX - headX)
        # if xDist > 10: xDist = (20 - foodX) - headX

        # yDist = foodY - headY
        # if yDist > 10: yDist = (20 - foodY) - headY

        # if yDist > xDist:
        if headX > foodX:
            if headX - foodX > 10:
                moveX = [(1,0),(-1,0)]
            else:
                moveX = [(-1,0),(1,0)]
        elif headX < foodX:
            if headX - foodX > 10:
                moveX = [(1,0),(-1,0)]
            else:
                moveX = [(-1,0),(1,0)]
        else:

        


        
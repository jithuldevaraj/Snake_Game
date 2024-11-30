from turtle import Turtle


FONT = ("Arial", 12, "normal")
ALIGN = "center"


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:  # Read data.txt file
            self.high_score =  int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("data.txt", "w") as file: # write the high score in data.txt
                file.write(str(self.score))
            with open("data.txt", "r") as file:  # Update high score 
                self.high_score = int(file.read())
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # Game over function
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game Over ", align=ALIGN, font=FONT)

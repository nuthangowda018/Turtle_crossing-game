from turtle import Turtle
import random
COLORS=["red","orange","yellow","blue","purple","green"]
STARTING_MOVE_DISTANCE=5
MOVE_INCREMENT=5

class Car_manager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars=[]
        self.hideturtle()
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        rand_num=random.randint(1,6)
        if rand_num==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            new_car.goto(x=300,y=random_y)
            self.all_cars.append(new_car)

    def mov_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed +=5

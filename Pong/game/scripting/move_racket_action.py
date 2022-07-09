from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        racket1 = cast.get_first_actor(RACKET_GROUP)
        racket2 = cast.get_first_actor(RACKET_GROUP2)
        body1 = racket1.get_body()
        body2 = racket2.get_body()
        velocity1 = body1.get_velocity()
        position1 = body1.get_position()
        velocity2 = body2.get_velocity()
        position2 = body2.get_position()
        # x = position.get_x()
        y1 = position1.get_y()
        y2 = position2.get_y()
        
        position1 = position1.add(velocity1)
        position2 = position2.add(velocity2)

        # if x < 0:
        #     position = Point(0, position.get_y())
        # elif x > (SCREEN_WIDTH - RACKET_WIDTH):
        #     position = Point(SCREEN_WIDTH - RACKET_WIDTH, position.get_y())
        if y1 < 0:
            position1 = Point(position1.get_x(), 0)
        elif y1 > (SCREEN_HEIGHT - RACKET_HEIGHT):
             position1 = Point(position1.get_x(), SCREEN_HEIGHT - RACKET_HEIGHT)
            
        body1.set_position(position1)
        
        if y2 < 0:
            position2 = Point(position2.get_x(), 0)
        elif y2 > (SCREEN_HEIGHT - RACKET_HEIGHT):
             position2 = Point(position2.get_x(), SCREEN_HEIGHT - RACKET_HEIGHT)
            
        body2.set_position(position2)
        
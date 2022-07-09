from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        racket1 = cast.get_first_actor(RACKET_GROUP)
        racket2 = cast.get_first_actor(RACKET_GROUP2)

        if self._keyboard_service.is_key_down(W): 
            racket1.swing_up()
        elif self._keyboard_service.is_key_down(S): 
            racket1.swing_down()
        else: 
            racket1.stop_moving()

        if self._keyboard_service.is_key_down(UP): 
            racket2.swing_up()
        elif self._keyboard_service.is_key_down(DOWN): 
            racket2.swing_down()
        else: 
            racket2.stop_moving()
        # if self._keyboard_service.is_key_down(LEFT):
        #     racket1.swing_left()
        # elif self._keyboard_service.is_key_down(RIGHT): 
        #     racket1.swing_right()        
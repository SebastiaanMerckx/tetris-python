import arcade
import time
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_DIAMETER = 20

SPRITE_SCALING_PLAYER = 0.2
SPRITE_SCALING_COIN = 0.1
COIN_COUNT = 3
STATE_DURATION = 100


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Create the sprite lists
        self.player_list = arcade.SpriteList()
        self.fixed_block_list = []
        self.incoming_block_list = None

        self.state = -1 #0: creating block, 1: dropping, 2: checking result
        self.count_state = 0

        # Score
        self.score = 0

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        arcade.draw_rectangle_outline(300, 300, 204, 404, arcade.color.BLACK, 2)
        arcade.draw_text("score: {}".format(self.score), 500, 300, arcade.color.BLACK)
        if self.incoming_block_list != None:
            for b in self.incoming_block_list['blocks']:
                if(self.state == 3):
                    arcade.draw_rectangle_filled(b['c_x'], b['c_y'], BLOCK_DIAMETER, BLOCK_DIAMETER, arcade.color.RED)
                else:
                    arcade.draw_rectangle_filled(b['c_x'], b['c_y'], BLOCK_DIAMETER, BLOCK_DIAMETER, arcade.color.YELLOW_GREEN)
                arcade.draw_rectangle_outline(b['c_x'], b['c_y'], BLOCK_DIAMETER, BLOCK_DIAMETER, arcade.color.BLACK)
        for b in self.fixed_block_list:
            arcade.draw_rectangle_filled(b['c_x'], b['c_y'], BLOCK_DIAMETER, BLOCK_DIAMETER, arcade.color.YELLOW_ORANGE)
            arcade.draw_rectangle_outline(b['c_x'], b['c_y'], BLOCK_DIAMETER, BLOCK_DIAMETER, arcade.color.BLACK)
        if(self.state == -1):
            arcade.draw_text("press key down to start", 200, 450, arcade.color.BLACK)
        if(self.state == 3):
            arcade.draw_text("GAME OVER", 200, 450, arcade.color.BLACK)

    def update(self, delta_time):
        # Generate a list of all coin sprites that collided with the player.
        if (self.state == 0):
            # create block...
            type = random.randrange(12)
            start = 470
            #print(type)
            if type == 0:
                self.incoming_block_list = {'type': type, 'c_x': 290, 'c_y': start, 'blocks' : []}
                self.incoming_block_list['blocks'].append({'c_x': 270, 'c_y': start})
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start})
                self.incoming_block_list['blocks'].append({'c_x': 310, 'c_y': start})
                self.incoming_block_list['blocks'].append({'c_x': 330, 'c_y': start})
            elif type == 1:
                self.incoming_block_list = {'type': type, 'c_x': 290, 'c_y': start-BLOCK_DIAMETER, 'blocks' : []}
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start-BLOCK_DIAMETER})
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start-2*BLOCK_DIAMETER})
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start+BLOCK_DIAMETER})
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start})
            elif type == 2:
                #  XX
                #   OX
                self.incoming_block_list = {'type': type, 'c_x': 290, 'c_y': start, 'blocks' : []}
                self.incoming_block_list['blocks'].append({'c_x': 270, 'c_y': start+BLOCK_DIAMETER})
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start+BLOCK_DIAMETER})
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start})
                self.incoming_block_list['blocks'].append({'c_x': 310, 'c_y': start})
            elif type == 3:
                #    X
                #   OX
                #   X
                self.incoming_block_list = {'type': type, 'c_x': 290, 'c_y': start, 'blocks' : []}
                self.incoming_block_list['blocks'].append({'c_x': 310, 'c_y': start+BLOCK_DIAMETER})
                self.incoming_block_list['blocks'].append({'c_x': 310, 'c_y': start})
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start})
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start-BLOCK_DIAMETER})
            elif type == 4:
                #   XX
                #  XO
                self.incoming_block_list = {'type': type, 'c_x': 290, 'c_y': start, 'blocks' : []}
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start+BLOCK_DIAMETER})
                self.incoming_block_list['blocks'].append({'c_x': 310, 'c_y': start+BLOCK_DIAMETER})
                self.incoming_block_list['blocks'].append({'c_x': 270, 'c_y': start})
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start})
            elif type == 5:
                #   X
                #   OX
                #    X
                self.incoming_block_list = {'type': type, 'c_x': 290, 'c_y': start, 'blocks' : []}
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start+BLOCK_DIAMETER})
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start})
                self.incoming_block_list['blocks'].append({'c_x': 310, 'c_y': start})
                self.incoming_block_list['blocks'].append({'c_x': 310, 'c_y': start-BLOCK_DIAMETER})
            elif type == 6:
                #  X
                # XOX
                self.incoming_block_list = {'type': type, 'c_x': 290, 'c_y': start, 'blocks' : []}
                self.incoming_block_list['blocks'].append({'c_x': 270, 'c_y': start})
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start})
                self.incoming_block_list['blocks'].append({'c_x': 310, 'c_y': start})
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start+BLOCK_DIAMETER})
            elif type == 7:
                # XX
                # OX
                self.incoming_block_list = {'type': type, 'c_x': 290, 'c_y': start, 'blocks' : []}
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start+BLOCK_DIAMETER})
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start})
                self.incoming_block_list['blocks'].append({'c_x': 310, 'c_y': start})
                self.incoming_block_list['blocks'].append({'c_x': 310, 'c_y': start+BLOCK_DIAMETER})
            elif type == 8:
                # XOX
                #   X
                self.incoming_block_list = {'type': type, 'c_x': 290, 'c_y': start+BLOCK_DIAMETER, 'blocks' : []}
                self.incoming_block_list['blocks'].append({'c_x': 270, 'c_y': start+BLOCK_DIAMETER})
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start+BLOCK_DIAMETER})
                self.incoming_block_list['blocks'].append({'c_x': 310, 'c_y': start+BLOCK_DIAMETER})
                self.incoming_block_list['blocks'].append({'c_x': 310, 'c_y': start})
            elif type == 9:
                #    X
                #    O
                #   XX
                self.incoming_block_list = {'type': type, 'c_x': 310, 'c_y': start, 'blocks' : []}
                self.incoming_block_list['blocks'].append({'c_x': 310, 'c_y': start+BLOCK_DIAMETER})
                self.incoming_block_list['blocks'].append({'c_x': 310, 'c_y': start})
                self.incoming_block_list['blocks'].append({'c_x': 310, 'c_y': start-BLOCK_DIAMETER})
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start-BLOCK_DIAMETER})
            elif type == 10:
                #   X
                # XOX
                self.incoming_block_list = {'type': type, 'c_x': 290, 'c_y': start, 'blocks' : []}
                self.incoming_block_list['blocks'].append({'c_x': 270, 'c_y': start})
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start})
                self.incoming_block_list['blocks'].append({'c_x': 310, 'c_y': start})
                self.incoming_block_list['blocks'].append({'c_x': 310, 'c_y': start+BLOCK_DIAMETER})
            elif type == 11:
                #   X
                #   O
                #   XX
                self.incoming_block_list = {'type': type, 'c_x': 290, 'c_y': start, 'blocks' : []}
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start+BLOCK_DIAMETER})
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start})
                self.incoming_block_list['blocks'].append({'c_x': 290, 'c_y': start-BLOCK_DIAMETER})
                self.incoming_block_list['blocks'].append({'c_x': 310, 'c_y': start-BLOCK_DIAMETER})
            self.state = 1
            self.count_state = 0
            if not self.canMoveDown():
                #todo: mark block in red...?
                self.state = 3
        elif(self.state == 1):
            if(self.count_state < STATE_DURATION):
                self.count_state = self.count_state + 1
            else:
                self.count_state = 0
                #actual update...: try to move down.
                if self.canMoveDown():
                    for b in self.incoming_block_list['blocks']:
                        b['c_y'] = b['c_y'] - BLOCK_DIAMETER
                    self.incoming_block_list['c_y'] = self.incoming_block_list['c_y'] - BLOCK_DIAMETER
                else:
                    for b in self.incoming_block_list['blocks']:
                        self.fixed_block_list.append(b)
                    self.incoming_block_list = None
                    self.state = 2
        elif(self.state == 2):
            if self.count_state == 0:
                completed_lines = []
                for i in range(110, 490, 20):
                    line = False
                    count_blocks = 0
                    for b in self.fixed_block_list:
                        if b['c_y'] == i:
                            count_blocks = count_blocks+1
                    if count_blocks == 10:
                        line = True
                        completed_lines.append(i)
                if(len(completed_lines) > 0):
                    self.score = self.score + len(completed_lines)*100
                    print('remove lines', completed_lines)
                    for c in completed_lines:
                        while(1):
                            element_found = False
                            index = -1
                            for b in self.fixed_block_list:
                                index = index + 1
                                if b['c_y'] == c:
                                    element_found = True
                                    break
                            if element_found:
                                self.fixed_block_list.pop(index)
                            else:
                                break
                    for b in self.fixed_block_list:
                        drop_down_count = 0
                        for c in completed_lines:
                            if b['c_y'] > c:
                                drop_down_count = drop_down_count + 1
                        b['c_y'] = b['c_y'] - drop_down_count * BLOCK_DIAMETER
                    self.count_state = 1
                else:
                    self.state_count = 0
                    self.state = 0
                    return
            else:
                self.count_state = self.count_state+1
                if(self.count_state > STATE_DURATION):
                    self.state = 0

        elif(self.state == 3): #lost
            self.state = 3

    def canMoveLeft(self):
        if self.incoming_block_list == None:
            return False
        for b in self.incoming_block_list['blocks']:
            if b['c_x'] < 230:
                return False
            for b_fixed in self.fixed_block_list:
                if b['c_x'] == b_fixed['c_x'] + BLOCK_DIAMETER and b['c_y'] == b_fixed['c_y']:
                    return False
        return True
    def canMoveRight(self):
        if self.incoming_block_list == None:
            return False
        for b in self.incoming_block_list['blocks']:
            if b['c_x'] > 370:
                return False
            for b_fixed in self.fixed_block_list:
                if b['c_x'] == b_fixed['c_x'] - BLOCK_DIAMETER and b['c_y'] == b_fixed['c_y']:
                    return False
        return True
    def canMoveDown(self):
        if self.incoming_block_list == None:
            return False
        for b in self.incoming_block_list['blocks']:
            if b['c_y'] == 110:
                return False
            for b_fixed in self.fixed_block_list:
                if b['c_x'] == b_fixed['c_x'] and b['c_y'] == b_fixed['c_y'] + BLOCK_DIAMETER:
                    return False
        return True

    def rotate(self):
        if self.incoming_block_list == None:
            return False
        if self.incoming_block_list['type'] == 7:
            return False
        #center remains the same, blocks turn around center.
        canTurn = True
        testBlocks = []
        for b in self.incoming_block_list['blocks']:
            x = self.incoming_block_list['c_x'] + (b['c_y'] - self.incoming_block_list['c_y'])
            y = self.incoming_block_list['c_y'] - (b['c_x'] - self.incoming_block_list['c_x'])
            newBlock = {'c_x': x, 'c_y': y}
            testBlocks.append(newBlock)
        for b in testBlocks:
            if b['c_y'] <= 110:
                return False
            if b['c_x'] < 210 or b['c_x']> 390:
                return False
            for bf in self.fixed_block_list:
                if (b['c_x'] == bf['c_x'] and  b['c_y'] == bf['c_y']) or 0:
                    print('no rotation possible')
                    return
        self.incoming_block_list['blocks'] = []
        for b in testBlocks:
            self.incoming_block_list['blocks'].append(b)

    def on_key_press(self, arg1, arg2):
        #print("on_key_press", arg1, arg2)
        if(arg1 == 65361):
            if self.canMoveLeft():
                self.incoming_block_list['c_x'] = self.incoming_block_list['c_x'] - BLOCK_DIAMETER
                for b in self.incoming_block_list['blocks']:
                    b['c_x'] = b['c_x'] - BLOCK_DIAMETER
        elif (arg1 == 65362):
            self.rotate()
        elif(arg1 == 65363):
            if self.canMoveRight():
                self.incoming_block_list['c_x'] = self.incoming_block_list['c_x'] + BLOCK_DIAMETER
                for b in self.incoming_block_list['blocks']:
                    b['c_x'] = b['c_x'] + BLOCK_DIAMETER
        elif (arg1 == 65364):
            if(self.state == -1):
                self.state = 0
            else:
                if self.canMoveDown():
                    self.incoming_block_list['c_y'] = self.incoming_block_list['c_y'] - BLOCK_DIAMETER
                    for b in self.incoming_block_list['blocks']:
                        b['c_y'] = b['c_y'] - BLOCK_DIAMETER
                else:
                    self.count_state = 9999999
        elif (arg1 == 114):
            self.incoming_block_list = None
            self.state = -1
            self.score = 0
            self.fixed_block_list = []
        else:
            print('pressed ', arg1)

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()

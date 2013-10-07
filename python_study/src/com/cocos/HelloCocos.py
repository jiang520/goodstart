#
# cocos2d
# http://cocos2d.org
#
# This code is so you can run the samples without installing the package
import sys
import os
from cocos import layer, actions
from cocos.sprite import Sprite
from random import random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
#

import cocos
from cocos.actions import *

# A color layer  is a Layer with the a color attribute
class HelloWorld(layer.util_layers.ColorLayer):
    def __init__(self):
        # blueish color
        super( HelloWorld, self ).__init__( 64,64,224,255)

        # a cocos.text.Label is a wrapper of pyglet.text.Label
        # with the benefit of being a CocosNode
        label = cocos.text.Label('Hello, World!',
            font_name='Times New Roman',
            font_size=32,
            anchor_x='center', anchor_y='center')

        # set the label in the center of the screen
        label.position = 320,240
        self.add( label,2 )
        
        # similar to cocos.text.Label, a cocos.sprite.Sprite
        # is a subclass of pyglet.sprite.Sprite with the befits of
        # being a CocosNode.
        sprite = cocos.sprite.Sprite('xiaoqingxin0624.jpg')
        
        # sprite in the center of the screen (default is 0,0)
        sprite.position = 0,240
        
        # sprite scale attribute starts with 3 (default 1 )
        sprite.scale = 0.9
        
        # add the sprite as a child, but with z=1 (default is z=0).
        # this means that the sprite will be drawn on top of the label
        self.add( sprite, z=1 )

        # create a ScaleBy action that lasts 2 seconds
        scale = ScaleBy(1.8, duration=2)
        
        move = actions.MoveBy((self.width, 0), 3)
        # tell the label to scale and scale back and repeat these 2 actions forever
        #label.do( Repeat( scale + Reverse( scale) ) )
        label.do(move)
        # tell the sprite to scaleback and then scale, and repeat these 2 actions forever
        # sprite.do(Repeat(move))
        sprite.do( Repeat( move+scale + Reverse(move)+Reverse(scale) ) )
        self.addTarget()
    def addTarget(self):
        target = cocos.sprite.Sprite("xiaoqingxin0624.jpg", (0, 0))
        winsize = cocos.director.director.get_window_size()
        minY = target.get_rect().height/2
        maxY = 80#winsize.height-target.get_rect().height/2
        rangeY = maxY-minY
        import random
        actualY = (random.Random.randint()%rangeY)+minY
        
        

if __name__ == "__main__":
    # director init takes the same arguments as pyglet.window
    cocos.director.director.init()

    # We create a new layer, an instance of HelloWorld
    hello_layer = HelloWorld ()
    
    # tell the layer to perform a Rotate action in 10 seconds.
    action_move = actions.MoveBy((-50, 80), 3);
    #hello_layer.do( RotateBy(160, duration=5) )
    #hello_layer.do(action_move)
    # A scene that contains the layer hello_layer
    main_scene = cocos.scene.Scene (hello_layer)

    # And now, start the application, starting with main_scene
    cocos.director.director.run (main_scene)

    # or you could have written, without so many comments:
    #      director.run( cocos.scene.Scene( HelloWorld() ) )

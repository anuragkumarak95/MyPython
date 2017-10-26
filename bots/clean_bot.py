from matplotlib import pyplot as plt
import random

# generate the canvas..
def gen_grid(size):
    canvas = [[True for i in range(size)] for i in range(size)]
    return canvas

# randomly put dirty tiles in the canvas..
def get_dirty(canvas):
    for i,row in enumerate(canvas):
        for j,_ in enumerate(row):
            canvas[i][j]=bool(random.getrandbits(1))
# TODO - func to find nearest dirty tile from our robots current position..
find_nn_dirty(canvas,point):
    x,y = point

# TODO - func to generate next move of our robot towards the  dirt, 
# if on dirt: clean it.
def move(curr,next_dirt):
    pass

if __name__=='__main__':
    canvas = gen_grid(100)
    get_dirty(canvas)
    print(canvas)

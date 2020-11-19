from matrix import *
import random

def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:
                print("XX", end='')
        print()

def rotate(blk):
    if blk == [ [ 0, 0, 1, 0], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ] ]:
        return [ [ 0, 0, 0, 0 ], [ 1, 1, 1, 1 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 0, 0, 0 ], [ 1, 1, 1, 1 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ]:
        return [ [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ] ]

    elif blk == [ [ 0, 0, 1, 1 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ],[ 0, 0, 0, 0 ]]:
        return [ [ 0, 1, 1, 1 ], [ 0, 0, 0, 1 ],[ 0, 0, 0, 0 ],[ 0, 0, 0, 0 ]]
    elif blk == [ [ 0, 1, 1, 1 ], [ 0, 0, 0, 1 ],[ 0, 0, 0, 0 ],[ 0, 0, 0, 0 ]]:
        return [ [ 0, 0, 0, 1 ], [ 0, 0, 0, 1 ], [ 0, 0, 1, 1 ],[ 0, 0, 0, 0 ]]
    elif blk == [ [ 0, 0, 0, 1 ], [ 0, 0, 0, 1 ], [ 0, 0, 1, 1 ],[ 0, 0, 0, 0 ]]:
        return [ [ 0, 1, 0, 0 ], [ 0, 1, 1, 1 ],[ 0, 0, 0, 0 ],[ 0, 0, 0, 0 ]]
    elif blk == [ [ 0, 1, 0, 0 ], [ 0, 1, 1, 1 ],[ 0, 0, 0, 0 ],[ 0, 0, 0, 0 ]]:
        return [ [ 0, 0, 1, 1 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ],[ 0, 0, 0, 0 ]]
    
    elif blk == [ [ 0, 1, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ],[ 0, 0, 0, 0 ] ]: 
        return [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 1 ], [ 0, 1, 1, 1 ],[ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 0, 0, 0 ], [ 0, 0, 0, 1 ], [ 0, 1, 1, 1 ],[ 0, 0, 0, 0 ] ]:
        return [ [ 0, 1, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 1, 1, 0 ],[ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 1, 0, 0 ], [ 0, 1, 0, 0 ], [ 0, 1, 1, 0 ],[ 0, 0, 0, 0 ] ]:
        return [ [ 0, 0, 0, 0 ], [ 0, 1, 1, 1 ], [ 0, 1, 0, 0 ],[ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 0, 0, 0 ], [ 0, 1, 1, 1 ], [ 0, 1, 0, 0 ],[ 0, 0, 0, 0 ] ]:
        return [ [ 0, 1, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ],[ 0, 0, 0, 0 ] ]

    elif blk == [ [ 0, 1, 0, 0], [ 0, 1, 1, 0 ], [ 0, 0, 1, 0 ],[ 0, 0, 0, 0 ] ]:
        return [ [ 0, 0, 0, 0], [ 0, 0, 1, 1 ], [ 0, 1, 1, 0 ],[ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 0, 0, 0], [ 0, 0, 1, 1 ], [ 0, 1, 1, 0 ],[ 0, 0, 0, 0 ] ]:
        return [ [ 0, 1, 0, 0], [ 0, 1, 1, 0 ], [ 0, 0, 1, 0 ],[ 0, 0, 0, 0 ] ]
    
    elif blk == [ [ 0, 0, 1, 0], [ 0, 1, 1, 0 ], [ 0, 1, 0, 0 ],[ 0, 0, 0, 0 ] ]:
        return [ [ 0, 0, 0, 0], [ 0, 1, 1, 0 ], [ 0, 0, 1, 1 ],[ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 0, 0, 0], [ 0, 1, 1, 0 ], [ 0, 0, 1, 1 ],[ 0, 0, 0, 0 ] ]:
        return [ [ 0, 0, 1, 0], [ 0, 1, 1, 0 ], [ 0, 1, 0, 0 ],[ 0, 0, 0, 0 ] ]

    elif blk == [ [ 0, 0, 1, 0 ], [ 0, 1, 1, 1 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ]:
        return [ [ 0, 0, 1, 0 ], [ 0, 0, 1, 1 ], [ 0, 0, 1, 0 ],[ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 0, 1, 0 ], [ 0, 0, 1, 1 ],[ 0, 0, 1, 0 ], [ 0, 0, 0, 0 ] ]:
        return [ [ 0, 0, 0, 0 ], [ 0, 1, 1, 1 ],  [ 0, 0, 1, 0 ], [ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 0, 0, 0 ], [ 0, 1, 1, 1 ], [ 0, 0, 1, 0 ], [ 0, 0, 0, 0 ] ]:
        return [ [ 0, 0, 1, 0 ], [ 0, 1, 1, 0 ],[ 0, 0, 1, 0 ], [ 0, 0, 0, 0 ] ]
    elif blk == [ [ 0, 0, 1, 0 ],[ 0, 1, 1, 0 ], [ 0, 0, 1, 0 ],[ 0, 0, 0, 0 ] ]:
        return [ [ 0, 0, 1, 0 ], [ 0, 1, 1, 1 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ]
   
    else:
        return blk
 

###
### initialize variables
###     
def random_blk():
    rand = random.randint(1,7) 
    if rand == 1:
        blk = [ [ 0, 0, 1, 0], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ] ] # ㅣ
    elif rand ==2:
        blk = [ [ 0, 0, 1, 1 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ],[ 0, 0, 0, 0 ] ] # r
    elif rand ==3:
        blk = [ [ 0, 1, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ],[ 0, 0, 0, 0 ] ] # ㄴ
    elif rand ==4:
        blk = [ [ 0, 1, 0, 0], [ 0, 1, 1, 0 ], [ 0, 0, 1, 0 ],[ 0, 0, 0, 0 ] ] # s
    elif rand ==5:
        blk = [ [ 0, 0, 1, 0 ], [ 0, 1, 1, 1 ],[ 0, 0, 0, 0 ],[ 0, 0, 0, 0 ] ] # ㅗ
    elif rand ==6:
        blk = [ [ 0, 0, 1, 0], [ 0, 1, 1, 0 ], [ 0, 1, 0, 0 ],[ 0, 0, 0, 0 ] ] # reversed s
    else:
        blk = [ [ 0, 1, 1, 0], [ 0, 1, 1, 0 ], [ 0, 0, 0, 0 ], [ 0, 0, 0, 0 ] ] # ㅁ

    return blk 


arrayBlk = [ [ 0, 0, 0, 0], [ 0, 0, 1, 1 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ] ]

### integer variables: must always be integer!
iScreenDy = 15
iScreenDx = 10
iScreenDw = 4
top = 0
left = iScreenDw + iScreenDx//2 - 2

newBlockNeeded = False

arrayScreen = [
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

###
### prepare the initial screen output
###  
iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
rnd_Blk = random_blk()
currBlk = Matrix(rnd_Blk)#(arrayBlk)
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left)
draw_matrix(oScreen); print()

###
### execute the loop
###

while True:
    key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
    if key == 'q':
        print('Game terminated...')
        break
    elif key == 'a': # move left  
        left -= 1
    elif key == 'd': # move right
        left += 1
    elif key == 's': # move downs
        top += 1
    elif key == 'w': # rotate the block clsockwise
        rnd_Blk = rotate(rnd_Blk)
        currBlk = Matrix(rnd_Blk)

    elif key == ' ': # drop the block
        while not tempBlk.anyGreaterThan(1):
            top +=1
            tempBlk = iScreen.clip(top, left, top+currBlk.get_dy() , left+currBlk.get_dx())
            tempBlk = tempBlk + currBlk
        
        top -=1
        newBlockNeeded = True
  
    else: 
        print('Wrong key!!!') 
        continue

    tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
    tempBlk = tempBlk + currBlk
    if tempBlk.anyGreaterThan(1):
        if key == 'a': # undo: move right
            print('fgdg')
            left += 1
        elif key == 'd': # undo: move left
            left -= 1
        elif key == 's': # undo: move up 
            top -= 1
            newBlockNeeded = True
        elif key == 'w': # undo: rotate the block counter-clockwise
            for i in range(3):
                rnd_Blk = rotate(rnd_Blk)
                currBlk = Matrix(rnd_Blk)
            

        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk

    oScreen = Matrix(iScreen)
    oScreen.paste(tempBlk, top, left)
    draw_matrix(oScreen); print()

    if newBlockNeeded:
        iScreen = Matrix(oScreen)
        top = 0
        left = iScreenDw + iScreenDx//2 - 2
        newBlockNeeded = False
        rnd_Blk = random_blk()
        currBlk = Matrix(rnd_Blk)
        tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
        tempBlk = tempBlk + currBlk
        if tempBlk.anyGreaterThan(1):
            print('Game Over!!!')
            break
        
        oScreen = Matrix(iScreen)
        oScreen.paste(tempBlk, top, left)
        draw_matrix(oScreen); print()
        
###
### end of the loop
###

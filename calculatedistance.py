import math

def getdistance (snakex,snakey,foodx,foody):

    X_minimum_distance = 0
    Y_minimum_distance = 0
    if snakex>foodx:
        #snake is on the right, food is to the left
        X_directdistance = abs(snakex-foodx)
        
        X_boundarydistance = (abs(600-snakex))+(abs(0-foodx))

        if X_directdistance<X_boundarydistance:
            #go directly
            X_minimum_distance = X_directdistance

        if X_directdistance == X_boundarydistance:
            X_minimum_distance

        else:
            #go through boundary
            X_minimum_distance = X_boundarydistance


    elif foodx>snakex:
        #snake is on the left, food is to the right
        X_directdistance = abs(snakex-foodx)

        X_boundarydistance = abs(0-snakex)+abs(600-foodx)
        
        if X_directdistance<X_boundarydistance:
            X_minimum_distance = X_directdistance

        else:
            X_minimum_distance = X_boundarydistance



    elif snakey>foody:
        #snake is on the right, food is to the left
        Y_directdistance = abs(snakey-foody)
        
        Y_boundarydistance = (abs(600-snakey))+(abs(0-foody))

        if Y_directdistance<Y_boundarydistance:
            #go directly
            Y_minimum_distance = Y_directdistance

        else:
            #go through boundary
            Y_minimum_distance = Y_boundarydistance


    elif foody>snakey:
        #snake is on the left, food is to the right
        Y_directdistance = abs(snakey-foody)

        Y_boundarydistance = abs(0-snakey)+abs(600-foody)
        
        if Y_directdistance<Y_boundarydistance:
            Y_minimum_distance = Y_directdistance

        else:
            Y_minimum_distance = Y_boundarydistance


    print(X_minimum_distance,Y_minimum_distance)
    return math.sqrt(X_minimum_distance**2+Y_minimum_distance**2)



e = getdistance(100,100,500,500)
print(e)
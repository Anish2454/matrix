from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    rows = len(matrix)
    if rows < 1:
        matrix.append([[]])
    cols = len(matrix[0])
    if cols % 2 != 0:
        print "Not an even number of points"
        return
    for i in range(len(matrix[0])/2):
        pos = 2*i
        x0 = matrix[0][pos]
        y0 = matrix[1][pos]
        x1 = matrix[0][pos+1]
        y1 = matrix[1][pos+1]
        draw_line(x0,y0,x1,y1,screen,color)


def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
    add_point(matrix, x0,y0,z0)
    add_point(matrix, x1,y1,z1)

def add_point( matrix, x, y, z=0 ):
    vals = [x,y,z,1]
    rows = len(matrix)
    #print "Number of rows: " + str(rows)
    if rows < 1:
        matrix.append([[]])
    cols = len(matrix[0])
    for i in range(cols):
        isZero = True
        for j in range(rows):
            if matrix[j][i] != 0:
                isZero = False
                pass
        if isZero:
            for k in range(rows):
                matrix[k][i] = vals[k]
            return
    for i in range(rows):
        matrix[i].append(vals[i])



def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)
    if ( B == 0 ):
        print "undefined"
    	#undefined slope
    	while (y <= y1):
    		plot(screen, color, x, y)
    		y += 1
    	return

    m = -1 * (float(A) / B)
    print "slope: " + str(m)

    #octants 1
    if ( m <= 1 and m > 0 ):
        #octant 1
        #print "oct 1"
        if A > 0:
            d = (2*A) + B

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= (2*B)
                x+= 1
                d+= (2*A)
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1

    if ( m > 1 ):
		#print "oct 2"
		#octant 2
		if A > 0:
			d = A + (2*B)

			while y < y1:
				plot(screen, color, x, y)
				if d < 0:
					x+= 1
					d+= (2*A)
				y+= 1
				d+= (2*B)
            #end octant 2 while
			plot(screen, color, x1, y1)
        #end octant 2
    if ( m <= 0 and m > -1):
		#print "oct 8"
		#octant 8
		if A <= 0:
			d = (2*A) - B

			while x < x1:
				plot(screen, color, x, y)
				if ( d > 0 ):
					y -= 1
					d += (2 * B)
				x += 1
				d -= (2 * A)
			#end octant 8 while
			plot(screen, color, x1, y1)
		#end octant 8
    if ( m <= -1 ):
		#print "oct 7"
		#octant 7
		if A < 0:
			d = A - (2*B)

			while y > y1:
				plot(screen, color, x, y)
				if ( d < 0 ):
					x += 1
					d -= (2 * A)
				y -= 1
				d += (2 * B)
			#end octant 7 while
			plot(screen, color, x1, y1)
		#end octant 7
    #print "end"
#end draw_line

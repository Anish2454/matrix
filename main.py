from display import *
from draw import *
from matrix import *

def main():
    screen = new_screen()
    color = [ 0, 255, 0 ]
    matrix = new_matrix()

    print "***TESTING MATRIX FUNCTIONS***"
    print "=============================="
    print
    print "1) print_matrix "
    print "Expected: "
    print "1  2  3"
    print "4  5  6"
    print "Result: "
    print_matrix([[1,2,3], [4,5,6]])
    print "Expected: "
    print "10"
    print "4"
    print "20"
    print "30"
    print "Result: "
    print_matrix([[10], [4], [20], [30]])
    print
    print
    print "2) ident"
    print "1x1: "
    print_matrix(ident([1]))
    print "2x2"
    print_matrix(ident([[1,1],[1,1]]))
    print "3x3"
    print_matrix(ident([[1,1,1],[1,1,1],[1,1,1]]))
    print
    print
    print "3) matrix_mult"
    print "3x3 mult by identity"
    print "Expected: "
    print "1  2  3"
    print "2  23  1"
    print "1  4  6"
    print "Result: "
    m2 = [[1,2,3],[2,23,1],[1,4,6]]
    matrix_mult(m2, ident(m2))
    print_matrix(m2)
    print
    print
    print "***GENERATING IMAGE...***"
    print "========================="
    print
    print "Lines to be drawn: "
    print "To be added using add_point: "
    print "(0,0) to (250,400)"
    print "(250,400) to (400,0)"
    print "To be added using add_edge: "
    print "(0, 200) to (400, 200)"
    print "(250, 0) to (250, 400)"
    print "(150, 150) to (275, 100)"
    print "(150, 100) to (275, 150)"

    add_point(matrix,0,0)
    add_point(matrix,250,400)

    add_point(matrix,250,400)
    add_point(matrix,400, 0)

    add_edge(matrix,0,200,0,400,200,0)
    add_edge(matrix,250,0,0,250,400,0)
    add_edge(matrix,150,150,0,275,100,0)
    add_edge(matrix,150,100,0,275,150,0)

    print "Resulting Matrix: "
    print_matrix(matrix)

    draw_lines( matrix, screen, color )
    save_extension(screen, "image.png")
    #display(screen)

main()

#Schach

import turtle
t = turtle.Turtle()
t.speed(0)

from colorama import Fore, Back, Style


piece = ""

w_pawn1 = 'a2'
w_pawn2 = 'b2'
w_pawn3 = 'c2'
w_pawn4 = 'd2'
w_pawn5 = 'e2'
w_pawn6 = 'f2'
w_pawn7 = 'g2'
w_pawn8 = 'h2'
w_rook1 = 'a1'
w_rook2 = 'h1'
w_horse1 = 'b1'
w_horse2 = 'g1'
w_knight1 = 'c1'
w_knight2 = 'f1'
w_king = 'e1'
w_queen = 'd1'

w_pieces = ['w_pawn1','w_pawn2','w_pawn3','w_pawn4','w_pawn5','w_pawn6',
'w_pawn7','w_pawn8','w_rook1','w_horse1','w_knight1','w_king','w_queen',
'w_knight2','w_horse2','w_rook2']

b_pawn1 = 'a7'
b_pawn2 = 'b7'
b_pawn3 = 'c7'
b_pawn4 = 'd7'
b_pawn5 = 'e7'
b_pawn6 = 'f7'
b_pawn7 = 'g7'
b_pawn8 = 'h7'
b_rook1 = 'a8'
b_rook2 = 'h8'
b_horse1 = 'b8'
b_horse2 = 'g8'
b_knight1 = 'c8'
b_knight2 = 'f8'
b_king = 'e8'
b_queen = 'd8'


b_pieces = ['b_pawn1','b_pawn2','b_pawn3','b_pawn4','b_pawn5','b_pawn6','b_pawn7',
'b_pawn8','b_rook1','b_horse1','b_knight1','b_queen','b_king','b_knight2','b_horse2',
'b_rook2']


def welcome():
    
    print("Welcome to Chess!")
    print("PyChess is played using chess notation.")
    print("Get your partner ready...")
    print("Let's play!")



def draw_pieces():
    global piece
    t.pencolor("red")
    t.right(90)
    t.forward(624)
    t.left(90)
    counter = 15
    for columns in range(2):
        for rows in range(8):
            piece = w_pieces[counter]
            t.penup()
            t.left(70)
            t.forward(40)
            t.pendown()
            t.write(piece)
            t.penup()
            t.backward(40)
            t.right(70)
            t.forward(78)
            counter -=1
        t.left(180)
        t.forward(624)
        t.right(90)
        t.forward(78)
        t.right(90)

    t.left(90)
    t.forward(468)
    t.right(90)

    counter = 15
    t.pencolor("blue")
    
    for columns in range(2):
        for rows in range(8):
            piece = b_pieces[counter]
            t.penup()
            t.right(70)
            t.forward(40)
            t.pendown()
            t.write(piece)
            t.penup()
            t.backward(40)
            t.left(70)
            t.forward(78)
            counter -=1
        t.right(180)
        t.forward(624)
        t.left(90)
        t.forward(78)
        t.left(90)
        

def print_board():

    colour1 = "black"
    colour2 = "white"

    t.penup()
    t.goto(-300,-300)
    t.pendown()
    t.backward(30)
    
    for big_square in range(4):
        t.forward(624)
        t.left(90)

    for columns in range(8):

        if colour1 == "black" and colour2 == "white" and columns > 0:
            colour1,colour2 = colour2,colour1

        elif colour2 == "black" and colour1 == "white" and columns > 1:
            colour2,colour1 = colour1,colour2

        elif colour1 == "black" and colour2 == "white" and columns > 2:
            colour1,colour2 = colour2,colour1

        elif colour2 == "black" and colour1 == "white" and columns > 3:
            colour2,colour1 = colour1,colour2

        elif colour1 == "black" and colour2 == "white" and columns > 4:
            colour1,colour2 = colour2,colour1

        elif colour2 == "black" and colour1 == "white" and columns > 5:
            colour2,colour1 = colour1,colour2

        elif colour1 == "black" and colour2 == "white" and columns > 6:
            colour1,colour2 = colour2,colour1

        elif colour2 == "black" and colour1 == "white" and columns > 7:
            colour2,colour1 = colour1,colour2

        for rows in range(8):

            t.begin_fill()
            
            for small_square in range(4):
                
                if colour1 != colour2:
                    
                    t.fillcolor(colour1)
                
                t.forward(78)
                t.left(90)
                
            t.end_fill()
            colour1,colour2 = colour2,colour1

            t.forward(78)

        t.left(90)
        t.forward(78)
        t.left(90)
        t.forward(624)
        t.right(180)



print_board(),draw_pieces()

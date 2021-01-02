# First Semester -> 2018
# -------------------------------------------------------------------
# TicTacToe Prog0 at TU Graz
# Name: Pasero Christian
# Student ID: 11820726
# -------------------------------------------------------------------


##********************************************************************************************************
##*************************************** Setup **********************************************************
##********************************************************************************************************

##Turtle_Setup##*************************
import turtle
global standard_turtle_width
screen = turtle.Screen()
screen.title("Tic Tac Toe")
standard_turtle_width = 5
turtle.setup(600,400)   #Screen size
pencil = turtle.Turtle()
pencil.speed(10)
pencil.width(standard_turtle_width)
pencil.hideturtle()
global color_player1
color_player1 = "black"
global color_player2
color_player2 = "black"

##Player_Setup##*************************
##Player1
global player1Wins
player1Wins = False
global player1c
player1c = []
global player1Points
player1Points = 0

##Player2
global player2Wins
player2Wins = False
global player2c
player2c = []
global player2Points
player2Points = 0

##Both_Player
global playerturn
playerturn = "player2"
global display_name
display_name = False
global winner_name
winner_name = ""


##Game_Setup##***************************
##Remis
global cycle
cycle = 0
global remis
remis = False
global remis_quantity
remis_quantity = 0
global play_type
play_type = ""
##********************************************************************************************************
##*************************************** Functions ******************************************************
##********************************************************************************************************

def drawField():
##Game_Cross
    pencil.penup()
    pencil.setposition(-150,50)
    pencil.pendown()
    pencil.setx(150)

    pencil.penup()
    pencil.setposition(-150,-50)
    pencil.pendown()
    pencil.setx(150)

    pencil.penup()
    pencil.setposition(-50,-150)
    pencil.pendown()
    pencil.sety(150)

    pencil.penup()
    pencil.setposition(50,-150)
    pencil.pendown()
    pencil.sety(150)

##Field_Numbers
    bright_color = 0.9
    numbers_pos_X = -120
    numbers_pos_Y = 60
    laufvariable_i = 1
    for y in range(3):
        for x in range(3):
            pencil.penup()
            pencil.setposition(numbers_pos_X, numbers_pos_Y)
            pencil.pendown()
            pencil.color(bright_color, bright_color, bright_color)
            pencil.write(str(laufvariable_i), move=False, align="left", font=("Arial", 50, "normal"))
            numbers_pos_X = numbers_pos_X + 100
            laufvariable_i = laufvariable_i + 1
        numbers_pos_Y = numbers_pos_Y - 100
        numbers_pos_X = -120

##Write_score
    position_score_X = -270
    position_score_Y = 150
    position_score_lineSpace = 20
    pencil.color(0,0,0)
    pencil.penup()
    pencil.home()
    pencil.setposition(position_score_X,position_score_Y)
    pencil.write("Player1: " + str(player1Points), move=False, align="left", font=("Arial", 12, "normal"))
    pencil.setposition(position_score_X,position_score_Y-position_score_lineSpace*1)
    pencil.write("Player2: " + str(player2Points), move=False, align="left", font=("Arial", 12, "normal"))
    pencil.setposition(position_score_X,position_score_Y-position_score_lineSpace*2)
    pencil.write("Remis  : " + str(remis_quantity), move=False, align="left", font=("Arial", 12, "normal"))
##Show_Name

    global display_name
    global winner_name
    position_winner_X = -100
    position_winner_Y = -180
    if display_name == True:
        display_name = False
        pencil.penup()
        pencil.setposition(position_winner_X,position_winner_Y)
        pencil.write("Winner of last game: " + str(winner_name), move=False, align="left", font=("Arial", 12, "normal"))

def select_color():
    global color_player1
    global color_player2

    print("You can chose one the following colors by just writing them out:")
    print("blue")
    print("red")
    print("green")
    print("black")

    color_player1 = input("Insert your color Player 1: ")

    if color_player1 == "blue" or color_player1 == "red" or color_player1 == "green" or color_player1 == "black":
        color_player2 = input("Insert your color Player 2: ")
        if color_player2 == "blue" or color_player2 == "red" or color_player2 == "green" or color_player2 == "black":
            print("Your chosen colors are: ")
            print("Player 1: " + str(color_player1))
            print("Player 2: " + str(color_player2))
        else:
            print("Insert a valid color")
            select_color()
    else:
        print("Insert a valid color")
        select_color()

def select_play_type():
    global play_type
    print("Chose a input type:")
    print("--k      | Keyboard")
    print("--m      | Mouse")
    play_type = input("Play Type: ")
    if play_type == "--k":
        print("You chose the keyboard for input")
        play_type = "keyboard"
    elif play_type == "--m":
        print("This game type is not available for this version.")
        select_play_type()
    else:
        print("Invalid Input...")
        select_play_type()


def drawX(positionX_X,positionX_Y):
    pencil.color(color_player1)
    pencil.penup()
    pencil.setposition(positionX_X, positionX_Y)
    pencil.pendown()
    pencil.right(45)
    pencil.forward(80)
    pencil.penup()
    pencil.right(135)
    pencil.forward(58)
    pencil.pendown()
    pencil.right(135)
    pencil.forward(80)
    pencil.penup()
    pencil.home()

def drawO(positionO_X,positionO_Y):
    pencil.color(color_player2)
    circle_size = 40
    pencil.penup()
    pencil.setposition(positionO_X,positionO_Y)
    pencil.pendown()
    pencil.circle(circle_size)
    pencil.penup()
    pencil.home()


def chooseplayer():
    global playerturn
    global player2c
    global player1c
    if playerturn == "player1":
        playerturn = "player2"
    else:
        playerturn = "player1"

def makeinput():
    global playerturn
    global field
    if play_type == "keyboard":
        field = input("It's your turn " + playerturn + ": ")

        try:
            if field in player1c or field in player2c:
                print("You can't choose this field. Select another one...")
                print()
                makeinput()
            elif int(field) >= 1 and int(field) <= 9 :
                if playerturn == "player1":
                    player1c.append(field)
                    player1c.sort()
                else:
                    player2c.append(field)
                    player2c.sort()
            else:
                print("Insert a valid number...")
                print()
                makeinput()
        except ValueError:
            print("Insert a valid number...")
            print()
            makeinput()
    else:
        input(screen.onclick(make_input_mouse))


def make_input_mouse(mouse_X,mouse_Y):
    global chosen_field_mouse
    global field
    global got_input_mouse
    got_input_mouse = True
    pos_field1_X, pos_field1_Y, pos_field_width, pos_field_height = -150, 150, 100, 100

    if mouse_X >= pos_field1_X and mouse_Y <= pos_field1_Y and mouse_X <= pos_field1_X + pos_field_width and mouse_Y >= pos_field1_Y - pos_field_height:  # Feld1
        field = "1"
    elif mouse_X >= pos_field1_X + pos_field_width and mouse_Y <= pos_field1_Y and mouse_X <= pos_field1_X + pos_field_width * 2 and mouse_Y >= pos_field1_Y + pos_field_height:  # Feld2
        field = "2"
    elif mouse_X >= pos_field1_X + pos_field_width * 2 and mouse_Y <= pos_field1_Y and mouse_X <= pos_field1_X + pos_field_width * 3 and mouse_Y >= pos_field1_Y + pos_field_height:  # Feld2
        field = "3"
    elif mouse_X >= pos_field1_X and mouse_Y <= pos_field1_Y - pos_field_height and mouse_X <= pos_field1_X + pos_field_width and mouse_Y >= pos_field1_Y - pos_field_height * 2:  # Feld4
        field = "4"
    elif mouse_X >= pos_field1_X + pos_field_width and mouse_Y <= pos_field1_Y - pos_field_height and mouse_X <= pos_field1_X + pos_field_width * 2 and mouse_Y >= pos_field1_Y - pos_field_height * 2:  # Feld2
        field = "5"
    elif mouse_X >= pos_field1_X + pos_field_width * 2 and mouse_Y <= pos_field1_Y - pos_field_height and mouse_X <= pos_field1_X + pos_field_width * 3 and mouse_Y >= pos_field1_Y - pos_field_height * 2:  # Feld2
        field = "6"
    elif mouse_X >= pos_field1_X and mouse_Y <= pos_field1_Y - pos_field_height * 2 and mouse_X <= pos_field1_X and mouse_Y >= pos_field1_Y + pos_field_height * 3:  # Feld2
        field = "7"
    elif mouse_X >= pos_field1_X + pos_field_width and mouse_Y <= pos_field1_Y - pos_field_height * 2 and mouse_X <= pos_field1_X + pos_field_width and mouse_Y >= pos_field1_Y + pos_field_height * 3:  # Feld2
        field = "8"
    elif mouse_X >= pos_field1_X + pos_field_width * 2 and mouse_Y <= pos_field1_Y - pos_field_height * 2 and mouse_X <= pos_field1_X + pos_field_width * 2 and mouse_Y >= pos_field1_Y + pos_field_height * 3:  # Feld2
        field = "9"
    return field



def drawinput():
    global playerturn
    global field
    Par1 = 0
    Par2 = 0
    PosO_X = 0
    PosO_Y = 0
    if (playerturn == "player1"):
        if field == "1":
            Par1 , Par2 = -130,130
        elif field == "2":
            Par1, Par2 = -30, 130
        elif field == "3":
            Par1, Par2 = 70,130
        elif field == "4":
            Par1, Par2 = -130,30
        elif field == "5":
            Par1, Par2 = -30,30
        elif field == "6":
            Par1, Par2 = 70,30
        elif field == "7":
            Par1, Par2 = -130,-70
        elif field == "8":
            Par1, Par2 = -30,-70
        elif field == "9":
            Par1, Par2 = 70,-70

        drawX(Par1,Par2)
    else:
        if field == "1":
            PosO_X, PosO_Y = -100,60
        elif field == "2":
            PosO_X, PosO_Y = 0, 60
        elif field == "3":
            PosO_X, PosO_Y = 100, 60
        elif field == "4":
            PosO_X, PosO_Y = -100, -40
        elif field == "5":
            PosO_X, PosO_Y = 0, -40
        elif field == "6":
            PosO_X, PosO_Y = 100, -40
        elif field == "7":
            PosO_X, PosO_Y = -100, -140
        elif field == "8":
            PosO_X, PosO_Y = 0, -140
        elif field == "9":
            PosO_X, PosO_Y = 100, -140

        drawO(PosO_X,PosO_Y)


def win_condition_check():
    global remis
    global remis_quantity
    global cycle
    global player1Wins
    global player2Wins
    global  player2Points

    if "1" in player1c and "2" in player1c and "3" in player1c: #Obere Reihe
        player1Wins = True
        draw_won_line_horizontal(100)
    elif "1" in player1c and "5" in player1c and "9" in player1c: #Links oben nach rechts unten
        player1Wins = True
        draw_won_line_159()
    elif "1" in player1c and "4" in player1c and "7" in player1c: #Links oben nach Links unten
        player1Wins = True
        draw_won_line_vertical(-100)
    elif "3" in player1c and "5" in player1c and "7" in player1c: #Rechts oben nach links unten
        player1Wins = True
        draw_won_line_357()
    elif "3" in player1c and "6" in player1c and "9" in player1c: #Rechts oben nach Rechts unten
        player1Wins = True
        draw_won_line_vertical(100)
    elif "4" in player1c and "5" in player1c and "6" in player1c: #Links mitte nach Rechts mitte
        player1Wins = True
        draw_won_line_horizontal(0)
    elif "7" in player1c and "8" in player1c and "9" in player1c: #Links unten nach Rechts unten
        player1Wins = True
        draw_won_line_horizontal(-100)
    elif "2" in player1c and "5" in player1c and "8" in player1c: #Mitte oben nach Mitte unten
        player1Wins = True
        draw_won_line_vertical(0)



    if "1" in player2c and "2" in player2c and "3" in player2c: #Obere Reihe
        player2Wins = True
        draw_won_line_horizontal(100)
    elif "1" in player2c and "5" in player2c and "9" in player2c: #Quer links oben nach rechts unten
        player2Wins = True
        draw_won_line_159()
    elif "1" in player2c and "4" in player2c and "7" in player2c: #Links oben nach rechts unten
        player2Wins = True
        draw_won_line_vertical(-100)
    elif "3" in player2c and "5" in player2c and "7" in player2c: #Rechts oben nach links unten
        player2Wins = True
        draw_won_line_357()
    elif "3" in player2c and "6" in player2c and "9" in player2c: #Rechts oben nach Rechts unten
        player2Wins = True
        draw_won_line_vertical(100)
    elif "4" in player2c and "5" in player2c and "6" in player2c: #Links mitte nach Rechts mitte
        player2Wins = True
        draw_won_line_horizontal(0)
    elif "7" in player2c and "8" in player2c and "9" in player2c: #Links unten nach Rechts unten
        player2Wins = True
        draw_won_line_horizontal(-100)
    elif "2" in player2c and "5" in player2c and "8" in player2c: #Mitte oben nach Mitte unten
        player2Wins = True
        draw_won_line_vertical(0)

    cycle = cycle + 1
    if cycle == 9:
        remis = True
        remis_quantity = remis_quantity + 1



def draw_won_line_159():
    pencil.color("red")
    pencil.width(10)
    pencil.penup()
    pencil.home()
    pencil.left(135)
    pencil.forward(200)
    pencil.pendown()
    pencil.right(180)
    pencil.forward(400)
    pencil.penup()
    pencil.home()
    pencil.color("black")
    pencil.width(standard_turtle_width)

def draw_won_line_357():
    pencil.color("red")
    pencil.width(10)
    pencil.penup()
    pencil.home()
    pencil.right(135)
    pencil.forward(200)
    pencil.pendown()
    pencil.right(180)
    pencil.forward(400)
    pencil.penup()
    pencil.home()
    pencil.color("black")
    pencil.width(standard_turtle_width)

def draw_won_line_horizontal(won_line_Y):
    pencil.color("red")
    pencil.width(10)
    pencil.penup()
    pencil.home()
    pencil.setposition(-150, won_line_Y)
    pencil.pendown()
    pencil.forward(300)
    pencil.penup()
    pencil.home()
    pencil.color("black")
    pencil.width(standard_turtle_width)

def draw_won_line_vertical(won_line_X):
    pencil.color("red")
    pencil.width(10)
    pencil.width(10)
    pencil.penup()
    pencil.home()
    pencil.setposition(won_line_X, 150)
    pencil.right(90)
    pencil.pendown()
    pencil.forward(300)
    pencil.penup()
    pencil.home()
    pencil.color("black")
    pencil.width(standard_turtle_width)



def commando():
    global player1Points
    global player2Points
    global player1Wins
    global player2Wins
    global remis_quantity
    global display_name
    global winner_name
    print("--newgame        | Start new game")
    print("--newcolor       | Change Player color")
    print("--entername      | Displays your Name")
    print("--gametype       | Change Input type")
    command = input("Auswahl: ")


    if command == "--newgame":
        if player1Wins == True:
            player1Points = player1Points + 1
        elif player2Wins == True:
            player2Points = player2Points + 1
    elif command == "--newcolor":
        select_color()
        commando()
    elif command == "--entername":
        display_name = True
        winner_name = input("Name: ")
        commando()
    elif command == "--gametype":
        select_play_type()
    else:
        print("Not a valid input")
        commando()
    print("Player1: " + str(player1Points) + " | Player2: " + str(player2Points) + " | Remis: " + str(remis_quantity))
##********************************************************************************************************
##*************************************** Main_Loop ******************************************************
##********************************************************************************************************

select_play_type()
select_color()
while True:
    player1Wins = False
    player2Wins = False
    remis = False
    cycle = 0

    playerturn = "player2"
    player1c = []
    player2c = []
    pencil.clear()
    drawField()
    while player1Wins == False and player2Wins == False and remis == False:
        chooseplayer()
        makeinput()
        drawinput()
        win_condition_check()

    commando()

turtle.done()

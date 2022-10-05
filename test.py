import turtle as tur
import os
import sys
from maze_generation import generate

import sys
sys.path.insert(0, os.getcwd() + '/mazes')

def game():
    grid_size = [150, 150]

    grid_map = generate(grid_size)
    values = {"player_pos": [0, 0], "y_range": [0, 0], "x_range": [0, 0], "exit_loc": [grid_size[0] - 1, grid_size[1] -1]}

    def FUR():
        tur.forward(40)
        tur.penup()
        tur.left(90)

    tur.setup(55 * 11, 55 * 11)
    tur.ht()
    tur.tracer(0, 0)
    tur.speed(0)
    tur.delay(0)
    tur.penup()
    tur.bgcolor("BLACK")
    tur.pencolor("#E5E4E2")


    def set_screen():
        max_range_y = values["player_pos"][1] + 6
        min_range_y = values["player_pos"][1] - 5

        if max_range_y > grid_size[1]:
            min_range_y -= max_range_y - grid_size[1]

        if min_range_y < 0:
            min_range_y = 0
            max_range_y += -1 * (values["player_pos"][1] - 5)

        min_range_x = values["player_pos"][0] - 5
        max_range_x = values["player_pos"][0] + 6

        if max_range_x > grid_size[0]:
            min_range_x -= max_range_x - grid_size[0]

        if min_range_x < 0:
            min_range_x = 0
            max_range_x += -1 * (values["player_pos"][0] - 5)

        values["y_range"] = [min_range_y, max_range_y]
        values["x_range"] = [min_range_x, max_range_x]

    def write_screen():
        tur.clear()
        for i in range(11):
            j = 0
            for cell in grid_map[values["x_range"][0] + i][values["y_range"][0] : values["y_range"][1]]:
                tur.setheading(90)
                tur.goto(i * 40 - 185, j * 40 - 215)
                if cell["walls"][3]:
                    tur.pendown()
                FUR()
                if cell["walls"][0]:
                    tur.pendown()
                FUR()
                if cell["walls"][2]:
                    tur.pendown()
                FUR()
                if cell["walls"][1]:
                    tur.pendown()
                FUR()
                if cell["location"] == values["exit_loc"]:
                    tur.forward(30)
                    tur.left(90)
                    tur.forward(10)
                    tur.pendown()
                    tur.begin_fill()
                    tur.color("GREEN")
                    tur.forward(20)
                    tur.left(90)
                    tur.forward(20)
                    tur.left(90)
                    tur.forward(20)
                    tur.left(90)
                    tur.forward(20)
                    tur.left(90)
                    tur.end_fill()
                    tur.color("#E5E4E2")
                    tur.penup()

                elif cell["location"] == values["player_pos"]:
                    tur.forward(20)
                    tur.left(90)
                    tur.forward(20)
                    #creates a red dot
                    tur.pendown()
                    tur.color("#00A8FF")
                    tur.dot(20)
                    #resets the pen
                    tur.color("#E5E4E2")
                    tur.penup()
                j += 1
        tur.update()

    def listen():
        tur.onkey(up, "Up")
        tur.onkey(down, "Down")
        tur.onkey(left, "Left")
        tur.onkey(right, "Right")
        tur.onkey(saveFile, "s")

        tur.listen()

    def up():
        if not grid_map[values["player_pos"][0]][values["player_pos"][1]]["walls"][0]:
            values["player_pos"][1] += 1
            set_screen()
            write_screen()
            test_status()

    def down():
        if not grid_map[values["player_pos"][0]][values["player_pos"][1]]["walls"][1]:
            values["player_pos"][1] -= 1
            set_screen()
            write_screen()
            test_status()

    def left():
        if not grid_map[values["player_pos"][0]][values["player_pos"][1]]["walls"][2]:
            values["player_pos"][0] -= 1
            set_screen()
            write_screen()
            test_status()

    def right():
        if not grid_map[values["player_pos"][0]][values["player_pos"][1]]["walls"][3]:
            values["player_pos"][0] += 1
            set_screen()
            write_screen()
            test_status()

    def test_status():
        if values["player_pos"] == values["exit_loc"]:
            game()

    def saveFile():
        save = tur.textinput("Save?", "Are you sure you want to save this file? (y/n): ")
        if save == "y":
            name = tur.textinput("FileName", "Enter a name: ")
            try:
                name += ".py"
            except:
                return listen()
            try:
                f = open(os.getcwd() + "/mazes/" + name, "x")
            except:
                print("A file with that name already exists:")
                saveFileError()
            finally:
                f.close()
            f = open(os.getcwd() + "/mazes/" + name, "w")
            f.write("data = " + str(grid_map) +'\ndef getData():\n\treturn data')
            f.close()
        listen()

    def saveFileError():
        name = tur.textinput("FileName", "A file with that name already exists\nPlease use a different name\nEnter name: ")
        try:
            name += ".py"
        except:
            listen()
            return
        try:
            f = open(os.getcwd() + "/mazes/" + name, "x")
        except:
            print("A file with that name already exists:")
            saveFileError()
        finally:
            f.close()
        f = open(os.getcwd() + "/mazes/" + name, "w")
        f.write("data = " + str(grid_map) +'\ndef getData():\n\treturn data')
        f.close()
        listen()

    set_screen()
    write_screen()
    listen()
    tur.mainloop()
game()

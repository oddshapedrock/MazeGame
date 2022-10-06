from maze_generation import generate_3d as generate
import turtle as tur

def game():
    grid_size = [11, 11, 3] #X Y Z

    grid_map = generate(grid_size) #Z X Y
    values = {"player_pos": [0, 0, 0], "y_range": [0, 0], "x_range": [0, 0], "exit_loc": [grid_size[2] - 1, grid_size[0] -1, grid_size[1] -1]}

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
        max_range_y = values["player_pos"][2] + 6
        min_range_y = values["player_pos"][2] - 5

        if max_range_y > grid_size[1]:
            min_range_y -= max_range_y - grid_size[1]

        if min_range_y < 0:
            min_range_y = 0
            max_range_y += -1 * (values["player_pos"][2] - 5)

        min_range_x = values["player_pos"][1] - 5
        max_range_x = values["player_pos"][1] + 6

        if max_range_x > grid_size[0]:
            min_range_x -= max_range_x - grid_size[0]

        if min_range_x < 0:
            min_range_x = 0
            max_range_x += -1 * (values["player_pos"][1] - 5)

        values["y_range"] = [min_range_y, max_range_y]
        values["x_range"] = [min_range_x, max_range_x]
    
    def draw_arrow(i, j, up):
        if up:
            tur.goto(i * 40 - 205, j * 40 - 193)
            tur.setheading(90)
            tur.color("#00FF55")
        else:
            tur.goto(i * 40 - 205, j * 40 - 197)
            tur.setheading(270)
            tur.color("#FF0028")
        tur.pensize(2)
        tur.forward(3)
        tur.pendown()
        tur.right(135)
        tur.forward(5)
        tur.left(180)
        tur.forward(5)
        tur.left(90)
        tur.forward(5)
        tur.color("#E5E4E2")
        tur.penup()
        tur.goto(i * 40 - 185, j * 40 - 215)
        tur.pensize(1)

    def write_screen():
        tur.clear()
        for i in range(11):
            j = 0
            for cell in grid_map[values["player_pos"][0]][values["x_range"][0] + i][values["y_range"][0] : values["y_range"][1]]:
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
                    
                if not cell["walls"][4]:
                    draw_arrow(i, j, True)
                    
                if not cell["walls"][5]:
                    draw_arrow(i, j, False)
                    
                j += 1
        tur.update()

    def listen():
        tur.onkey(forward, "w")
        tur.onkey(backward, "s")
        tur.onkey(left, "a")
        tur.onkey(right, "d")
        tur.onkey(switch_planes, "space")
        tur.onkey(saveFile, "q")

        tur.listen()

    def switch_planes():
        if not grid_map[values["player_pos"][0]][values["player_pos"][1]][values["player_pos"][2]]["walls"][4] or not grid_map[values["player_pos"][0]][values["player_pos"][1]][values["player_pos"][2]]["walls"][5]:
            tur.onkey(up, "w")
            tur.onkey(down, "s")
            tur.onkey(None, "a")
            tur.onkey(None, "d")
            tur.onkey(None, "Up")
            tur.onkey(None, "Down")
            tur.onkey(None, "q")

    def forward():
        if not grid_map[values["player_pos"][0]][values["player_pos"][1]][values["player_pos"][2]]["walls"][0]:
            values["player_pos"][2] += 1
            set_screen()
            write_screen()
            test_status()

    def backward():
        if not grid_map[values["player_pos"][0]][values["player_pos"][1]][values["player_pos"][2]]["walls"][1]:
            values["player_pos"][2] -= 1
            set_screen()
            write_screen()
            test_status()

    def left():
        if not grid_map[values["player_pos"][0]][values["player_pos"][1]][values["player_pos"][2]]["walls"][2]:
            values["player_pos"][1] -= 1
            set_screen()
            write_screen()
            test_status()

    def right():
        if not grid_map[values["player_pos"][0]][values["player_pos"][1]][values["player_pos"][2]]["walls"][3]:
            values["player_pos"][1] += 1
            set_screen()
            write_screen()
            test_status()
    
    def up():
        if not grid_map[values["player_pos"][0]][values["player_pos"][1]][values["player_pos"][2]]["walls"][4]:
            values["player_pos"][0] += 1
            set_screen()
            write_screen()
            test_status()
            listen()
    
    def down():
        if not grid_map[values["player_pos"][0]][values["player_pos"][1]][values["player_pos"][2]]["walls"][5]:
            values["player_pos"][0] -= 1
            set_screen()
            write_screen()
            test_status()
            listen()
            
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
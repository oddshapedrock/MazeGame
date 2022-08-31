import random
import datetime
import os
#for the graphics
import turtle as tur

date = datetime.datetime
startTime = date.now()

#procedurally generated Maze
#takes an optional player input -> (#maze rows, #maze collumns) default of 50
#creating a random starting point and a random end point somewhere within the maze
#Generates a maze within boudaries by creating a path from start to finish and branches off that path
#loads a 11x11 view of the maze with the character in the middle and cords at the top left of the screen
#prompts the character for a movement direction (up, down, left, right) with optional distance (direction, distance) default of 1
#checks for border collision -> if false {move player to position > rewrite screen with player at center} 
#								if true {error message (detected collision try a different value)}
#reprompts for movement
#game ends when player reaches exit and displays total time

#clear the screen
os.system('clear||cls') #clears the screen for both linux and windows terminals

#reloads the starting time
def run():
	global startTime
	startTime = date.now()

#gets the current time
def getTime():
	print(date.now())
	
#gets the amount of time the program has been runing
def runTime():
	return (date.now() - startTime)
	
#starts a new instance of the game
def game():

	gridSize = [11, 11] #row x column
	
	#The entirety of the map
	gridMap = []
	
	#creates rows in the gridMap
	i = 0
	while i < gridSize[0]:
		gridMap.append([])
		#creates columns in the grid Map
		j = 0
		while j < gridSize[1]:
			gridMap[i].append([])
			j += 1
		i += 1
	
	
	#creates a grid and tiles with atributes for each point in the grid
	#tells which walls each tile has if the tile is currently part of the maze, its location
	#if the tile has been visited
	#if the tile contains the player
	#if the tile contains the exit
	i = 0
	for row in gridMap:
		j = 0 
		for box in row:
			box.append({
			"isWall": [True, True, True, True], #[top, bottom, left, right]
			"isMaze": False,
			"isLine": False,
			"location": [i, j],
			"visited": False,
			"player": False,
			"isExit": False,
			})
			j += 1
		i += 1


	
	#creates the snake class with the direction and location input
	#direction is next point to travel, and location is current point in the grid.
	#used to manage and keep track of snakes position and direction
	class Snake:
		def __init__(self, direction, location):
			self.direction = direction
			self.location = location

		def getloc(self):
			return self.location

		def getDir(self):
			return self.direction

		#newDir takes an array  ["up", "down", "left", "right"] 
		#formated as [True, True, True, True] use False as necessary
		#determines the possible directions of travel
		#falses in the possibleMoves input indicate inpossible direction to travel
		#sets the direction as a number 0-3 -> up down left right or -1 for no directions
		def newDir(self, possibleMoves):
			i = 0
			j = 0
			for move in possibleMoves:
				#if the move is true add a tally (j)
				if move:
					j += 1
				#replace move with #0-3 and value
				possibleMoves[i] = {"point": i, "value": possibleMoves[i]}
				i += 1
			#if no tallys -> no possible directions
			#if tallys picks random move
			if not j == 0:
				#creates a random number from the amount of possible moves
				randomNum = random.randint(0, j-1)
				for move in possibleMoves:
					#if move is True and the random number has been iterated through selects point
					if move["value"]:
						if randomNum == 0:
							self.direction = move["point"]
							return
						randomNum -= 1
			else:
				#returns -1 (no possible directions)
				self.direction = -1
				return

	#class to create changing values
	#a holder/replacement for global values
	#should be seperated later
	class holder: 
		def __init__(self, playerX, playerY, minRangeY, maxRangeY, minRangeX, maxRangeX, stLoc, space, snakeNum, exitX, exitY):
			self.playerX = playerX
			self.playerY = playerY
			self.minRangeY = minRangeY
			self.maxRangeY = maxRangeY
			self.minRangeX = minRangeX
			self.maxRangeX = maxRangeX
			self.stLoc = stLoc
			self.space = space
			self.snakeNum = snakeNum
			self.exitX = exitX
			self.exitY = exitY
			
	#initailize the holder as values
	values = holder(0, 0, 0, 0, 0, 0, [0, 0], 0, 0, 0, 0)

	#player
	#playerPos takes two arguments an x and a y value
	#sets the players X and Y to the respective values
	#updates the players position on the grid
	def playerPos(x, y): 
		playerPosArr = [x, y]
		gridMap[values.playerX][values.playerY][0]["player"] = False
		gridMap[x][y][0]["player"] = True
		values.playerX = playerPosArr[0]
		values.playerY = playerPosArr[1]
	
	#creates an 11 by 11 grid to be displayed by the screenk
	#prevents out of range error as well as adding what falls over the edge to the other side to maintain 11x11 grid
	#sets the X and Y ranges
	def setScreen():
		#centers around the player Y position range of 11
		values.maxRangeY = values.playerY + 6
		values.minRangeY = values.playerY - 5
		#if Y range is greater than the grid increase Y min by spill over
		if values.maxRangeY > gridSize[1]:
			values.minRangeY -= values.maxRangeY - (gridSize[1])
		#if Y range dips below grid increase Y max by spill over, and set min Y to zero to prevent error
		if values.minRangeY < 0:
			values.minRangeY = 0
			values.maxRangeY += -1 * (values.playerY - 5)

		#centers around the player X position range of 11
		values.minRangeX = values.playerX - 5
		values.maxRangeX = values.playerX + 6
		#if X range is greater than the grid increase X min by spill over
		if values.maxRangeX > gridSize[0]:
			values.minRangeX -= values.maxRangeX - (gridSize[0])
		#if X range dips below grid increase X max by spill over, and set min X to zero to prevent error
		if values.minRangeX < 0:
			values.minRangeX = 0
			values.maxRangeX += -1 * (values.playerX - 5)

	setScreen()
	
	#getPos takes to agruments and x and a y cordinate
	#returns the tile data of in the given x y location
	def getPos(x, y):
		return gridMap[x][y]

	#Create default values
	exitDefault = True
	startDefault = True
	
	#exit generation defaults to top right corner
	if exitDefault == True:
		#gets top right corner of grid
		getPos(gridSize[0] - 1, gridSize[1] - 1)[0]["isExit"] = True
		#sets the exitX and exit Y variables to the exit location
		values.exitX = gridSize[0] - 1
		values.exitY = gridSize[1] - 1
		
	#start generation defaults to bottom left corner
	if startDefault == True:
		#sets position to (0, 0)
		x = 0
		y = 0
		playerPos(x, y)
		
	#possiblMove takes no arguments
	#tests if the near by location is unvisited and part of the map
	#creates an array used to help determine the random direction for the snake
	#if a possible move appends true to an array
	#if not possible appends false
	#returns array
	def possibleMove():
		PossibleMoveArr = []
		#if the snakes Y location + 1 is a point in the grid
		if s1.getloc()[1] + 1 < gridSize[0]:
			#if the Y location +1 has not been visited or is part of the maze append true
			if not getPos(s1.getloc()[0], s1.getloc()[1] + 1)[0]["visited"] or getPos(s1.getloc()[0], s1.getloc()[1] +1)[0]["isMaze"]:
				PossibleMoveArr.append(True)
			else:
				PossibleMoveArr.append(False)
		else:
			PossibleMoveArr.append(False)
		#if the snakes Y location - 1 is a point in the grid
		if s1.getloc()[1] - 1 >= 0:
			#if the Y location -1 has not been visited or is part of the maze append true
			if not getPos(s1.getloc()[0], s1.getloc()[1] -1)[0]["visited"] or getPos(s1.getloc()[0], s1.getloc()[1] -1)[0]["isMaze"]:
				PossibleMoveArr.append(True)
			else:
				PossibleMoveArr.append(False)
		else:
			PossibleMoveArr.append(False)
		#if the snakes X location - 1 is a point in the grid
		if s1.getloc()[0] - 1 >= 0:
			#if the X location -1 has not been visited or is part of the maze append true
			if not getPos(s1.getloc()[0] -1, s1.getloc()[1])[0]["visited"] or getPos(s1.getloc()[0] -1, s1.getloc()[1])[0]["isMaze"]:
				PossibleMoveArr.append(True)
			else:
				PossibleMoveArr.append(False)
		else:
			PossibleMoveArr.append(False)
		#if the snakes X location - 1 is a point in the grid
		if s1.getloc()[0] + 1 < gridSize[1]:
			#if the X location -1 has not been visited or is part of the maze append true
			if not getPos(s1.getloc()[0] +1, s1.getloc()[1])[0]["visited"] or getPos(s1.getloc()[0] +1, s1.getloc()[1])[0]["isMaze"]:
				PossibleMoveArr.append(True)
			else:
				PossibleMoveArr.append(False)
		else:
			PossibleMoveArr.append(False)
		#return the array
		return PossibleMoveArr
	
	#newVisit takes 6 arguments, [current X, current Y, future X, future Y, direction to remove wall, opposite wall direction]
	#sets the current and future locations as visited and part of the line
	#removes the walls in that have been traveled over
	#sets the snakes new location
	def newVisit(x, y, locX, locY, direct1, direct2):
		getPos(x, y)[0]["visited"] = True
		getPos(x, y)[0]["isLine"] = True
		getPos(x, y)[0]["isWall"][direct1] = False
		s1.location = [locX, locY]
		getPos(locX, locY)[0]["visited"] = True
		getPos(locX, locY)[0]["isLine"] = True
		getPos(locX, locY)[0]["isWall"][direct2] = False
	
	
	#makePath takes one argument a starting location
	#from that starting location the snake moves around the maze randomly until it links with another part of the maze
	#if it gets stuck the snake tries re pathing from the begining and makes its way down the line until it can path again
	#if for some reason it breaks prematurely, the tiles that were iterated over are reset
	#this is the bulk of the actual maze generation
	def makePath(startingLoc):
		smoothBreak = False
		#an array to keep track of all visited locations by snake
		locationData = [startingLoc]
		#loop to continue until the snake has met with an existing part of the maze
		while True:
			#changes direction of the snake
			s1.newDir(possibleMove())
			
			#if no possible directions of travel
			#if this is the first snake, break
			#else backtrack
			if s1.getDir() == -1:
				if values.snakeNum == 0:
					smoothBreak = True
					break
				else:
					i = 0
					#starts back at the first point in the snake and checks for possible moves
					#if none are found checks the next point on the path
					while s1.getDir() == -1:
						s1.location = locationData[i]
						s1.newDir(possibleMove())
						i += 1
			#if the location == to part of the maze -> Stop
			if getPos(s1.getloc()[0], s1.getloc()[1])[0]["isMaze"]:
				smoothBreak = True
				break

			#checks what direction the snake is traveling in, Up, Down, left, Right
			#creates a new visit for the new tile location
			#adds the new tiles location to the tile array
			if s1.getDir() == 0:
				newVisit(s1.getloc()[0], s1.getloc()[1], s1.getloc()[0], s1.getloc()[1] + 1, 0, 1)
				locationData.append(s1.getloc())
			elif s1.getDir() == 1:
				newVisit(s1.getloc()[0], s1.getloc()[1], s1.getloc()[0], s1.getloc()[1] - 1, 1, 0)
				locationData.append(s1.getloc())
			elif s1.getDir() == 2:
				newVisit(s1.getloc()[0], s1.getloc()[1], s1.getloc()[0] - 1, s1.getloc()[1], 2, 3)
				locationData.append(s1.getloc())
			elif s1.getDir() == 3:
				newVisit(s1.getloc()[0], s1.getloc()[1], s1.getloc()[0] + 1, s1.getloc()[1], 3, 2)
				locationData.append(s1.getloc())
					
		#iterates through the locations and makes them part of the maze if the snake sucessfully connected
		#else resets the tiles at those locations
		for location in locationData:
			if smoothBreak == True:
				getPos(location[0], location[1])[0]["isMaze"] = True
			else:
				getPos(location[0], location[1])[0]["isWall"] = [True, True, True, True]

		#resets the locationData array
		locationData = [startingLoc]
	
	#if space == 0 there are still unvisited locations in the grid
	values.space = 0
	
	#newStLoc takes no arguments
	#it determines if start locations still exist
	#if they do it sets a new start location
	#if they do not sets space to 2 ending the snake loop
	def newStLoc():
		openPoints = []
		#iterates through each cell of the grid map
		for row in gridMap:
			for box in row:
				#if the tile is part of the maze adds it to the openPoints array
				if box[0]["isMaze"] == False:
					openPoints.append(box)
					
		#gets last item position in the array
		num = len(openPoints) - 1
		#if there are still locations available
		if num >= 0:
			#picks a random point between 0 and the number of items in the array
			point = random.randint(0, num)
			#sets the new starting location to the randomly selected position in the array
			values.stLoc = openPoints[point][0]['location']
		else:
			values.space = 2
	
	#continuously creates new snakes at different starting locations
	while values.space < 1:
		#sets a new start location
		newStLoc()
		#creates a snake at the start location
		s1 = Snake(0, values.stLoc)
		#path finds to an existing point in the maze
		makePath(values.stLoc)
		#helps track the number of snakes
		values.snakeNum += 1

		
	
	#sets up the turtle graphics
	tur.setup(55 * 11, 55 * 11)
	#helps make the turtile practically instantainious
	tur.delay(0)
	tur.ht()
	tur.tracer(0, 0)
	#sets the pen
	tur.penup()
	tur.pensize(7)
	
	displayMap = []
	
	#writeScreen takes no arguments
	#write screen writes the tile information to the screen
	#acts as a form of display
	def writeScreen():
		#clears the screen
		tur.clear()

		i = 0
		displayMap = []
		#iterates through each display cell 11 X 11
		while i < 11:
			j = 0
			#makes a grid with a range using the x and y range values
			for grid in gridMap[values.minRangeX + i][values.minRangeY : values.maxRangeY]:
				
				#forwardUpRotate takes no arguments
				#it moves the turtle forward the gird amount lifts the pen and rotates
				#getting it ready for the next wall
				def forwardUpRotate():
					tur.forward(40)
					tur.penup()
					tur.left(90)
				
				#catches some random case specific errors
				try:
					tur.setheading(90)
					#goes to grid location
					tur.goto(i * 40 - 185, j * 40 - 215)
					#displays the exit
					if grid[0].get("isExit") == True:
						tur.color("black", "yellow")
						tur.begin_fill()
					#if the Right wall exists put the pen down
					if grid[0].get("isWall")[3] == True:
						tur.pendown()
					#move forwarrd the grid amount and rotate
					forwardUpRotate()
					#if the top wall exists put the pen down
					if grid[0].get("isWall")[0] == True:
						tur.pendown()
					#move forwarrd the grid amount and rotate
					forwardUpRotate()
					#if the Left wall exists put the pen down
					if grid[0].get("isWall")[2] == True:
						tur.pendown()
					#move forwarrd the grid amount and rotate
					forwardUpRotate()
					#if the Bottom wall exists put the pen down
					if grid[0].get("isWall")[1] == True:
						tur.pendown()
					#move forwarrd the grid amount
					tur.forward(40)
					tur.penup()
					#end fill for the exit display
					if grid[0].get("isExit") == True:
						tur.end_fill()
						#returns colors to default
						tur.color("black", "white")
				except:
					print()
					
				#displays the player at the player location
				if grid[0]["location"] == [values.playerX, values.playerY]:
					#moves to the middle of the tile
					tur.left(135)
					tur.forward(28.5)
					#creates a red dot
					tur.pendown()
					tur.color("red")
					tur.dot(20)
					#resets the pen
					tur.color("black")
					tur.penup()
					
				j += 1
			i += 1
	
	writeScreen()
	#updates the turtle to display the graphics
	tur.update()
	
	#Playing functionality listens for keys and tests if game is over
	#end game takes no arguments
	#turns off the key ability
	#prints a win message 
	#starts a new maze
	def endGame():
		tur.onkey(None, "Up")  # This will call the up function if the "Left" arrow key is pressed
		tur.onkey(None, "Down")
		tur.onkey(None, "Left")
		tur.onkey(None, "Right")
		print("Yay you did it")		
		game()
	
	#testStatus takes no arguments
	#checks if the player is at the exit
	#if true ends the game
	def testStatus():
		if values.playerX == values.exitX and values.playerY == values.exitY:
			endGame()
			
	#up takes no arguments
	#checks for up key press
	#checks for a wall above the player
	#if no wall exists moves the player and updates the graphics
	def up():
		if not getPos(values.playerX, values.playerY)[0]["isWall"][0]:
			values.playerY += 1
			setScreen()
			writeScreen()
			testStatus()
			
	#down takes no arguments
	#checks for down key press
	#checks for a wall below the player
	#if no wall exists moves the player and updates the graphics
	def down():
		if not getPos(values.playerX, values.playerY)[0]["isWall"][1]:
			values.playerY -= 1
			setScreen()
			writeScreen()
			testStatus()

	#left takes no arguments
	#checks for left key press
	#checks for a wall left of the player
	#if no wall exists moves the player and updates the graphics
	def left():
		if not getPos(values.playerX, values.playerY)[0]["isWall"][2]:
			values.playerX -= 1
			setScreen()
			writeScreen()
			testStatus()

	#right takes no arguments
	#checks for right key press
	#checks for a wall right of above the player
	#if no wall exists moves the player and updates the graphics
	def right():
		if not getPos(values.playerX, values.playerY)[0]["isWall"][3]:
			values.playerX += 1
			setScreen()
			writeScreen()
			testStatus()


	#key listeners
	#call the corresponding keys function
	tur.onkey(up, "Up")
	tur.onkey(down, "Down")
	tur.onkey(left, "Left")
	tur.onkey(right, "Right")

	#enables turtle listeners
	tur.listen()
	
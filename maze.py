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
	
	
	#numbers each box in the rows
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
	
	#generates the maze walls
	#will create a line and store all line point locations, after line is finished isLine: False, isMaze: True

	
	#creates the player class with inputs for direction and location
	class Snake:
		def __init__(self, direction, location):
			self.direction = direction
			self.location = location

		def getloc(self):
			return self.location

		def getDir(self):
			return self.direction

		#takes an array  ["up", "down", "left", "right"] formated as [True, True, True, True] use False as necessary
		def newDir(self, possibleMoves):
			i = 0
			j = 0
			for move in possibleMoves:
				if move:
					j += 1
				possibleMoves[i] = {"point": i, "value": possibleMoves[i]}
				i += 1
			if not j == 0:
				randomNum = random.randint(0, j-1)
				for move in possibleMoves:
					if move["value"]:
						if randomNum == 0:
							self.direction = move["point"]
							return
						randomNum -= 1
			else:
				self.direction = -1
				return

	#print(s1.getDir())
		
	
	
	#class to create changing values
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
			
	values = holder(0, 0, 0, 0, 0, 0, [0, 0], 0, 0, 0, 0)
	
	#clears the screen
	#os.system('clear||cls') #clears the screen for both linux and windows terminals

	#temporary variables
	def playerPos(x, y): 
		playerPosArr = [x, y]
		gridMap[values.playerX][values.playerY][0]["player"] = False
		gridMap[x][y][0]["player"] = True
		values.playerX = playerPosArr[0]
		values.playerY = playerPosArr[1]
	
	#prevents out of range error as well as adding what falls over the edge to the other side to maintain 11x11 grid
	def setScreen():
		values.maxRangeY = values.playerY + 6
		values.minRangeY = values.playerY - 5
		if values.maxRangeY > gridSize[1]:
			values.minRangeY -= values.maxRangeY - (gridSize[1])
		if values.minRangeY < 0:
			values.minRangeY = 0
			values.maxRangeY += -1 * (values.playerY - 5)

		values.minRangeX = values.playerX - 5
		values.maxRangeX = values.playerX + 6
		
		if values.maxRangeX > gridSize[0]:
			values.minRangeX -= values.maxRangeX - (gridSize[0])
		if values.minRangeX < 0:
			values.minRangeX = 0
			values.maxRangeX += -1 * (values.playerX - 5)

	setScreen()
	
	def getPos(x, y):
		return gridMap[x][y]

	exitDefault = True
	startDefault = True
	
	#exit generation
	if exitDefault == True:
		getPos(gridSize[0] - 1, gridSize[1] - 1)[0]["isExit"] = True
		values.exitX = gridSize[0] - 1
		values.exitY = gridSize[1] - 1
		
	#start generation
	if startDefault == True:
		x = 0
		y = 0
		playerPos(x, y)
		
	#tests if the near by location is unvisited and part of the map
	def possibleMove():
		PossibleMoveArr = []
		if s1.getloc()[1] + 1 < gridSize[0]:
			if not getPos(s1.getloc()[0], s1.getloc()[1] + 1)[0]["visited"] or getPos(s1.getloc()[0], s1.getloc()[1] +1)[0]["isMaze"]:
				PossibleMoveArr.append(True)
			else:
				PossibleMoveArr.append(False)
		else:
			PossibleMoveArr.append(False)
		if s1.getloc()[1] - 1 >= 0:
			if not getPos(s1.getloc()[0], s1.getloc()[1] -1)[0]["visited"] or getPos(s1.getloc()[0], s1.getloc()[1] -1)[0]["isMaze"]:
				PossibleMoveArr.append(True)
			else:
				PossibleMoveArr.append(False)
		else:
			PossibleMoveArr.append(False)
		if s1.getloc()[0] - 1 >= 0:
			if not getPos(s1.getloc()[0] -1, s1.getloc()[1])[0]["visited"] or getPos(s1.getloc()[0] -1, s1.getloc()[1])[0]["isMaze"]:
				PossibleMoveArr.append(True)
			else:
				PossibleMoveArr.append(False)
		else:
			PossibleMoveArr.append(False)
		if s1.getloc()[0] + 1 < gridSize[1]:
			if not getPos(s1.getloc()[0] +1, s1.getloc()[1])[0]["visited"] or getPos(s1.getloc()[0] +1, s1.getloc()[1])[0]["isMaze"]:
				PossibleMoveArr.append(True)
			else:
				PossibleMoveArr.append(False)
		else:
			PossibleMoveArr.append(False)
		return PossibleMoveArr
	
	#takes 6 arguments, [current X, current Y, future X, future Y, direction to remove wall, opposite wall direction]
	def newVisit(x, y, locX, locY, direct1, direct2):
		getPos(x, y)[0]["visited"] = True
		getPos(x, y)[0]["isLine"] = True
		getPos(x, y)[0]["isWall"][direct1] = False
		s1.location = [locX, locY]
		getPos(locX, locY)[0]["visited"] = True
		getPos(locX, locY)[0]["isLine"] = True
		getPos(locX, locY)[0]["isWall"][direct2] = False
	
	
	#stores locations of all points visited by snake to call back later
	
	def makePath(startingLoc):
		smoothBreak = False
		locationData = [startingLoc]
		while True:
			s1.newDir(possibleMove())
			#breaks the loop if no other possible paths or it reaches part of the maze
			if s1.getDir() == -1:
				if values.snakeNum == 0:
					smoothBreak = True
					break
				else:
					i = 0
					while s1.getDir() == -1:
						s1.location = locationData[i]
						s1.newDir(possibleMove())
						i += 1
			if getPos(s1.getloc()[0], s1.getloc()[1])[0]["isMaze"]:
				smoothBreak = True
				break

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
					

		for location in locationData:
			if smoothBreak == True:
				getPos(location[0], location[1])[0]["isMaze"] = True
			else:
				getPos(location[0], location[1])[0]["isWall"] = [True, True, True, True]


		locationData = [startingLoc]
	
	values.space = 0
	
	def newStLoc():
		openPoints = []
		for row in gridMap:
			for box in row:
				if box[0]["isMaze"] == False:
					openPoints.append(box)
					
		num = len(openPoints) - 1
		if num >= 0:
			point = random.randint(0, num)
			values.stLoc = openPoints[point][0]['location']
		else:
			values.space = 2
	
	while values.space < 1:
		newStLoc()
		s1 = Snake(0, values.stLoc)
		makePath(values.stLoc)
		values.snakeNum += 1

		
	

	tur.setup(55 * 11, 55 * 11)
	tur.delay(0)
	tur.ht()
	tur.tracer(0, 0)
	tur.penup()
	tur.pensize(7)
	
	displayMap = []
	
		#Writes the screen in 11x11 grid based on the location of the player
	def writeScreen():
		#clears the screen
		#os.system('clear||cls') #clears the screen for both linux and windows terminals
		oldLocVal = gridMap[values.playerX][values.playerY]
		gridMap[values.playerX][values.playerY] = ["X"]
		i = 0
		while i < 11:
			j = 0
			displayMap.append([])
			for grid in gridMap[values.minRangeX + i][values.minRangeY : values.maxRangeY]:
				displayMap[i].append([i , j])
				j += 1
			i += 1
		gridMap[values.playerX][values.playerY] = oldLocVal
	writeScreen()
	
	
	def writeScreen2():
		#clears the screen
		tur.clear()
		#os.system('clear||cls') #clears the screen for both linux and windows terminals
		oldLocVal = gridMap[values.playerX][values.playerY]

		i = 0
		displayMap = []
		while i < 11:
			j = 0
			for grid in gridMap[values.minRangeX + i][values.minRangeY : values.maxRangeY]:
				try:
					tur.setheading(90)
					tur.goto(i * 40 - 185, j * 40 - 215)
					#displays the exit
					if grid[0].get("isExit") == True:
						tur.color("black", "yellow")
						tur.begin_fill()
					#displays the walls
					if grid[0].get("isWall")[3] == True:
						tur.pendown()
					tur.forward(40)
					tur.penup()
					tur.left(90)
					if grid[0].get("isWall")[0] == True:
						tur.pendown()
					tur.forward(40)
					tur.penup()
					tur.left(90)
					if grid[0].get("isWall")[2] == True:
						tur.pendown()
					tur.forward(40)
					tur.penup()
					tur.left(90)
					if grid[0].get("isWall")[1] == True:
						tur.pendown()
					tur.forward(40)
					tur.penup()
					if grid[0].get("isExit") == True:
						tur.end_fill()
						tur.color("black", "white")
				except:
					print()
				#displays the player
				if grid[0]["location"] == [values.playerX, values.playerY]:
					tur.left(135)
					tur.forward(28.5)
					tur.pendown()
					tur.color("red")
					tur.dot(20)
					tur.color("black")
					tur.penup()
					
				j += 1
			i += 1
		gridMap[values.playerX][values.playerY] = oldLocVal
	
	writeScreen2()
	tur.update()
	
	#Playing functionality listens for keys and tests if game is over
	
	def endGame():
		tur.onkey(None, "Up")  # This will call the up function if the "Left" arrow key is pressed
		tur.onkey(None, "Down")
		tur.onkey(None, "Left")
		tur.onkey(None, "Right")
		print("Yay you did it")		
		game()
	
	def testStatus():
		if values.playerX == values.exitX and values.playerY == values.exitY:
			endGame()
	
	def up():
		if not getPos(values.playerX, values.playerY)[0]["isWall"][0]:
			values.playerY += 1
			setScreen()
			writeScreen2()
			testStatus()
			
	def down():
		if not getPos(values.playerX, values.playerY)[0]["isWall"][1]:
			values.playerY -= 1
			setScreen()
			writeScreen2()
			testStatus()

	def left():
		if not getPos(values.playerX, values.playerY)[0]["isWall"][2]:
			values.playerX -= 1
			setScreen()
			writeScreen2()
			testStatus()

	def right():
		if not getPos(values.playerX, values.playerY)[0]["isWall"][3]:
			values.playerX += 1
			setScreen()
			writeScreen2()
			testStatus()


	tur.onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
	tur.onkey(down, "Down")
	tur.onkey(left, "Left")
	tur.onkey(right, "Right")

	tur.listen()
	
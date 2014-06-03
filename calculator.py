from Tkinter import *
from math import *

class Calculator:
	def __init__(self):
		self.history = True
		self.scientific = False
		self.colorList = ["Blue", "Green", "Grey", "Pink", "Purple", "Light Blue", "Light Green"]
		self.color = "Grey"
		self.regCalculator()
		
	def regCalculator(self):
		self.buttons = ["7", "8", "9", "/", "(", "4", "5", "6", "*", ")", "1", "2", "3", "-", "C", "0", ".", "(-)", "+", "="]
		self.initialize()
	
	def sciCalculator(self):
		self.buttons = ["asin", "acos", "atan", "^", "pi", "sin", "cos", "tan", "log", "sqrt", "7", "8", "9", "/", "(", "4", "5", "6", "*", ")", "1", "2", "3", "-", "C", "0", ".", "(-)", "+", "="]
		self.initialize()
	
	def initialize(self):
		self.root = Tk()
		self.root.title("Calculator")
		
		#--------------- Create Frames ---------------
		self.displayFrame = Frame(self.root)
		self.displayFrame.pack()
		
		self.buttonsFrame = Frame(self.root)
		self.buttonsFrame.pack()
		
		#--------------- Create Display ---------------
		self.display = Text(self.displayFrame, height = 2, width = 21)
		self.display.pack()
		
		#--------------- Create Menu Items ---------------
		self.menuBar = Menu(self.root)
		
		self.fileMenu = Menu(self.menuBar, tearoff = 0)
		self.fileMenu.add_command(label = "View History", command = self.historyBox)
		self.fileMenu.add_command(label = "Quit", command = self.root.destroy)
		self.menuBar.add_cascade(label = "File", menu = self.fileMenu)
		
		self.editMenu = Menu(self.menuBar, tearoff = 0)
		self.editMenu.add_command(label = "Options", command = self.optionsBox)
		self.editMenu.add_command(label = "Grapher", command = self.graphBox)
		self.menuBar.add_cascade(label = "Edit", menu = self.editMenu)
		
		self.helpMenu = Menu(self.menuBar, tearoff = 0)
		self.helpMenu.add_command(label = "About", command = self.aboutBox)
		self.menuBar.add_cascade(label = "Help", menu = self.helpMenu)
		
		self.root.config(menu = self.menuBar)
		
		#--------------- Create Buttons ---------------
		column = 0
		row = 0
		
		for button in self.buttons:
			command = lambda x = button: self.click(x)
			if button == "=":
				self.equal = Button(self.buttonsFrame, text = button, width = 3, padx = 3, pady = 3, command = command, bg = self.color)
				self.equal.grid(row = row, column = column)
			else:
				Button(self.buttonsFrame, text = button, width = 3, padx = 3, pady = 3, command = command).grid(row = row, column = column)
			column += 1
			if column > 4:
				row += 1
				column = 0
				
		self.root.mainloop()
	
	def click(self, key):
		if key == "asin":
			self.display.insert(END, "asin(")
		elif key == "acos":
			self.display.insert(END, "acos(")
		elif key == "atan":
			self.display.insert(END, "atan(")
		elif key == "^":
			self.display.insert(END, "**")
		elif key == "sin":
			self.display.insert(END, "sin(")
		elif key == "cos":
			self.display.insert(END, "cos(")
		elif key == "tan":
			self.display.insert(END, "tan(")
		elif key == "log":
			self.display.insert(END, "log10(")
		elif key == "sqrt":
			self.display.insert(END, "sqrt(")
		elif key == "=":
			self.evaluate()
		elif key == "(-)":
			self.display.insert(END, "-")
		elif key == "C":
			self.display.delete(1.0, END)
		else:
			self.display.insert(END, key)
		
	def evaluate(self):
		entry = self.display.get(1.0, END)
		try:
			result = str(eval(entry))
		except:
			self.display.delete(1.0, END)
			self.display.insert(END, "error")
			result = "ERROR"
		else:
			self.display.delete(1.0, END)
			self.display.insert(END, result)
		
		if self.history == True:
			entry = entry.strip()
			result = result.strip()

			file = open("history.txt", "a")
			file.write("%s = %s \n" % (entry, result))
			file.close()
		
	def optionsBox(self):
		self.optionsWindow = Toplevel()
		
		label = Label(self.optionsWindow, text = "Calculator Type:")
		label.pack()
		
		radFrame = Frame(self.optionsWindow)
		radFrame.pack()
		
		self.v = IntVar()
		
		radioButton1 = Radiobutton(radFrame, text = "Regular", variable = self.v, value = 1)
		if self.scientific == False:
			radioButton1.select()
		radioButton1.pack(side = LEFT)
		
		radioButton2 = Radiobutton(radFrame, text = "Scientific", variable = self.v, value = 2)
		if self.scientific == True:
			radioButton2.select()
		radioButton2.pack()
		
		label2 = Label(self.optionsWindow, text = "Other:")
		label2.pack()
		
		self.checkVar = IntVar()
		
		check = Checkbutton(self.optionsWindow, text = "Enable History", variable = self.checkVar)
		if self.history == True:
			check.select()
		check.pack()
		
		
		colorLabel = Label(self.optionsWindow, text = "Equals Sign Color:")
		colorLabel.pack()
		
		self.colorBox = Listbox(self.optionsWindow, height = 7)
		self.colorBox.pack()
		
		x = -1		
		for color in self.colorList:
			self.colorBox.insert(END, color)
			x += 1
			if color == self.color:
				self.colorBox.selection_set(x)
				self.colorBox.activate(x)
		
		okayButton = Button(self.optionsWindow, text = "Okay", width = 7, command = self.optionCommand)
		okayButton.pack()
		
	def optionCommand(self):
		self.color = self.colorBox.get(ACTIVE)
		self.equal.config(bg = self.color)
		
		if self.checkVar.get() == 1:
			self.history = True
		else:
			self.history = False
		if self.v.get() == 1:
			if self.scientific == False:
				self.optionsWindow.destroy()
			else:
				self.scientific = False
				self.root.destroy()
				self.regCalculator()
		elif self.v.get() == 2:
			if self.scientific == True:
				self.optionsWindow.destroy()
			else:
				self.scientific = True
				self.root.destroy()
				self.sciCalculator()		
		
	def aboutBox(self):
		self.aboutWindow = Toplevel()
		
		label = Label(self.aboutWindow, text = "Created by Benjamin Kumar")
		label.pack()
		
		okayButton = Button(self.aboutWindow, text = "Okay", width = 5, command = self.aboutWindow.destroy)
		okayButton.pack()
		
	def graphBox(self):
		self.graphWindow = Toplevel()

		self.width = 400
		self.height = 400

		label = Label(self.graphWindow, text = "Grapher")
		label.pack()
		
		self.entryFrame = Entry(self.graphWindow)
		self.entryFrame.pack()
		
		label2 = Label(self.entryFrame, text = "f(x) = ")
		label2.pack(side = LEFT)

		self.entry = Entry(self.entryFrame)
		self.entry.pack()

		frame = Frame(self.graphWindow)
		frame.pack()

		button1 = Button(frame, text = "Enter", command = self.graph)
		button1.pack(side = LEFT)

		button2 = Button(frame, text = "Clear", command = self.clear)
		button2.pack(side = LEFT)
		
		button3 = Button(frame, text = "Help", command = self.help)
		button3.pack(side = LEFT)

		self.canvas = Canvas(self.graphWindow, width=self.width, height=self.height)
		self.canvas.pack()

		self.createGrid(self.canvas,20)
		
	def createGrid(self, canvas, lineDistance):
		for x in range(lineDistance, self.width, lineDistance):
			if x != self.width/2:
				canvas.create_line(x, 0, x, self.height, fill = "#476042", width = 0.5)
			else:
				canvas.create_line(x, 0, x, self.height, fill = "#476042", width = 1.5)
		for y in range(lineDistance, self.height, lineDistance):
			if y != self.height/2:
				canvas.create_line(0, y, self.width, y, fill = "#476042", width = 0.5)
			else:
				canvas.create_line(0, y, self.width, y, fill = "#476042", width = 1.5)

	def graph(self):
		x = 1
		equation = self.entry.get()
		try:
			result = eval(equation)
		except:
			self.entry.delete(0, END)
			self.entry.insert(END, "error")
		else:
			list = []
			lines = []
			for x in range(-self.width/2, self.width/2):
				x = x/20.0
				try:
					result = eval(equation)
				except ZeroDivisionError:
					lines.append(self.canvas.create_line(list, width = 2))
					list = []
					self.canvas.create_line(((x*20) + (self.width/2)), 0, ((x*20) + (self.width/2)), 400, width = 2, dash = (20,))
				else:
					y = -((result)*20)
					list.append((x*20) + (self.width/2))
					list.append(y + (self.height/2))
			lines.append(self.canvas.create_line(list, width = 2))

	def clear(self):
		self.entry.delete(0, END)
		self.canvas.delete(ALL)
		self.createGrid(self.canvas,20)
		
	def help(self):
		self.helpWindow = Toplevel()
		
		self.helpText = Text(self.helpWindow, height = 20, width = 47)
		self.helpText.pack()
		
		file = open("graphHelp.txt")
		list = file.readlines()
		
		for line in list:
			self.helpText.insert(END, line)
		
		self.helpText.config(state = "disabled")		
		
	def historyBox(self):
		self.historyWindow = Toplevel()
		
		self.text = Text(self.historyWindow, height = 20, width = 47)
		self.text.pack(side = LEFT, fill = Y)
		
		self.scroll = Scrollbar(self.historyWindow)
		self.scroll.pack(side = RIGHT, fill = Y)
		
		self.scroll.config(command = self.text.yview)
		self.text.config(yscrollcommand = self.scroll.set)
		
		file = open("history.txt")
		list = file.readlines()
		
		for line in list:
			self.text.insert(END, line)
			
		self.text.config(state = "disabled")

calculator = Calculator()

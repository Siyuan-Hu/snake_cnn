import sys  
import time  
import curses

DX=[-1,0,1,0]
DY=[0,1,0,-1]

class Apple:
	def setLoc(self,_x,_y):
		self.x=_x
		self.y=_y

class Snake:
	def __init__(self):
		self.head=Knot(5,5)
		next=Knot(5,4)
		self.head.setNext(next)
		self.head.next.setNext(Knot(5,3))
	def move(self, dir):
		if self.head.x+DX[dir-1]==APPLE.x and self.head.y+DY[dir-1]==APPLE.y:
			newhead=Knot(APPLE.x,APPLE.y)
			newhead.next=self.head
			self.head=newhead
			return
		self.head.move(dir)
		draw()

class Knot:
	def __init__(self, _x, _y):
		self.next=None
		self.x=_x
		self.y=_y
	def setNext(self, knot):
		self.next=knot
	def setLoc(self, _x, _y):
		if self.next!=None:
			self.next.setLoc(self.x, self.y)
		self.x=_x
		self.y=_y
	def move(self, dir):
		self.next.setLoc(self.x, self.y)
		if dir==1:
			self.x-=1
		if dir==2:
			self.y+=1
		if dir==3:
			self.x+=1
		if dir==4:
			self.y-=1

def draw():
	stdscr.refresh()
	for i in range(10):
		for j in range(10):
			stdscr.addch(i,j,'0')
	stdscr.addch(APPLE.x,APPLE.y,'3')
	stdscr.addch(SNAKE.head.x,SNAKE.head.y,'2')
	knot=SNAKE.head.next
	while knot!=None:
		stdscr.addch(knot.x,knot.y,'1')
		knot=knot.next

def testControl():
	APPLE.setLoc(3,5)
	dirs=[1,1,1,2,2,3,3,3,3,4,4,4,4]
	for dirr in dirs:
		SNAKE.move(dirr)
		time.sleep(1)

def keyboardControl():
	while 1:
		content = raw_input()
		if content=='\x1b[A':
		    dirr=1
		if content=='\x1b[B':
		    dirr=3
		if content=='\x1b[C':
		    dirr=2
		if content=='\x1b[D':
			dirr=4
		SNAKE.move(dirr)

def test():
	dirs=[1,1,1,2,2,3]
	for dirr in dirs:
		print dirr
		sys.stdout.flush() 
		time.sleep(1)

SNAKE=Snake()
APPLE=Apple()
stdscr = curses.initscr()
#testControl()
keyboardControl()
curses.endwin()

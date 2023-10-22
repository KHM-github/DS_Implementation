from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class DrawingBox:
    def __init__(self):
        self.TopLeftX=0.0
        self.TopLeftY=0.0
        self.BottomRightX=0.0
        self.BottomRightY=0.0
        self.drawing=False
        # red에서 시작
        self.color='r'

    def MyDisplay(self):	
        # ViewPort 크기 초기 윈도우 크기와 동일하게 설정
        glViewport(0, 0, 500, 500)
        glClear(GL_COLOR_BUFFER_BIT)
        glBegin(GL_POLYGON) 
        # Coordination Conversion (From GLUT to GL + View Volume Position)
        glVertex3f(self.TopLeftX/ 500.0,(500.0-self.TopLeftY)/500.0, 0.0)     		  
        glVertex3f(self.TopLeftX/500.0,(500.0-self.BottomRightY)/500.0, 0.0)
        glVertex3f(self.BottomRightX/500.0,(500.0-self.BottomRightY)/500.0, 0.0)     	  
        glVertex3f(self.BottomRightX/500.0,(500.0-self.TopLeftY)/500.0, 0.0)

        # RGBCMY 색 변환 정의
        if self.color =='r': glColor3f(1.0,0.0,0.0)
        elif self.color =='g': glColor3f(0.0,1.0,0.0)
        elif self.color =='b': glColor3f(0.0,0.0,1.0)
        elif self.color =='c': glColor3f(0.0,1.0,1.0)
        elif self.color =='m': glColor3f(1.0,0.0,1.0)
        elif self.color =='y': glColor3f(1.0,1.0,0.0)

        glEnd()
        glFlush()			

    def MyMouseClick(self, Button, State, X, Y):	
        if Button==GLUT_LEFT_BUTTON and State==GLUT_DOWN:	
            self.TopLeftX = X
            self.TopLeftY = Y
            # 좌클릭 시 Drawing 시작
            self.drawing = True
            self.BottomRightX = self.TopLeftX
            self.BottomRightY = self.TopLeftY
        # 좌클릭 뗐을 시 Drawing 종료
        if Button ==GLUT_LEFT_BUTTON and State==GLUT_UP:
            self.drawing = False
        # 우클릭시엔 동작 X
        else: return

    def MyMouseMove(self, X, Y):	
        # 클릭하지 않고 커서 움직일 시에는 아무 동작 X
        if not self.drawing: return	
        self.BottomRightX = X
        self.BottomRightY = Y
        glutPostRedisplay()
    
    def MyKeyDown(self,key,X,Y):
        if key == b'r': self.color='r'
        elif key == b'g': self.color='g'
        elif key == b'b': self.color='b'
        elif key == b'c': self.color='c'
        elif key == b'm': self.color='m'
        elif key == b'y': self.color='y'
        glutPostRedisplay()
    # 키를 뗐을 때 redisplay -> 색상 즉시 변경
    def MyKeyUp(self, key, X, Y):
        glutPostRedisplay()

    def main(self):
        glutInit()				
        # glutInitDisplayMode(GLUT_RGB)
        glutInitWindowSize(500, 500)    	
        # glutInitWindowPosition(0, 0)
        glutCreateWindow("Mouse CallBack")

        glMatrixMode(GL_PROJECTION)   
        glLoadIdentity()
        glOrtho(0.0, 1.0, 0.0, 1.0, -1.0, 1.0) 				
        glutDisplayFunc(self.MyDisplay) 
        glutMouseFunc(self.MyMouseClick)					
        glutMotionFunc(self.MyMouseMove)	
        glutKeyboardFunc(self.MyKeyDown)	
        glutKeyboardUpFunc(self.MyKeyUp)			
        glutMainLoop()

m = DrawingBox()
m.main()

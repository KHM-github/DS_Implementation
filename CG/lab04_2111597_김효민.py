from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class MovingBox:
    def __init__(self):
        # box1 좌표, step
        self.x = 0.0
        self.y = 0.0
        self.xstep = 2.0
        self.ystep = 2.0
        # box2 좌표, step
        self.z= 33.0
        self.w= -57.0
        self.zstep = 3.0
        self.wstep = 3.0

        self.rsize = 25
        self.windowWidth = 100
        self.windowHeight =100
        self.speed = 33

    def draw(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1.0, 0.0, 0.0)    # box1
        glRectf(self.x, self.y, self.x + self.rsize, self.y - self.rsize)
        glColor3f(0.0, 1.0, 0.0)	# box2    
        glRectf(self.z, self.w, self.z + self.rsize, self.w - self.rsize)
        glutSwapBuffers()

    def TimerFunction(self, value):
        # first box
        if self.x >(self.windowWidth - self.rsize):	    # right wall
            self.xstep = -self.xstep
            self.x = self.windowWidth - self.rsize

        if self.x < -self.windowWidth:			        # left wall
            self.xstep = -self.xstep
            self.x = -self.windowWidth; 

        if self.y > self.windowHeight:			        # top wall
            self.ystep = -self.ystep
            self.y = self.windowHeight

        if self.y < (-self.windowHeight + self.rsize):	# bottom wall
            self.ystep = -self.ystep
            self.y = -self.windowHeight + self.rsize     

        self.x += self.xstep
        self.y += self.ystep

        # second box
        if self.z >(self.windowWidth - self.rsize):	    # right wall
            self.zstep = -self.zstep
            self.z = self.windowWidth - self.rsize

        if self.z < -self.windowWidth:			        # left wall
            self.zstep = -self.zstep
            self.z = -self.windowWidth; 

        if self.w > self.windowHeight:			        # top wall
            self.wstep = -self.wstep
            self.w = self.windowHeight

        if self.w < (-self.windowHeight + self.rsize):	# bottom wall
            self.wstep = -self.wstep
            self.w = -self.windowHeight + self.rsize     

        self.z += self.zstep
        self.w += self.wstep

        glutPostRedisplay()
        glutTimerFunc(self.speed, self.TimerFunction, 1)
        
    def MyMainMenu(self, entryID):

        # speed는 step사이 간격 -> 높을수록 느려짐		
        if entryID == 1:
            self.speed = 66
        elif entryID == 2:
            self.speed = 33
        elif entryID == 3:
            self.speed = 11

        glutPostRedisplay()
    			

    def ChangeSize(self, w, h):

        if (h == 0): h = 1
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        aspectRatio = w / h
        if w <= h:
            self.windowWidth = 100
            self.windowHeight = 100 / aspectRatio   # use aspectRatio
            glOrtho(-100.0, 100.0, -self.windowHeight, self.windowHeight, 1.0, -1.0)
        else:
            self.windowWidth = 100 * aspectRatio    # use aspectRatio
            self.windowHeight = 100
            glOrtho(-self.windowWidth, self.windowWidth, -100.0, 100.0, 1.0, -1.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

    def main(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
        glutInitWindowSize(800, 600)
        glutCreateWindow("Timer CallBack")

        # 속도 조절 Menu (우클릭 시 호출)
        glutCreateMenu(self.MyMainMenu)
        glutAddMenuEntry("Slow",1)
        glutAddMenuEntry("Normal",2)
        glutAddMenuEntry("Fast",3)
        glutAttachMenu(GLUT_RIGHT_BUTTON)

        glutDisplayFunc(self.draw)
        glutReshapeFunc(self.ChangeSize)
        glutTimerFunc(self.speed, self.TimerFunction, 1)

        glutMainLoop()
            
d = MovingBox()
d.main()
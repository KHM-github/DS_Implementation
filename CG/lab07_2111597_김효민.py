# Solar System and Mars

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class SolarSystem:
    def __init__(self):
        self.angle = 0.0
        self.angle2 = 0.0
        self.speed = 35
        self.depth = 1
        self.myview = 9

    def menu(self, value):
        if value == 1:
            self.speed = 50  # fast
        elif value == 2:
            self.speed = 35  # normal
        elif value == 3:
            self.speed = 15  # slow
        elif value == 4:
            self.depth = 1
        elif value == 5:
            self.depth = 0

        if value >= 6:
            self.myview = value
        glutPostRedisplay()  # create display event

    def display(self):
        glShadeModel(GL_SMOOTH)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        if self.depth == 1:
            glEnable(GL_DEPTH_TEST)  # visibility test on
        else:
            glDisable(GL_DEPTH_TEST)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        if self.myview == 6:  # front view
            gluLookAt(0.0, 0.0, 320.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        elif self.myview == 7:  # top view
            gluLookAt(0.0, 320.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0)
        elif self.myview == 8:  # Side view
            gluLookAt(320.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        elif self.myview == 9:  # perspective view
            gluLookAt(30.0, 30.0, 300.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

        # Sun
        glColor3ub(200, 0, 200)
        glutSolidSphere(13.0, 15, 15)
        #  Earth
        glPushMatrix()
        glRotatef(self.angle, 0.0, 1.0, 0.0)
        glTranslatef(70.0, 0.0, 0.0)
        glColor3ub(0, 255, 0)
        glutSolidSphere(8.0, 15, 15)

        # Moon
        glPushMatrix()
        glRotatef(self.angle, 0.0, 1.0, 0.0)
        glTranslatef(20.0, 0.0, 0.0)
        glColor3ub(255, 255, 0)
        glutSolidSphere(4.0, 15, 15)
        glPopMatrix()
        glPopMatrix()

        # Mars
        glPushMatrix()
        glRotatef(45, 0.0, 0.0, 1.0)  # z-rotation by 45 degree
        glRotatef(self.angle2, 0.0, 1.0, 0.0)
        glTranslatef(-120.0, 0.0, 0.0)
        glColor3ub(255, 0, 0)
        glutSolidSphere(5.0, 20, 20)

        # Mars' Moon
        glPushMatrix()  # save ctm
        glRotatef(self.angle2, 0.0, 1.0, 0.0)  # rotate
        glTranslatef(20.0, 0.0, 0.0)  # distance from mars
        glColor3ub(0, 0, 255)
        glutSolidSphere(3.0, 15, 15)  # draw mars moon
        glPopMatrix()
        glPopMatrix()
        # gluLookAt(0.0, 30.0, 300.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

        glutSwapBuffers()

    def timerFunc(self, value):
        self.angle += 2.5
        if self.angle >= 360.0:
            self.angle = 0.0

        self.angle2 -= 1.2  # decrease angle by 1.2
        if self.angle2 >= 360.0:
            self.angle2 = 0.0  # angle2 reset to 360

        glutPostRedisplay()  # create display event
        glutTimerFunc(self.speed, self.timerFunc, 1)  # create new timer

    def changeSize(self, w, h):
        if h == 0:
            h = 1
        aspect = w / h

        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        gluPerspective(45.0, aspect, 1.0, 1500.0)

    def main(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(800, 600)
        glutCreateWindow(b"OpenGL Solar System")

        glEnable(GL_DEPTH_TEST)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glutReshapeFunc(self.changeSize)
        glutDisplayFunc(self.display)

        nMenu = glutCreateMenu(self.menu)
        glutAddMenuEntry("Slow", 1)
        glutAddMenuEntry("Normal", 2)
        glutAddMenuEntry("Fast", 3)
        glutAddMenuEntry("Depth Test On", 4)
        glutAddMenuEntry("Depth Test Off", 5)
        glutAddMenuEntry("Front View", 6)
        glutAddMenuEntry("Top View", 7)
        glutAddMenuEntry("Side View", 8)
        glutAddMenuEntry("Perspective View", 9)
        glutAttachMenu(GLUT_RIGHT_BUTTON)

        glutTimerFunc(self.speed, self.timerFunc, 1)
        glutMainLoop()


s = SolarSystem()
s.main()

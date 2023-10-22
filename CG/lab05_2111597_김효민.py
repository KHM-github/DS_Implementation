# rect 그리기와 solar system

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class SolarSystem:
    def __init__(self):
        self.entryID = 1

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        if self.entryID == 1:
            self.drawBox_a()
        elif self.entryID == 2:
            self.drawBox_b()
        elif self.entryID == 3:
            self.drawBox_c()
        elif self.entryID == 4:
            self.drawSolar()
        glFlush()

    def drawBox_a(self):
        glTranslatef(0.0, 0.0, 0.0)
        glColor(1.0, 0.0, 0.0)
        glRectf(0.1, -0.1, -0.1, 0.1)
        glTranslate(-0.6, 0, 0)
        glColor(0, 0, 1.0)
        glRectf(0.1, -0.1, -0.1, 0.1)
        glTranslate(0, -0.5, 0)
        glColor(1, 1, 0)
        glRectf(0.1, -0.1, -0.1, 0.1)

    def drawBox_b(self):
        glTranslatef(0.0, 0.0, 0.0)
        glColor(1, 0, 0)
        glRectf(0.1, -0.1, -0.1, 0.1)
        glTranslate(-0.5, 0, 0)
        glRotate(45, 0.0, 0.0, 1.0)
        glColor(1, 1, 0)
        glRectf(0.1, -0.1, -0.1, 0.1)

    def drawBox_c(self):
        glTranslatef(0.0, 0.0, 0.0)
        glColor(1, 0, 0)
        glRectf(0.1, -0.1, -0.1, 0.1)
        glRotate(45, 0.0, 0.0, 1.0)
        glTranslate(-0.6, 0, 0)
        glColor(1, 1, 0)
        glRectf(0.1, -0.1, -0.1, 0.1)

    def drawSolar(self):
        glTranslatef(0.0, 0.0, 0.0)

        # sun
        glColor3f(1.0, 0.0, 0.0)
        glutSolidSphere(0.15, 15, 15)

        glPushMatrix()  # Save the sun's position

        glTranslatef(-0.5, 0.5, 0.0)  # move to the earth's position
        glColor3f(0.0, 0.0, 1.0)
        glutSolidSphere(0.1, 15, 15)  # earth

        glPushMatrix()  # save the earth's position

        # move to the moon position
        glTranslatef(1, -0.25, 0.0)
        glColor3f(1.0, 1.0, 1.0)
        glutSolidSphere(0.05, 15, 15)  # moon

        # back to the earth's position
        glPopMatrix()
        # back to the sun's position
        glPopMatrix()

        # save sun's position
        glPushMatrix()
        glTranslatef(0.5, 0.0, 0.0)
        # draw mars here
        glColor3f(0.0, 1.0, 0.0)
        glutSolidSphere(0.12, 15, 15)  # draw mars
        # back to the sun
        glPopMatrix()
        glFlush()

    def myMenu(self, entryID):
        self.entryID = entryID
        if entryID == 1:
            self.drawBox_a()
        elif entryID == 2:
            self.drawBox_b()
        elif entryID == 3:
            self.drawBox_c()
        elif entryID == 4:
            self.drawSolar()
        glutPostRedisplay()

    def main(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(600, 600)
        glutInitWindowPosition(0, 0)
        glutCreateWindow(b"Solar System")

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)

        MyMainMenuID = glutCreateMenu(self.myMenu)
        glutAddMenuEntry("draw a", 1)
        glutAddMenuEntry("draw b", 2)
        glutAddMenuEntry("draw c", 3)
        glutAddMenuEntry("draw solar", 4)
        glutAttachMenu(GLUT_RIGHT_BUTTON)

        # register display callback
        glutDisplayFunc(self.display)
        glutMainLoop()


s = SolarSystem()
s.main()

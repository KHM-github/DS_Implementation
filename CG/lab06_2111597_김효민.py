# View 4종류 + Camera Work 4종류

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class Viewing:
    def __init__(self):
        self.vertices = [
            [-1.0, -1.0, -1.0],
            [1.0, -1.0, -1.0],
            [1.0, 1.0, -1.0],
            [-1.0, 1.0, -1.0],
            [-1.0, -1.0, 1.0],
            [1.0, -1.0, 1.0],
            [1.0, 1.0, 1.0],
            [-1.0, 1.0, 1.0],
        ]

        self.colors = [
            [0.0, 0.0, 0.0],
            [1.0, 0.0, 0.0],
            [1.0, 1.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [1.0, 0.0, 1.0],
            [1.0, 1.0, 1.0],
            [0.0, 1.0, 1.0],
        ]

        self.myview = 7
        self.camera_work = 1

        # Rotation angle and distance
        self.angle = 0.0
        self.distance = 0.0

    def polygon(self, a, b, c, d):
        glBegin(GL_POLYGON)
        glColor3fv(self.colors[a])
        glVertex3fv(self.vertices[a])
        glColor3fv(self.colors[b])
        glVertex3fv(self.vertices[b])
        glColor3fv(self.colors[c])
        glVertex3fv(self.vertices[c])
        glColor3fv(self.colors[d])
        glVertex3fv(self.vertices[d])
        glEnd()

    def colorcube(self):
        self.polygon(0, 3, 2, 1)
        self.polygon(4, 7, 6, 5)
        self.polygon(3, 7, 6, 2)
        self.polygon(0, 4, 5, 1)
        self.polygon(1, 2, 6, 5)
        self.polygon(0, 3, 7, 4)

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # tilting
        if self.camera_work == 0:
            glRotatef(self.angle, 1.0, 0.0, 0.0)  # x axis
            print("Tilting")
        # panning
        elif self.camera_work == 1:
            glRotatef(self.angle, 0.0, 1.0, 0.0)  # y axis
            print("Panning")
        # rolling
        elif self.camera_work == 2:
            glRotatef(self.angle, 0.0, 0.0, 1.0)  # z axis
            print("Rolling")
        # dollying
        elif self.camera_work == 3:
            glTranslatef(0.0, 0.0, self.distance)
            print("Dollying")

        if self.myview == 4:  # front view
            gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
            print("Front View")
        elif self.myview == 5:  # top view
            gluLookAt(0.0, 5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0)
            print("Top View")
        elif self.myview == 6:  # side view
            gluLookAt(5.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
            print("Side View")
        elif self.myview == 7:  # perspective view
            gluLookAt(2.0, 2.0, 7.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
            print("Perspective View")

        self.colorcube()
        glutSwapBuffers()

    # Respond to arrow keys
    def SpecialKeys(self, key, x, y):
        if key == GLUT_KEY_UP:
            self.distance -= 5.0
        elif key == GLUT_KEY_DOWN:
            self.distance += 5.0
        elif key == GLUT_KEY_LEFT:
            self.angle -= 3.0
        elif key == GLUT_KEY_RIGHT:
            self.angle += 3.0
        self.angle = self.angle % 360
        glutPostRedisplay()

    def myMenu(self, value):
        if value < 4:
            self.camera_work = value
            # self.myview = 7
        else:
            self.myview = value

        self.angle = 0.0
        self.distance = 0.0
        glutPostRedisplay()

    def myReshape(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()

        if w <= h:
            glFrustum(-2.0, 2.0, -2.0 * h / w, 2.0 * h / w, 2.0, 20.0)
        else:
            glFrustum(-2.0 * w / h, 2.0 * w / h, -2.0, 2.0, 2.0, 20.0)

        glMatrixMode(GL_MODELVIEW)

    def main(self):
        glutInit()
        glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
        glutInitWindowSize(500, 500)
        glutCreateWindow(b"colorcube viewpoint")

        glutReshapeFunc(self.myReshape)
        glutDisplayFunc(self.display)
        glutSpecialFunc(self.SpecialKeys)

        # Create the Menu
        glutCreateMenu(self.myMenu)
        glutAddMenuEntry("Tilting", 0)
        glutAddMenuEntry("Panning", 1)
        glutAddMenuEntry("Rolling", 2)
        glutAddMenuEntry("Dolling", 3)
        glutAddMenuEntry("Front View", 4)
        glutAddMenuEntry("Top View", 5)
        glutAddMenuEntry("Side View", 6)
        glutAddMenuEntry("Perspective", 7)
        glutAttachMenu(GLUT_RIGHT_BUTTON)

        glEnable(GL_DEPTH_TEST)
        glutMainLoop()


v = Viewing()
v.main()

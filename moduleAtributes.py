import numpy as np
import matplotlib.pyplot as plt


class Atributes3d():
    def __init__(self, showAxes, x_y_z, square, square_p, figure, ax):
        self.showAxes = showAxes
        self.showX_Y_Z = x_y_z
        self.square = square

        if showAxes:
            ax.set_xlabel('X', fontsize=16, color='royalblue')
            ax.set_ylabel('Y', fontsize=16, color='royalblue')
            ax.set_zlabel('Z', fontsize=16, color='royalblue')
        if x_y_z:
            if figure == 'tor':
                axes = plt.gca()
                axes.set_zlim([0, 2])
            elif figure == 'halfSphere':
                axes = plt.gca()
                axes.set_zlim([0, 4])
            elif figure == 'cube' or figure == 'sphere':
                axes = plt.gca()
                axes.set_zlim([-2, 2])
                axes.set_xlim([-2, 2])
                axes.set_ylim([-2, 2])
        if square:
            if figure == 'tor':
                S = 4 * (pow(np.pi, 2)) * square_p
                S = str(round(S, 2))
                ax.text2D(-0.15, 1.04, "Площадь фигуры(Тора): " + str(S), color='royalblue',
                          fontsize=13, transform=ax.transAxes)
                ax.text2D(-0.15, 0.96, "Формула: " +"S=4π^2*Rr ", color='royalblue',
                          fontsize=13, transform=ax.transAxes)
            elif figure == 'halfSphere':
                S = (4 * np.pi * (pow(square_p, 2))) / 2
                S = str(round(S, 2))
                ax.text2D(-0.15, 1.04, "Площадь фигуры(Полусферы): " + str(S), color='royalblue',
                          fontsize=13, transform=ax.transAxes)
                ax.text2D(-0.15, 0.96, "Формула: " + "S=(4πR^2)/2 ", color='royalblue',
                          fontsize=13, transform=ax.transAxes)
            elif figure == 'cube':
                S = 6*pow(square_p, 2)
                S = str(round(S, 2))
                ax.text2D(-0.15, 1.04, "Площадь фигуры(Куба): " + str(S), color='royalblue',
                          fontsize=13, transform=ax.transAxes)
                ax.text2D(-0.15, 0.96, "Формула: " + "S=6h^2 ", color='royalblue',
                          fontsize=13, transform=ax.transAxes)
            elif figure == 'sphere':
                S = (4 * np.pi * (pow(square_p, 2)))
                S = str(round(S, 2))
                ax.text2D(-0.15, 1.04, "Площадь фигуры(Сферы): " + str(S), color='royalblue',
                          fontsize=13, transform=ax.transAxes)
                ax.text2D(-0.15, 0.96, "Формула: " + "S=4πR^2 ", color='royalblue',
                          fontsize=13, transform=ax.transAxes)

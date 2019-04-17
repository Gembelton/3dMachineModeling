"Импортирование модулей для построения пространственных фигур"
import numpy as np
import matplotlib.pyplot as plt
import socket
from tkinter import *
from itertools import product, combinations

# импортирование чекбоксов,дополнительного меню, и дополнительных атрибутов при построении
from moduleAtributes import Atributes3d
from moduleCheckbar import Checkbar
from moduleOtherDraw import OtherDraw


class ButChooseTor():

    def __init__(self):
        self.but = Button(root,
                          text="Тор",  # надпись на кнопке
                          width=14,  # ширина
                          bg="white", fg="black", font="courier 14")  # цвет фона и надписи
        self.but.bind("<Button-1>", self.localEvent)  # чем нажать, чтобы вызвать (что-то
        self.but.grid(row=2, column=1)  # размещение кнопки
        self.S = 0

    # само событие
    def localEvent(self, event):
        fig = plt.figure(facecolor='white')
        fig.canvas.set_window_title('Изображение тора')
        ax = fig.add_subplot(111, projection='3d')
        # атрибуты(чекбоксы):
        atribute = Atributes3d(chCoords.var_states(),
                               chAxes.var_states(),
                               chSquare.var_states(),
                               0.5, 'tor', ax)  # радиус,название,поверхность

        t = np.linspace(0, 2 * np.pi, 50)
        th, ph = np.meshgrid(t, t)
        r = 0.2
        x, y, z = (1 + r * np.cos(ph)) * np.cos(th), \
                  (1 + r * np.cos(ph)) * np.sin(th), \
                  r * np.sin(ph)

        r * np.sin(ph)

        ax.plot_wireframe(x, y, z, rstride=2, cstride=2, linewidth=1)
        self.but.flash()
        plt.show()


class ButChooseHalfSphere():

    def __init__(self):
        self.but = Button(root,
                          text="Полусфера",  # надпись на кнопке
                          width=14,  # ширина
                          bg="white", fg="black", font="courier 14")  # цвет фона и надписи
        self.but.bind("<Button-1>", self.localEvent)  # чем нажать, чтобы вызвать (что-то
        self.but.grid(row=3, column=1)  # размещение кнопки

    # само событие
    def localEvent(self, event):
        fig = plt.figure(facecolor='white')
        fig.canvas.set_window_title('Изображение полусферы')
        ax = fig.add_subplot(111, projection='3d')
        # атрибуты(чекбоксы):
        atribute = Atributes3d(chCoords.var_states(),
                               chAxes.var_states(),
                               chSquare.var_states(),
                               0.5, 'halfSphere', ax)  # радиус,название,поверхность

        # phi azimuthal angle
        n_theta = 25  # плотность точек по горизонтали
        n_phi = 20  # плотность точек по вертикали
        radius = 2
        theta, phi = np.mgrid[0.0:0.5 * np.pi:n_theta * 1j, 0.0:2.0 * np.pi:n_phi * 1j]
        x = radius * np.sin(theta) * np.cos(phi)
        y = radius * np.sin(theta) * np.sin(phi)
        z = radius * np.cos(theta)
        inp = []
        for j in phi[0, :]:
            for i in theta[:, 0]:
                val = 0.7 + np.cos(j) * np.sin(i + np.pi / 4.)  # put something useful here
                inp.append([j, i, val])
        inp = np.array(inp)

        # reshape the input array to the shape of the x,y,z arrays.
        c = inp[:, 2].reshape((n_phi, n_theta)).T

        # Set colours and render

        # use facecolors argument, provide array of same shape as z
        # cm.<cmapname>() allows to get rgba color from array.
        # array must be normalized between 0 and 1
        ax.plot_wireframe(x, y, z, rstride=2, cstride=2, linewidth=1)
        self.but.flash()
        plt.show()


class ButChooseCube():

    def __init__(self):
        self.but = Button(root,
                          text="Куб",  # надпись на кнопке
                          width=14,  # ширина
                          bg="white", fg="black", font="courier 14")  # цвет фона и надписи
        self.but.bind("<Button-1>", self.localEvent)  # чем нажать, чтобы вызвать (что-то
        self.but.grid(row=4, column=1)  # размещение кнопки
        self.S = 0

    # само событие
    def localEvent(self, event):
        fig = plt.figure(facecolor='white')
        fig.canvas.set_window_title('Изображение куба')
        ax = fig.add_subplot(111, projection='3d')
        atribute = Atributes3d(chCoords.var_states(),
                               chAxes.var_states(),
                               chSquare.var_states(),
                               2, 'cube', ax)  # радиус,название,поверхность

        # draw cube
        r = [-1, 1]
        for s, e in combinations(np.array(list(product(r, r, r))), 2):
            if np.sum(np.abs(s - e)) == r[1] - r[0]:
                ax.plot3D(*zip(s, e), color="royalblue", linewidth=1)
        self.but.flash()
        plt.show()


class ButChooseSphere():

    def __init__(self):
        self.but = Button(root,
                          text="Сфера",  # надпись на кнопке
                          width=14,  # ширина
                          bg="white", fg="black", font="courier 14")  # цвет фона и надписи
        self.but.bind("<Button-1>", self.localEvent)  # чем нажать, чтобы вызвать (что-то
        self.but.grid(row=5, column=1)  # размещение кнопки

    # само событие
    def localEvent(self, event):
        fig = plt.figure(facecolor='white')
        fig.canvas.set_window_title('Изображение сферы')
        ax = fig.add_subplot(111, projection='3d')
        atribute = Atributes3d(chCoords.var_states(),
                               chAxes.var_states(),
                               chSquare.var_states(),
                               0.5, 'sphere', ax)  # радиус,название,поверхность
        # draw сфера
        r = [-1, 1]
        u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:30j]
        x = np.cos(u) * np.sin(v)
        y = np.sin(u) * np.sin(v)
        z = np.cos(v)
        ax.plot_wireframe(x, y, z, color="royalblue", linewidth=1)
        self.but.flash()
        plt.show()


class ButHelp():

    def __init__(self):
        self.but = Button(root,
                          text="Помощь",  # надпись на кнопке
                          width=10,  # ширина
                          bg="white", fg="black", font=("courier", '12', 'bold'))  # цвет фона и надписи
        self.but.bind("<Button-1>", self.localEvent)  # чем нажать, чтобы вызвать (что-то
        self.but.grid(row=5, column=2)  # размещение кнопки

    # само событие
    def localEvent(self, event):
        helpRoot = Tk()  # окно
        helpRoot.title(u'Помощь')
        helpRoot.geometry('350x200+500+200')  # ширина=303, высота=295, расположение на экране x,y
        helpRoot.resizable(False, False)  # разрешение на изменение размера окна, ширина и высота
        data = 0
        try:
            sock = socket.socket()
            sock.connect(('localhost', 9090))
            sock.send(b'requestToServer')
            data = sock.recv(1024)
            sock.close()
            Label(helpRoot, text=data, justify=LEFT, font="courier 12").grid(row=1, column=1, sticky=W)
        except:
            Label(helpRoot, text="     "
                                 "Соединение не установлено", font="courier 12").grid(row=1, column=1, sticky=W)


if __name__ == '__main__':
    root = Tk()  # окно
    root.title(u'Построение пространственных фигур')
    root.geometry('463x212+480+200')  # ширина=303, высота=295, расположение на экране x,y
    root.resizable(False, False)  # разрешение на изменение размера окна, ширина и высота
    Label(root, text="  Выбор фигуры:", font="courier 12").grid(row=1, column=1, sticky=W)
    Label(root, text="   Дополнительные параметры:", font="courier 12").grid(row=1, column=2)

    ##########################################################################
    # экземпляры классов кнопок
    butTor = ButChooseTor()
    butHalfSphere = ButChooseHalfSphere()
    butCube = ButChooseCube()
    butSphere = ButChooseSphere()
    butOtherDraw = OtherDraw(root)
    butHelp = ButHelp()
    chAxes = Checkbar(root, "Зафиксировать оси", [2, 2])
    chCoords = Checkbar(root, "Подписать оси", [3, 2])
    chSquare = Checkbar(root, "Вычислить S", [4, 2])
    ##########################################################################

    root.mainloop()

# создать кнопочку помощь, в которой будет информация отправленная с сервера

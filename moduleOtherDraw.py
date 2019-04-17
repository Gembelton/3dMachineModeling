import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from itertools import product, combinations
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D


class OtherDraw():

    def __init__(self, screen):
        self.but = Button(screen,
                          text='Свой рисунок',  # надпись на кнопке
                          width=14,  # ширина
                          bg="lightcyan", fg="black", font=('Courier', '14', 'bold'))  # цвет фона и надписи
        self.but.bind("<Button-1>", self.localEvent)  # чем нажать, чтобы вызвать (что-то
        self.but.grid(row=6, column=1)  # размещение кнопки
        self.S = 0

    # само событие
    def localEvent(self, event):
        NewRoot = Tk()  # окно
        NewRoot.title(u'Произвольное построение')
        NewRoot.geometry('165x185+500+200')  # ширина=303, высота=295, расположение на экране x,y
        NewRoot.resizable(False, False)  # разрешение на изменение размера окна, ширина и высота
        Label(NewRoot, text="Ваши фигуры:", font="courier 12").grid(row=1, column=1, sticky=W)

        class UserPicture_1():

            def __init__(self):
                self.but = Button(NewRoot,
                                  text="Цветок",  # надпись на кнопке
                                  width=14,  # ширина
                                  bg="white", fg="black", font="courier 14")  # цвет фона и надписи
                self.but.bind("<Button-1>", self.localdraw)  # чем нажать, чтобы вызвать (что-то
                self.but.grid(row=3, column=1)  # размещение кнопки

            # само событие
            def localdraw(self, event):
                def f(x, y):
                    return np.sin(np.sqrt(x ** 2 + y ** 2))

                # бутон
                x = np.linspace(-6, 6, 30)
                y = np.linspace(-6, 6, 30)

                X, Y = np.meshgrid(x, y)
                Z = f(X, Y)

                fig = plt.figure()
                fig.canvas.set_window_title('Розочка')
                ax = plt.axes(projection='3d')
                ax.contour3D(X, Y, Z, 40, cmap='plasma')
                ax.set_xlabel('x')
                ax.set_ylabel('y')
                ax.set_zlabel('z')
                axes = plt.gca()
                axes.set_zlim([-4, 4])
                axes.set_xlim([-40, 40])
                axes.set_ylim([-40, 40])
                # стебель
                t = np.linspace(-4 * np.pi, 4 * np.pi, 100)
                r = t ** 2 / 80 + 1
                x = r * np.cos(t)  # праметрическое уравнение кривой
                y = r * np.sin(t)
                z = t / (np.pi * 1.25) - 3.88
                ax.plot(x, y, z, linewidth=4, c="green")

                plt.show()

        class UserPicture_2():

            def __init__(self):
                self.but = Button(NewRoot,
                                  text="Анимация",  # надпись на кнопке
                                  width=14,  # ширина
                                  bg="white", fg="black", font="courier 14")  # цвет фона и надписи
                self.but.bind("<Button-1>", self.localdraw)  # чем нажать, чтобы вызвать (что-то
                self.but.grid(row=5, column=1)  # размещение кнопки

            # само событие
            def localdraw(self, event):
                # координатные функции
                xs = lambda u, v: (R + v * np.cos(n * u / 2)) * np.cos(u)
                ys = lambda u, v: (R + v * np.cos(n * u / 2)) * np.sin(u)
                zs = lambda u, v: v * np.sin(n * u / 2)

                def initpict():
                    global u
                    u = np.linspace(0, du, 1)  # очистка вектора u перед стартовым кадром

                def redraw(i):  # рисование i-го кадра
                    global u
                    u = np.append(u, (i + 1) * du)  # добавление точки к вектору u
                    U, V = np.meshgrid(u, v)
                    X = xs(U, V)
                    Y = ys(U, V)
                    Z = zs(U, V)
                    ax.clear()
                    # после очистки восстанавливаем видимые размеры графической области
                    ax.set_xlim3d(xyLeft, xyRight)
                    ax.set_ylim3d(xyLeft, xyRight)
                    ax.set_zlim3d(-H, H)
                    ax.plot(xc, yc, zc, color='darkmagenta', linewidth=3)  # направляющая окружность
                    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow', alpha=0.9)

                R = 4
                H = 2
                n = 1
                NumFrames = 40  # количество кадров
                du = 2 * np.pi / NumFrames
                xyRight = R + 1
                xyLeft = -xyRight
                fig = plt.figure(facecolor='white')
                fig.set_dpi(100)
                ax = Axes3D(fig, xlim=(xyLeft, xyRight), ylim=(xyLeft, xyRight), zlim=(-H, H))
                # координаты точек направляющей окружности одинаковые для всех кадров
                t = np.linspace(0, 2 * np.pi, 100)
                vt = np.zeros(np.size(t))
                xc = xs(t, vt)
                yc = ys(t, vt)
                zc = zs(t, vt)
                # массив параметра v поверхности одинаков для всех моментов времени
                v = np.linspace(-H / 2, H / 2, 11)
                anim = animation.FuncAnimation(fig, redraw, init_func=initpict,

                                               frames=NumFrames, interval=20, repeat=True, blit=False)
                plt.show()

        class UserPicture_3():

            def __init__(self):
                self.but = Button(NewRoot,
                                  text="Каркас",  # надпись на кнопке
                                  width=14,  # ширина
                                  bg="white", fg="black", font="courier 14")  # цвет фона и надписи
                self.but.bind("<Button-1>", self.localdraw)  # чем нажать, чтобы вызвать (что-то
                self.but.grid(row=2, column=1)  # размещение кнопки

            # само событие
            def localdraw(self, event):
                fig = plt.figure()
                ax = fig.gca(projection='3d')
                ax.set_aspect("equal")

                # draw cube
                r = [-1, 1]
                points = list(product(r, r, r))
                axes = plt.gca()
                axes.set_zlim([-1.5, 1.5])
                axes.set_xlim([-2, 2])
                axes.set_ylim([-1.5, 1.5])
                # Add roof

                points.append([0., -1, 1.5])
                points.append([0., 1, 1.5])
                # Convert to array
                points = np.array(points)

                # Plot
                ax.scatter(points[:, 0], points[:, 1], points[:, 2])
                for s, e in combinations(points, 2):
                    # All diagonals will be greater than 2
                    if np.sum(np.abs(s - e)) <= 2:
                        ax.plot3D(*zip(s, e), color="saddlebrown", linewidth=3)

                plt.show()

        user1 = UserPicture_1()
        user2 = UserPicture_2()
        user3 = UserPicture_3()

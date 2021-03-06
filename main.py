from sys import setrecursionlimit
from tkinter import *
import time
from ctypes import windll
from matplotlib.pyplot import cla, plot, scatter, subplots, isinteractive
import numpy as np
from matplotlib import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.font_manager as fm


setrecursionlimit(10**6)


# matplotlib font 설정
path = "C:\Workspace\parabolic-motion-simulation\Pretendard-Medium.ttf"
fontprop = fm.FontProperties(fname=path)

params = {"xtick.labelsize": 20, "ytick.labelsize": 20}
rcParams.update(params)


root = Tk()
root.wm_title("포물선 운동 시뮬레이션")

# 해상도 구하기
width_px = root.winfo_screenwidth()
user32 = windll.user32
user32.SetProcessDPIAware()
w = user32.GetSystemMetrics(0)

# 해상도에 따라 창크기 맞춤
if w == 3840:
    root.geometry("2560x1440")

elif w == 2560:
    root.geometry("1920x1080")

else:
    root.geometry("1280x720")


def para_clac():
    v0 = float(e_v0.get())
    ang = np.deg2rad(int(e_ang.get()))
    mg = float(e_mg.get())

    r = int(v0**2 * np.sin(2 * ang) / mg)
    h = int(v0**2 * ((np.sin(ang)) ** 2) / 2 * mg)

    t_flight = 2 * v0 * np.sin(ang) / mg
    t = np.linspace(0, t_flight, 100, dtype=float)

    return v0, ang, mg, r, h, t_flight, t


# 실시간으로 포물선을 그리는 함수
def para_plot():
    global line, canvas

    # dt = 0
    e_bh.delete(0, "end")
    e_br.delete(0, "end")

    v0, ang, mg, r, h, t_flight, t = para_clac()

    e_bh.insert(0, h)
    e_br.insert(0, r)

    def x(tt):
        return v0 * np.cos(ang) * tt

    def y(tt):
        return v0 * np.sin(ang) * t - 0.5 * mg * tt**2

    t = np.linspace(0, t_flight, 100000, dtype=float)

    plot(x(t), y(t))

    figure.canvas.draw()
    figure.canvas.flush_events()

    # for n in range(100):
    #     e_t.delete(0, "end")
    #     dt = t[n]
    #     e_t.insert(0, dt)

    #     ux = float(v0 * np.cos(ang))
    #     uy = v0 * np.sin(ang) - mg * dt

    #     e_v.delete(0, "end")
    #     v = np.round(((ux**2 + uy**2) ** 0.5), 3)
    #     e_v.insert(0, v)

    #     parax = np.round((v0 * np.cos(ang) * dt), 3)
    #     paray = np.round((v0 * np.sin(ang) * dt - 0.5 * mg * dt**2), 3)

    #     time.sleep(0.1)


def run():
    para_plot()


# 그래프가 출력될 프레임
graph_frame = Frame(root, relief="solid", bd=3, bg="white")
graph_frame.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="nsew")

# 시뮬로 알 수 있는 정보들이 출력될 프레임
info_frame = Frame(root, width=230, bg="white")
info_frame.grid(row=0, column=2, columnspan=2, sticky="nsew")

# 사용자가 조절할 수 있는 값들의 입력공간이 보일 프레임
input_frame = Frame(root, width=230, relief="solid", bd=2, bg="white")
input_frame.grid(row=1, column=2, columnspan=2, sticky="nsew")


# 그래프
# fig = Figure()

# isinteractive()

figure, ax = subplots()
ax.set_title("포물선 운동 시물레이션", fontproperties=fontprop, fontsize=30)
ax.set_xlabel("x", fontsize=20)
ax.set_ylabel("y", fontsize=20)
ax.grid(True)

(line,) = ax.plot([], [])

figure.canvas = FigureCanvasTkAgg(figure, master=graph_frame)
figure.canvas.draw()

toolbar = NavigationToolbar2Tk(figure.canvas, graph_frame, pack_toolbar=False)
toolbar.update()

toolbar.grid(row=1, column=0, sticky="nsew")
figure.canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")


# ani = FuncAnimation(fig, para_plot, frames=60, interval=20)
# canvas.draw()


# # (발사 후 흐른) 시간 레이블 & 엔트리
# lb_t = Label(info_frame, text="      시간 :", bg="white", font=(None, 15))
# e_t = Entry(info_frame, width=6, bg="white", bd=0, justify="right", font=(None, 15))
# lb_tu = Label(info_frame, text=" s", bg="white", font=(None, 15))
# lb_t.grid(row=0, column=0, pady=20)
# e_t.grid(row=0, column=1, pady=20)
# lb_tu.grid(row=0, column=2, pady=20)

# # (공의) 속도 레이블 & 엔트리
# lb_v = Label(info_frame, text="      속도 :", bg="white", font=(None, 15))
# e_v = Entry(info_frame, width=6, bg="white", bd=0, justify="right", font=(None, 15))
# lb_vu = Label(info_frame, text="m/s", bg="white", font=(None, 15))
# lb_v.grid(row=1, column=0, pady=20)
# e_v.grid(row=1, column=1, pady=20)
# lb_vu.grid(row=1, column=2, pady=20)

# 공의 높이 레이블 & 엔트리
lb_bh = Label(info_frame, text="      높이 :", bg="white", font=(None, 15))
e_bh = Entry(info_frame, width=6, bg="white", bd=0, justify="right", font=(None, 15))
lb_bhu = Label(info_frame, text="m", bg="white", font=(None, 15))
lb_bh.grid(row=0, column=0, pady=20)
e_bh.grid(row=0, column=1, pady=20)
lb_bhu.grid(row=0, column=2, pady=20)

# 공이 날라간 거리 레이블 & 엔트리
lb_br = Label(info_frame, text="      거리 :", bg="white", font=(None, 15))
e_br = Entry(info_frame, width=6, bg="white", bd=0, justify="right", font=(None, 15))
lb_bru = Label(info_frame, text="m", bg="white", font=(None, 15))
lb_br.grid(row=1, column=0, pady=20)
e_br.grid(row=1, column=1, pady=20)
lb_bru.grid(row=1, column=2, pady=20)

# (공의) 발사(초기)속도 레이블 & 엔트리
lb_v0 = Label(input_frame, text="발사속도 :", bg="white", font=(None, 15))
e_v0 = Entry(input_frame, width=6, bg="white", bd=0, justify="right", font=(None, 15))
lb_v0u = Label(input_frame, text="m/s", bg="white", font=(None, 15))
lb_v0.grid(row=0, column=0, pady=20)
e_v0.grid(row=0, column=1, pady=20)
lb_v0u.grid(row=0, column=2, pady=20)

# (공의) 발사각도 레이블 & 엔트리
lb_ang = Label(input_frame, text="발사각도 :", bg="white", font=(None, 15))
e_ang = Entry(input_frame, width=6, bg="white", bd=0, justify="right", font=(None, 15))
lb_angu = Label(input_frame, text="°", bg="white", font=(None, 15))
lb_ang.grid(row=1, column=0, pady=20)
e_ang.grid(row=1, column=1, pady=20)
lb_angu.grid(row=1, column=2, pady=20)

# 중력 가속도 레이블 & 엔트리
lb_mg = Label(input_frame, text="중력가속도 :", bg="white", font=(None, 15))
e_mg = Entry(input_frame, width=6, bg="white", bd=0, justify="right", font=(None, 15))
lb_mgu = Label(input_frame, text="m/s²", bg="white", font=(None, 15))
lb_mg.grid(row=2, column=0, pady=20)
e_mg.grid(row=2, column=1, pady=20)
lb_mgu.grid(row=2, column=2, pady=20)
# 기본적으로 중력 가속도 값을 입력해줌
e_mg.insert(0, 9.806)

# 사용자 지정 값 입력 버튼
button = Button(
    input_frame,
    text="확인",
    width=10,
    height=2,
    relief="ridge",
    overrelief="solid",
    bg="white",
    activebackground="white",
    font=(None, 15),
    command=run,
)
button.grid(row=3, column=0, columnspan=3, pady=20)


# 각 프레임의 크기를 창 크기가 변할때 같이 일정하게 변하도록함
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

graph_frame.grid_rowconfigure(0, weight=1)
graph_frame.grid_columnconfigure(0, weight=1)


root.mainloop()

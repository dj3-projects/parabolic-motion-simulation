from tkinter import *
from matplotlib import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure


root = Tk()
root.title("포물선 운동 시뮬레이션")
root.geometry("1080x720")


# 그래프가 출력될 프레임
graph_frame = Frame(root, relief="solid", bd=3, bg="white")
graph_frame.grid(row=0, column=0, rowspan=2, columnspan=2, sticky="nsew")

# 시뮬로 알 수 있는 정보들이 출력될 프레임
info_frame = Frame(root, width=230, bg="white")
info_frame.grid(row=0, column=2, columnspan=2, sticky="nsew")

# 사용자가 조절할 수 있는 값들의 입력공간이 보일 프레임
input_frame = Frame(root, width=230, relief="solid", bd=2, bg="white")
input_frame.grid(row=1, column=2, columnspan=2, sticky="nsew")


# (발사 후 흐른) 시간 레이블 & 엔트리
lb_t = Label(info_frame, text="      시간 :", bg="white", font=(None, 15))
e_t = Entry(info_frame, width=6, bg="white", bd=0, justify="right", font=(None, 15))
lb_tu = Label(info_frame, text=" s", bg="white", font=(None, 15))
lb_t.grid(row=0, column=0, pady=15)
e_t.grid(row=0, column=1, pady=15)
lb_tu.grid(row=0, column=2, pady=15)

# (공의) 속도 레이블 & 엔트리
lb_v = Label(info_frame, text="      속도 :", bg="white", font=(None, 15))
e_v = Entry(info_frame, width=6, bg="white", bd=0, justify="right", font=(None, 15))
lb_vu = Label(info_frame, text="m/s", bg="white", font=(None, 15))
lb_v.grid(row=1, column=0, pady=15)
e_v.grid(row=1, column=1, pady=15)
lb_vu.grid(row=1, column=2, pady=15)


# 각 프레임의 크기를 창 크기가 변할때 같이 일정하게 변하도록함
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)


root.mainloop()

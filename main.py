from tkinter import *
from tkinter import ttk, messagebox
import time

tk = Tk()
tk.title("Моделирование подводной лодки")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 0)
canvas = Canvas(tk, width=1200, height=750, highlightthickness=0)
canvas.pack()
# tk.update()
canvas_height = 500
canvas_width = 50
bg = PhotoImage(file="pictures/background.gif")
w = bg.width()
h = bg.height()

deg = 0

for x in range(0, 5):
    for y in range(0, 5):
        canvas.create_image(x * w, y * h, image=bg, anchor='nw')
        sprites = []
        running = True

Spare_torpedoes = [0, 0, 0, 0, 0]

Spare_torpedoes[0] = IntVar()
Spare_torpedoes[1] = IntVar()
Spare_torpedoes[2] = IntVar()
Spare_torpedoes[3] = IntVar()
Spare_torpedoes[4] = IntVar()

cistern12 = [0, 0, 0, 0, 0]
cistern12[0] = IntVar()
cistern12[1] = IntVar()
cistern12[2] = IntVar()
cistern12[3] = IntVar()
cistern12[4] = IntVar()

oil2_1 = [0, 0, 0, 0, 0]
oil2_1[0] = IntVar()
oil2_1[1] = IntVar()
oil2_1[2] = IntVar()
oil2_1[3] = IntVar()
oil2_1[4] = IntVar()

oil2_2 = [0, 0, 0, 0, 0]
oil2_2[0] = IntVar()
oil2_2[1] = IntVar()
oil2_2[2] = IntVar()
oil2_2[3] = IntVar()
oil2_2[4] = IntVar()

oil1_2 = [0, 0, 0, 0, 0]
oil1_2[0] = IntVar()
oil1_2[1] = IntVar()
oil1_2[2] = IntVar()
oil1_2[3] = IntVar()
oil1_2[4] = IntVar()

water1 = [0, 0, 0, 0, 0]
water1[0] = IntVar()
water1[1] = IntVar()
water1[2] = IntVar()
water1[3] = IntVar()
water1[4] = IntVar()

food = [0, 0, 0, 0, 0]
food[0] = IntVar()
food[1] = IntVar()
food[2] = IntVar()
food[3] = IntVar()
food[4] = IntVar()

food5 = [0, 0, 0, 0, 0]
food5[0] = IntVar()
food5[1] = IntVar()
food5[2] = IntVar()
food5[3] = IntVar()
food5[4] = IntVar()

# Вторая вкладка
water4 = [0, 0, 0, 0, 0]
water4[0] = IntVar()
water4[1] = IntVar()
water4[2] = IntVar()
water4[3] = IntVar()
water4[4] = IntVar()

summ1 = [0, 0, 0, 0, 0]
summ1[0] = IntVar()
summ1[1] = IntVar()
summ1[2] = IntVar()
summ1[3] = IntVar()
summ1[4] = IntVar()

summ2 = [0, 0, 0, 0, 0]
summ2[0] = IntVar()
summ2[1] = IntVar()
summ2[2] = IntVar()
summ2[3] = IntVar()
summ2[4] = IntVar()

equalization_tank = [0, 0, 0, 0, 0]
equalization_tank[0] = IntVar()
equalization_tank[1] = IntVar()
equalization_tank[2] = IntVar()
equalization_tank[3] = IntVar()
equalization_tank[4] = IntVar()

new_trim_systems = [0, 0, 0, 0, 0]
new_trim_systems[0] = IntVar()
new_trim_systems[1] = IntVar()
new_trim_systems[2] = IntVar()
new_trim_systems[3] = IntVar()
new_trim_systems[4] = IntVar()

aft_trim_systems = [0, 0, 0, 0, 0]
aft_trim_systems[0] = IntVar()
aft_trim_systems[1] = IntVar()
aft_trim_systems[2] = IntVar()
aft_trim_systems[3] = IntVar()
aft_trim_systems[4] = IntVar()

main_summ = [0, 0, 0, 0, 0]
main_summ[0] = IntVar()
main_summ[1] = IntVar()
main_summ[2] = IntVar()
main_summ[3] = IntVar()
main_summ[4] = IntVar()

var = 0

\

def input_window():
    input_window = Tk()
    input_window.geometry("850x300")
    input_window.title("Данные для рассчёта")
    input_window.wm_attributes("-topmost", 1)
    input_window.wm_attributes('-alpha', 50)
    input_canvas = Canvas(input_window, width=800, height=750, highlightthickness=0, bg='blue')

    main = Label(input_window, text='Всего грузов: ')
    tab_control = ttk.Notebook(input_window)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Переменные грузы')
    tab_control.add(tab2, text='Вспомогательный балласт')
    Label(tab1, text="Наименование грузов") \
        .grid(row=0, column=0, rowspan=2, pady=10, padx=10)
    Label(tab1, text="Нормальная нагрузка") \
        .grid(row=0, column=1, columnspan=2)
    Label(tab1, text="Дифферентовка за (дата), тс") \
        .grid(row=0, column=3)
    Label(tab1, text="Фактическая нагрузка, тс") \
        .grid(row=0, column=4)
    Label(tab1, text="Наименование нагрузки") \
        .grid(row=0, column=5, columnspan=2)
    Label(tab1, text="p, тс") \
        .grid(row=1, column=1)
    Label(tab1, text="х, м") \
        .grid(row=1, column=2)
    Label(tab1, text="delta p, тс") \
        .grid(row=1, column=5)
    Label(tab1, text="delta M, тс м") \
        .grid(row=1, column=6)
    Label(tab1, text="") \
        .grid(row=2, column=1, columnspan=7)

    Label(tab1, text="Запасные торпеды") \
        .grid(row=3, column=0)

    en11 = Entry(tab1, width=10, textvariable=Spare_torpedoes[0])
    en12 = Entry(tab1, width=10, textvariable=Spare_torpedoes[1])
    en13 = Entry(tab1, width=10, textvariable=Spare_torpedoes[2])

    Entry(tab1, width=10) \
        .grid(row=3, column=3)

    Label(tab1, text="Торпедозаместительные цистерны №1 и 2") \
        .grid(row=4, column=0)
    en21 = Entry(tab1, width=10, textvariable=cistern12[0])
    en22 = Entry(tab1, width=10, textvariable=cistern12[1])
    en23 = Entry(tab1, width=10, textvariable=cistern12[2])

    Entry(tab1, width=10) \
        .grid(row=4, column=3)

    Label(tab1, text="Масло в цистерне судового запаса масла №2") \
        .grid(row=5, column=0)
    en31 = Entry(tab1, width=10, textvariable=oil2_1[0])
    en32 = Entry(tab1, width=10, textvariable=oil2_1[1])
    en33 = Entry(tab1, width=10, textvariable=oil2_1[2])

    Entry(tab1, width=10) \
        .grid(row=5, column=3)

    Label(tab1, text="Масло в цистерне цирукляционного масла №2") \
        .grid(row=6, column=0)
    en41 = Entry(tab1, width=10, textvariable=oil2_2[0])
    en42 = Entry(tab1, width=10, textvariable=oil2_2[1])
    en43 = Entry(tab1, width=10, textvariable=oil2_2[2])
    Entry(tab1, width=10) \
        .grid(row=6, column=3)

    Label(tab1, text="Масло в цистернах грязного масла №1 и 2") \
        .grid(row=7, column=0)
    en51 = Entry(tab1, width=10, textvariable=oil1_2[0])
    en52 = Entry(tab1, width=10, textvariable=oil1_2[1])
    en53 = Entry(tab1, width=10, textvariable=oil1_2[2])
    Entry(tab1, width=10) \
        .grid(row=7, column=3)

    Label(tab1, text="Питательная вода в цистерне №1") \
        .grid(row=8, column=0)
    en61 = Entry(tab1, width=10, textvariable=water1[0])
    en62 = Entry(tab1, width=10, textvariable=water1[1])
    en63 = Entry(tab1, width=10, textvariable=water1[2])
    Entry(tab1, width=10) \
        .grid(row=8, column=3)

    Label(tab1, text="Провизия в цистерне №5") \
        .grid(row=9, column=0)
    en71 = Entry(tab1, width=10, textvariable=food[0])
    en72 = Entry(tab1, width=10, textvariable=food[1])
    en73 = Entry(tab1, width=10, textvariable=food[2])
    Entry(tab1, width=10) \
        .grid(row=9, column=3)

    Label(tab1, text="Пресная вода в цистерне №4") \
        .grid(row=10, column=0)
    en81 = Entry(tab1, width=10, textvariable=food5[0])
    en82 = Entry(tab1, width=10, textvariable=food5[1])
    en83 = Entry(tab1, width=10, textvariable=food5[2])
    Entry(tab1, width=10) \
        .grid(row=10, column=3)

    Label(tab1, text="Итого переменных грузов") \
        .grid(row=11, column=0)

    # Вторая вкладка

    Label(tab2, text="Наименование грузов") \
        .grid(row=0, column=0, rowspan=2, pady=10, padx=10)
    Label(tab2, text="Нормальная нагрузка") \
        .grid(row=0, column=1, columnspan=2)
    Label(tab2, text="Дифференовка за (дата), тс") \
        .grid(row=0, column=3)
    Label(tab2, text="Фактическая нагрузка, тс") \
        .grid(row=0, column=4)
    Label(tab2, text="Наименование нагрузки") \
        .grid(row=0, column=5, columnspan=2)
    Label(tab2, text="p, тс") \
        .grid(row=1, column=1)
    Label(tab2, text="х, м") \
        .grid(row=1, column=2)
    Label(tab2, text="delta p, тс") \
        .grid(row=1, column=5)
    Label(tab2, text="delta M, тс м") \
        .grid(row=1, column=6)
    Label(tab2, text="") \
        .grid(row=2, column=1, columnspan=7)

    Label(tab2, text="Уравнительная цистерна") \
        .grid(row=3, column=0)
    in31 = Entry(tab2, width=10, textvariable=equalization_tank[0])
    in32 = Entry(tab2, width=10, textvariable=equalization_tank[1])
    in33 = Entry(tab2, width=10, textvariable=equalization_tank[2])
    Entry(tab2, width=10) \
        .grid(row=3, column=3)

    Label(tab2, text="Новые дифферентные цистерны") \
        .grid(row=4, column=0)
    in41 = Entry(tab2, width=10, textvariable=new_trim_systems[0])
    in42 = Entry(tab2, width=10, textvariable=new_trim_systems[1])
    in43 = Entry(tab2, width=10, textvariable=new_trim_systems[2])
    Entry(tab2, width=10) \
        .grid(row=4, column=3)

    Label(tab2, text="Кормовые дифферентные цистерны") \
        .grid(row=5, column=0)
    in51 = Entry(tab2, width=10, textvariable=aft_trim_systems[0])
    in52 = Entry(tab2, width=10, textvariable=aft_trim_systems[1])
    in53 = Entry(tab2, width=10, textvariable=aft_trim_systems[2])
    Entry(tab2, width=10) \
        .grid(row=5, column=3)

    Label(tab2, text="Итого вспомогательного баланса") \
        .grid(row=6, column=0)
    Label(tab2, text="ВСЕГО") \
        .grid(row=7, column=0)

    def calc():
        try:
            # Первая вкладка
            Spare_torpedoes[0].set(en11.get())
            # print(Spare_torpedoes[0].get())
            Spare_torpedoes[1].set(en12.get())
            # print(Spare_torpedoes[1].get())
            Spare_torpedoes[2].set(en13.get())
            # print(Spare_torpedoes[2].get())
            Spare_torpedoes[3].set(Spare_torpedoes[2].get() - Spare_torpedoes[0].get())
            Spare_torpedoes[4].set(Spare_torpedoes[3].get() * Spare_torpedoes[1].get())
            text35 = Label(tab1, text=str(Spare_torpedoes[3].get()))
            text36 = Label(tab1, text=str(Spare_torpedoes[4].get()))

            cistern12[0].set(en21.get())
            # print(cistern12[0].get())
            cistern12[1].set(en22.get())
            # print(cistern12[1].get())
            cistern12[2].set(en23.get())
            # print(cistern12[2].get())
            cistern12[3].set(cistern12[2].get() - cistern12[0].get())
            cistern12[4].set(cistern12[3].get() * cistern12[1].get())
            text45 = Label(tab1, text=str(cistern12[3].get()))
            text46 = Label(tab1, text=str(cistern12[4].get()))

            oil2_1[0].set(en31.get())
            # print(oil2_1[0].get())
            oil2_1[1].set(en32.get())
            # print(oil2_1[1].get())
            oil2_1[2].set(en33.get())
            # print(oil2_1[2].get())
            oil2_1[3].set(oil2_1[2].get() - oil2_1[0].get())
            oil2_1[4].set(oil2_1[3].get() * oil2_1[1].get())
            text55 = Label(tab1, text=str(oil2_1[3].get()))
            text56 = Label(tab1, text=str(oil2_1[4].get()))

            oil2_2[0].set(en41.get())
            # print(oil2_2[0].get())
            oil2_2[1].set(en42.get())
            # print(oil2_2[1].get())
            oil2_2[2].set(en43.get())
            # print(oil2_2[2].get())
            oil2_2[3].set(oil2_2[2].get() - oil2_2[0].get())
            oil2_2[4].set(oil2_2[3].get() * oil2_2[1].get())
            text65 = Label(tab1, text=str(oil2_2[3].get()))
            text66 = Label(tab1, text=str(oil2_2[4].get()))

            oil1_2[0].set(en51.get())
            # print(oil1_2[0].get())
            oil1_2[1].set(en52.get())
            # print(oil1_2[1].get())
            oil1_2[2].set(en53.get())
            # print(oil1_2[2].get())
            oil1_2[3].set(oil1_2[2].get() - oil1_2[0].get())
            oil1_2[4].set(oil1_2[3].get() * oil1_2[1].get())
            text75 = Label(tab1, text=str(oil1_2[3].get()))
            text76 = Label(tab1, text=str(oil1_2[4].get()))

            water1[0].set(en61.get())
            # print(water1[0].get())
            water1[1].set(en62.get())
            # print(water1[1].get())
            water1[2].set(en63.get())
            # print(water1[2].get())
            water1[3].set(water1[2].get() - water1[0].get())
            water1[4].set(water1[3].get() * water1[1].get())
            text85 = Label(tab1, text=str(water1[3].get()))
            text86 = Label(tab1, text=str(water1[4].get()))

            food[0].set(en71.get())
            # print(food[0].get())
            food[1].set(en72.get())
            # print(food[1].get())
            food[2].set(en73.get())
            # print(food[2].get())
            food[3].set(food[2].get() - food[0].get())
            food[4].set(food[3].get() * food[1].get())
            text95 = Label(tab1, text=str(food[3].get()))
            text96 = Label(tab1, text=str(food[4].get()))

            food5[0].set(en81.get())
            # print(food5[0].get())
            food5[1].set(en82.get())
            # print(food5[1].get())
            food5[2].set(en83.get())
            # print(food5[2].get())
            food5[3].set(food5[2].get() - food5[0].get())
            food5[4].set(food5[3].get() * food5[1].get())
            text105 = Label(tab1, text=str(food5[3].get()))
            text106 = Label(tab1, text=str(food5[4].get()))

            # строка ИТОГО первой вкладки
            summ1[0].set(
                Spare_torpedoes[0].get() + cistern12[0].get() + oil2_1[0].get() + oil2_2[0].get() + oil1_2[0].get() +
                water1[0].get() + food[0].get() + food5[0].get())
            summ1[2].set(
                Spare_torpedoes[2].get() + cistern12[2].get() + oil2_1[2].get() + oil2_2[2].get() + oil1_2[2].get() +
                water1[2].get() + food[2].get() + food5[2].get())
            summ1[3].set(
                Spare_torpedoes[3].get() + cistern12[3].get() + oil2_1[3].get() + oil2_2[3].get() + oil1_2[3].get() +
                water1[3].get() + food[3].get() + food5[3].get())
            summ1[4].set(
                Spare_torpedoes[4].get() + cistern12[4].get() + oil2_1[4].get() + oil2_2[4].get() + oil1_2[4].get() +
                water1[4].get() + food[4].get() + food5[4].get())

            text_summ10 = Label(tab1, text=str(summ1[0].get()))
            text_summ12 = Label(tab1, text=str(summ1[2].get()))
            if float(summ1[3].get()) != 0:
                text_summ13 = Label(tab1, text=str(summ1[3].get()), fg='red')
            else:
                text_summ13 = Label(tab1, text=str(summ1[3].get()), fg='green')
            text_summ14 = Label(tab1, text=str(summ1[4].get()))
            deg = int(summ1[3].get())

            text_summ24 = Label(tab2, text=str(summ2[4].get()))

            # Вторая вкладка
            # equalization_tank - полностью готово
            textF14 = Label(tab2, text=str(-summ1[3].get()), fg='green')  # text_summ13
            equalization_tank[0].set(in31.get())
            equalization_tank[1].set(in32.get())

            equalization_tank[3].set(-summ1[3].get())
            equalization_tank[2].set(equalization_tank[0].get() - summ1[3].get())
            textE14 = Label(tab2, text=str(equalization_tank[0].get() - summ1[3].get()),
                            fg='green')  # water4[0] -summ1[3].get()
            # textG14 = Label(tab2, text=str(float(equalization_tank[1].get()*(-summ1[3].get()))), fg='green')
            textG14 = Label(tab2, text=str(float(equalization_tank[1].get() * (-summ1[3].get()))), fg='green')
            equalization_tank[4].set(equalization_tank[1].get() * (-summ1[3].get()))
            # new_trim_systems

            # textF15 = Label(tab2, text=str(-summ1[3].get()), fg='green')
            new_trim_systems[0].set(in41.get())
            new_trim_systems[1].set(in42.get())
            new_trim_systems[2].set(new_trim_systems[0].get() + new_trim_systems[3].get())

            new_trim_systems[4].set(float(new_trim_systems[1].get() * (summ1[3].get())))

            textE15 = Label(tab2, text=str(new_trim_systems[0].get() + new_trim_systems[3].get()),
                            fg='green')  # water4[0] -summ1[3].get()
            textG15 = Label(tab2, text=str(float(new_trim_systems[1].get() * (summ1[3].get()))), fg='green')

            # aft_trim_systems

            aft_trim_systems[0].set(in51.get())
            aft_trim_systems[1].set(in52.get())
            aft_trim_systems[2].set(aft_trim_systems[0].get() + aft_trim_systems[3].get())
            aft_trim_systems[3].set(
                (summ1[4].get() + equalization_tank[4].get()) / (new_trim_systems[1].get() + aft_trim_systems[1].get()))

            new_trim_systems[3].set(abs((summ1[4].get() + equalization_tank[4].get()) / (
                    new_trim_systems[1].get() + aft_trim_systems[1].get())))
            textF15 = Label(tab2, text=new_trim_systems[3].get(), fg='red')
            # print(summ1[4].get(), new_trim_systems[4].get(), new_trim_systems[1].get() )

            textF16 = Label(tab2, text=aft_trim_systems[3].get(), fg='red')
            textE16 = Label(tab2, text=str(aft_trim_systems[0].get() + aft_trim_systems[3].get()),
                            fg='green')  # water4[0] -summ1[3].get()
            textG16 = Label(tab2, text=str(float(-(aft_trim_systems[1].get() * aft_trim_systems[3].get()))), fg='green')
            aft_trim_systems[4].set(float(-(aft_trim_systems[1].get() * aft_trim_systems[3].get())))

            # строка ИТОГО ВТОРОЙ вкладки
            summ2[0].set(
                equalization_tank[0].get() + new_trim_systems[0].get() + aft_trim_systems[0].get())
            summ2[2].set(
                equalization_tank[2].get() + new_trim_systems[2].get() + aft_trim_systems[2].get())
            summ2[3].set(
                equalization_tank[3].get() + new_trim_systems[3].get() + aft_trim_systems[3].get())
            summ2[4].set(
                equalization_tank[4].get() + new_trim_systems[4].get() + aft_trim_systems[4].get())
            # print(equalization_tank[4].get(), new_trim_systems[4].get(), aft_trim_systems[4].get())
            text_summ20 = Label(tab2, text=str(summ2[0].get()))
            text_summ22 = Label(tab2, text=str(summ2[2].get()))
            text_summ23 = Label(tab2, text=str(summ2[3].get()), fg='red')
            text_summ24 = Label(tab2, text=str(summ2[4].get()))

            # Общее ИТОГО main_summ
            main_summ[0].set(
                summ1[0].get() + summ2[0].get())
            main_summ[2].set(
                summ1[2].get() + summ2[2].get())
            main_summ[3].set(
                summ1[3].get() + summ2[3].get())
            main_summ[4].set(
                summ1[4].get() + summ2[4].get())

            textB18 = Label(tab2, text=str(main_summ[0].get()))
            textE18 = Label(tab2, text=str(main_summ[2].get()))
            textF18 = Label(tab2, text=str(main_summ[3].get()))
            textG18 = Label(tab2, text=str(main_summ[4].get()))

            text35.grid(row=3, column=5)
            text36.grid(row=3, column=6)
            text45.grid(row=4, column=5)
            text46.grid(row=4, column=6)
            text55.grid(row=5, column=5)
            text56.grid(row=5, column=6)
            text65.grid(row=6, column=5)
            text66.grid(row=6, column=6)
            text75.grid(row=7, column=5)
            text76.grid(row=7, column=6)
            text85.grid(row=8, column=5)
            text86.grid(row=8, column=6)
            text95.grid(row=9, column=5)
            text96.grid(row=9, column=6)
            text105.grid(row=10, column=5)
            text106.grid(row=10, column=6)

            '''
            text115.grid(row=11, column=5)
            text116.grid(row=11, column=6)
            '''
            # итого переменных грузов:
            text_summ10.grid(row=11, column=1)
            text_summ12.grid(row=11, column=4)
            text_summ13.grid(row=11, column=5)
            text_summ14.grid(row=11, column=6)

            # Вторая вкладка
            textF14.grid(row=3, column=5)
            textE14.grid(row=3, column=4)
            textG14.grid(row=3, column=6)

            textF15.grid(row=4, column=5)
            textE15.grid(row=4, column=4)
            textG15.grid(row=4, column=6)

            textF16.grid(row=5, column=5)
            textE16.grid(row=5, column=4)
            textG16.grid(row=5, column=6)

            # Итого балласта
            text_summ20.grid(row=6, column=1)
            text_summ22.grid(row=6, column=4)
            text_summ23.grid(row=6, column=5)
            text_summ24.grid(row=6, column=6)

            textB18.grid(row=7, column=1)
            textE18.grid(row=7, column=4)
            textF18.grid(row=7, column=5)
            textG18.grid(row=7, column=6)

            input_window.update_idletasks()
            input_window.update()
            deg = -deg
            if deg < 0:
                im = PhotoImage(file="pictures/nose.gif")
                w = int(im.width()/2)
                h = int(im.height()/2)
                message = canvas.create_image(w, h, image=im)

            elif deg > 0:
                im = PhotoImage(file="pictures/back.gif")
                w = int(im.width()/2)
                h = int(im.height()/2)
                message = canvas.create_image(w, h, image=im)
            s.rotate(deg)

        except:
            pass

        def saving_data():
            #Функция формирования текстового отчёта

            with open('Результаты вычислений.txt', 'w', encoding='utf-8') as f:
                head = ['Наименование грузов','Нормальная нагрузка p, тс','Нормальная нагрузка х, м', 'Фактическая нагрузка, p тс', 'Фактическая нагрузка, M тс m', 'Изменение нагрузки']



                context1 = ['Spare_torpedoes','cistern12','oil2_1','oil2_2','oil1_2','water1','food','food5','summ1']

                context2 = ['Запасные торпеды','Торпедозаместительные цистерны 1 и 2','Масло в цистерне судового запаса масла 2','Масло в цистерне циркулярного масла 2','Масло в цистарнах грязного масла 1 и 2','Питательная вода в цистерне 1','Провизия в цистерне 5','Пресная вода в цистерне 4','Итого переменных грузов']
                context3 = ['equalization_tank','new_trim_systems','aft_trim_systems','summ2 ','main_summ']
                context4 = ['Уравнительная цистерна','Носовые диф. цистерны','Кормовые диф. цистерны','Итого вспомогательного баласта','ВСЕГО']
                #f.write("{:^5}".format("x"))
                tab = '\t'
                sep = '|'
                for x in head:
                    if x == 'Наименование грузов':
                        f.write(x.ljust(55))
                        f.write(sep)
                    else:
                        f.write(x.center(29))
                        #f.write(tab)
                        f.write(sep)
                f.write('\n')
                f.write(' - '*67)
                f.write('\n')
                f.write('ПЕРЕМЕННЫЕ ГРУЗЫ'.center(143))
                f.write('\n')
                f.write(' - ' * 67)
                f.write('\n')
                i = 0
                for x in context2:
                    f.write(x.ljust(48))
                    #f.write('\t')
                    try:
                        for j in range(6):

                            f.write('{:^15}'.format('|'))
                            data = context1[i]
                            if data == 'Spare_torpedoes':
                                f.write('{:^15}'.format(f'{Spare_torpedoes[j].get()}'))
                            elif data == 'cistern12':
                                f.write('{:^15}'.format(f'{cistern12[j].get()}'))
                            elif data == 'oil2_1':
                                f.write('{:^15}'.format(f'{oil2_1[j].get()}'))
                            elif data == 'oil2_2':
                                f.write('{:^15}'.format(f'{oil2_2[j].get()}'))
                            elif data == 'oil1_2':
                                f.write('{:^15}'.format(f'{oil1_2[j].get()}'))
                            elif data == 'water1':
                                f.write('{:^15}'.format(f'{water1[j].get()}'))
                            elif data == 'food':
                                f.write('{:^15}'.format(f'{food[j].get()}'))
                            elif data == 'food5':
                                f.write('{:^15}'.format(f'{food5[j].get()}'))
                            elif data == 'summ1':
                                f.write('{:^15}'.format(f'{summ1[j].get()}'))

                    except IndexError:
                        pass
                    f.write('\n')
                    i+=1

                f.write('\n')
                f.write(' - ' * 67)
                f.write('\n')
                f.write('ВСПОМОГАТЕЛЬНЫЙ БАЛАСТ'.center(143))
                f.write('\n')
                f.write(' - ' * 67)
                f.write('\n')
                i = 0
                for x in context4:
                    f.write(x.ljust(48))
                    # f.write('\t')
                    try:
                        for j in range(6):

                            f.write('{:^15}'.format('|'))
                            data = context3[i]
                            if data == 'equalization_tank':
                                f.write('{:^15}'.format(f'{equalization_tank[j].get()}'))
                            elif data == 'new_trim_systems':
                                f.write('{:^15}'.format(f'{new_trim_systems[j].get()}'))
                            elif data == 'aft_trim_systems':
                                f.write('{:^15}'.format(f'{aft_trim_systems[j].get()}'))
                            elif data == 'summ2':
                                f.write('{:^15}'.format(f'{summ2[j].get()}'))
                            elif data == 'main_summ':
                                f.write('{:^15}'.format(f'{main_summ[j].get()}'))
                    except IndexError:
                        pass
                    f.write('\n')
                    i += 1

        btn_save = Button(tab1, text='Сохранить в файл', command=saving_data).grid(row=13, column=4)
        btn_save = Button(tab2, text='Сохранить в файл', command=saving_data).grid(row=13, column=4)






    btn_test = Button(tab1, text='Рассчитать', command=calc).grid(row=13, column=3)
    btn_test = Button(tab2, text='Рассчитать', command=calc).grid(row=13, column=3)

    en11.grid(row=3, column=1)
    en12.grid(row=3, column=2)
    en13.grid(row=3, column=4)
    en21.grid(row=4, column=1)
    en22.grid(row=4, column=2)
    en23.grid(row=4, column=4)
    en31.grid(row=5, column=1)
    en32.grid(row=5, column=2)
    en33.grid(row=5, column=4)
    en41.grid(row=6, column=1)
    en42.grid(row=6, column=2)
    en43.grid(row=6, column=4)
    en51.grid(row=7, column=1)
    en52.grid(row=7, column=2)
    en53.grid(row=7, column=4)
    en61.grid(row=8, column=1)
    en62.grid(row=8, column=2)
    en63.grid(row=8, column=4)
    en71.grid(row=9, column=1)
    en72.grid(row=9, column=2)
    en73.grid(row=9, column=4)
    en81.grid(row=10, column=1)
    en82.grid(row=10, column=2)
    en83.grid(row=10, column=4)

    # Вторая вкладка
    in31.grid(row=3, column=1)
    in32.grid(row=3, column=2)
    in41.grid(row=4, column=1)
    in42.grid(row=4, column=2)
    in51.grid(row=5, column=1)
    in52.grid(row=5, column=2)

    # text35.grid(row=3, column=5)

    tab_control.pack(expand=1, fill='both')
    input_canvas.pack()
    input_window.update_idletasks()
    input_window.update()

    main.pack()


btn3 = Button(tk, text="Ввод данных для рассчёта", command=input_window).place(x=500, y=700)


# entry.pack()

# entry.pack()

def system():
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


class Submarine:
    def __init__(self):
        self.canvas = canvas
        self.rotate_pict = [PhotoImage(file=f"pictures/different_deg/{x}.gif") for x in range(-45, 46)]
        self.sub = PhotoImage(file="pictures/lodka.gif")
        self.d1 = PhotoImage(file="pictures/d1.gif")
        self.d2 = PhotoImage(file="pictures/d2.gif")
        self.d3 = PhotoImage(file="pictures/d3.gif")
        self.d4 = PhotoImage(file="pictures/d4.gif")
        self.d5 = PhotoImage(file="pictures/d5.gif")
        self.d6 = PhotoImage(file="pictures/d6.gif")
        self.d7 = PhotoImage(file="pictures/d7.gif")
        self.d8 = PhotoImage(file="pictures/d8.gif")
        self.d9 = PhotoImage(file="pictures/d9.gif")
        self.d10 = PhotoImage(file="pictures/d10.gif")
        self.d11 = PhotoImage(file="pictures/d11.gif")
        self.d12 = PhotoImage(file="pictures/d12.gif")
        self.d13 = PhotoImage(file="pictures/d13.gif")
        self.d14 = PhotoImage(file="pictures/d14.gif")
        self.d15 = PhotoImage(file="pictures/d15.gif")
        self.d16 = PhotoImage(file="pictures/d16.gif")
        self.d17 = PhotoImage(file="pictures/d17.gif")
        self.d18 = PhotoImage(file="pictures/d18.gif")
        self.d19 = PhotoImage(file="pictures/d19.gif")
        self.d20 = PhotoImage(file="pictures/d20.gif")
        self.d21 = PhotoImage(file="pictures/d21.gif")
        self.d22 = PhotoImage(file="pictures/d22.gif")
        self.d23 = PhotoImage(file="pictures/d23.gif")
        self.d24 = PhotoImage(file="pictures/d24.gif")
        self.d25 = PhotoImage(file="pictures/d25.gif")

        self.div = [self.d1, self.d2, self.d3, self.d4, self.d5, self.d6, self.d7, self.d8, self.d9, self.d10, self.d11,
                    self.d12,
                    self.d13, self.d14, self.d15, self.d16, self.d17, self.d18, self.d19, self.d20, self.d21, self.d22,
                    self.d23, self.d24, self.d25]

        self.start = [600, 200]
        self.id = canvas.create_image(self.start[0], self.start[1], image=self.div[1])
        self.x = 0
        self.y = -1
        self.canvas_height = self.canvas.winfo_height()
        self.pos = self.canvas.coords(self.id)
        self.xy = [(300, 115), (900, 115), (900, 386), (300, 386)]

        self.pos = self.canvas.coords(self.id)

    def draw(self):
        pos = self.canvas.coords(self.id)
        if pos[1] >= 500 or pos[1] <= 250:
            self.canvas.move(self.id, 0, 0)

    def emersion(self):

        self.canvas.itemconfig(self.id, image=self.sub)
        pos = self.canvas.coords(self.id)
        if pos[1] > 250.0:
            deep = 250
            print(deep)
            m = 25
            while pos[1] >= self.start[1]:
                pos = self.canvas.coords(self.id)
                currentDeep = int(pos[1]) - 250
                j = int(currentDeep % 10)

                if j == 0:
                    m = m - 1
                self.canvas.itemconfig(self.id, image=self.div[m])
                self.canvas.move(self.id, 0, -1)

                system()

    def diving(self):
        self.canvas.itemconfig(self.id, image=self.sub)
        pos = self.canvas.coords(self.id)
        if self.pos[1] < 500.0:
            deep = 250
            m = 0
            while pos[1] <= 500:
                pos = self.canvas.coords(self.id)
                currentDeep = int(pos[1]) - self.start[1]
                j = int(currentDeep % 10)

                if j == 0:
                    m += 1
                try:
                    self.canvas.itemconfig(self.id, image=self.div[m])
                    self.canvas.move(self.id, 0, 1)
                except IndexError:
                    pass
                system()

            self.draw()
        elif self.pos[1] > 500.0:
            self.canvas.move(self.id, 0, 0)
            self.draw()
            system()

    def rotate(self, deg):

        self.canvas.itemconfig(self.id, image=self.sub)
        pos = self.canvas.coords(self.id)
        for x in range(-45, 46):
            self.canvas.itemconfig(self.id, image=self.rotate_pict[deg + 45])
            system()
        # print(rotate_pict)


deg = 15
s = Submarine()
s.rotate(deg=0)
btn1 = Button(tk, text="Всплытие!", command=s.emersion, width=15).place(x=1050, y=650)
btn2 = Button(tk, text="Погружение!", command=s.diving, width=15).place(x=1050, y=700)
# btn3 = Button(tk, text="Поворот!", command=s.rotate(15), width=15).place(x=1050, y=550)

# btn2 = Button(tk, text="Ввести параметры для расчёта!", command=new_window()).place(x=75, y=100)
# btn2 = Button(tk, text="Погружение!", command=s.diving).place(x=75, y=100)
# btn1.pack()
# btn2.pack()

mainloop()

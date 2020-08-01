from manimlib.imports import *
import sys
sys.path.append('..')


class Functon_parity(GraphScene):
    CONFIG = {
        "x_min": -3,
        "x_max": 3,
        "x_tick_frequency": 1,
        # "x_labeled_nums": range(-3, 4, 1),
        "x_axis_label": "$x$",
        "y_min": -1,
        "y_max": 9,
        "y_tick_frequency": 1,
        # "y_labeled_nums": range(0, 10, 1),
        "y_axis_label": "$y$",

        # "y_axis_height": 6,
        # "x_axis_height": 12,
        # "graph_origin": LEFT_SIDE / 7 * 6 + BOTTOM / 4 * 3,
        "graph_origin": ORIGIN+2*DOWN+2.5*LEFT,
        "text1": "设函数的定义域为D关于原点对称",
        "text2": "若对于任意$x\in D$",
        "text3": "恒有f(x)=f(-x)成立",
        "text4": "则$f(x)$为偶函数",
        "text5": "函数图像关于y轴对称",
        "text6": "$x$",
        "text7": "$-x$"

    }

    def construct(self):
        text = TextMobject(self.text1, self.text2, self.text3,
                           self.text4, self.text5, self.text6, self.text7)
        text.move_to(RIGHT*7+1.3*UP)
        text.scale(0.5)
        self.setup_axes(animate=True)
        self.wait()
        graph_yellow = self.get_graph(
            self.func, x_min=3, x_max=0, color=YELLOW)
        graph_red = self.get_graph(self.func, x_min=-3, x_max=0, color=RED)
        graph_head_red = self.get_graph(self.func, x_min=-3, x_max=-1.5)
        graph_head_yellow = self.get_graph(self.func, x_min=3, x_max=1.5)
        self.play(ShowCreation(graph_yellow),
                  ShowCreation(graph_red), run_time=3)
        self.wait(3)
        # 创造两个点
        d1 = Dot()
        d2 = Dot()
        # 将两个点移到各自的位置
        d1.move_to(graph_head_red.get_start())
        d2.move_to(graph_head_yellow.get_start())
        self.play(Write(text[0]))
        self.wait()
        self.add(d1, d2)
        self.wait(1)
        # 新建两条虚线
        dash_line4 = self.get_vertical_line_to_graph(
            -3, graph_head_red, line_class=DashedLine, color=WHITE)
        dash_line5 = self.get_vertical_line_to_graph(
            3, graph_head_yellow, line_class=DashedLine, color=WHITE)
        self.play(ShowCreation(dash_line4), ShowCreation(dash_line5))
        """
        实现在函数图像的两侧有两个点，同时有虚线，随着点的移动而更新
        """
        self.wait(3)
        self.play(FadeOut(dash_line4), FadeOut(dash_line5))

        self.wait()
        self.play(
            MoveAlongPath(d1, graph_head_red),
            MoveAlongPath(d2, graph_head_yellow),
            run_time=4
        )
        # 创建四条虚线
        dash_line1 = DashedLine(start=self.coords_to_point(
            1.5, 0), end=self.coords_to_point(1.5, self.func(1.5)), color=BLUE)
        dash_line2 = DashedLine(start=self.coords_to_point(-1.5, self.func(
            -1.5)), end=self.coords_to_point(1.5, self.func(1.5)), color=BLUE)
        dash_line3 = DashedLine(start=self.coords_to_point(
            -1.5, 0), end=self.coords_to_point(-1.5, self.func(1.5)), color=BLUE)
        text[1].move_to(text[0].get_center())

        self.wait(3)
        text[5].move_to(self.coords_to_point(1.5, -0.5))
        text[6].move_to(self.coords_to_point(-1.5, -0.5))
        self.play(ReplacementTransform(text[0], text[1]))
        self.wait(3)
        self.play(
            ShowCreation(dash_line1),
            ShowCreation(dash_line2),
            ShowCreation(dash_line3),
        )

        self.wait(3)
        text[2].move_to(text[1].get_center())

        self.play(Write(text[5]),
                  Write(text[6]))
        self.wait()
        self.play(ReplacementTransform(text[1], text[2]))
        self.wait(3)

        graph_end_red = self.get_graph(self.func, x_min=-1.5, x_max=0)
        graph_end_yellow = self.get_graph(self.func, x_min=1.5, x_max=0)
        self.play(
            FadeOut(dash_line1),
            FadeOut(dash_line2),
            FadeOut(dash_line3),
            FadeOut(text[5]),
            FadeOut(text[6])
        )
        self.play(
            MoveAlongPath(d1, graph_end_yellow),
            MoveAlongPath(d2, graph_end_red),
            run_time=4
        )
        self.play(FadeOut(d1), FadeOut(d2))
        text[3].move_to(text[2].get_center())
        self.wait()
        self.play(ReplacementTransform(text[2], text[3]))
        self.wait(3)
        text[4].move_to(text[3].get_center())
        self.play(ReplacementTransform(text[3], text[4]))
        self.wait()
    def func(self, x):
        return x**2


class Functon_parity_1(GraphScene):
    CONFIG = {
        "x_min": -3,
        "x_max": 3,
        "x_tick_frequency": 1,
        # "x_labeled_nums": range(-3, 4, 1),
        "x_axis_label": "$x$",

        "y_min": -8,
        "y_max": 8,
        "y_tick_frequency": 1,
        # "y_labeled_nums": range(0, 10, 1),
        "y_axis_label": "$y$",

        # "y_axis_height": 6,
        # "x_axis_height": 12,
        # "graph_origin": LEFT_SIDE / 7 * 6 + BOTTOM / 4 * 3,
        "graph_origin": 2*LEFT,
        # "fill_opacity": 0.5,
        # 可能要移动下坐标的位置
        "text1": "同理",
        "text2": "若$f(x) = -f(-x)$",
        "text3": "则$f(x)$为奇函数",
        "text4": "函数图像关于原点对称"
    }

    def construct(self):
        self.setup_axes(animate=False)
        text = TextMobject(self.text1, self.text2, self.text3, self.text4)
        text.scale(0.6)
        text.move_to(RIGHT*7.5+2.5*UP)
        self.wait(3)
        graph = self.get_graph(self.func, x_min=-2, x_max=2, color=GREEN)
        graph_label = self.get_graph_label(
            graph, label="f(x)", x_val=3, direction=LEFT)
        # 创建16个点对象
        dot_list = []
        x = -2
        for i in range(17):
            dot_list.append(Dot(radius=0.05))
            dot_list[i].move_to(self.coords_to_point(
                x, self.func(x)-(0.05 if x > 0 else -0.05)))
            self.play(ShowCreation(dot_list[i]), run_time=0.2)
            x += 0.25
        self.wait(3)
        self.play(ShowCreation(graph), run_time=3)
        self.wait(3)
        self.play(Write(text[0]))
        text[1].move_to(text[0].get_center())
        self.wait(3)
        self.play(ReplacementTransform(text[0], text[1]))
        self.wait(3)
        text[2].move_to(text[1].get_center())
        self.play(ReplacementTransform(text[1], text[2]))
        text[3].move_to(text[2].get_center())
        self.wait(3)
        self.play(ReplacementTransform(text[2], text[3]))
        self.wait()
        self.play(
            Rotate(
                graph,
                PI,
                run_time=4,
            )
        )

    def func(self, x):
        return x**3


class Question(Scene):
    def construct(self):
        question1 = TextMobject("Q:设f(x)为定义在(-m,m)的奇函数")
        question2 = TextMobject("若f(x)在(0,m)内单调增加,")
        question3 = TextMobject("证明f(x)在(-m,0)内也单调增加")
        text0 = TextMobject("证：在(-m,0)中任取$x_1,x_2$,且$x_1>x_2$")
        text1 = TextMobject("则$-x_1,-x_2 \\in (0,m)$,且$-x_1<-x_2$")
        text2 = TextMobject("$\\because f(x)$为奇函数")
        text3 = TextMobject("$\\therefore$"," $f($","$x_1$",")"," = ","$-f($","$-x_1$",")",","," $f($","$x_2$",")"," = ","$-f($","$-x_2$",")")
        text4 = TextMobject("又$f($x$)$在$(0,m)$中单调递增")
        text5 = TextMobject("$\\therefore$"," $f($","$-x_1$",")"," < ","$f($","$-x_2$",")")
        text6 = TextMobject("$\\therefore$"," $-f($","$-x_1$",")"," > ","$-f($","$-x_2$",")")
        text7 = TextMobject("即$f(x_1)>f(x_2)$")
        text8 = TextMobject("$\\therefore f(x)$在$(-m,0)$中也单调递增")
        question_group = VGroup(question2,question3)
        question_group.arrange(
            DOWN,
            aligned_edge = LEFT,
            buff=0.45
        )
        question1.move_to(2*UP)
        question_group.move_to(question1.get_center()+1.5*DOWN+0.3*RIGHT)
        for x in [question1,question2,question3]:
            self.play(FadeInFrom(x,UP))
            self.wait(3)
        self.wait(1)
        text0.move_to(1*LEFT+3*UP)
        self.play(
            FadeOut(question1),
            FadeOut(question2),
            FadeOut(question3),
        )
        self.wait()
        text0.scale(0.8)
        text_group1 = VGroup(text1,text2,text3,text4,text5,text6,text7,text8)
        text_group1.arrange(
            DOWN,
            aligned_edge = LEFT,
            buff=0.42
        )
        text_group1.next_to(text0.get_center()+3.4*DOWN+3.9*LEFT)
        text_group1.scale(0.8)
        self.play(Write(text0))
        self.wait(3)
        # for i in text_group1:
        #     self.play(Write(i))
        self.play(FadeInFrom(text1,UP))
        self.wait(3)
        self.play(ReplacementTransform(text1.copy(),text2))
        self.wait(3)
        self.play(
            Write(text3[:9])
        )
        self.wait(3)
        self.play(
            ReplacementTransform(text3[1].copy(),text3[9]),
            ReplacementTransform(text3[5].copy(),text3[13]),
            ReplacementTransform(text3[3].copy(),text3[11]),
            ReplacementTransform(text3[7].copy(),text3[15]),
            ReplacementTransform(text3[4].copy(),text3[12]),
        )
        self.wait()
        self.play(
            ReplacementTransform(text3[2].copy(),text3[10]),
            ReplacementTransform(text3[6].copy(),text3[-2]),
        )
        self.wait(3)
        self.play(FadeInFrom(text4,UP))
        self.wait(3)
        self.play(ReplacementTransform(text4.copy(),text5))
        self.wait(3)
        self.play(
            ReplacementTransform(text5[0].copy(),text6[0]),
            ReplacementTransform(text5[1].copy(),text6[1]),
            ReplacementTransform(text5[3].copy(),text6[3]),
            ReplacementTransform(text5[4].copy(),text6[4]),
            ReplacementTransform(text5[5].copy(),text6[5]),
            ReplacementTransform(text5[7].copy(),text6[7]),
            ReplacementTransform(text5[0].copy(),text6[0]),
        )
        self.wait(3)
        self.play(
            ReplacementTransform(text5[2].copy(),text6[2]),
            ReplacementTransform(text5[6].copy(),text6[6]),

        )
        self.wait(3)
        self.play(Write(text7))
        self.wait(3)
        self.play(
            ReplacementTransform(text7.copy(),text8)
        )
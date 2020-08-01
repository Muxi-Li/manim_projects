import random
from manimlib.imports import *
import sys
sys.path.append('..')


class FunctionGraph(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "x_tick_frequency": 1,
        "x_labeled_nums": range(0, 11, 1),
        "x_axis_label": "$x$",

        "y_min": 0,
        "y_max": 100,
        "y_tick_frequency": 10,
        "y_labeled_nums": range(0, 110, 10),
        "y_axis_label": "$y$",

        "y_axis_height": 6,
        "x_axis_height": 12,
        # "graph_origin": LEFT_SIDE / 7 * 6 + BOTTOM / 4 * 3,
        "graph_origin": 2.5 * DOWN + 4 * LEFT,

    }

    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(self.func, color=GREEN)
        graph_label = self.get_graph_label(
            graph, label="y=x^2", x_val=5, direction=RIGHT)
        self.play(ShowCreation(graph), ShowCreation(graph_label), run_time=3)
        self.wait()
        self.play(
            FadeOutAndShiftDown(graph_label)
        )
        x1 = 5
        x2 = 7
        # 生成两个点
        point1 = self.input_to_graph_point(x1, graph)
        point2 = self.input_to_graph_point(x2, graph)
        # pline1 = self.get_vertical_line_to_graph(x1,graph,color=YELLOW)
        # pline2 = self.get_vertical_line_to_graph(x2,graph,color=YELLOW)
        ptext1 = TextMobject("(x1,y1)")
        ptext2 = TextMobject("(x2,y2)")
        # graph1 = self.get_graph(self.func,color=RED,x_min=x1,x_max=x2)
        ptext1.next_to(point1, direction=LEFT)
        ptext2.next_to(point2, direction=LEFT)
        # 绘制两条虚线
        # dash_line1 = DashedLine(start=graph.get_corner()+x1*RIGHT,end=graph.get_corner()+point1,color=RED,stroke_width=3)
        # dash_line2 = DashedLine(start=graph.get_corner()+x2*RIGHT,end=graph.get_corner()+point2,color=RED,stroke_width=3)

        self.play(ShowCreation(ptext1), ShowCreation(ptext2))

        self.wait()
        # self.play(ShowCreation(graph1))

    def func(self, x):
        return x**2


class GraphTest(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "x_tick_frequency": 1,
        # "x_labeled_nums": range(0, 11, 1),
        "x_axis_label": "$x$",

        "y_min": 0,
        "y_max": 100,
        "y_tick_frequency": 10,
        # "y_labeled_nums": range(0, 110, 10),
        "y_axis_label": "$y$",
        "graph_origin": 3 * DOWN + 6 * LEFT,

    }

    def construct(self):
        # 创建一个坐标系
        self.setup_axes(animate=True)
        graph = self.get_graph(self.func, x_min=5, x_max=10, color=WHITE)
        graph_label = self.get_graph_label(
            graph, label="f(x)", x_val=10, direction=LEFT, color=RED)
        self.play(
            ShowCreation(graph),
            ShowCreation(graph_label)

        )
        self.wait()
        # 镜头1
        text1 = TextMobject("设函数f(x)的定义域为D")
        text1.scale(0.8)
        text1.next_to(self.coords_to_point(1, 80))
        # 画两条虚线
        dash_line1 = DashedLine(start=self.coords_to_point(
            5, 0), end=self.coords_to_point(5, 25), color=BLUE)
        dash_line2 = DashedLine(start=self.coords_to_point(
            10, 0), end=self.coords_to_point(10, 100), color=BLUE)
        self.play(Write(text1))
        self.wait()
        self.play(ShowCreation(dash_line1), ShowCreation(dash_line2))
        self.wait(3)

        # 镜头2
        self.play(FadeOut(text1), FadeOut(dash_line1), FadeOut(dash_line2))
        self.wait()
        text2 = TextMobject("取区间I，且$I\subset D$")
        text2.scale(0.8)
        text2.next_to(self.coords_to_point(1, 80))
        self.play(Write(text2))
        # 此处缺一个下括号动画
        self.wait()
        dash_line7 = DashedLine(start=self.coords_to_point(
            5, 0), end=self.coords_to_point(5, 25), color=BLUE)
        dash_line8 = DashedLine(start=self.coords_to_point(
            9, 0), end=self.coords_to_point(9, 81), color=BLUE)
        graph1 = self.get_graph(func=self.func, x_min=5, x_max=9, color=YELLOW)
        self.play(
            ShowCreation(dash_line7),
            ShowCreation(dash_line8),
        )

        self.play(ShowCreation(graph1))
        self.wait(3)

        # 镜头3
        self.play(FadeOut(text2), FadeOut(dash_line7), FadeOut(dash_line8))
        self.wait()

        text3 = TextMobject("任取$x_1$和$x_2\subset I$,且$x_1<x_2$")
        text3.scale(0.8)
        text3.next_to(self.coords_to_point(1, 80))
        # 在函数图像上绘制两个点
        p1 = Dot()
        p2 = Dot()
        p1.move_to(self.coords_to_point(6, 36-1), DOWN)
        p2.move_to(self.coords_to_point(8, 64-1), DOWN)
        # 创建四条虚线
        dash_line3 = DashedLine(start=self.coords_to_point(
            6, 0), end=self.coords_to_point(6, 36), color=BLUE)
        dash_line4 = DashedLine(start=self.coords_to_point(
            0, 36), end=self.coords_to_point(6, 36), color=BLUE)
        dash_line5 = DashedLine(start=self.coords_to_point(
            8, 0), end=self.coords_to_point(8, 64), color=BLUE)
        dash_line6 = DashedLine(start=self.coords_to_point(
            0, 64), end=self.coords_to_point(8, 64), color=BLUE)
        self.play(
            Write(text3)
        )
        self.wait()
        self.play(
            ShowCreation(p1),
            ShowCreation(p2),
            ShowCreation(dash_line3),
            ShowCreation(dash_line4),
            ShowCreation(dash_line5),
            ShowCreation(dash_line6),
        )
        self.wait(3)

        # # 创建位置标注
        dtext1 = TextMobject("(x1,y1)")
        dtext2 = TextMobject("(x2,y2)")
        dtext1.scale(0.7)
        dtext2.scale(0.7)
        dtext1.next_to(self.coords_to_point(6, self.func(6)+7), direction=LEFT)
        dtext2.next_to(self.coords_to_point(8, self.func(8)+7), direction=LEFT)
        self.play(
            ShowCreation(dtext1),
            ShowCreation(dtext2)
        )
        self.wait(3)

        # 镜头4
        self.play(FadeOut(text3))
        self.wait()
        text4 = TextMobject("恒有$f(x_1)<f(x_2)$")
        text4.scale(0.8)
        text4.next_to(self.coords_to_point(1, 80))
        self.play(Write(text4))
        self.wait(1)
        graph2 = self.get_graph(func=self.func, x_min=6, x_max=8, color=RED)
        self.play(ShowCreation(graph2))
        self.wait(3)

        # 镜头5
        self.play(FadeOut(text4))
        self.wait()
        text5 = TextMobject("则f(x)在区间I上单调递增")
        text5.scale(0.8)
        text5.next_to(self.coords_to_point(1, 80))
        self.play(Write(text5))

    def func(self, x):
        return x**2


class GraphTest2(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "x_tick_frequency": 1,
        # "x_labeled_nums": range(0, 11, 1),
        "x_axis_label": "$x$",

        "y_min": 0,
        "y_max": 100,
        "y_tick_frequency": 10,
        # "y_labeled_nums": range(0, 110, 10),
        "y_axis_label": "$y$",
        "graph_origin": 3 * DOWN + 6 * LEFT,
    }

    def construct(self):
        self.setup_axes(animate=False)

        # 创建坐标系
        graph = self.get_graph(func=self.func, x_min=1, x_max=8, color=WHITE)
        graph_label = self.get_graph_label(
            graph, label="f(x)", x_val=1, direction=RIGHT)
        # 创建两个点
        d1 = Dot()
        d2 = Dot()
        d1.move_to(self.coords_to_point(2, 50-1), DOWN)
        d2.move_to(self.coords_to_point(5, 20-1), DOWN)
        # 创建两条虚线
        dash_line1 = DashedLine(start=self.coords_to_point(
            2, 0), end=self.coords_to_point(2, 50), color=BLUE)
        dash_line2 = DashedLine(start=self.coords_to_point(
            2, 0), end=self.coords_to_point(2, 50), color=BLUE)
        dash_line3 = DashedLine(start=self.coords_to_point(
            5, 0), end=self.coords_to_point(5, 20), color=BLUE)
        dash_line4 = DashedLine(start=self.coords_to_point(
            0, 20), end=self.coords_to_point(5, 20), color=BLUE)
        # 创建标注
        text1 = TextMobject("$(x_1,y_1)$")
        text2 = TextMobject("$(x_2,y_2)$")
        text1.scale(0.7)
        text2.scale(0.7)
        text1.next_to(self.coords_to_point(2, 50), direction=RIGHT)
        text2.next_to(self.coords_to_point(5, 24), direction=RIGHT)
        self.add(graph, graph_label, d1, d2, dash_line1,
                 dash_line2, dash_line3, dash_line4, text1, text2)
        self.wait()

        # 标注
        text3 = TextMobject("同理，若$f(x_1)>f(x_2)$", "则$f(x)$在区间I上单调递减")
        text3.scale(0.8)
        text3[0].next_to(self.coords_to_point(5, 80))
        text3[1].next_to(self.coords_to_point(5, 80))

        self.wait(3)

        self.play(Write(text3[0]))
        self.wait(3)
        self.play(FadeOut(text3[0]))
        self.wait()
        self.play(Write(text3[1]))
        self.wait(4)

    def func(self, x):
        return 100/x


class Question(Scene):
    def construct(self):
        text1 = TextMobject("Q:怎么证明一个函数在某个区间的单调性？", height=8, width=8)
        text2 = TexMobject("Example:", "y", "=", "x", "+",
                           "\\ln{x}", ",", "x\\in \\left(0,+\\infty \\right)")
        text3 = TextMobject("证明：")
        text4 = TextMobject("在$(0,+\\infty \\right)$任取$x_1$和$x_2$,且$x_1<x_2$")
        text5 = TexMobject("y_1", "=", "x_1", "+", "\\ln", "{x_1}")
        text6 = TexMobject("y_2", "=", "x_2", "+", "\\ln", "{x_2}")
        text7 = TexMobject("y_1", "-", "y_2", "=",
                           "\\left( x_1-x_2 \\right)+ \\left( \\ln{x_1}-\\ln{x_2} \\right)"),
        text8 = TexMobject("=", "x_1", "-", "x_2", "+",
                           "\\ln{", "{x_1}", "\\over", "{x_2}","}")
        text9 = TexMobject("\\because  x_1<x_2")
        text10 = TexMobject("\\therefore ", "x_1-x_2<0",
                            ",", "\\frac{x_1}{x_2}<1")
        text11 = TextMobject("$\\therefore$","$\\ln{\\frac{x_1}{x_2}}$","<","0")
        text12 = TextMobject("$\\therefore$","$y_1 < y_2$")
        text13 = TextMobject("$\\therefore$", "y函数在$(0,+\infty)$上递增")
        text_group1_2 = VGroup(text1, text2)
        text_group1_2.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.5
        )
        text_group1_2.move_to(np.array([0, 1, 0]))
        self.play(Write(text1))
        self.wait(3)
        self.play(
            Transform(text1, text2)
        )
        transform_text = TexMobject("y", "=", "x", "+",
                                    "\\ln{x}", ",", "x\\in \\left(0,+\\infty \\right)")
        transform_text.move_to(np.array([-4, 3, 0]))
        self.wait(3)
        self.play(
            Transform(text1, transform_text)
        )
        self.wait(3)
        text3.move_to(transform_text.get_center()+1*DOWN+2.5*LEFT)
        self.play(Write(text3))
        self.wait(3)

        text4.move_to(np.array([-1, 2, 0]))
        self.play(FadeInFrom(text4, UP))
        self.wait(3)
        text5.move_to(np.array([-3.5, 1, 0]))
        self.play(Write(text5))
        self.wait(3)
        text6.move_to(np.array([-3.5, 0, 0]))
        # self.play(ReplacementTransform(text5.copy(), text6))
        self.play(
            Transform(text5[1].copy(),text6[1]),
            Transform(text5[3].copy(),text6[3]),
            Transform(text5[4].copy(),text6[4])
        )
        self.wait(1)
        self.play(
            Transform(text5[0].copy(),text6[0]),
            Transform(text5[2].copy(),text6[2]),
            Transform(text5[5].copy(),text6[5])
        )
        transform_text7 = TexMobject("y_1", "-", "y_2", "=",
                                     "\\left( x_1-x_2 \\right)+ \\left( \\ln{x_1}-\\ln{x_2} \\right)")
        transform_text7.move_to(np.array([-1.5, -1, 0]))
        self.wait(3)
        self.play(ReplacementTransform(text6.copy(), transform_text7))
        self.wait(3)

        text8.move_to(np.array([-1.8, -2, 0]))
        self.play(Write(text8))

        transform_text8 = TexMobject(
            "y_1-y_2=x_1-x_2+ln{{x_1}\\over{x_2}}")
        transform_text8.move_to(transform_text7.get_center()+2*LEFT)
        self.wait(3)
        self.play(
            FadeOut(transform_text7),
            ReplacementTransform(text8, transform_text8)
        )
        self.wait()
        text9.move_to(transform_text8.get_center()+1*DOWN+0.5*LEFT)
        self.play(Write(text9))
        text10.move_to(text9.get_center()+1*DOWN+1.4*RIGHT)
        self.wait()
        self.play(Write(text10))
        text11.move_to(text10.get_center()+1.5*LEFT)
        self.wait(3)
        self.play(ReplacementTransform(text10,text11))
        text12.move_to(text10.get_center())
        self.wait(3)
        self.play(ReplacementTransform(text11,text12))
        self.wait(3)
        text13.move_to(text12.get_center()+7*RIGHT)
        self.play(ReplacementTransform(text12.copy(),text13))









class Test(GraphScene):
    def construct(self):
        # plane = NumberPlane()  # 添加网格
        # plane.add_coordinates()  # 显示坐标
        # self.play(ShowCreation(plane))
        # # d = Dot()
        # text1 = TextMobject("2", "=", "1", "+", "1")
        # text2 = TextMobject("3", "=", "1", "+", "2")
        # vg = VGroup(text1, text2)
        # vg.arrange(
        #     DOWN,
        #     aligned_edge=LEFT,
        #     buff=0.5
        # )
        # self.wait()
        # vg.move_to(np.array([-5, 3, 0]))
        # self.play(Write(text1))
        # self.wait()
        # self.play(Write(text2[1]), Write(text2[3]))
        # self.wait(0.5)
        # self.play(
        #     Transform(text1[0].copy(), text2[0]),
        #     Transform(text1[2].copy(), text2[2]),
        #     Transform(text1[4].copy(), text2[4]),
        # )
        text1 = TexMobject("a")
        text2 = TexMobject("b")
        text3 = TexMobject("c")
        text4 = TexMobject("d")
        self.play(Write(text1))
        self.wait()
        self.play(Transform(text1,text2))
        self.wait()
        text1.move_to(1*UP)
        text2.move_to(1*DOWN)


        self.play(Write(text1),Write(text2))






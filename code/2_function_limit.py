import math
import sys
sys.path.append('..')
from manimlib.imports import *


class FunctionDefine(Scene):
    CONFIG = {
        "number1": "1\\\ 1.5\\\ 2\\\ 2.5\\\ 3",
        "number2": "2\\\ 3\\\ 4\\\ 5\\\ 6",
        "indicate_A_number": "\\\ 3.5",
        "indicate_B_number": "\\\ 7",
        "define_1": "假设数集A和B",
        "define_2": "对于$A$中的任意一个元素$x$",
        "define_3": "通过对应法则$f$",
        "define_4": "总能在$B$中有唯一确定的元素$y$与之对应",
        "define_5": "则称$x$和$y$存在函数关系",
        "define_6": "通常记为$y = f(x),x \\in A$",
        "introduction": "在介绍函数极限之前先来明确一下函数的概念和邻域",
        "ellipse_A": "A",
        "ellipse_B": "B",
        "domain": "定义域",
        "range": "值域",
        "f": "对应法则$f(x)=2x$"

    }

    def construct(self):
        # 创建文字对象
        # define = TextMobject(self.define_1, self.define_2, self.define_3,
        #                      self.define_4, self.define_5, self.define_6)
        define_1 = TextMobject(self.define_1)
        define_2 = TextMobject(self.define_2)
        define_3 = TextMobject(self.define_3)
        define_4 = TextMobject(self.define_4)
        define_5 = TextMobject(self.define_5)
        define_6 = TextMobject(self.define_6)
        define_1.move_to(2*DOWN)
        define_1.scale(0.7)
        # 创建两个椭圆
        ellipse1 = Ellipse()
        ellipse2 = Ellipse()
        # 设置椭圆的大小、颜色、旋转角度、位置
        ellipse_parametters = [(ellipse1, YELLOW, 2, PI/2, np.array([-2, 1, 0])),
                               (ellipse2, BLUE, 2, PI/2, np.array([2, 1, 0]))]
        for ellipse, color, size, anger, coord in ellipse_parametters:
            ellipse.set_color(color)
            ellipse.scale(size)
            ellipse.rotate(anger)
            ellipse.move_to(coord)
        # 引言
        introduction = TextMobject(self.introduction)
        introduction.scale(0.8)
        self.play(Write(introduction))
        self.wait(3)
        self.play(FadeOutAndShift(introduction, DOWN))
        # 显示椭圆
        self.play(
            FadeInFrom(ellipse1, UP),
            FadeInFrom(ellipse2, UP)
        )
        self.wait()
        # 显示：假设数集A和B
        ellipse_A = TextMobject(self.ellipse_A)
        ellipse_B = TextMobject(self.ellipse_B)
        ellipse_A.move_to(ellipse1.get_center()+2.3*UP)
        ellipse_B.move_to(ellipse2.get_center()+2.3*UP)

        self.play(
            Write(define_1),
            FadeInFrom(ellipse_A, UP),
            FadeInFrom(ellipse_B, UP),
        )
        self.wait()
        # 创建椭圆里面显示的数字
        text1 = TextMobject(self.number1, self.indicate_A_number)
        text2 = TextMobject(self.number2, self.indicate_B_number)
        text_parametters = [(text1, 0.8, ellipse1.get_center()),
                            (text2, 0.8, ellipse2.get_center())]
        for text, size, coord in text_parametters:
            text.scale(size)
            text.move_to(coord)
        # 显示椭圆元素
        self.play(
            FadeInFrom(text1, UP),
            FadeInFrom(text2, UP)
        )
        self.wait()
        # 显示："define_2": "对于$A$中的任意一个元素$x$"
        define_2.scale(0.7)
        define_2.move_to(define_1.get_center())
        self.play(
            ReplacementTransform(define_1, define_2),
        )
        self.wait(1)
        self.play(
            CircleIndicate(text1[1]),
            run_time=2

        )
        self.wait()
        # 显示："define_3": "通过对应法则$f$"
        define_3.scale(0.7)
        define_3.move_to(define_1.get_center())
        self.play(
            ReplacementTransform(define_2, define_3)
        )
        self.wait(3)
        # 显示："define_4": "总能在$B$中有唯一确定的元素$y$与之对应"
        define_4.scale(0.7)
        define_4.move_to(define_1.get_center())
        self.play(
            ReplacementTransform(define_3, define_4)
        )
        self.wait(1)
        self.play(
            CircleIndicate(text2[1]),
            run_time=2
        )
        # 创建六个箭头,并移到相应位置
        arrow_list = []
        for i in range(6):
            arrow_list.append(Arrow(1.8*LEFT+0.25*DOWN+0.5 *
                                    i*UP, 1.9*RIGHT+0.25*DOWN+0.5*i*UP))
        self.wait(1)
        self.play(
            GrowArrow(arrow_list[0])
        )
        self.wait()
        for arrow in arrow_list[1:]:
            self.play(ShowCreation(arrow))
        self.wait()
        # 显示："define_5": "则称$x$和$y$存在函数关系"
        define_5.scale(0.7)
        define_5.move_to(define_1.get_center())
        self.play(
            ReplacementTransform(define_4, define_5)
        )
        self.wait(3)
        # 显示："define_6": "通常记为$y = f(x),x \\in A$"
        define_6.scale(0.7)
        define_6.move_to(define_1.get_center())
        self.play(
            ReplacementTransform(define_5, define_6)
        )
        self.wait()
        domain, range_y, f = TextMobject(self.domain), TextMobject(
            self.range), TextMobject(self.f)
        other_parametters = [(domain, 0.7, YELLOW, ellipse1.get_center(
        )+1.7*LEFT), (range_y, 0.7, BLUE, ellipse2.get_center()+1.5*RIGHT), (f, 0.5, WHITE, arrow_list[5].get_center()+0.3*UP)]
        for para, size, color, coord in other_parametters:
            para.scale(size)
            para.set_color(color)
            para.move_to(coord)
        self.play(
            FadeInFrom(domain, UP),
            FadeInFrom(range_y, UP),
            FadeInFrom(f, UP),
        )
        self.wait(4)


class Area(GraphScene):
    CONFIG = {
        "define_1": "在数轴上取一点$a$",
        "define_2": "设$\\sigma$为一正数",
        "define_3": "则开区间$(a-\\sigma,a+\\sigma)$称为$a$的邻域",
        "define_4": "当$\\sigma \\rightarrow 0$时",
        "define_5": "$a-\\sigma,a+\\sigma$逼近于点$a$",
        "other": "这种简单的理解也可以延伸到二维平面和三维空间上"
    }
    def construct(self):

        # 创建一条数轴
        number_line = NumberLine(x_min=-3, x_max=3)
        values_x = [(np.array([-3, 0, 0]), "-3"), (np.array([-3, 0, 0]), "$a-\\sigma$"), (np.array([-2, 0, 0]), "-2"), (np.array([-1, 0, 0]), "-1"),
                    (np.array([0, 0, 0]), "$a$"), (np.array([1, 0, 0]), "1"), (np.array([2, 0, 0]), "2"), (np.array([3, 0, 0]), "$a+\\sigma$"), (np.array([3, 0, 0]), "3")]
        axis_x_label = VGroup()
        for position, x_label in values_x:
            text = TextMobject(x_label)
            text.scale(0.7)
            text.next_to(position, DOWN)
            axis_x_label.add(text)
        self.play(ShowCreation(number_line))
        self.wait()
        # 显示："difine_1":"在数轴上取一点$a$"
        define_1 = TextMobject(self.define_1)
        define_1.scale(0.7)
        define_1.move_to(1.2*DOWN)
        self.play(
            ShowCreation(axis_x_label[4]),
            FadeInFrom(define_1, DOWN)
        )
        self.wait(3)
        # 显示："difine_2":"设$\\sigma$为一正数"
        define_2 = TextMobject(self.define_2)
        define_2.scale(0.7)
        define_2.move_to(define_1.get_center())
        self.play(ReplacementTransform(define_1, define_2))
        self.wait(3)
        brace_top_large_label = VGroup(axis_x_label[0], axis_x_label[-1])
        brace_top_middle_label = VGroup(axis_x_label[2], axis_x_label[-3])
        brace_top_small_label = VGroup(axis_x_label[3], axis_x_label[-4])

        # 创建上括号
        brace_top_large = Brace(brace_top_large_label,
                                UP, buff=MED_LARGE_BUFF+0.4)
        brace_top_middle = Brace(
            brace_top_middle_label, UP, buff=MED_LARGE_BUFF+0.2)
        brace_top_small = Brace(brace_top_small_label, UP, buff=MED_LARGE_BUFF)
        # 显示："define_3":"则开区间$(a-\\sigma,a+\\sigma)$称为$a$的邻域"
        define_3 = TextMobject(self.define_3)
        define_3.scale(0.7)
        define_3.move_to(define_1.get_center())
        self.play(
            ReplacementTransform(define_2, define_3),
            ShowCreation(axis_x_label[1]),
            ShowCreation(axis_x_label[-2]),
            FadeInFrom(brace_top_large, UP)
        )
        self.wait(3)
        # 显示："define_4":"当$a \\rightarrow 0$时"
        define_4 = TextMobject(self.define_4)
        define_4.scale(0.7)
        define_4.move_to(define_1.get_center())
        self.play(ReplacementTransform(define_3, define_4))
        self.wait(3)
        # 显示："define_5":"$a-\\sigma,a+\\sigma$逼近于点$a$"
        define_5 = TextMobject(self.define_5)
        define_5.scale(0.7)
        define_5.move_to(define_1.get_center())
        self.play(ReplacementTransform(define_4, define_5))
        self.wait()
        self.play(
            axis_x_label[1].shift, RIGHT,
            axis_x_label[-2].shift, LEFT,
            FadeOutAndShift(brace_top_large, DOWN),
            FadeInFrom(brace_top_middle, UP)
        )
        self.wait()
        self.play(
            axis_x_label[1].shift, RIGHT,
            axis_x_label[-2].shift, LEFT,
            axis_x_label[1].shift, RIGHT,
            FadeOutAndShift(brace_top_middle, DOWN),
            FadeInFrom(brace_top_small, UP)
        )

        self.wait(3)
        other = TextMobject(self.other)
        other.scale(0.7)
        other.move_to(define_1.get_center())
        self.play(ReplacementTransform(define_5, other))
        self.wait(4)


class FunctionLimitToValue(GraphScene):
    CONFIG = {
        "define_1": "设函数$f(x)$在点$x_0$的某一去心邻域内有定义",
        "define_2": "如果存在常数A",
        "define_3": "对于任意给定的正数$\\varepsilon$,可以理解成很小很小的正数",
        "define_4": "总存在正数$\\sigma$",
        "define_5": "使当$x$满足$0<\\left|x-{x}_{0}\\right|<\\sigma$时",
        "define_6": "$f(x)$满足$\\left|f(x)-A\\right|<\\varepsilon$",
        "define_7": "即当$\\sigma$趋于0时",
        "define_8": "$\\varepsilon$趋于0",
        "define_9": "$f(x-\\sigma)\\rightarrow A,f(x+\\sigma)\\rightarrow A$",
        "define_10": "那么A叫为函数$f(x)$当$x\\rightarrow x_0$时的极限",
        "define_11": "翻译成大白话就是：",
        "define_12": "$\\lim _{x\\rightarrow x_0}{f(x)=A}$或$f(x)\\rightarrow A$(当$x\\rightarrow x_0$)",
        "label_A": "$A$",
        "label_A1": "$A+\\varepsilon$",
        "x_min": 0,
        "x_max": 10,
        "x_tick_frequency": 1,
        "axes_color": BLUE,

        "y_min": 10,
        "y_max": 30,
        "y_tick_frequency": 5,
        "graph_origin": 2.3 * DOWN + 4 * LEFT,
    }
    def construct(self):
        self.wait(3)
        introduction = TextMobject("这里讲两种函数的极限：趋于某个值和趋于无穷的极限")
        self.play(FadeInFrom(introduction,UP))
        self.wait(3)
        self.play(FadeOutAndShift(introduction,DOWN))
        # 创建一个坐标系
        self.setup_axes()
        graph = self.get_graph(self.func, x_min=1, x_max=9, color=GREEN)
        graph_label = self.get_graph_label(
            graph, label="f(x)", x_val=9, direction=LEFT, color=WHITE)
        self.play(ShowCreation(graph), ShowCreation(graph_label), run_time=2)
        self.wait(3)
        define_1 = TextMobject(self.define_1)
        define_2 = TextMobject(self.define_2)
        define_3 = TextMobject(self.define_3)
        define_4 = TextMobject(self.define_4)
        define_5 = TextMobject(self.define_5)
        define_6 = TextMobject(self.define_6)
        define_7 = TextMobject(self.define_7)
        define_8 = TextMobject(self.define_8)
        define_9 = TextMobject(self.define_9)
        define_10 = TextMobject(self.define_10)
        define_11 = TextMobject(self.define_11)
        define_12 = TextMobject(self.define_12)
        define_1.scale(0.6)
        define_1.move_to(3.1*DOWN)
        define_parametters = [define_2, define_3,
                              define_4, define_5, define_6, define_7, define_8, define_9, define_10, define_11, define_12]
        for define in define_parametters:
            define.scale(0.6)
            define.move_to(define_1.get_center())
        # 显示："define_1":"设函数$f(x)$在点$x_0$的某一去心邻域内有定义"
        self.play(Write(define_1))
        self.wait(1)

        values_x = [(i, '-') for i in range(1, 8)]
        for value in [(2, "$x_0-\\sigma$"), (5, "$x_0$"), (8, "$x_0+\\sigma$")]:
            values_x.append(value)
        axis_x_label = VGroup()
        for x_coord, x_text in values_x:
            text = TextMobject(x_text)
            text.scale(0.7)
            text.next_to(self.coords_to_point(
                x_coord, 10), DOWN, buff=SMALL_BUFF)
            axis_x_label.add(text)
        self.play(
            # *[FadeInFrom(label, UP) for label in axis_x_label[-3:]]
            FadeInFrom(axis_x_label[-2], UP)
        )
        self.wait()
        dashed_line_x0 = DashedLine(start=self.coords_to_point(
            5, 10), end=self.coords_to_point(5, self.func(5)), color=YELLOW)
        circle_x0 = Circle(
            radius=0.1, arc_center=self.coords_to_point(5, self.func(5)))
        self.play(ShowCreation(dashed_line_x0), ShowCreation(circle_x0))
        self.wait(3)
        # 显示："define_2": "如果存在常数A"
        self.play(ReplacementTransform(define_1, define_2))
        dashed_line_A = DashedLine(start=self.coords_to_point(
            0, self.func(5)), end=self.coords_to_point(5, self.func(5)))
        label_A = TextMobject(self.label_A)
        label_A.scale(0.8)
        label_A.next_to(self.coords_to_point(0, self.func(5)), direction=LEFT)
        self.wait(1)
        self.play(ShowCreation(dashed_line_A), ShowCreation(label_A))
        self.wait(3)

        # 显示："define_3": "对于任意给定的正数$\\varepsilon$,可以理解成很小很小的正数"
        self.play(ReplacementTransform(define_2, define_3))
        dashed_line_A1 = DashedLine(
            start=self.coords_to_point(0, self.func(2)), end=self.coords_to_point(9, self.func(2)))
        dashed_line_A2 = DashedLine(start=self.coords_to_point(
            2, 10), end=self.coords_to_point(2, self.func(2)))
        dashed_line_A3 = DashedLine(start=self.coords_to_point(
            8, 10), end=self.coords_to_point(8, self.func(8)))
        label_A1 = TextMobject(self.label_A1)
        label_A1.scale(0.8)
        label_A1.next_to(self.coords_to_point(0, self.func(2)), direction=LEFT)
        self.wait(1)
        self.play(
            ShowCreation(dashed_line_A1),
            ShowCreation(label_A1),
        )
        self.wait(3)

        # 显示："define_4": "总存在正数$\\sigma$"
        self.play(ReplacementTransform(define_3, define_4))
        self.wait(1)
        self.play(

            FadeInFrom(axis_x_label[-1]),
            FadeInFrom(axis_x_label[-3]),
        )
        self.wait(1)
        self.play(
            # ShowCreation(dashed_line_A1),

            ShowCreation(dashed_line_A2),
            ShowCreation(dashed_line_A3),
        )
        self.wait(3)

        # 显示："define_5": "使当$x$满足$0<\\left|x-{x}_{0}\\right|<\\sigma$时"
        self.play(ReplacementTransform(define_4, define_5))
        self.wait(3)

        # 显示："define_6": "$f(x)$满足$\\left|f(x)-A\\right|<\\varepsilon$"
        self.play(ReplacementTransform(define_5, define_6))
        self.wait(3)

        # 显示："define_7":"即当$sigma\\$趋于0时"
        self.play(ReplacementTransform(define_6, define_7))
        self.wait(3)

        # 显示："define_8":"$\\varepsilon$趋于0"
        self.play(ReplacementTransform(define_7, define_8),
                  )
        self.wait(2)
        for i in range(1, 3):
            self.play(
                FadeOut(dashed_line_A1),
                FadeOut(dashed_line_A2),
                FadeOut(dashed_line_A3),
                axis_x_label[-3].shift, RIGHT,
                axis_x_label[-1].shift, LEFT,
                label_A1.next_to, self.coords_to_point(0, self.func(2+i))
            )
            dashed_line_A1 = DashedLine(
                start=self.coords_to_point(0, self.func(2+i)), end=self.coords_to_point(9, self.func(2+i)))
            dashed_line_A2 = DashedLine(start=self.coords_to_point(
                2+i, 10), end=self.coords_to_point(2+i, self.func(2+i)))
            dashed_line_A3 = DashedLine(start=self.coords_to_point(
                8-i, 10), end=self.coords_to_point(8-i, self.func(8-i)))
            self.play(
                ShowCreation(dashed_line_A1),
                ShowCreation(dashed_line_A2),
                ShowCreation(dashed_line_A3),
            )
            self.wait()

        # self.wait(3)

        # 显示："define_9":"$f(x-\\sigma)\\rightarrow A$,f(x+\\sigma)\\rightarrow A"
        self.play(ReplacementTransform(define_8, define_9))
        self.wait(3)

        # 显示："define_10": "那么A叫为函数$f(x)$当$x\\rightarrow x_0$时的极限"
        self.play(ReplacementTransform(define_9, define_10))
        self.wait(3)

        # 显示："define_11": "翻译成大白话就是："
        self.play(ReplacementTransform(define_10, define_11))
        self.wait(3)

        # 显示："define_12": "$\\lim _{x\\rightarrow x_0}{f(x)=A}$或$f(x)\\rightarrow A$(当$x\\rightarrow x_0$)"
        self.play(ReplacementTransform(define_11, define_12))
        self.wait(3)

    def setup_axes(self):
        # 自定义坐标系
        GraphScene.setup_axes(self)
        self.y_axis.shift(
            DOWN*abs(self.y_axis[0].points[0]-self.x_axis[0].points[0]))

        self.y_axis_label_mob.next_to(self.y_axis[0].get_end(), LEFT)

    def func(self, x):
        return (x-5)**2+13


class FunctionLimitToInf(GraphScene):
    CONFIG = {
        "x_min": -30,
        "x_max": 30,
        "x_tick_frequency": 5,
        "axes_color": BLUE,

        "y_min": -1,
        "y_max": 1.5,
        "y_tick_frequency": 1,
        "graph_origin": ORIGIN,
        "define_1": "对于这个函数$f(x)$",
        "define_2": "当$x \\rightarrow \\infty $时",
        "define_3": "$f(x)\\rightarrow 0$",
        "define_4": "趋于无穷的极限和趋于某个值的极限有着相似的定义"

    }

    def construct(self):
        self.setup_axes()
        define_1 = TextMobject(self.define_1)
        define_2 = TextMobject(self.define_2)
        define_3 = TextMobject(self.define_3)
        define_4 = TextMobject(self.define_4)
        graph1 = self.get_graph(self.func, x_min=0.01, x_max=30, color=GREEN)
        graph2 = self.get_graph(self.func, x_min=-30, x_max=-0.01, color=GREEN)

        self.wait(3)
        self.play(
            ShowCreation(graph1),
            ShowCreation(graph2)
        )
        self.wait(3)
        define_1.scale(0.7)
        define_1.move_to(2.7*DOWN)
        self.play(Write(define_1))
        self.wait(3)
        define_2.scale(0.7)
        define_2.move_to(define_1.get_center())
        self.play(ReplacementTransform(define_1, define_2))
        self.wait(1)
        circle1 = Circle(
            radius=0.2, arc_center=self.coords_to_point(30, 0))
        circle2 = Circle(
            radius=0.2, arc_center=self.coords_to_point(-30, 0))
        self.play(
            ShowCreation(circle1),
            ShowCreation(circle2),
        )
        # self.wait(2)
        # self.play(Write(define_2))
        self.wait(3)
        define_3.scale(0.7)
        define_3.move_to(define_1.get_center())
        self.play(ReplacementTransform(define_2, define_3))
        self.wait(3)

        define_4.scale(0.7)
        define_4.move_to(define_1.get_center())
        self.play(ReplacementTransform(define_3, define_4))
        self.wait(3)

    def func(self, x):
        return math.sin(x)/x


class Question(Scene):
    CONFIG = {
        "question_1": "Q:用函数极限的定义证明",
        "question_2": "$\\lim _{ x\\rightarrow -\\frac { 1 }{ 2 }  }{ \\frac { 1-4{ x }^{ 2 } }{ 2x+1 }  } =2$",
        "prove_1":"证明：",
        "prove_2": "$\\because x \\rightarrow 0,x \\neq -\\frac{1}{2}$",
        "prove_3": "$\\left| \\frac { 1-4{ x }^{ 2 } }{ 2x+1 } -2 \\right| =\\left| 1-2x-2 \\right| =2\\left| x-(-\\frac { 1 }{ 2 } ) \\right| $",
        "prove_4": "要使$\\left| \\frac { 1-4{ x }^{ 2 } }{ 2x+1 } -2 \\right| < \\varepsilon$",
        "prove_5":"只要$\\left| x-(-\\frac { 1 }{ 2 } ) \\right| <\\frac { \\varepsilon }{ 2 } $",
        "prove_6":"$\\therefore \\forall \\varepsilon >0$,取$\\delta =\\frac { \\varepsilon  }{ 2 } $",
        "prove_7":"则当$0<\\left| x-(-\\frac { 1 }{ 2 } ) \\right| <\\delta $时",
        "prove_8":"就有$\\left| \\frac { 1-4{ x }^{ 2 } }{ 2x+1 } -2 \\right| < \\varepsilon$",
        "prove_9":"即$\\lim _{ x\\rightarrow -\\frac { 1 }{ 2 }  }{ \\frac { 1-4{ x }^{ 2 } }{ 2x+1 }}=2$"
    }

    def construct(self):
        question_1 = TextMobject(self.question_1)
        question_2 = TextMobject(self.question_2)
        prove_1 = TextMobject(self.prove_1)
        prove_2 = TextMobject(self.prove_2)
        prove_3 = TextMobject(self.prove_3)
        prove_4 = TextMobject(self.prove_4)
        prove_5 = TextMobject(self.prove_5)
        prove_6 = TextMobject(self.prove_6)
        prove_7 = TextMobject(self.prove_7)
        prove_8 = TextMobject(self.prove_8)
        prove_9 = TextMobject(self.prove_9)
        question_group = VGroup(question_1,question_2)
        question_group.arrange(
            DOWN,
            buff=0.4
        )
        self.wait()
        self.play(FadeInFrom(question_1,UP))
        self.wait(1)
        self.play(Write(question_2))
        self.wait(3)
        self.play(
            FadeOut(question_1),
            question_2.to_edge,UL
        )
        self.wait(3)
        prove_1.scale(0.8)
        prove_1.move_to(6.2*LEFT+2.5*UP)
        self.play(FadeInFrom(prove_1,UP))
        self.wait(3)
        # prove_10 = question_2.copy()
        prove_group = VGroup(prove_2,prove_3,prove_4,prove_5,prove_6,prove_7,prove_8,prove_9)
        prove_group.arrange(
            DOWN,
            aligned_edge = LEFT,
            buff=0.2
        )
        prove_group.scale(0.8)
        prove_group.move_to(1.8*LEFT+0.3*DOWN)
        # self.play(Write(prove_10))
        self.play(FadeInFrom(prove_2,UP))
        self.wait(3)
        self.play(FadeInFrom(prove_3,UP))
        self.wait(3)
        self.play(ReplacementTransform(prove_3.copy(),prove_4))
        self.wait(3)
        self.play(ReplacementTransform(prove_4.copy(),prove_5))
        self.wait(3)
        self.play(FadeInFrom(prove_6,UP))
        self.wait(3)
        self.play(FadeInFrom(prove_7,UP))
        self.wait(3)
        self.play(ReplacementTransform(prove_7.copy(),prove_8))
        self.wait(3)
        self.play(ReplacementTransform(prove_8.copy(),prove_9))
        self.wait(4)
        # self.play(ReplacementTransform(prove_9.copy(),prove_10))
        # self.wait(4)
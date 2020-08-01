import math
from manimlib.imports import *
import sys
sys.path.append('..')


class MyAxes(GraphScene):

    def construct(self):
        line = Line()
        d1 = Dot().move_to(2*RIGHT)
        d2 = Dot().move_to(2*UP)
        line.put_start_and_end_on(d1.get_center(), d2.get_center())
        self.play(ShowCreation(line))
        self.wait()


class Infinity(GraphScene):
    CONFIG = {
        "x_labels": None,
    }

    def construct(self):
        text = TextMobject("无穷大与无穷小").scale(0.8)
        rec1 = Rectangle(width=0.1, color=BLUE)\
            .set_fill(BLUE, 1)\
            .move_to(2*LEFT)
        rec2 = Rectangle(width=4, height=6, color=BLACK)\
            .set_fill(BLACK, 1)\
            .next_to(rec1, direction=RIGHT, buff=0)
        rec2.add_updater(
            lambda r: r.next_to(rec1, direction=RIGHT, buff=0)
        )
        self.add(text, rec2)
        self.play(
            FadeInFrom(rec1, UP)
        )
        self.wait(1)
        self.play(
            rec1.shift, 4*RIGHT,
            # rate_func=there_and_back,
            # run_time=3
        )
        self.wait()
        self.play(
            rec1.shift, 4*LEFT,
            # rate_func=there_and_back,
            # run_time=3
        )
        self.wait(1)
        self.play(FadeOutAndShift(rec1, DOWN))
        # 创建两个坐标轴
        self.setup_axes_x()
        graph_x = self.get_graph(lambda x: x, x_min=-5.5, x_max=5.5, color=RED)
        # 函数图像、坐标轴、label集
        graph_axies_group = VGroup(
            self.axes, graph_x)
        self.play(ShowCreation(graph_x))

        # self.play(ShowCreation(graph_infty_right),ShowCreation(graph_infty_left),ShowCreation(graph_x))
        self.wait()
        definitions = [
            "$x \\rightarrow x_0$",
            "$\\forall \\varepsilon>0,\\exists \\sigma>0$,当$0<\\left|x-x_0\\right|<\\sigma$时",
            "$f(x)$满足：$\\left|f(x)\\right|<\\varepsilon$",
            "即$f(x)$是当$x \\rightarrow x_0$时的无穷小",
            "$x \\rightarrow \\infty$",
            "$\\forall \\varepsilon>0,\\exists X>0$,当$\\left|x\\right|>X$时",
            "$f(x)$满足：$\\left|f(x)\\right|<\\varepsilon$",
            "即$f(x)$是当$x \\rightarrow \\infty$时的无穷小",
            "总结：",
            "$\\lim_{x \\to x_0}f(x)=0$或$\\lim_{x \\to \\infty}f(x)=0$",
            "那么$f(x)$就是当$x \\rightarrow x_0$或$x \\rightarrow \\infty$的无穷小"
        ]
        definitions_mob = VGroup(
            VGroup(
                *[
                    TextMobject(mob).scale(0.6)for mob in definitions[:4]
                ]
            ).arrange(
                DOWN,
                aligned_edge=LEFT
            ).to_edge(LEFT),
            VGroup(
                *[
                    TextMobject(mob).scale(0.6)for mob in definitions[4:8]
                ]
            ).arrange(
                DOWN,
                aligned_edge=LEFT
            ).to_edge(LEFT),
            VGroup(
                *[
                    TextMobject(mob).scale(0.6)for mob in definitions[8:]
                ]
            ).arrange(
                DOWN,
                aligned_edge=LEFT
            ).to_edge(LEFT)
        )
        captions = [
            "注意这里的$\\varepsilon$是任意的正数",
            "可以理解成$\\varepsilon$是无限接近于零的正数",
            "既然$\\left|f(x)\\right|$满足永远小于一个疯狂接近零的正数",
            "那么$f(x)$也疯狂接近于零",
        ]
        captions_mob = VGroup(
            *[
                TextMobject(mob).scale(0.6)
                                .to_edge(DOWN) for mob in captions
            ]
        )

        # 在图像上建立四个点
        x_d1 = Dot().move_to(self.coords_to_point(-4, 0))
        x_d2 = Dot().move_to(self.coords_to_point(4, 0))
        y_d1 = Dot().move_to(self.coords_to_point(0, -4))
        y_d2 = Dot().move_to(self.coords_to_point(0, 4))
        x_y_d1 = Dot().move_to(self.coords_to_point(-4, -4))
        x_y_d2 = Dot().move_to(self.coords_to_point(4, 4))
        # 点集
        dot_group = VGroup(
            x_d1,
            x_d2,
            y_d1,
            y_d2,
            x_y_d1,
            x_y_d2
        )
        self.play(Write(definitions_mob[0][:3]))
        self.wait()
        self.play(FadeInFrom(self.x_axis_labels, UP),
                  FadeInFrom(self.y_axis_labels, LEFT))
        vertical_dashed_line1 = DashedLine(x_d1, x_y_d1)
        vertical_dashed_line2 = DashedLine(x_d2, x_y_d2)
        plane_dashed_line1 = DashedLine(y_d1, x_y_d1)
        plane_dashed_line2 = DashedLine(y_d2, x_y_d2)
        # 线集
        line_group = VGroup(
            vertical_dashed_line1,
            vertical_dashed_line2,
            plane_dashed_line1,
            plane_dashed_line2
        )
        self.add(x_d1, x_d2, y_d1, y_d2, x_y_d1, x_y_d2)
        self.wait(1)
        self.play(
            *[
                ShowCreation(line) for line in line_group
            ],
        )
        self.wait()
        self.play(Write(captions_mob[0][:2]))
        self.wait(3)
        for cap in captions_mob[1:]:
            self.play(Transform(captions_mob[0], cap))
            self.wait(3)
        self.wait()
        # 创建各个部分的update函数
        x_tracker = ValueTracker(-4)
        x_y_d1.add_updater(
            lambda d: d.move_to(self.coords_to_point(
                x_tracker.get_value(), x_tracker.get_value()))
        )
        x_y_d2.add_updater(
            lambda d: d.move_to(
                self.coords_to_point(-x_tracker.get_value(), -x_tracker.get_value()))
        )
        x_d1.add_updater(
            lambda d: d.move_to(self.coords_to_point(x_tracker.get_value(), 0))
        )
        x_d2.add_updater(
            lambda d: d.move_to(
                self.coords_to_point(-x_tracker.get_value(), 0))
        )
        y_d1.add_updater(
            lambda d: d.move_to(self.coords_to_point(0, x_tracker.get_value()))
        )
        y_d2.add_updater(
            lambda d: d.move_to(self.coords_to_point(
                0, -x_tracker.get_value()))
        )
        vertical_dashed_line1.add_updater(
            lambda line: line.put_start_and_end_on(
                x_d1.get_center(), x_y_d1.get_center())
        )
        vertical_dashed_line2.add_updater(
            lambda line: line.put_start_and_end_on(
                x_d2.get_center(), x_y_d2.get_center())
        )
        plane_dashed_line1.add_updater(
            lambda line: line.put_start_and_end_on(
                y_d1.get_center(), x_y_d1.get_center())
        )
        plane_dashed_line2.add_updater(
            lambda line: line.put_start_and_end_on(
                y_d2.get_center(), x_y_d2.get_center())
        )
        self.x_axis_labels[0].add_updater(
            lambda label: label.next_to(x_d1.get_center(), direction=DL)
        )
        self.x_axis_labels[2].add_updater(
            lambda label: label.next_to(x_d2.get_center(), direction=DOWN)
        )
        self.y_axis_labels[0].add_updater(
            lambda label: label.next_to(y_d1.get_center(), direction=DL)
        )
        self.y_axis_labels[1].add_updater(
            lambda label: label.next_to(y_d2.get_center(), direction=LEFT)
        )
        self.play(
            x_tracker.increment_value, 3,
            run_time=4
        )
        self.remove(x_tracker)
        self.play(Write(definitions_mob[0][3]))
        self.wait(3)
        graph_group = VGroup(
            graph_axies_group,
            dot_group,
            line_group,
            self.x_axis_labels,
            self.y_axis_labels

        )
        self.play(
            FadeOutAndShiftDown(captions_mob[0]),
            FadeOutAndShiftDown(graph_group),
            FadeOutAndShiftDown(definitions_mob[0])
        )
        graph_axies_group.scale(0.5)\
                         .shift(2*UP)
        self.wait(3)
        self.setup_axes_infty()
        graph_infty_right = self.get_graph(
            self.func, x_min=1/6, x_max=6, color=YELLOW)
        graph_infty_left = self.get_graph(
            self.func, x_min=-6, x_max=-1/6, color=YELLOW)
        # 函数图像、坐标轴、label集
        graph_axies_group1 = VGroup(
            graph_infty_right,
            graph_infty_left,
            self.axes,
            # 缺少labels
        )
        self.play(ShowCreation(graph_infty_right),
                  ShowCreation(graph_infty_left))
        self.wait()
        self.play(FadeInFrom(definitions_mob[1], UP))
        # 创建两个点
        self.wait(3)
        x_y_d3 = Dot().move_to(self.coords_to_point(-1/6, -6))
        x_y_d4 = Dot().move_to(self.coords_to_point(1/6, 6))
        dot_group1 = VGroup(x_y_d3, x_y_d4)
        self.add(x_y_d3, x_y_d4)
        self.wait()
        # 创建update函数
        x_tracker1 = ValueTracker(1/6)
        x_y_d3.add_updater(
            lambda d: d.move_to(self.coords_to_point(
                x_tracker1.get_value(), self.func(x_tracker1.get_value())))
        )
        x_y_d4.add_updater(
            lambda d: d.move_to(
                self.coords_to_point(-x_tracker1.get_value(), self.func(-x_tracker1.get_value())))
        )
        self.play(
            x_tracker1.increment_value, (6-1/6),
            run_time=4
        )

        self.wait(2)
        self.play(
            FadeOutAndShift(definitions_mob[1], DOWN),
            FadeOutAndShift(dot_group1),
            graph_axies_group1.scale, 0.5,
            graph_axies_group1.shift, 2*DOWN,
            FadeInFrom(graph_axies_group, UP)
        )
        self.wait()
        self.play(FadeInFrom(definitions_mob[2], UP))

    def func(self, x):
        return 1/x

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        self.y_axis.label_direction = LEFT

    def setup_axes_x(self):
        self.x_min = -6
        self.x_max = 6
        self.y_min = -6
        self.y_max = 6
        self.x_tick_frequency = 2
        self.y_tick_frequency = 2

        self.x_axis_width = 6
        self.y_axis_height = 6
        self.graph_origin = 3*RIGHT
        self.axes_color = BLUE
        # self.x_leftmost_tick = 1
        self.setup_axes()
        x_values = [
            (-4, "$x_0-\\sigma$", DL),
            (0.5, "$x_0$", DOWN),
            (4, "$x+\\sigma$", DOWN)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_text, x_direction in x_values:
            text = TextMobject(x_text).scale(0.6)\
                                      .next_to(self.coords_to_point(x_val, 0), direction=x_direction)
            self.x_axis_labels.add(text)
        y_values = [
            (-4, "$-\\varepsilon$", DL),
            (4, "$\\varepsilon$", LEFT)
        ]
        self.y_axis_labels = VGroup()
        for y_val, y_text, y_direction in y_values:
            text = TextMobject(y_text).scale(0.6)\
                                      .next_to(self.coords_to_point(0, y_val), direction=y_direction)
            self.y_axis_labels.add(text)

        self.play(Write(self.x_axis), Write(self.y_axis))

    def setup_axes_infty(self):
        self.x_min = -6
        self.x_max = 6
        self.y_min = -6
        self.y_max = 6
        self.x_tick_frequency = 2
        self.y_tick_frequency = 2

        self.x_axis_width = 6
        self.y_axis_height = 6
        self.graph_origin = 3*RIGHT
        self.axes_color = BLUE
        self.setup_axes()

        self.play(Write(self.x_axis), Write(self.y_axis))


class Infinitesimal(GraphScene):
    CONFIG = {
        "x_min": -1,
        "x_max": 7,
        "y_min": -1,
        "y_max": 7,
        "x_tick_frequency": 2,
        "y_tick_frequency": 2,
        "x_axis_width": 6,
        "y_axis_height": 6,
        "axes_color": BLUE,
        "x_axis.label_direction": DOWN,
        "y_axis.label_direction": LEFT,
        "graph_origin": 2*DOWN

    }

    def construct(self):
        self.setup_axes1()
        graph1 = self.get_graph(
            self.func1, x_min=1/7+1, x_max=7, color=RED)
        self.play(ShowCreation(graph1))
        # 函数图像集
        graph_group1 = VGroup(
            graph1,
            self.axes,
            self.x_axis_labels,
            self.y_axis_labels
        )
        l = DashedLine(self.coords_to_point(1, -1), self.coords_to_point(1, 8))
        self.wait()
        self.play(ShowCreation(l))
        self.wait()
        self.play(FadeOut(l))
        self.remove(l)
        self.wait()
        # 无穷大的定义
        definitions = [
            "$x \\rightarrow x_0$",
            "$\\forall M>0,\\exists \\sigma>0$,当$0<\\left|x-x_0\\right|<\\sigma$时",
            "$f(x)$满足：$\\left|f(x)\\right|>M$",
            "即$f(x)$是当$x \\rightarrow x_0$时的无穷大",
            "$x \\rightarrow \\infty$",
            "$\\forall M>0,\\exists X>0$,当$\\left|x\\right|>X$时",
            "$f(x)$满足：$\\left|f(x)\\right|>M$",
            "即$f(x)$是当$x \\rightarrow \\infty$时的无穷大",
            "总结：",
            "$\\lim_{x \\to x_0}f(x)=\\infty$或$\\lim_{x \\to \\infty}f(x)=\\infty$",
            "那么$f(x)$就是当$x \\rightarrow x_0$或$x \\rightarrow \\infty$的无穷大"
        ]
        # 定义语句的位置
        definitions_mob = VGroup(
            VGroup(
                *[TextMobject(mob).scale(0.6) for mob in definitions[:4]]
            ).arrange(
                DOWN,
                aligned_edge=LEFT
            ).to_edge(LEFT),
            VGroup(
                *[TextMobject(mob).scale(0.6) for mob in definitions[4:8]]
            ).arrange(
                DOWN,
                aligned_edge=LEFT
            ).to_edge(LEFT),
            VGroup(
                *[TextMobject(mob).scale(0.6) for mob in definitions[8:]]
            ).arrange(
                DOWN,
                aligned_edge=LEFT
            ).to_edge(LEFT)
        )
        # 字幕语句
        captions = [
            "注意这里的$M$是任意的正数",
            "可以理解成$M$是无限增大的正数",
            "既然$\\left|f(x)\\right|$满足永远大于一个疯狂增长的正数",
            "那么$\\left|f(x)\\right|$也肯定无限增大,趋于无穷大"

        ]
        captions_mob = VGroup(
            *[
                TextMobject(mob).scale(0.6)
                                .to_edge(DOWN) for mob in captions
            ]
        )
        # 函数上的点
        d_x_y = Dot().move_to(self.coords_to_point(5, self.func1(5)))
        d_x = Dot().move_to(self.coords_to_point(5, 0))
        d_y = Dot().move_to(self.coords_to_point(0, self.func1(5)))
        # 点集
        dot_group = VGroup(d_x, d_y, d_x_y)
        # 虚线
        vertical_line = DashedLine(d_x, d_x_y)
        plane_line = DashedLine(d_y, d_x_y, dash_spacing=0.5)
        # 线集
        line_group = VGroup(vertical_line, plane_line)
        # 显示定义
        for defs in definitions_mob[0][:3]:
            self.play(FadeInFrom(defs, UP))
            self.wait(2)
        # 显示labels
        self.play(
            FadeInFrom(self.x_axis_labels),
            FadeInFrom(self.y_axis_labels)
        )
        self.wait(1)
        self.play(ShowCreation(dot_group))
        self.wait(1)
        self.play(ShowCreation(line_group))
        self.wait()
        # 添加update函数
        self.tracker = ValueTracker(5)
        d_x_y.add_updater(self.update_d_x_y)
        d_x.add_updater(self.update_d_x)
        d_y.add_updater(self.update_d_y)

        def update_ver_line(mob):
            l = DashedLine(d_x, d_x_y)
            mob.become(l)
        # def update_pla_line(mob):
        #     l = DashedLine(d_y,d_x_y)
        #     mob.become(l)
        vertical_line.add_updater(update_ver_line)
        plane_line.add_updater(
            lambda l: l.put_start_and_end_on(
                d_y.get_center(), d_x_y.get_center())
        )
        self.x_axis_labels[1].add_updater(self.update_x_label)
        self.y_axis_labels[0].add_updater(self.update_y_label)
        self.play(Write(captions_mob[0]))
        self.wait(3)
        for cap in captions_mob[1:]:
            self.play(Transform(captions_mob[0], cap))
            self.wait(3)
        self.play(
            self.tracker.increment_value, -(4-1/7),
            run_time=4
        )
        # self.tracker.remove()
        self.wait()
        self.play(FadeInFrom(definitions_mob[0][3], UP))
        self.wait(3)
        # 全集
        group_all = VGroup(
            graph_group1,
            dot_group,
            # line_group
        )
        self.play(FadeOut(group_all),
                  FadeOut(captions_mob[0]),
                  FadeOut(vertical_line),
                  FadeOut(plane_line),
                  FadeOut(definitions_mob[0]))
        self.wait()
        # 新的坐标系
        self.setup_axes2()
        graph2 = self.get_graph(self.func2, x_min=-1, x_max=7, color=YELLOW)
        # 函数图像集
        graph_group2 = VGroup(graph2, self.axes)
        self.play(ShowCreation(graph2))
        self.wait()
        self.play(FadeInFrom(definitions_mob[1], UP))
        self.wait(3)
        # 创建点
        self.t_offset = 1
        d = Dot().move_to(graph2.point_from_proportion(2))
        self.add(d)

        def update_dot(mob, dt):
            rate = dt*0.2
            mob.move_to(graph2.point_from_proportion(
                (self.t_offset + rate) % 1))
            self.t_offset += rate
        d.add_updater(update_dot)
        self.add(graph2, d)
        self.wait(4)
        d.remove_updater(update_dot)
        self.wait()
        self.play(
            FadeOutAndShift(definitions_mob[1], DOWN),
            FadeOutAndShift(graph_group2),
            FadeInFrom(definitions_mob[2], UP),
        )
        self.wait()

    def update_d_x(self, d):
        d.move_to(self.coords_to_point(self.tracker.get_value(), 0))

    def update_d_y(self, d):
        d.move_to(self.coords_to_point(
            0, self.func1(self.tracker.get_value())))

    def update_d_x_y(self, d):
        d.move_to(self.coords_to_point(self.tracker.get_value(),
                                       self.func1(self.tracker.get_value())))

    def update_x_label(self, label):
        label.next_to(self.coords_to_point(
            self.tracker.get_value(), 0), direction=DOWN, buff=0.1)

    def update_y_label(self, label):
        label.next_to(self.coords_to_point(0, self.func1(
            self.tracker.get_value())), direction=LEFT, buff=0.1)

    def func1(self, x):
        return 1/(x-1)

    def func2(self, x):
        return 0.1*np.exp(x)

    def setup_axes2(self):
        self.x_min = -1
        self.x_max = 7
        self.y_min = -1
        self.y_max = 7
        self.x_tick_frequency = 2
        self.y_tick_frequency = 2
        self.x_axis_width = 6
        self.y_axis_height = 6
        self.axes_color = BLUE
        # self.x_axis.label_direction = DOWN
        # self.y_axis.label_direction = LEFT
        self.graph_origin = 1.5*RIGHT+2*DOWN
        self.setup_axes()

    def setup_axes1(self):
        self.setup_axes()
        x_values = [
            (1, "$x_0$", UL),
            (5, "$x_0+\\sigma$", DOWN)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_text, direction in x_values:
            text = TextMobject(x_text).scale(0.6)\
                                      .next_to(self.coords_to_point(x_val, 0), direction=direction, buff=0.1)
            self.x_axis_labels.add(text)
        y_values = [(1/5, "$M$")]
        self.y_axis_labels = VGroup()
        for y_val, y_text in y_values:
            text = TextMobject(y_text).scale(0.6)\
                                      .next_to(self.coords_to_point(0, y_val), direction=LEFT, buff=0.1)
            self.y_axis_labels.add(text)

        # 绘制坐标轴动画
        self.play(ShowCreation(self.x_axis), ShowCreation(self.y_axis))

    def setup_axes(self):
        GraphScene.setup_axes(self)

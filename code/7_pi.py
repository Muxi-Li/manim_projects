from manimlib.imports import *
import sys

sys.path.append('..')

class Cylinder(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=-60 * DEGREES)
        cylinder = ParametricSurface(
            lambda u, v: np.array([
                np.cos(v*TAU),
                np.sin(v*TAU),
                2 * (1 - u)
            ]),
            resolution=(6, 35)).fade(0.3)  # Resolution of the surfaces
        # self.add(cylinder)
        surface1 = ParametricSurface(
            lambda u, v:np.array([
                u*np.cos(v * TAU),
                u*np.sin(v * TAU),
                2
            ])
        )
        surface2 = ParametricSurface(
            lambda u, v: np.array([
                u * np.cos(v * TAU),
                u * np.sin(v * TAU),
                0
            ])
        )
        self.add(surface1,surface2,cylinder)
class Sphere(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=-60 * DEGREES)
        sphere = ParametricSurface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]), v_min=0, v_max=TAU, u_min=-PI / 2, u_max=PI / 2, checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32))
        self.add(sphere)
class Cone(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=60 * DEGREES, theta=-60 * DEGREES)
        cone = ParametricSurface(
            lambda u, v: np.array([
                u * np.cos(v),
                u * np.sin(v),
                u
            ]), v_min=0, v_max=TAU, u_min=-2, u_max=0, checkerboard_colors=[GREEN_D, GREEN_E],
            resolution=(15, 32)).scale(1)
        cone.move_to(np.array([0,0,1]))
        self.add(cone)
class Scene1(MovingCameraScene):
    def construct(self):
        captions = [
            '由圆周率，你能想到什么呢？',               # 0
            '比如',                                   # 1
            '还有',                                   # 2
            '甚至',                                   # 3
            "这些都跟圆周率有关",                      # 4
            "那么圆周率在一开始是怎么计算出来的？",      # 5
            "小学老师曾对我们说",                      # 6
            "用一个圆形的轮子就可以计算圆周率",         # 7
            "我还真信了",                             # 8
            "（公元前287年-前212年）",
            "阿基米德",
            """
            阿基米德是希腊化时代著名的数学家、
            物理学家、天文学家、工程师等。早
            在两千多年前，阿基米德就利用极限
            的思想，算出了圆周率的前两位小数，
            开创了几何计算圆周率的先河。
            """

        ]
        captions_mob = VGroup(
            *[
                Text(mob,font='方正黑体简体').scale(0.4)\
                         .to_edge(DOWN) for mob in captions
            ]
        )
        formula = [
            "S=\\pi r^2",                               # 0
            "S=\\frac{\\theta \pi r^2}{360^{\\circ}}",  # 1
            "L=\\frac{\\theta \pi r}{180^{\\circ}}",    # 2
            "V=\\frac{4}{3}\\pi r^3",                   # 3
            "V=\\pi r^2 h",                             # 4
            "V=\\frac{1}{3}\\pi r^2 h",                 # 5
            "f(x;\\mu ,\\sigma )=\\frac{1}{\\sigma \\sqrt{2\\pi} } \\exp \\left(-\\frac{(x-\\mu)^2}{2\\sigma^2}\\right)",
            "\\sum_{n=1}^{\\infty}\\frac{1}{n^2}=\\lim_{x \\to +\\infty} \\left(\\frac{1}{1^2}+\\frac{1}{2^2}+\\cdots +\\frac{1}{n^2}\\right)=\\frac{\\pi^2}{6}",
            """  \\pi = \\cfrac{4}{1 
          + \\cfrac{1^2}{3
          + \\cfrac{2^2}{5 
          + \\cfrac{3^2}{7
          + \\cfrac{4^2}{9
          +\\ddots }} } } }""",
           "\\frac{\\pi}{2}=\\sum_{k=0}^{\\infty}\\frac{k!}{\\left(2k+1\\right)!!}=\\sum_{k=0}^{\\infty}\\frac{2^kk!^2}{\\left(2k+1\\right)!}",
           "C=2\\pi r",
           "\\pi=\\frac{c}{2r}",
        ]
        formula_mob = VGroup(
            *[TexMobject(mob).scale(0.8) for mob in formula]
        )
        formula_mob1 = VGroup(*[formula for formula in formula_mob[3:6]])
        formula_mob1.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=1.5
        ).shift(2*RIGHT)
        formula_mob2 = VGroup(
            *[formula for formula in formula_mob[6:9]]
        )
        formula_mob2.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.4
        ).shift(2*LEFT)
        formula_mob[9].next_to(formula_mob[8],direction=RIGHT,buff=1.5)
        notes = [
            "S",
            "S",
            'L',
            "r",
            "r",
            "\\theta",
            "r",
            "\\theta"
        ]
        notes_mob = VGroup(
            *[
                TexMobject(mob).scale(0.6) for mob in notes
            ]
        )
        circle = Circle(radius=0.8,color=YELLOW)
        circle.set_fill(PINK,opacity=1)
        secter = Sector(outer_radius=0.8,stroke_width=5,start_angle=PI/4,angle=PI*7/4,color=BLUE,stroke_color=YELLOW)
        arc = Arc(radius=0.8,start_angle=45*DEGREES,angle=315*DEGREES,color=RED,stroke_color=YELLOW)
        geometry_mob = VGroup(circle,secter,arc)
        geometry_mob.arrange(
            RIGHT,
            aligned_edge=DOWN,
            buff=0.6
        )
        self.play(Write(captions_mob[0]))
        self.wait()
        self.play(ReplacementTransform(captions_mob[0],captions_mob[1]))
        # self.wait(1)
        self.play(
            *[
                ShowCreation(mob) for mob in geometry_mob
            ]
        )
        # self.wait(1)
        self.play(
            geometry_mob.arrange,DOWN,{'buff':0.6},
            geometry_mob.shift,3*LEFT
        )
        # self.wait(1)
        d1 = Dot(radius=0.06).move_to(circle.get_arc_center())
        d2 = Dot(radius=0.06).move_to(secter.get_center())
        d3 = Dot(radius=0.06).move_to(arc.get_arc_center())
        l1 = DashedLine(d3,arc.get_start())
        l2 = DashedLine(d3,arc.get_end())
        angle_arc2 = Arc(arc_center=d2.get_center(),radius=0.2,start_angle=45*DEGREES,angle=315*DEGREES,color=RED)
        angle_arc3 = Arc(arc_center=d3.get_center(),radius=0.2,start_angle=45*DEGREES,angle=315*DEGREES,color=RED)
        sphere = ImageMobject(r"C:\Manim\manim\media\videos\7_pi\images\Sphere1-1.png").scale(0.8)
        cylinder = ImageMobject(r"C:\Manim\manim\media\videos\7_pi\images\Cylinder1-1.png").scale(0.8)
        cone = ImageMobject(r"C:\Manim\manim\media\videos\7_pi\images\Cone1-1.png").scale(0.8)
        self.play(
            *[ShowCreation(d) for d in [d1,d2,d3,l1,l2,angle_arc2,angle_arc3]]
        )
        # self.wait(0.5)
        arrows_data = [
            (d1.get_center(),d1.get_center()+0.8*LEFT),
            (d2.get_center(), d2.get_center() + 0.8*LEFT),
            (d3.get_center(), d3.get_center() + 0.8*LEFT),
        ]
        arrow_mob = VGroup()
        for d1,d2 in arrows_data:
            arrow = Arrow(d1,d2,buff=0)
            arrow.set_angle(45*DEGREES)
            arrow_mob.add(arrow)
        notes_data = [
            (0,arrow_mob[0].get_start(),LEFT,0.5),
            (1,arrow_mob[1].get_start(),LEFT,0.5),
            (2,arrow_mob[2].get_start(),LEFT,1),
            (3,arrow_mob[0].get_center(),DOWN,0.1),
            (4,arrow_mob[1].get_center(), DOWN, 0.1),
            (5,angle_arc2, UP, 0.1),
            (6,arrow_mob[2].get_center(), DOWN, 0.1),
            (7,angle_arc3, UP, 0.1),
        ]
        for i,tar,dir,buff in notes_data:
            notes_mob[i].next_to(tar,direction=dir,buff=buff)
        self.play(ShowCreation(arrow_mob))
        # self.wait(1)
        self.play(
            *[Write(mob) for mob in notes_mob]
        )
        # self.wait(1)
        for formula,g in zip(formula_mob[:3],geometry_mob):
            formula.next_to(g,direction=RIGHT,buff=4)
        self.play(
            *[ShowCreation(formula) for formula in formula_mob[:3]]
        )
        self.wait()
        self.play(
            FadeOut(
                Group(*self.mobjects)
            )
        )
        self.play(Write(captions_mob[2]))
        cylinder.shift(2 * LEFT)
        sphere.next_to(cylinder, UP, 0.4)
        cone.next_to(cylinder, DOWN, 0.4)
        self.play(
            *[
                FadeInFrom(mob, dir) for mob, dir in zip([cylinder, sphere, cone], [LEFT, UP, DOWN])
            ]
        )
        self.play(
            *[Write(mob) for mob in formula_mob[3:6]]
        )
        self.wait()
        self.play(
            FadeOut(
                Group(*self.mobjects)
            )
        )
        self.play(Write(captions_mob[3]))
        self.wait(4)
        self.play(
            *[Write(formula) for formula in formula_mob[6:10]]
        )
        self.wait()
        self.play(
            FadeOut(
                Group(*self.mobjects)
            )
        )
        self.play(Write(captions_mob[4]))
        self.wait()
        for cap in captions_mob[5:8]:
            self.play(Transform(captions_mob[4],cap))
            self.wait()
        self.play(FadeOut(captions_mob[4]))
        self.camera.frame.save_state()
        self.camera.frame.move_to(3*RIGHT)
        r = 1
        o = Dot(radius=0.07, color=GREEN).shift(UP)
        p = Dot(radius=0.07, color=RED)
        q = p.deepcopy()
        w = p.deepcopy()
        c = Circle(arc_center=o.get_center(), radius=r, color=BLUE)
        arrow = Arrow(o.get_center(), p.get_center(), buff=0, color=YELLOW)
        l = Line(p, w, color="#99CC33")
        theta = ValueTracker(0)

        def get_o(theta):
            return (theta * r * RIGHT + UP)

        o.add_updater(
            lambda o: o.move_to(get_o(theta.get_value()))
        )
        c.add_updater(
            lambda c: c.move_to(o.get_center())
        )

        def get_p(theta):
            return (RIGHT * r * (theta - np.sin(theta)) + UP * r * (1 - np.cos(theta)))

        p.add_updater(
            lambda p: p.move_to(get_p(theta.get_value()))
        )

        def get_w(theta):
            return (theta * r * RIGHT)

        w.add_updater(
            lambda d: d.move_to(get_w(theta.get_value()))
        )
        arrow.add_updater(
            lambda mob: mob.become(
                Arrow(
                    o.get_center(),
                    p.get_center(),
                    buff=0,
                    color=YELLOW
                )
            )
        )
        l.add_updater(
            lambda l: l.become(
                Line(q.get_center(), w.get_center(), color="#99CC33")
            )
        )
        self.add(o, p, c, arrow, l, q, w)
        self.wait()
        self.play(
            theta.increment_value, 2 * PI,
            run_time=6
        )
        brace = Brace(l,direction=DOWN,buff=0.2)
        formula_mob[10].next_to(brace,direction=DOWN,buff=0.1)
        formula_mob[11].next_to(formula_mob[10],direction=DOWN,buff=0.5)
        captions_mob[8].next_to(formula_mob[11],direction=DOWN,buff=1)
        self.play(
            *[FadeInFrom(mob) for mob in [brace,formula_mob[10]]]
        )
        self.wait(1)
        self.play(Write(formula_mob[11]))
        self.wait()

        self.play(Write(captions_mob[8]))
        self.wait()
        self.play(
            FadeOut(
                Group(*self.mobjects)
            )
        )
        Restore(self.camera.frame)
        # self.camera.frame.move_to(3 * LEFT)
        img = ImageMobject(r'C:\Manim\manim\media\videos\7_pi\images\Archimedes.png') \
              .scale(2)\
              .shift(1.8*LEFT)
        captions_mob[9].next_to(img,direction=DOWN,buff=0.2)
        captions_mob[10].next_to(captions_mob[9],direction=DOWN,buff=0.2)
        captions_mob[11].next_to(img,direction=RIGHT,buff=1)
        self.play(FadeInFrom(img,UP))
        self.play(
            *[FadeInFrom(mob,UP) for mob in captions_mob[9:]]
        )
        self.wait()

class Introduction(Scene):
    CONFIG = {
        "captions":[
            '由圆周率，你能想到什么呢？',  # 0
            '比如',  # 1
            '还有',  # 2
            '甚至',  # 3
            "这些都跟圆周率有关",                    # 4
            "那么圆周率是怎么计算出来的？",           # 5
            "小学老师曾对我们说",                    # 6
            "用一个圆形的轮子就可以计算圆周率",       # 7
            "当时我信了",                           # 8
            "古今中外，无数数学家在圆周率上的探索",   # 9
            "贯穿了数学上千年的发展历史",            # 10
            "从一开始的近似值3",                    # 11
            "到小数点后万亿位",                     # 12
            "每一位数都代表着时代的进步",            # 13
            "其中，阿基米德开创了几何计算圆周率的先河"  # 14
        ],
        "archimedes":[
            "阿基米德是希腊化时代著名的数学家、",
            "物理学家、天文学家、工程师等。",
            "早在两千多年前，阿基米德就利用极限",
            "的思想，算出了圆周率的前两位小数，",
            "开创了几何计算圆周率的先河。",
        ],
        "formula_sl":[
            "S=\\pi r^2",                               # 0
            "S=\\frac{\\theta \pi r^2}{360^{\\circ}}",  # 1
            "L=\\frac{\\theta \pi r}{180^{\\circ}}",    # 2
        ],
        "formula_v":[
            "V=\\frac{4}{3}\\pi r^3",   # 0
            "V=\\pi r^2 h",             # 1
            "V=\\frac{1}{3}\\pi r^2 h", # 2
        ],
        "formula_o":[
            "f(x;\\mu ,\\sigma )=\\frac{1}{\\sigma \\sqrt{2\\pi} } \\exp \\left(-\\frac{(x-\\mu)^2}{2\\sigma^2}\\right)",
            "\\sum_{n=1}^{\\infty}\\frac{1}{n^2}=\\lim_{x \\to +\\infty} \\left(\\frac{1}{1^2}+\\frac{1}{2^2}+\\cdots +\\frac{1}{n^2}\\right)=\\frac{\\pi^2}{6}",
            "\\frac{\\pi}{2}=\\sum_{k=0}^{\\infty}\\frac{k!}{\\left(2k+1\\right)!!}=\\sum_{k=0}^{\\infty}\\frac{2^kk!^2}{\\left(2k+1\\right)!}",
            """  \\pi = \\cfrac{4}{1 
                      + \\cfrac{1^2}{3
                      + \\cfrac{2^2}{5 
                      + \\cfrac{3^2}{7
                      + \\cfrac{4^2}{9
                      +\\ddots }} } } }
            """],
        "notes":[
            "S",
            "S",
            'L',
            "r",
            "r",
            "\\theta",
            "r",
            "\\theta"
        ],
        # 体积图形
        "sphere": ImageMobject(r"C:\Manim\manim\media\videos\7_pi\images\Sphere1-1.png").scale(0.8),
        "cylinder": ImageMobject(r"C:\Manim\manim\media\videos\7_pi\images\Cylinder1-1.png").scale(0.8),
        "cone": ImageMobject(r"C:\Manim\manim\media\videos\7_pi\images\Cone1-1.png").scale(0.8),

        "circle":Circle(
                        radius=0.8,
                        color=YELLOW,
                        fill_color=ORANGE,
                        fill_opacity=0.3
        ),
        "secter": Sector(
                        outer_radius=0.8,
                        stroke_width=5,
                        start_angle=PI / 4,
                        angle=PI * 7 / 4,
                        fill_color=ORANGE,
                        fill_opacity=0.3,
                        stroke_color=YELLOW
        ),
        "arc": Arc(
                    radius=0.8,
                    start_angle=45 * DEGREES,
                    angle=315 * DEGREES,
                    color=RED,
                    stroke_color=YELLOW
        ),

    }

    def construct(self):
        # captions
        captions_mob = VGroup(
            *[
                Text(mob,font='方正黑体简体').scale(0.4)\
                         .to_edge(DOWN) for mob in self.captions
            ]
        )
        # 有关圆的面积和周长公式
        formula_sl = VGroup(
            *[
                TexMobject(mob,color=RED_D).scale(0.8) for mob in self.formula_sl
            ]
        )
        formula_sl.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=1.5
        ).shift(3*RIGHT)
        # 体积公式
        formula_v = VGroup(
            *[
                TexMobject(mob,color=RED_D).scale(0.8) for mob in self.formula_v
            ]
        )
        formula_v.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=1.5
        ).shift(3*RIGHT)
        # 其他公式
        formula_o = VGroup(
            *[
                TexMobject(mob,color=RED_D).scale(0.8) for mob in self.formula_o
            ]
        )
        empty_mob = VectorizedPoint().to_edge(DOWN)
        # 平面图形
        geometry_mob = VGroup(self.circle, self.secter, self.arc)
        geometry_mob.arrange(
            RIGHT,
            aligned_edge=DOWN,
            buff=0.6
        )
        self.cylinder.shift(3 * LEFT)
        self.sphere.next_to(self.cylinder, UP, 0.4)
        self.cone.next_to(self.cylinder, DOWN, 0.4)

        for i in range(2):
            self.play(Transform(empty_mob,captions_mob[i]))
            self.wait()
        self.play(ShowCreation(geometry_mob))
        self.play(
            geometry_mob.arrange, DOWN, {'buff': 0.6},
            geometry_mob.shift, 3 * LEFT
        )
        # 调用乱七八糟的显示函数
        self.display_notes()
        self.play(
            *[Write(mob) for mob in formula_sl]
        )
        self.wait()
        self.play(
            FadeOut(
                Group(*self.mobjects)
            )
        )
        self.play(
            Write(captions_mob[2])
        )
        self.play(
            *[
                FadeInFrom(mob, dir) for mob, dir in zip([self.cylinder, self.sphere, self.cone], [LEFT, UP, DOWN])
            ]
        )
        self.play(
            *[Write(mob) for mob in formula_v]
        )
        self.wait()

        self.play(
            FadeOut(
                Group(*self.mobjects)
            )
        )
        self.play(Write(captions_mob[3]))
        self.wait(15)
        # 这里接列表镜头

        for cap in captions_mob[4:9]:
            self.play(
                Transform(captions_mob[3],cap)
            )
            self.wait()
        self.play(
            FadeOut(
                Group(*self.mobjects)
            )
        )

        r = 1
        o = Dot(radius=0.07).move_to(UP+3*LEFT)
        p = Dot(radius=0.07).shift(3*LEFT)
        q = p.deepcopy()
        w = p.deepcopy()
        c = Circle(arc_center=o.get_center(), radius=r,color=RED_D)
        arrow = Arrow(o.get_center(), p.get_center(), buff=0,color=YELLOW_C)
        l = Line(p, w,color=GREEN_SCREEN)
        theta = ValueTracker(0)

        def get_o(theta):
            return (3*LEFT+theta * r * RIGHT + UP)

        o.add_updater(
            lambda o: o.move_to(get_o(theta.get_value()))
        )
        c.add_updater(
            lambda c: c.move_to(o.get_center())
        )

        def get_p(theta):
            return (3*LEFT+RIGHT * r * (theta - np.sin(theta)) + UP * r * (1 - np.cos(theta)))

        p.add_updater(
            lambda p: p.move_to(get_p(theta.get_value()))
        )

        def get_w(theta):
            return (3*LEFT+theta * r * RIGHT)

        w.add_updater(
            lambda d: d.move_to(get_w(theta.get_value()))
        )
        arrow.add_updater(
            lambda mob: mob.become(
                Arrow(
                    o.get_center(),
                    p.get_center(),
                    buff=0,
                    color=YELLOW_C
                )
            )
        )
        l.add_updater(
            lambda l: l.become(
                Line(q.get_center(), w.get_center(), color=GREEN_SCREEN)
            )
        )
        self.add(o, p, c, arrow, l, q, w)
        self.wait()
        self.play(
            theta.increment_value, 2 * PI,
            run_time=5
        )
        self.wait(0.5)
        brace = Brace(l,direction=UP,buff=0.2)
        tex1 = TexMobject("C=2\\pi r",color=YELLOW_C)\
               .scale(0.8)\
               .next_to(brace,direction=DOWN,buff=0.1)

        tex2 = TexMobject("\\pi=\\frac{c}{2r}",color=YELLOW_C)\
               .scale(0.8)\
               .next_to(tex1,direction=DOWN,buff=0.5)
        self.play(
            *[FadeInFromDown(mob) for mob in [tex1,brace]]
        )
        self.wait(0.5)
        self.play(
            ReplacementTransform(tex1.copy(),tex2)
        )
        self.wait(2)
        self.play(
            FadeOut(
                Group(*self.mobjects)
            )
        )
        self.play(Write(captions_mob[9]))
        for cap in captions_mob[10:]:
            self.play(
                Transform(captions_mob[9],cap)
            )
            self.wait()
        # 下面接各个计算方法
        self.wait(6)

    def display_notes(self):
        notes_mob = VGroup(
            *[
                TexMobject(mob).scale(0.6) for mob in self.notes
            ]
        )
        d1 = Dot(radius=0.06).move_to(self.circle.get_arc_center())
        d2 = Dot(radius=0.06).move_to(self.secter.get_center())
        d3 = Dot(radius=0.06).move_to(self.arc.get_arc_center())
        l1 = DashedLine(d3, self.arc.get_start())
        l2 = DashedLine(d3, self.arc.get_end())
        angle_arc2 = Arc(arc_center=d2.get_center(),
                         radius=0.2,
                         start_angle=45 * DEGREES,
                         angle=315 * DEGREES,
                         color=RED
        )
        angle_arc3 = Arc(arc_center=d3.get_center(),
                         radius=0.2,
                         start_angle=45 * DEGREES,
                         angle=315 * DEGREES,
                         color=RED
        )
        self.add(d1,d2,d3,l1,l2,angle_arc2,angle_arc3)
        # self.wait(0.5)
        arrows_data = [
            (d1.get_center(), d1.get_center() + 0.8 * LEFT),
            (d2.get_center(), d2.get_center() + 0.8 * LEFT),
            (d3.get_center(), d3.get_center() + 0.8 * LEFT),
        ]
        arrow_mob = VGroup()
        for d1,d2 in arrows_data:
            arrow = Arrow(d1,d2,buff=0)
            arrow.set_angle(45*DEGREES)
            arrow_mob.add(arrow)
        notes_data = [
            (0, arrow_mob[0].get_start(), LEFT, 0.5),
            (1, arrow_mob[1].get_start(), LEFT, 0.5),
            (2, arrow_mob[2].get_start(), LEFT, 1),
            (3, arrow_mob[0].get_center(), DOWN, 0.1),
            (4, arrow_mob[1].get_center(), DOWN, 0.1),
            (5, angle_arc2, UP, 0.1),
            (6, arrow_mob[2].get_center(), DOWN, 0.1),
            (7, angle_arc3, UP, 0.1),
        ]
        for i,tar,dir,buff in notes_data:
            notes_mob[i].next_to(tar,
                                 direction=dir,
                                 buff=buff
            )
        self.add(arrow_mob,notes_mob)


class Table(Scene):
    CONFIG = {
        "rows":4,
        "columns":1,
        "height":6,
        "width":10,
        "formula_o": [
            "f(x;\\mu ,\\sigma )=\\frac{1}{\\sigma \\sqrt{2\\pi} } \\exp \\left(-\\frac{(x-\\mu)^2}{2\\sigma^2}\\right)",
            "\\frac{\\pi}{2}=\\sum_{k=0}^{\\infty}\\frac{k!}{\\left(2k+1\\right)!!}=\\sum_{k=0}^{\\infty}\\frac{2^kk!^2}{\\left(2k+1\\right)!}",
            "\\sum_{n=1}^{\\infty}\\frac{1}{n^2}=\\lim_{x \\to +\\infty} \\left(\\frac{1}{1^2}+\\frac{1}{2^2}+\\cdots +\\frac{1}{n^2}\\right)=\\frac{\\pi^2}{6}",
            """  \\pi = \\cfrac{4}{1 
                      + \\cfrac{1^2}{3
                      + \\cfrac{2^2}{5 
                      + \\cfrac{3^2}{7
                      + \\cfrac{4^2}{9
                      +\\ddots }} } } }
            """],
        "scale_data":[0.5,0.5,0.5,0.5],
        "notes":[
            "概率密度函数",
            "无穷级数",
            "巴塞尔问题",
            "连分数",
        ]

    }
    def construct(self):
        notes_mob = VGroup(
            *[
                Text(mob,font="方正黑体简体",color=YELLOW_C).scale(0.3) for mob in self.notes
            ]
        )
        formula_o = VGroup(
            *[
                TexMobject(mob,color=RED_D).scale(size) for mob,size in zip(self.formula_o,self.scale_data)
            ]
        )
        formula_o.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.4
        )
        rows = self.rows
        columns = self.columns
        height = self.height
        width = self.width
        rec = Rectangle(height=height,width=width)
        # 表格的四个点的坐标
        left_top = height/2*UP+width/2*LEFT
        right_down = height/2*DOWN+width/2*RIGHT
        right_top = height/2*UP+width/2*RIGHT
        left_down = height/2*DOWN+width/2*LEFT
        print(left_down)
        l1 = Line(left_top,right_top)
        formula_o[0].next_to(l1,direction=DOWN,buff=0.2)
                    # .shift(RIGHT)
        notes_mob[0].next_to(formula_o[0],direction=LEFT,buff=1)
        l2 = Line(left_top,right_top).next_to(formula_o[0],direction=DOWN,buff=0.2)
        formula_o[1].next_to(l2,direction=DOWN,buff=0.2)
                    # .shift(RIGHT)
        notes_mob[1].next_to(formula_o[1],direction=LEFT,buff=1.5)
        l3 = Line(left_top,right_top).next_to(formula_o[1],direction=DOWN,buff=0.2)
        formula_o[2].next_to(l3,direction=DOWN,buff=0.2)
                    # .shift(RIGHT)
        notes_mob[2].next_to(formula_o[2],direction=LEFT,buff=0.8)
        l4 = Line(left_top,right_top).next_to(formula_o[2],direction=DOWN,buff=0.2)
        formula_o[3].next_to(l4,direction=DOWN,buff=0.2)
                    # .shift(RIGHT)
        notes_mob[3].next_to(formula_o[3],direction=LEFT,buff=2)
        l5 = Line(left_top,left_down).shift((notes_mob[0].get_width()+0.3)*RIGHT)
        row_lines = VGroup(l2,l3,l4,l5)
        formula_o.shift(RIGHT)
        # self.add(rec,row_lines)
        self.play(FadeIn(rec),FadeIn(row_lines))
        self.wait()
        self.play(
            *[Write(note) for note in notes_mob]
        )
        self.wait()
        self.play(
            *[Write(mob) for mob in formula_o]
        )
        self.wait(4)

import random

class Demo1(Scene):
    def construct(self):
        # 创建六个矩形框
        rec_mob = VGroup(
            *[
                Rectangle(height=2,width=3,color=YELLOW) for i in range(6)
            ]
        )

        geo_mob = VGroup()

        # 阿基米德割圆法
        c1 = Circle(radius=1,color=RED_D)
        d1 = Dot(radius=0.05)
        ins_reg_polygon = RegularPolygon(
            n=6,
            radius=1,
            color=BLUE_D,
            stroke_width=4

        )
        cir_reg_polygon = RegularPolygon(
            n=6,
            radius=1,
            inscribed=False,
            color=BLUE_D,
            stroke_width=4

        )
        archimedes = VGroup(c1,ins_reg_polygon,cir_reg_polygon,d1).scale(0.8)
        geo_0 = VGroup(archimedes,rec_mob[0])
        geo_mob.add(geo_0)
        # archimedes.move_to(rec_mob[0])

       # 刘徽割圆法
        c2 = Circle(radius=1,color=RED_D)
        d2 = Dot(radius=0.05)
        ins_reg_polygon_6 = RegularPolygon(
            n=6,
            radius=1,
            color=BLUE_D,
            stroke_width=4
        )
        ins_reg_polygon_12 = RegularPolygon(
            n=12,
            radius=1,
            color=GREEN_SCREEN,
            stroke_width=4

        )
        verticles = ins_reg_polygon_12.get_vertices()
        lines = VGroup()
        for i in range(6):
            l = Line(verticles[i],verticles[6+i],color=PINK)
            lines.add(l)
        liuhui = VGroup(c2,ins_reg_polygon_6,ins_reg_polygon_12,lines).scale(0.8)
        geo_1 = VGroup(liuhui,rec_mob[1])
        geo_mob.add(geo_1)

        # 布丰投针
        lines_mob = VGroup()
        for angle,d in zip([45*DEGREES,135*DEGREES],[0.5*LEFT,1.1*RIGHT]):
            l = Line(color=RED_D)
            l.set_length(0.4)
            l.shift(d)
            l.set_angle(angle)
            lines_mob.add(l)

        rectangle_mob = VGroup(
            *[
                Rectangle(height=2,
                          width=0.6,
                          fill_color="#9f9f9f",
                          fill_opacity=0.5,
                          stroke_opacity=0,
                ) for i in range(3)
            ]
        )
        rectangle_mob.arrange(
            LEFT,
            aligned_edge=DOWN,
            buff=0.6
        )
        tex_l = TexMobject("l").scale(0.5)\
                               .next_to(lines_mob[0],direction=DOWN,buff=0.05)
        tex_t = TexMobject("t").scale(0.5)\
                               .shift(0.8*UP)
        geo_2 = VGroup(rectangle_mob,rec_mob[2],lines_mob,tex_l,tex_t)
        geo_mob.add(geo_2)

        #蒙地卡罗方法
        c4 = Circle(radius=1,color=RED_D)
        x_y = [(random.uniform(-1.5,1.5),random.uniform(-1,1)) for _ in range(500)]
        dots_mob = VGroup()
        for x,y in x_y:
            if (x**2+y**2) < 1:
                d = Dot(radius=0.02,color=RED_D).move_to(np.array([x,y,0]))
                dots_mob.add(d)
            else:
                d = Dot(radius=0.02,color=BLUE_D).move_to(np.array([x,y,0]))
                dots_mob.add(d)
        monte = VGroup(dots_mob,c4,rec_mob[3])
        geo_mob.add(monte)

        # 莱布尼茨公式
        tex1 = TexMobject("\\frac{\\pi }{4}=\\sum_{n=0}^{\\infty } \\frac{(-1)^n}{2n+1} ",color=RED_D).scale(0.8)
        geo_4 = VGroup(rec_mob[4],tex1)
        geo_mob.add(geo_4)

        # 拉马努金
        tex2 = TexMobject("\\frac{1}{\pi} = \\frac{2\\sqrt{2} }{9801} \\sum_{k=0}^{\\infty } \\frac{(4k)!(1103+26390k)}{k!^4(396^{4k})} ",color=RED_D).scale(0.35)
        geo_5 = VGroup(rec_mob[5],tex2)
        geo_mob.add(geo_5)

        # 设置矩形边框位置
        geo_data = [
            (-4,2,0),
            (0,2,0),
            (4,2,0),
            (-4,-0.5,0),
            (0,-0.5,0),
            (4,-0.5,0)
        ]
        for geo,position in zip(geo_mob,geo_data):
            position = np.array(position)
            geo.move_to(position)
        tex = TexMobject("......").next_to(rec_mob[4],direction=DOWN,buff=0.5)
        self.play(
            *[
                GrowFromCenter(mob) for mob in geo_mob
            ]
        )
        self.wait()
        self.play(Write(tex))
        self.wait(14)
        self.play(
            *[
                FadeOut(mob) for mob in [geo_mob[1:],tex]
            ]
        )
        self.play(
            ApplyFunction(
                lambda mob:mob.move_to(ORIGIN)\
                              .scale(2),
                geo_mob[0]
            )
        )
        self.wait(4)








class Scene2(Scene):
    CONFIG = {
        "captions":[
            "阿基米德从周长的角度出发",                   # 0
            "提出了正多边形竭尽圆周的做法",               # 1
            "随着圆的内接正多边形和外切正多边形边数的增加", # 2
            "正多边形的周长逐渐逼近圆的周长",              # 3
            "当边数足够多时",                            # 4
            "甚至可以用正多边形的周长代替圆的周长",        # 5
            "利用圆的周长公式，可以估算出圆周率的大小" ,     # 6
            "如果只是亲自用计算器计算的话",               # 7
            "视频到这里本就可以结束了",                     # 8
            "但在古代并没有计算器",                      # 9
        ],
        "titles":VGroup(
            *[
                Text(title,font="方正黑体简体").scale(0.4) for title in ["内接正多边形","外切正多边形","周长","周长"]
            ]
        ),
        "num_edge":[TexMobject("n = " + str(n)).scale(0.8) for n in range(3,21,1)],
        "inscribed_regular_polygon":[
            RegularPolygon(n=m,radius=1,color=GREEN_SCREEN).shift(3*LEFT+UP) for m in range(3,21,1)
        ],
        "circumscribed_regular_polygon":[
            RegularPolygon(n=m,radius=1,inscribed=False,color=BLUE_D).shift(3*RIGHT+UP) for m in range(3,21)
        ],
        "circles":[Circle(radius=1),Circle(radius=1)],
        "empty_mobjects":VGroup(VectorizedPoint(2*LEFT+UP),     # 0
                                VectorizedPoint(2*RIGHT+UP),    # 1
                                VectorizedPoint(ORIGIN),        # 2
                                VectorizedPoint().to_edge(DOWN),# 3
        ),  # 空物体，我是这么理解的
        "j":0,
        "formulas":[
            "P_n < 2\\pi r < Q_n",
            "\\frac{P_n}{2r} <\\pi < \\frac{Q_n}{2r}",
            "\\frac{na_n}{2r} < \\pi < \\frac{nb_n}{2r}",
            "n\\sin \\frac{180^\\circ}{n} < \\pi < n\\tan \\frac{180^\\circ}{n}"
        ],
        "notes":[
            "$a_n:$ 内接正多边形边长",
            "$b_n:$ 外切正多边形边长",
        ],
        "formula_a1":TexMobject(
            "C_1C_3",
            "="
            "\\frac{1}{2}",
            "a_n",
            "=",
            "r",
            "\\sin",
            "{\\theta",
            "\\over",
            "2}",
        ).scale(0.8),
        "formula_a2": TexMobject(
            "a_n",
            "=",
            "2",
            "r",
            "\\sin",
            "{\\theta",
            "\\over",
            "2}",
        ).scale(0.8),
        "formula_a3": TexMobject(
            "a_n",
            "=",
            "2",
            "r",
            "\\sin",
            "{180^{\\circ}",
            "\\over",
            "n}"
        ).scale(0.8),
        "formula_b1": TexMobject(
            "D_1D_3",
            "="
            "\\frac{1}{2}",
            "b_n",
            "=",
            "r",
            "\\tan",
            "{\\theta",
            "\\over",
            "2}",
        ).scale(0.8),
        "formula_b2": TexMobject(
            "b_n",
            "=",
            "2",
            "r",
            "\\tan",
            "{\\theta",
            "\\over",
            "2}",
        ).scale(0.8),
        "formula_b3": TexMobject(
            "b_n",
            "=",
            "2",
            "r",
            "\\tan",
            "{180^{\\circ}",
            "\\over",
            "n}"
        ).scale(0.8),
        "theta1":TexMobject(
            "\\theta",
            "=",
            "{360^{\\circ}",
            "\\over",
            "n}"
        ).scale(0.8),
        "theta2": TexMobject(
            "\\frac{\\theta}"
            "{2}",
            "=",
            "{180^{\\circ}",
            "\\over",
            "n}"
        ).scale(0.8),
        "n":[TexMobject("n="+str(n)).scale(0.8) for n in range(6,97)],
        "pi":[TexMobject(format(n*np.sin(np.pi/n),'.4f')+"<\\pi<"+format(n*np.tan(np.pi/n),'.4f'),color=RED_D).scale(0.8) for n in range(6,97)],
        "t2c":{
            "a_n":GREEN_SCREEN,
            "b_n":BLUE_D,
            "\\pi":RED_D,
            "\\theta":PURPLE,
        }

    }
    def construct(self):

        tex_mob = VGroup(
            self.formula_a1.set_color_by_tex_to_color_map(self.t2c),
            self.formula_a2.set_color_by_tex_to_color_map(self.t2c),
            self.formula_a3.set_color_by_tex_to_color_map(self.t2c),
            self.formula_b3.set_color_by_tex_to_color_map(self.t2c),
            self.formula_b2.set_color_by_tex_to_color_map(self.t2c),
            self.formula_b1.set_color_by_tex_to_color_map(self.t2c),
        )
        tex_mob[1:5].arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.3
        )
        # 字幕设置
        captions_mob = VGroup(
            *[Text(cap,font="方正黑体简体").scale(0.4)\
                                          .to_edge(DOWN) for cap in self.captions
            ]
        )
        # 公式设置
        formula_mob = VGroup(
            *[
                TexMobject(formula,color=YELLOW_C).scale(0.8)\
                               .shift(2*DOWN) for formula in self.formulas
            ]
        )
        formula_mob[2].shift(2*UP)
        formula_mob[3].to_corner(UL)

        # 注释语句设置
        notes_mob = VGroup(
            *[TextMobject(note).scale(0.8) for note in self.notes]
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.4
        )

        # 边框
        surroud_recs = VGroup(
            *[SurroundingRectangle(mob,buff=1) for mob in self.circles]
        ).shift(UP)
        # 折线箭头
        broken_line_mob = VGroup(
            VGroup(
                Line(np.array([-3,-1.6,0]),np.array([-3,-2,0])),
                Line(np.array([-3.021,-2,0]),np.array([-1.4,-2,0]))
            ),
            VGroup(
                Line(np.array([3, -1.6, 0]), np.array([3, -2, 0])),
                Line(np.array([3.021, -2, 0]), np.array([1.4, -2, 0]))
            ),
        )
        broken_line_mob[0][1].add_tip()
        broken_line_mob[1][1].add_tip()

        self.wait()
        self.play(ShowCreation(surroud_recs))
        self.wait(0.5)
        self.play(
            surroud_recs[0].shift,3*LEFT,
            surroud_recs[1].shift,3*RIGHT
        )
        # 对title的位置设置
        title_pos_data = [
            (0,surroud_recs[0],DOWN,0.2),
            (1, surroud_recs[1], DOWN, 0.2),
            (2, broken_line_mob[0][0].get_end(), LEFT, 0.2),
            (3, broken_line_mob[1][0].get_end(), RIGHT, 0.2),
        ]
        for i,tar,dir,buff in title_pos_data :
            self.titles[i].next_to(tar,direction=dir,buff=buff)
        self.circles[0].shift(3*LEFT+UP)
        self.circles[1].shift(3*RIGHT+UP)
        self.wait(0.1)
        self.play(
            *[GrowFromCenter(c) for c in self.circles]
        )
        self.play(*[FadeInFrom(title,UP) for title in self.titles[:2]])
        self.wait(1)
        for i in range(len(self.inscribed_regular_polygon)):
            if i in [0,1,8,9,15,16,17]:
                self.play(Transform(self.empty_mobjects[3],captions_mob[self.j]))
                self.j += 1
            self.play(
                Transform(self.empty_mobjects[0], self.inscribed_regular_polygon[i],run_time=1.3),
                Transform(self.empty_mobjects[1], self.circumscribed_regular_polygon[i], run_time=1.3),
                Transform(self.empty_mobjects[2], self.num_edge[i], run_time=1.3),
            )
            self.wait(0.01)
        self.play(Write(formula_mob[0]))
        self.wait(1)
        self.add(broken_line_mob)
        self.wait(1)
        self.play(*[ShowCreationThenFadeOut(title) for title in self.titles[2:4]])
        self.wait(1)
        self.play(ReplacementTransform(formula_mob[0], formula_mob[1]))
        self.wait(1)
        self.play(
            FadeOut(
                Group(*self.mobjects[:10])
            ),
            formula_mob[1].shift,2*UP
        )
        self.wait(0.5)
        self.play(ReplacementTransform(formula_mob[1],formula_mob[2]))
        notes_mob.next_to(formula_mob[1],direction=DOWN,buff=0.4)
        self.wait(1)
        self.play(*[ShowCreationThenFadeOut(note,run_time=3) for note in notes_mob[:2]])
        self.wait(1)
        self.play(
            formula_mob[2].to_corner,UL
        )
        self.wait(1)
        l1, l2 = self.get_geo()
        # 调整一下推导过程公式的位置
        for theta in [self.theta1,self.theta2]:
            theta.shift(LEFT)
        for i,tex in enumerate(tex_mob):
            if i == 0 or i == 1:
                tex.next_to(formula_mob[2],direction=DOWN,aligned_edge=LEFT,buff=0.3)
            elif i != 5:
                tex.next_to(tex_mob[i-1],direction=DOWN,aligned_edge=LEFT,buff=0.3)
            else:
                tex.next_to(tex_mob[3], direction=DOWN, aligned_edge=LEFT, buff=0.3)
        # tex_mob[1:5].next_to(formula_mob[2],direction=DOWN,aligned_edge=LEFT,buff=0.3)
        for formula,l in zip([self.formula_b1[0],self.formula_a1[0]],[l1,l2]):
            self.play(ReplacementTransform(l.copy(),formula))
        self.wait(1)
        self.play(
            *[
                Write(formula) for formula in [self.formula_a1[1:], self.formula_b1[1:]]
            ]
        )
        self.wait(1)
        self.play(
            ReplacementTransform(self.formula_a1,self.formula_a2)
        )
        self.play(
            ReplacementTransform(self.formula_b1, self.formula_b2)
        )
        self.wait(1)
        self.play(Write(self.theta1))
        self.wait(1)
        self.play(ReplacementTransform(self.theta1,self.theta2))
        self.wait(1)
        self.play(
            Write(self.formula_a3[:5]),
            Write(self.formula_b3[:5]),
        )
        self.wait(1)
        self.play(
            ReplacementTransform(self.theta2.copy(),self.formula_a3[5:]),
            ReplacementTransform(self.theta2.copy(), self.formula_b3[5:]),
        )
        self.wait(1)
        self.play(
            *[
                ShowCreationThenDestructionAround(mob) for mob in [self.formula_a3,self.formula_b3,formula_mob[2]]
            ]
        )
        self.wait(1)
        self.play(
            ReplacementTransform(formula_mob[2],formula_mob[3]),
        )
        self.wait(1)
        self.play(
            FadeOut(self.geomertry),
            FadeOut(tex_mob),
            FadeOut(self.theta2),
            formula_mob[3].move_to,ORIGIN,
            formula_mob[3].to_edge,UP

        )
        for n in self.n:
            n.next_to(formula_mob[3],direction=DOWN,buff=1)
        self.wait(1)
        self.play(
            Write(self.n[0]),
            Write(self.pi[0])
        )
        self.wait(1)
        for n,pi in zip(self.n[1:],self.pi[1:]):
            self.play(
                Transform(self.n[0],n),
                Transform(self.pi[0],pi),
                # rate_func=2*t
            )
            self.wait(0.01)
        self.wait()
        self.play(Write(captions_mob[7]))
        self.wait()
        self.play(
            Transform(captions_mob[7],captions_mob[8])
        )
        self.wait()
        self.play(
            Transform(captions_mob[7],captions_mob[9])
        )
        self.wait()


    def get_geo(self):
        ins_reg_polygon = RegularPolygon(n=6, radius=2, start_angle=90 * DEGREES)
        cir_reg_polygon = RegularPolygon(n=6, radius=2, start_angle=90 * DEGREES, inscribed=False)
        circle = Circle(radius=2)
        geo_mob = VGroup(circle, ins_reg_polygon, cir_reg_polygon)
        dots_data = [
            ('o', ORIGIN),
            ('c1', ins_reg_polygon.get_vertices()[-1]),
            ('c2', ins_reg_polygon.get_vertices()[-2]),
            ('c3', np.array([ins_reg_polygon.get_vertices()[-2][0], 0, 0])),
            ('d1', cir_reg_polygon.get_vertices()[-1]),
            ('d2', cir_reg_polygon.get_vertices()[-2]),
            ('d3', 2 * RIGHT),
        ]
        dots = {}
        dots_mob = VGroup()
        for name, tar in dots_data:
            d = Dot(radius=0.05).move_to(tar)
            dots[name] = d
            dots_mob.add(d)
        lines_data = [
            ('od1', dots['o'], dots['d1']),
            ('od2', dots['o'], dots['d2']),
            ('od3', dots['o'], dots['d3']),
            ('d1d3', dots['d1'], dots['d3']),
            ('c1c3', dots['c1'], dots['c3']),
        ]
        lines = {}
        lines_mob = VGroup()
        for name, d1, d2 in lines_data:
            l = Line(d1, d2)
            lines[name] = l
            lines_mob.add(l)

        angle_d1_o_d2 = Angle(dots['d1'].get_center(), dots['o'].get_center(), dots['d2'].get_center(), color=RED,
                              radius=0.5, stroke_width=4)
        angle_d1_o_d3 = Angle(dots['d1'].get_center(), dots['o'].get_center(), dots['d3'].get_center(), color=PINK,
                              radius=1, stroke_width=4)
        angle_o_c3_c1 = Rectangle(height=0.25, width=0.25, fill_color=YELLOW, fill_opacity=0.5, stroke_opacity=0) \
            .move_to(dots['c3'].get_center()) \
            .shift(0.125 * LEFT) \
            .shift(0.125 * UP)
        angle1 = TexMobject("\\theta").scale(0.5).move_to(0.6 * RIGHT + 0.2 * DOWN)
        angle2 = TexMobject("\\frac{\\theta}{2}").scale(0.5).move_to(1.2 * RIGHT + 0.3 * UP)
        angle = VGroup(angle_d1_o_d2, angle_d1_o_d3, angle_o_c3_c1, angle1, angle2)
        tex = [
            "O",  # 0
            "D_1",  # 1
            "D_2",  # 2
            "D_3",  # 3
            "C_1",  # 4
            "C_2",  # 5
            "C_3"  # 6
        ]
        tex_mob = VGroup(
            *[TexMobject(t).scale(0.5) for t in tex]
        )
        tex_data = [
            (0, dots['o'], LEFT, 0.2),
            (1, dots['d1'], UR, 0.1),
            (2, dots['d2'], DR, 0.1),
            (3, dots['d3'], RIGHT, 0.1),
            (4, dots['c1'], LEFT, 0.2),
            (5, dots['c2'], LEFT, 0.2),
            (6, dots['c3'], DL, 0.2),
        ]
        for i, d, dir, buff in tex_data:
            tex_mob[i].next_to(d, direction=dir, buff=buff)

        self.wait(1)
        # for g in geo_mob:
        #     self.play(ShowCreation(g))
        # self.wait(0.1)
        # self.play(*[ShowCreation(d) for d in dots_mob])
        # self.wait(0.1)
        # self.play(
        #     *[Write(tex) for tex in tex_mob]
        # )
        # self.wait(0.1)
        # self.play(
        #     *[ShowCreation(l) for l in lines_mob]
        # )
        # self.play(
        #     *[ShowCreation(a) for a in angle]
        # )
        # self.wait(0.1)

        geomertry = VGroup(geo_mob, dots_mob, lines_mob, tex_mob, angle)
        self.play(FadeIn(geomertry))
        self.wait(1)
        self.play(
            geomertry.to_corner, UR,
            run_time=1
        )
        self.geomertry = geomertry
        return geomertry[2][3:5]




class Demo(Scene):
    def construct(self):
        tex1 = TexMobject("a+b=c").shift(UP)
        tex2 = TexMobject("a+b=d").shift(DOWN)
        self.add(tex1,tex2)
        self.wait()
        fade_mobject = [mobject for mobject in self.mobjects if mobject is not tex1]
        self.play(
            FadeOut(
                Group(*fade_mobject)
            ),
            tex1.to_corner,UL
        )
        self.wait()

    def get_geomertry(self):
        ins_reg_polygon = RegularPolygon(n=6,radius=2,start_angle=90*DEGREES)
        cir_reg_polygon = RegularPolygon(n=6,radius=2,start_angle=90*DEGREES,inscribed=False)
        circle=Circle(radius=2)
        geo_mob = VGroup(circle,ins_reg_polygon,cir_reg_polygon)
        dots_data = [
            ('o',ORIGIN),
            ('c1', ins_reg_polygon.get_vertices()[-1]),
            ('c2', ins_reg_polygon.get_vertices()[-2]),
            ('c3', np.array([ins_reg_polygon.get_vertices()[-2][0],0,0])),
            ('d1', cir_reg_polygon.get_vertices()[-1]),
            ('d2', cir_reg_polygon.get_vertices()[-2]),
            ('d3', 2*RIGHT),
        ]
        dots = {}
        dots_mob = VGroup()
        for name,tar in dots_data:
            d = Dot(radius=0.05).move_to(tar)
            dots[name] = d
            dots_mob.add(d)
        lines_data = [
            ('od1',dots['o'],dots['d1']),
            ('od2', dots['o'], dots['d2']),
            ('od3', dots['o'], dots['d3']),
            ('d1d3', dots['d1'], dots['d3']),
            ('c1c3', dots['c1'], dots['c3']),
        ]
        lines = {}
        lines_mob = VGroup()
        for name,d1,d2 in lines_data:
            l = Line(d1,d2)
            lines[name] = l
            lines_mob.add(l)


        angle_d1_o_d2 = Angle(dots['d1'].get_center(),dots['o'].get_center(),dots['d2'].get_center(),color=RED,radius=0.5,stroke_width=4)
        angle_d1_o_d3 = Angle(dots['d1'].get_center(),dots['o'].get_center(),dots['d3'].get_center(),color=PINK,radius=1,stroke_width=4)
        angle_o_c3_c1 = Rectangle(height=0.25, width=0.25, fill_color=YELLOW, fill_opacity=0.5, stroke_opacity=0) \
                        .move_to(dots['c3'].get_center()) \
                        .shift(0.125 * LEFT) \
                        .shift(0.125 * UP)
        angle1 = TexMobject("\\theta").scale(0.5).move_to(0.6*RIGHT+0.2*DOWN)
        angle2 = TexMobject("\\frac{\\theta}{2}").scale(0.5).move_to(1.2*RIGHT+0.3*UP)
        angle = VGroup(angle_d1_o_d2,angle_d1_o_d3,angle_o_c3_c1,angle1,angle2)
        tex = [
            "O",        # 0
            "D_1",      # 1
            "D_2",      # 2
            "D_3",      # 3
            "C_1",      # 4
            "C_2",      # 5
            "C_3"       # 6
        ]
        tex_mob = VGroup(
            *[TexMobject(t).scale(0.5) for t in tex]
        )
        tex_data = [
            (0,dots['o'],LEFT,0.2),
            (1, dots['d1'], UR, 0.1),
            (2, dots['d2'], DR, 0.1),
            (3, dots['d3'], RIGHT, 0.1),
            (4, dots['c1'], LEFT, 0.2),
            (5, dots['c2'], LEFT, 0.2),
            (6, dots['c3'], DL, 0.2),
        ]
        for i,d,dir,buff in tex_data:
            tex_mob[i].next_to(d,direction=dir,buff=buff)

        self.wait()
        for g in geo_mob:
            self.play(ShowCreation(g))
        self.wait(1)
        self.play(*[ShowCreation(d) for d in dots_mob])
        self.wait(1)
        self.play(
            *[Write(tex) for tex in tex_mob]
        )
        self.wait(1)
        self.play(
            *[ShowCreation(l) for l in lines_mob]
        )
        self.play(
            *[ShowCreation(a) for a in angle]
        )
        self.wait()
        geomertry = VGroup(geo_mob,dots_mob,lines_mob,tex_mob,angle)
        self.play(
            geomertry.to_corner,UR,
            run_time=2
        )
        return geomertry[2][3:5]
        # return geomertry

class Demo2(Scene):
    CONFIG = {
        "t2c":{
            "\\pi":BLUE_D,
            "a_n":YELLOW,
            "b_n":LIGHT_BROWN,
            "\\Leftarrow":RED,
            "b_{96}":LIGHT_BROWN
        },
    }
    def construct(self):
        tex = TexMobject(
            "{OA",
            "\\over",
            "AG}",
            "=",
            "{OF",
            "+",
            "OA",
            "\\over",
            "AF}",
            "=",
            "{OF",
            "\\over",
            "AF}",
            "+",
            "{OA",
            "\\over",
            "AF}",
            ">",
            "\\frac{2334\\frac{1}{4}}{153}+\\frac{2339\\frac{1}{4}}{153}=\\frac{4673\\frac{1}{2}}{153}",
        )
        self.add(tex)
        self.debugteX(tex)
    def debugteX(self,texm):
        for i,j in zip(range(100),texm):
            tex_id = TextMobject(str(i)).scale(0.3).set_color(PURPLE)
            tex_id.move_to(j)
            self.add(tex_id)

class Scene3(MovingCameraScene):
    CONFIG = {
        "t2c":{
            "\\pi": BLUE_D,
            "a_n": YELLOW_C,
            "b_n": RED_C,
            "b_{96}":RED_C,
            "\\Leftarrow":ORANGE,
            "\\Rightarrow":ORANGE
        },
        "ft2c":{
            "OA":GREEN_SCREEN,
            "OC":ORANGE,
            "OD":ORANGE,
            "OE":ORANGE,
            "OF": ORANGE,
            "OG": ORANGE,
            "AC":LIGHT_PINK,
            "AD": BLUE_D,
            "AE": BLUE_D,
            "AF": BLUE_D,
            "AG": BLUE_D,
            "CD":RED_E,
            "DE":RED_E,
            "EF":RED_E,
            "FG":RED_E,
        },
        "title":[
            "外切正多边形",   # 0
            "内接正多边形",   # 1
        ],
        "table_tex1":[
            "\\angle AOC",
            "\\angle AOD",
            "\\angle AOE",
            "\\angle AOF",
            "\\angle AOG",
        ],
        "table_tex2":[
            "30^\\circ",
            "15^\\circ",
            "7.5^\\circ",
            "3.75^\\circ",
            "1.875^\\circ",
        ],
        "table_tex3":[
            "AC",
            "AD",
            "AE",
            "AF",
            "AG",
        ],
        "table_tex4":[
            "\\frac{1}{2}b_6",
            "\\frac{1}{2}b_{12}",
            "\\frac{1}{2}b_{24}",
            "\\frac{1}{2}b_{48}",
            "\\frac{1}{2}b_{96}",
        ],
        "table_tex5":[
            "n",
            "6",
            "12",
            "24",
            "48",
            "96",
        ],
        "table_tex6":[
            "目标式子",
            "${r\\over \\frac{1}{2}b_6}$",
            "${r\\over \\frac{1}{2}b_{12}}$",
            "${r\\over \\frac{1}{2}b_{24}}$",
            "${r\\over \\frac{1}{2}b_{48}}$",
            "${r\\over \\frac{1}{2}b_{96}}$",
        ],
        "talbe_tex6_1":[
            "目标式子",
            "${OA\\over AC}$",
            "${OA\\over AD}$",
            "${OA\\over AE}$",
            "${OA\\over AF}$",
            "${OA\\over AG}$",
        ],
        "n":[TexMobject("n="+str(n)).scale(0.7) for n in [6,12,24,48,96]],

    }
    def construct(self):
        table_tex1 = VGroup(
            *[
                TexMobject(t).scale(0.6) for t in self.table_tex1
            ]
        ).arrange(
            RIGHT,
            aligned_edge=DOWN,
            buff=0.5
        )
        table_tex2 = VGroup(
            *[
                TexMobject(t).scale(0.6) for t in self.table_tex2
            ]
        )
        table_tex3 = VGroup(
            *[
                TexMobject(t).scale(0.6) for t in self.table_tex3
            ]
        )
        table_tex4 = VGroup(
            *[
                TexMobject(t).scale(0.6) for t in self.table_tex4
            ]
        )
        table_tex5 = VGroup(
            *[
                TexMobject(t).scale(0.6) for t in self.table_tex5
            ]
        ).arrange(
            RIGHT,
            aligned_edge=DOWN,
            buff=0.5
        )
        table_tex6 = VGroup(
            *[
                TextMobject(t).scale(0.9) for t in self.table_tex6
            ]
        )
        table_tex6_1 = VGroup(
            *[
                TextMobject(t).scale(0.9) for t in self.talbe_tex6_1
            ]
        )
        table_tex5.move_to(table_tex1, aligned_edge=RIGHT)
        for t1,t2,t3,t4,t5,t6,t6_1 in zip(table_tex1,table_tex2,table_tex3,table_tex4,table_tex5[1:],table_tex6[1:],table_tex6_1[1:]):
            t2.next_to(t1,direction=DOWN,buff=0.5)
            t3.next_to(t1,direction=DOWN,buff=1+t2.get_height())
            t4.next_to(t1,direction=DOWN,buff=1.5+t2.get_height()+t3.get_height())
            t5.move_to(t1)
            t6.move_to(t2)
            t6_1.move_to(t6)
        table_tex5[0].next_to(table_tex5[1],direction=LEFT,buff=1)
        table_tex6[0].next_to(table_tex6[1],direction=LEFT,buff=0.5)
        table_tex6_1[0].next_to(table_tex6_1[1],direction=LEFT,buff=0.5)

        tex = TexMobject(
            "{",            # 0
            "2",            # 1
            "r",            # 2
            "\\over",       # 3
            "a_n",          # 4
            "}",            # 5
            "\\Rightarrow",  # 6
            "{",            # 7
            "n",            # 8
            "a_n",          # 9
            "\\over",       # 10
            "2",            # 11
            "r",            # 12
            "}",            # 13
            "<",            # 14
            "\\pi",         # 15
            "<",            # 16
            "{",            # 17
            "n",            # 18
            "b_n",          # 19
            "\\over",       # 20
            "2",            # 21
            "r",            # 22
            "}",            # 23
            "\\Leftarrow", # 24
            "{",            # 25
            "r",            # 26
            "\\over",       # 27
            "\\frac{1}{2}", # 28
            "b_n",          # 29
            "}",            # 30
            tex_to_color_map=self.t2c
        ).scale(0.8)
        tex1 = TexMobject(
            "{",            # 0
            "n",            # 1
            "b_n",          # 2
            "\\over",       # 3
            "2",            # 4
            "r",            # 5
            "}",            # 6
            "\\Leftarrow",  # 7
            "{",            # 8
            "b_n",          # 9
            "\\over",       # 10
            "2",            # 11
            "r",            # 12
            "}",            # 13
            "\\Leftarrow",  # 14
            "{",            # 15
            "2",            # 16
            "r",            # 17
            "\\over",       # 18
            "b_n",          # 19
            "}",            # 20
            "\\Leftarrow",  # 21
            "{",            # 22
            "r",            # 23
            "\\over",       # 24
            "\\frac{1}{2}", # 25
            "b_n",          # 26
            "}",            # 27
            tex_to_color_map=self.t2c
        ).scale(0.8)
        tex1.next_to(tex,direction=DOWN,buff=0.4)
        tex2 = TexMobject(
            "{",
            "n",
            "a_n",
            "\\over",
            "2",
            "r",
            "}",
            "\\Leftarrow",
            "{",
            "a_n",
            "\\over",
            "2",
            "r",
            "}",
            "\\Leftarrow",
            "{",
            "2",
            "r",
            "\\over",
            "a_n",
            "}",
            # "\\Leftarrow",
            # "{",
            # "r",
            # "\\over",
            # "\\frac{1}{2}",
            # "a_n",
            # "}",
            tex_to_color_map=self.t2c
        ).scale(0.8)

        tex2.next_to(tex1,direction=DOWN,aligned_edge=LEFT,buff=0.4)
        title = VGroup(
            *[
                Text(mob,font="方正黑体简体").scale(0.3) for mob in self.title
            ]
        )
        f6_1 = TexMobject(
            "{OA",
            "\\over",
            "AC}",
            "=",
            "\\sqrt{3}",
            ">",
            "\\frac{265}{153}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f6_1.set_color_by_tex_to_color_map(self.ft2c)
        f6_2 = TexMobject(
            "{OC",
            "\\over",
            "AC}",
            "=",
            "2",
            "=",
            "\\frac{306}{153}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f6_2.set_color_by_tex_to_color_map(self.ft2c)
        f6 = VGroup(f6_1,f6_2).arrange(
            RIGHT,
            aligned_edge=DOWN,
            buff=1.4
        )
        f12_1 = TexMobject(
            "{OC",
            "\\over",
            "OA}",
            "=",
            "{CD",
            "\\over",
            "AD}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f12_1.set_color_by_tex_to_color_map(self.ft2c)
        f12_2 = TexMobject(
            "{OC",
            "+",
            "OA",
            "\\over",
            "OA}",
            "=",
            "{CD",
            "+",
            "AD",
            "\\over",
            "AD}",
            "=",
            "{AC",
            "\\over",
            "AD}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f12_2.set_color_by_tex_to_color_map(self.ft2c)
        f12_3 = TexMobject(
            "{OA",
            "\\over",
            "AD}",
            "=",
            "{OC",
            "+",
            "OA",
            "\\over",
            "AC}",
            "=",
            "{OC",
            "\\over",
            "AC}",
            "+",
            "{OA",
            "\\over",
            "AC}",
            ">",
            "2+\\frac{265}{153}=\\frac{571}{153}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f12_3.set_color_by_tex_to_color_map(self.ft2c)

        f12_4 = TexMobject(
            "{OA",
            "\\over",
            "AD}",
            ">",
            "\\frac{571}{153}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f12_4.set_color_by_tex_to_color_map(self.ft2c)

        f12_5 = TexMobject(
            "{OD^2",
            "\\over",
            "AD^2}",
            "=",
            "{OA^2",
            "+",
            "AD^2",
            "\\over",
            "AD^2}",
            ">",
            "\\frac{571^2}{153^2}+1=\\frac{349450}{23409}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f12_5.set_color_by_tex_to_color_map(self.ft2c)

        f12_6 = TexMobject(
            "{OD",
            "\\over",
            "AD}",
            ">",
            "\\frac{591\\frac{1}{8}}{153}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f12_6.set_color_by_tex_to_color_map(self.ft2c)
        f12 = VGroup(f12_1,f12_2,f12_3,f12_4,f12_5,f12_6)
        f24_1 = TexMobject(
            "{OD",
            "\\over",
            "OA}",
            "=",
            "{DE",
            "\\over",
            "AE}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f24_1.set_color_by_tex_to_color_map(self.ft2c)
        f24_2 = TexMobject(
            "{OD",
            "+",
            "OA",
            "\\over",
            "OA}",
            "=",
            "{DE",
            "+",
            "AE",
            "\\over",
            "AE}",
            "=",
            "{AD",
            "\\over",
            "AE}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f24_2.set_color_by_tex_to_color_map(self.ft2c)
        f24_3 = TexMobject(
            "{OA",
            "\\over",
            "AE}",
            "=",
            "{OD",
            "+",
            "OA",
            "\\over",
            "AD}",
            "=",
            "{OD",
            "\\over",
            "AD}",
            "+",
            "{OA",
            "\\over",
            "AD}",
            ">",
            "\\frac{591\\frac{1}{8}}{153}+\\frac{571}{153}=\\frac{1162\\frac{1}{8}}{153}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f24_3.set_color_by_tex_to_color_map(self.ft2c)

        f24_4 = TexMobject(
            "{OA",
            "\\over",
            "AE}",
            ">",
            "\\frac{1162\\frac{1}{8}}{153}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f24_4.set_color_by_tex_to_color_map(self.ft2c)

        f24_5 = TexMobject(
            "{OE^2",
            "\\over",
            "AE^2}",
            "=",
            "{OA^2",
            "+",
            "AE^2",
            "\\over",
            "AE^2}",
            ">",
            "(\\frac{1162\\frac{1}{8}}{153})^2+1=\\frac{1373943\\frac{33}{64}}{23409}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f24_5.set_color_by_tex_to_color_map(self.ft2c)

        f24_6 = TexMobject(
            "{OE",
            "\\over",
            "AE}",
            ">",
            "\\frac{1172\\frac{1}{8}}{153}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f24_6.set_color_by_tex_to_color_map(self.ft2c)

        f24 = VGroup(f24_1,f24_2,f24_3,f24_4,f24_5,f24_6)
        f48_1 = TexMobject(
            "{OE",
            "\\over",
            "OA}",
            "=",
            "{EF",
            "\\over",
            "AF}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f48_1.set_color_by_tex_to_color_map(self.ft2c)

        f48_2 = TexMobject(
            "{OE",
            "+",
            "OA",
            "\\over",
            "OA}",
            "=",
            "{EF",
            "+",
            "AF",
            "\\over",
            "AF}",
            "=",
            "{AE",
            "\\over",
            "AF}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f48_2.set_color_by_tex_to_color_map(self.ft2c)

        f48_3 = TexMobject(
            "{OA",
            "\\over",
            "AF}",
            "=",
            "{OE",
            "+",
            "OA",
            "\\over",
            "AE}",
            "=",
            "{OE",
            "\\over",
            "AE}",
            "+",
            "{OA",
            "\\over",
            "AE}",
            ">",
            "\\frac{1172\\frac{1}{8}}{153}+\\frac{1162\\frac{1}{8}}{153}=\\frac{2334\\frac{1}{4}}{153}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f48_3.set_color_by_tex_to_color_map(self.ft2c)

        f48_4 = TexMobject(
            "{OA",
            "\\over",
            "AF}",
            ">",
            "\\frac{2334\\frac{1}{4}}{153}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f48_4.set_color_by_tex_to_color_map(self.ft2c)

        f48_5 = TexMobject(
            "{OF^2",
            "\\over",
            "AF^2}",
            "=",
            "{OA^2",
            "+",
            "AF^2",
            "\\over",
            "AF^2}",
            ">",
            "(\\frac{2334\\frac{1}{4}}{153})^2+1=\\frac{349450}{23409}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f48_5.set_color_by_tex_to_color_map(self.ft2c)

        f48_6 = TexMobject(
            "{OF",
            "\\over",
            "AF}",
            ">",
            "\\frac{2339\\frac{1}{4}}{153}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f48_6.set_color_by_tex_to_color_map(self.ft2c)
        f48 = VGroup(f48_1,f48_2,f48_3,f48_4,f48_5,f48_6)
        f96_1 = TexMobject(
            "{OF",
            "\\over",
            "OA}",
            "=",
            "{FG",
            "\\over",
            "AG}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f96_1.set_color_by_tex_to_color_map(self.ft2c)

        f96_2 = TexMobject(
            "{OF",
            "+",
            "OA",
            "\\over",
            "OA}",
            "=",
            "{FG",
            "+",
            "AG",
            "\\over",
            "AG}",
            "=",
            "{AF",
            "\\over",
            "AG}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f96_2.set_color_by_tex_to_color_map(self.ft2c)

        f96_3 = TexMobject(
            "{OA",
            "\\over",
            "AG}",
            "=",
            "{OF",
            "+",
            "OA",
            "\\over",
            "AF}",
            "=",
            "{OF",
            "\\over",
            "AF}",
            "+",
            "{OA",
            "\\over",
            "AF}",
            ">",
            "\\frac{2334\\frac{1}{4}}{153}+\\frac{2339\\frac{1}{4}}{153}=\\frac{4673\\frac{1}{2}}{153}",
        ).scale(0.5)
        f96_3.set_color_by_tex_to_color_map(self.ft2c)
        f96_4 = TexMobject(
            "{OA",
            "\\over",
            "AG}",
            ">",
            "\\frac{4673\\frac{1}{2}}{153}",
        ).scale(0.5)
        f96_4.set_color_by_tex_to_color_map(self.ft2c)
        f96 = VGroup(f96_1,f96_2,f96_3,f96_4)
        fpi_1 = TexMobject(
            "{r",
            "\\over",
            "\\frac{1}{2}b_{96}}",
            ">",
            "\\frac{4673\\frac{1}{2}}{153}",
            tex_to_color_map=self.t2c
        ).scale(0.8)
        fpi_2 = TexMobject(
            "{2r",
            "\\over",
            "b_{96}}",
            ">",
            "\\frac{4673\\frac{1}{2}}{153}",
            tex_to_color_map=self.t2c
        ).scale(0.8)
        fpi_3 = TexMobject(
            "{2r",
            "\\over",
            "96",
            "b_{96}}",
            ">",
            "\\frac{4673\\frac{1}{2}}{153\\times 96}",
            tex_to_color_map=self.t2c
        ).scale(0.8)
        fpi_4 = TexMobject(
            "{96",
            "b_{96}",
            "\\over",
            "2r}",
            "<",
            "\\frac{14688}{4673\\frac{1}{2}}",
            "<",
            "3+\\frac{667\\frac{1}{2}}{4672\\frac{1}{2}}=3\\frac{1}{7}",
            tex_to_color_map=self.t2c
        ).scale(0.8)
        fpi_5 = TexMobject(
            "\\pi",
            "<",
            "{96",
            "b_{96}",
            "\\over",
            "2r}",
            "<",
            "3\\frac{1}{7}",
            tex_to_color_map=self.t2c
        ).scale(0.8)
        fpi = VGroup(fpi_1,fpi_2,fpi_3,fpi_4,fpi_5).move_to(2*LEFT+DOWN)
        notes = [
            "角平分线定理：",
            "合比定理：",
            "更比定理：",
        ]
        notes_mob = VGroup(
            *[
                Text(mob,font="方正黑体简体").scale(0.3) for mob in notes
            ]
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.5
        )
        out_geo = self.get_out_geo()
        in_geo = self.get_in_geo()
        for cor,geo,tit in zip([UL,UR],[out_geo,in_geo],title):
            self.play(
                FadeIn(geo)
            )
            self.wait(0.01)
            self.play(
                geo.to_corner,cor
            )
            tit.next_to(geo,direction=DOWN,buff=0.3)
            self.play(DrawBorderThenFill(tit))
            self.wait(0.1)
        self.play(GrowFromCenter(tex[7:23]))
        self.wait(0.1)
        self.play(
            *[ShowIncreasingSubsets(mob) for mob in [tex1,tex2]]
        )
        self.wait(0.5)
        self.play(
            *[
                ShowCreationThenFadeAround(mob) for mob in [tex1[22:],tex2[15:]]
            ]
        )
        self.wait(1)
        self.play(
            ReplacementTransform(tex1,tex[:7]),
            ReplacementTransform(tex2, tex[23:])
        )
        self.wait()
        self.play(
            FadeOut(in_geo),
            FadeOut(title[1]),
            ApplyMethod(title[0].move_to,title[1]),
            ApplyMethod(out_geo.to_corner,UR),
            ApplyFunction(lambda mob:mob.to_corner(UL).scale(0.8),tex),
        )
        self.wait()
        self.play(
            *[Write(t) for t in table_tex1]
        )
        self.wait(1)
        for t1, t2 in zip(table_tex1, table_tex2):
            self.play(
                ReplacementTransform(t1.copy(), t2)
            )
        self.wait(1)
        self.play(
            *[Write(t) for t in table_tex3]
        )
        for t3, t4 in zip(table_tex3, table_tex4):
            self.play(
                ReplacementTransform(t3.copy(), t4)
            )
        self.wait()
        self.play(
            FadeOutAndShiftDown(table_tex1),
            FadeOutAndShiftDown(table_tex2),
            FadeInFrom(table_tex5,UP),
            Write(table_tex6[0]),
        )
        self.wait()
        self.play(
            ShowCreationThenFadeAround(tex[25:])
        )
        for t in table_tex6[1:]:
            self.play(ReplacementTransform(tex[25:].copy(),t))
            self.wait(0.1)
        self.wait()
        for i in range(1,6):
            self.play(
                FadeOut(table_tex6[i]),
                ReplacementTransform(table_tex3[i-1].copy(),table_tex6_1[i])
            )
            self.wait(0.1)
        self.wait()
        self.play(
            FadeOut(table_tex5),
            FadeOut(table_tex3),
            FadeOut(table_tex4),
            FadeOut(table_tex6[0]),
            ApplyFunction(
                lambda mob:mob.to_corner(UL)\
                              .shift(1.2*DOWN+0.7*LEFT)\
                              .scale(0.7),
                table_tex6_1
            )
        )
        self.wait()
        for n in self.n:
            n.next_to(table_tex6_1,direction=DOWN,aligned_edge=LEFT,buff=0.3)
        self.play(Write(self.n[0]))
        indic_rec = ShowCreationThenDestructionAround(table_tex6_1[1]).get_rect()
        self.play(
            ShowCreationThenDestructionAround(table_tex6_1[1]),
            ShowCreation(indic_rec)
        )
        self.wait(1)
        # AH OC OD OE OF OG OA AC AD AE AF AG CD DE EF FG
        # 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
        self.play(
            out_geo[1][1].set_color,ORANGE,
            out_geo[1][6].set_color, GREEN_SCREEN,
            out_geo[1][7].set_color, LIGHT_PINK,
            Write(f6_1),
            Write(f6_2),
        )
        self.wait()
        self.play(
            f6[0].next_to,title[0],{"direction":DOWN,"buff":0.4},
            f6[1].next_to,self.n[0],{"direction":DOWN,"buff": 0.4,"aligned_edge":LEFT},
            # out_geo[1][7].set_color, WHITE,
            out_geo[1][8].set_color, BLUE_D,
            out_geo[1][12].set_color, RED_E,
        )
        self.wait()
        notes_mob.next_to(f6[1],direction=DOWN,buff=0.4,aligned_edge=LEFT)
        self.wait()
        for i,fn in enumerate([f12,f24,f48,f96]):
            for note,f in zip(notes_mob,fn[:3]):
                f.next_to(note,direction=RIGHT,buff=0.5)
            fn[3].next_to(notes_mob[2],direction=RIGHT,buff=0.5)
            if i < 3:
                fn[4].next_to(fn[3],direction=DOWN,aligned_edge=LEFT,buff=0.5)
                fn[5].next_to(f12[3],direction=DOWN,aligned_edge=LEFT,buff=0.5)

        self.play(Write(notes_mob))
        # AH OC OD OE OF OG OA AC AD AE AF AG CD DE EF FG
        # 0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
        f = [f12,f24,f48,f96]
        for i,fn in zip(range(4),f):

            self.play(
                indic_rec.move_to,table_tex6_1[i+2],
                Transform(self.n[0],self.n[i+1]),
                Write(fn[0]),
            )
            self.wait()
            for t in fn[1:3]:
                self.play(Write(t))
                self.wait()
            self.play(
                ShowCreationThenFadeAround(fn[1][:5]),
                ShowCreationThenFadeAround(fn[1][12:]),
                ShowCreationThenFadeAround(fn[2][:9]),
            )
            self.play(
                ReplacementTransform(fn[2], fn[3])
            )
            self.wait()
            if i != 3:
                self.play(Write(fn[4]))
                self.wait()
                self.play(ReplacementTransform(fn[4],fn[5]))
                self.wait()
                if i == 0:
                    self.play(
                        fn[3].next_to,f6[0],{"direction":DOWN,"aligned_edge":LEFT,"buff":0.4},
                        fn[5].next_to,f6[1],{"direction":RIGHT,"buff":0.4},
                        FadeOut(fn[0]),
                        FadeOut(fn[1]),
                    )
                else:
                    self.play(
                        fn[3].next_to, f[i-1][3], {"direction": DOWN, "aligned_edge": LEFT, "buff": 0.4},
                        fn[5].next_to, f[i-1][5], {"direction": RIGHT, "buff": 0.4},
                        FadeOut(fn[0]),
                        FadeOut(fn[1]),
                    )
        self.wait()
        self.play(
            *[
                FadeOut(t) for t in [notes_mob,f96[:2],f6[1],f12[5],f24[5],f48[5]]
            ]
        )
        self.wait()
        self.play(
            ShowCreationThenFadeAround(tex[25:]),
            ShowCreationThenFadeAround(f96[3]),
        )
        self.wait(1)
        for pi in fpi:
            self.play(
                Transform(f96[3],pi)
            )
            self.wait()
    def get_out_geo(self):
        sector = AnnularSector(
            fill_opacity=0,
            stroke_width=4,
            inner_radius=0,
            angle=TAU/2,
        )
        # H O A B C D E F G
        # 0 1 2 3 4 5 6 7 8
        points = self.get_out_points()
        self.out_points = points
        # 创建线段
        # AH OC OD OE OF OG OA AC AD AE AF AG CD DE EF FG
        # 20 14 15 16 17 18 12 24 25 26 27 28 45 56 67 78
        lines = VGroup()
        for start,end in [(2,0),(1,4),(1,5),(1,6),(1,7),(1,8),(1,2),(2,4),(2,5),(2,6),(2,7),(2,8),(4,5),(5,6),(6,7),(7,8)]:
            l = Line(np.array(points[start]),np.array(points[end]),stroke_width=4)
            lines.add(l)
        # 创建标注
        notes = ["O","A","B","C","D","E","F","G"]
        #        /   /   /   /   /   /   /   /
        #       0   1   2   3   4   5   6   7
        notes_mob = VGroup(
            *[
                TexMobject(note).scale(0.6) for note in notes
            ]
        )
        # 顺序：O A B C D E F G
        #      / / / / / / / /
        #     1 2 3 4 5 6 7 8
        directions = [
            UP,
            DOWN,
            DOWN,
            LEFT,
            LEFT,
            LEFT,
            LEFT,
            DL,
        ]
        buffs = [0.1,0.2,0.2,0.1,0.1,0.1,0.1,0.3]
        for note,i,direction,buff in zip(notes_mob,range(8),directions,buffs):
            note.next_to(points[i+1],direction=direction,buff=buff)
        arrow = Arrow(
            notes_mob[7],
            points[8],
            stroke_width=3,
        )
        out_geo = VGroup(sector,lines,notes_mob,arrow)
        return out_geo
        # self.add(sector,lines,notes_mob,arrow)
    def get_out_points(self):
        # 顺序：H O A B C D E F G
        angle = 45*DEGREES
        r = 2
        coords = [(-2,2.2,0),(0,0,0),(-2,0,0),(2,0,0)]
        for _ in range(5):
            coord = (-2,r*np.tan(angle),0)
            coords.append(coord)
            angle /= 2
        return coords
    def get_in_geo(self):
        sector = AnnularSector(
            fill_opacity=0,
            stroke_width=4,
            inner_radius=0,
            angle=TAU / 2,
        )
        # O A B C D E F G
        # 0 1 2 3 4 5 6 7
        points = self.get_in_points()
        # 创建线段
        # AC BC AD BD AE AF AG
        # 13 23 14 24 15 16 17
        lines = VGroup()
        for start,end in [(1,3),(2,3),(1,4),(2,4),(1,5),(1,6),(1,7)]:
            l = Line(np.array(points[start]),np.array(points[end]),stroke_width=2)
            lines.add(l)
        # 创建标注
        notes = ["O","A","B","C","D","E","F","G"]
        #        /   /   /   /   /   /   /   /
        #       0   1   2   3   4   5   6   7
        notes_mob = VGroup(
            *[
                TexMobject(note).scale(0.6) for note in notes
            ]
        )
        directions = [DOWN,DOWN,DOWN,UP,UR,UR,UR,RIGHT]
        buffs = [0.1,0.1,0.1,0.1,0.1,0.1,0.05,0.2]
        for note,i,dir,buf in zip(notes_mob,range(8),directions,buffs):
            note.next_to(points[i],direction=dir,buff=buf)
        # self.add(sector,lines,notes_mob)

        in_geo = VGroup(sector,lines,notes_mob)
        return in_geo
    def get_in_points(self):
        # 顺序： O A B C D E F G
        r = 2
        angle = 60*DEGREES
        coords = [(0,0,0),(-2,0,0),(2,0,0)]
        for _ in range(5):
            x = r*np.cos(angle)
            y = r*np.sin(angle)
            coords.append((x,y,0))
            angle /= 2

        return coords



class Scene4(Scene):
    CONFIG = {
        "t2c": {
            "\\pi": BLUE_D,
            "a_n": YELLOW_C,
            "b_n": RED_C,
            "b_{96}": RED_C,
            "\\Leftarrow": ORANGE,
            "\\Rightarrow": ORANGE
        },
        "table_tex1": [
            "\\angle BAC",
            "\\angle BAD",
            "\\angle BAE",
            "\\angle BAF",
            "\\angle BAG",
        ],
        "table_tex2": [
            "30^\\circ",
            "15^\\circ",
            "7.5^\\circ",
            "3.75^\\circ",
            "1.875^\\circ",
        ],
        "table_tex3": [
            "BC",
            "BD",
            "BE",
            "BF",
            "BG",
        ],
        "table_tex4": [
            "a_6",
            "a_{12}",
            "a_{24}",
            "a_{48}",
            "a_{96}",
        ],
        "table_tex5": [
            "n",
            "6",
            "12",
            "24",
            "48",
            "96",
        ],
        "table_tex6": [
            "目标式子",
            "${2r\\over a_6}$",
            "${2r\\over a_{12}}$",
            "${2r\\over a_{24}}$",
            "${2r\\over a_{48}}$",
            "${2r\\over a_{96}}$",
        ],
        "talbe_tex6_1": [
            "目标式子",
            "${AB\\over BC}$",
            "${AB\\over BD}$",
            "${AB\\over BE}$",
            "${AB\\over BF}$",
            "${AB\\over BG}$",
        ],
        "n": [TexMobject("n=" + str(n)).scale(0.7) for n in [6, 12, 24, 48, 96]],
        "ft2c": {
            "AB":BLUE_D,
            "BH":BLUE_D,
            "AH":BLUE_D,
            "BD":YELLOW_C,
            "HD":YELLOW_C,
            "HC":YELLOW_C,
            "AC":GREEN_SCREEN,
            "AD":GREEN_SCREEN,
            "AE":GREEN_SCREEN,
            "AF":GREEN_SCREEN,
            "AG":GREEN_SCREEN,
            "BC":YELLOW_C,
            "BE":YELLOW_C,
            "BF":YELLOW_C,
            "BG":YELLOW_C
        },
    }
    def construct(self):
        table_tex1 = VGroup(
            *[
                TexMobject(t).scale(0.6) for t in self.table_tex1
            ]
        ).arrange(
            RIGHT,
            aligned_edge=DOWN,
            buff=0.5
        )
        table_tex2 = VGroup(
            *[
                TexMobject(t).scale(0.6) for t in self.table_tex2
            ]
        )
        table_tex3 = VGroup(
            *[
                TexMobject(t).scale(0.6) for t in self.table_tex3
            ]
        )
        table_tex4 = VGroup(
            *[
                TexMobject(t).scale(0.8) for t in self.table_tex4
            ]
        )
        table_tex5 = VGroup(
            *[
                TexMobject(t).scale(0.6) for t in self.table_tex5
            ]
        ).arrange(
            RIGHT,
            aligned_edge=DOWN,
            buff=0.5
        )
        table_tex6 = VGroup(
            *[
                TextMobject(t).scale(0.9) for t in self.table_tex6
            ]
        )
        table_tex6_1 = VGroup(
            *[
                TextMobject(t).scale(0.9) for t in self.talbe_tex6_1
            ]
        )
        table_tex5.move_to(table_tex1, aligned_edge=RIGHT)
        for t1,t2,t3,t4,t5,t6,t6_1 in zip(table_tex1,table_tex2,table_tex3,table_tex4,table_tex5[1:],table_tex6[1:],table_tex6_1[1:]):
            t2.next_to(t1,direction=DOWN,buff=0.5)
            t3.next_to(t1,direction=DOWN,buff=1+t2.get_height())
            t4.next_to(t1,direction=DOWN,buff=1.5+t2.get_height()+t3.get_height())
            t5.move_to(t1)
            t6.move_to(t2)
            t6_1.move_to(t6)
        table_tex5[0].next_to(table_tex5[1],direction=LEFT,buff=1)
        table_tex6[0].next_to(table_tex6[1],direction=LEFT,buff=0.5)
        table_tex6_1[0].next_to(table_tex6_1[1],direction=LEFT,buff=0.5)
        in_geo = self.get_in_geo()
        in_geo.to_corner(UR)
        tex = TexMobject(
            "{",  # 0
            "2",  # 1
            "r",  # 2
            "\\over",  # 3
            "a_n",  # 4
            "}",  # 5
            "\\Rightarrow",  # 6
            "{",  # 7
            "n",  # 8
            "a_n",  # 9
            "\\over",  # 10
            "2",  # 11
            "r",  # 12
            "}",  # 13
            "<",  # 14
            "\\pi",  # 15
            "<",  # 16
            "3\\frac{1}{7}",
            # "{",  # 17
            # "n",  # 18
            # "b_n",  # 19
            # "\\over",  # 20
            # "2",  # 21
            # "r",  # 22
            # "}",  # 23
            # "\\Leftarrow",  # 24
            # "{",  # 25
            # "r",  # 26
            # "\\over",  # 27
            # "\\frac{1}{2}",  # 28
            # "b_n",  # 29
            # "}",  # 30
            tex_to_color_map=self.t2c
        ).scale(0.8)
        tex.to_corner(UL)
        f6_1 = TexMobject(
            "{AC",
            "\\over",
            "BC}",
            "=",
            "\\sqrt{3}",
            "<",
            "\\frac{1351}{780}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f6_1.set_color_by_tex_to_color_map(self.ft2c)
        f6_2 = TexMobject(
            "{AB",
            "\\over",
            "BC}",
            "=",
            "2",
            "=",
            "\\frac{1560}{780}",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f6_2.set_color_by_tex_to_color_map(self.ft2c)
        f6 = VGroup(f6_1, f6_2).arrange(
            RIGHT,
            aligned_edge=DOWN,
            buff=1.4
        )
        f12_1 = TexMobject(
           "\\angle",
            "BAD",
            "=",
            "\\angle",
            "HAC",
            "=",
            "\\angle",
            "HBD",
            # tex_to_color_map=self.ft2c
        ).scale(0.5)
        f12_1.set_color_by_tex_to_color_map(self.ft2c)
        f12_2 = TexMobject(
            "\\bigtriangleup",
            "ABD",
            "\\sim",
            "\\bigtriangleup",
            "AHC",
            "\\sim",
            "\\bigtriangleup",
            "BHD",
        ).scale(0.5)
        f12_2.set_color_by_tex_to_color_map(self.ft2c)

        f12_3 = TexMobject(
            "{AD",
            "\\over",
            "BD}",
            "=",
            "{BD",
            "\\over",
            "HD}",
            "=",
            "{AC",
            "\\over",
            "HC}",
            "=",
            "{AB",
            "\\over",
            "BH}",
        ).scale(0.5)
        f12_3.set_color_by_tex_to_color_map(self.ft2c)

        f12_4 = TexMobject(
            "{AD",
            "\\over",
            "BD}",
            "=",
            "{AB",
            "+",
            "AC",
            "\\over",
            "BH",
            "+",
            "HC}",
            "=",
            "{AB",
            "+",
            "AC",
            "\\over",
            "BC}"
        ).scale(0.5)
        f12_4.set_color_by_tex_to_color_map(self.ft2c)

        f12_5 = TexMobject(
            "{AD",
            "\\over",
            "BD}",
            "=",
            "{AB",
            "\\over",
            "BC}",
            "+",
            "{AC",
            "\\over",
            "BC}",
            "<",
            "2+\\frac{1351}{780}=\\frac{2911}{780}"
        ).scale(0.5)
        f12_5.set_color_by_tex_to_color_map(self.ft2c)

        f12_6 = TexMobject(
            "{AD",
            "\\over",
            "BD}",
            "<",
            "\\frac{2911}{780}"
        ).scale(0.5)
        f12_6.set_color_by_tex_to_color_map(self.ft2c)

        f12_7 = TexMobject(
            "{AB^2",
            "\\over",
            "BD^2}",
            "=",
            "{AD^2",
            "+",
            "BD^2",
            "\\over",
            "BD^2}",
            "<",
            "\\frac{2911^2}{780^2}+1=\\frac{9082321}{608400}",
        ).scale(0.5)
        f12_7.set_color_by_tex_to_color_map(self.ft2c)

        f12_8 = TexMobject(
            "{AB",
            "\\over",
            "BD}",
            "<",
            "\\frac{3013\\frac{3}{4}}{780}",
        ).scale(0.5)
        f12_8.set_color_by_tex_to_color_map(self.ft2c)

        f12 = VGroup(f12_1,f12_2,f12_3,f12_4,f12_5,f12_6,f12_7,f12_8)
        f24_1 = TexMobject(
            "{AE",
            "\\over",
            "BE}",
            "=",
            "{AB",
            "+",
            "AD",
            "\\over",
            "BD}",
            "<",
            "\\frac{3013\\frac{3}{4}}{780}+\\frac{2911}{780}=\\frac{1823}{240}"
        ).scale(0.5)
        f24_1.set_color_by_tex_to_color_map(self.ft2c)

        f24_2 = TexMobject(
            "{AE",
            "\\over",
            "BE}",
            "<",
            "\\frac{1823}{240}"
        ).scale(0.5)
        f24_2.set_color_by_tex_to_color_map(self.ft2c)

        f24_3 = TexMobject(
            "{AB^2",
            "\\over",
            "BE^2}",
            "=",
            "{BE^2",
            "+",
            "AE^2",
            "\\over",
            "BE^2}",
            "<",
            "(\\frac{1823}{240})^2+1=\\frac{3380929}{57600}",
        ).scale(0.5)
        f24_3.set_color_by_tex_to_color_map(self.ft2c)

        f24_4 = TexMobject(
            "{AB",
            "\\over",
            "BE}",
            "<",
            "\\frac{1838\\frac{9}{11}}{240}",
        ).scale(0.5)
        f24_4.set_color_by_tex_to_color_map(self.ft2c)

        f24 = VGroup(f24_1,f24_2,f24_3,f24_4)
        f48_1 = TexMobject(
            "{AF",
            "\\over",
            "BF}",
            "=",
            "{AB",
            "+",
            "AE",
            "\\over",
            "BE}",
            "<",
            "\\frac{1838\\frac{9}{11}}{240}+\\frac{1823}{240}=\\frac{3661\\frac{9}{11}}{240}"
        ).scale(0.5)
        f48_1.set_color_by_tex_to_color_map(self.ft2c)

        f48_2 = TexMobject(
            "{AF",
            "\\over",
            "BF}",
            "<",
            "\\frac{3661\\frac{9}{11}}{240}"
        ).scale(0.5)
        f48_2.set_color_by_tex_to_color_map(self.ft2c)

        f48_3 = TexMobject(
            "{AB^2",
            "\\over",
            "BF^2}",
            "=",
            "{BF^2",
            "+",
            "AF^2",
            "\\over",
            "BF^2}",
            "<",
            "(\\frac{3661\\frac{9}{11}}{240})^2+1=\\frac{1018405}{4356}",
        ).scale(0.5)
        f48_3.set_color_by_tex_to_color_map(self.ft2c)

        f48_4 = TexMobject(
            "{AB",
            "\\over",
            "BF}",
            "<",
            "\\frac{1009\\frac{1}{6}}{66}",
        ).scale(0.5)
        f48_4.set_color_by_tex_to_color_map(self.ft2c)

        f48 = VGroup(f48_1,f48_2,f48_3,f48_4)
        f96_1 = TexMobject(
            "{AG",
            "\\over",
            "BG}",
            "=",
            "{AB",
            "+",
            "AF",
            "\\over",
            "BF}",
            "<",
            "\\frac{1009\\frac{1}{6}}{66}+\\frac{3661\\frac{9}{11}}{240}=\\frac{2016\\frac{1}{6}}{66}"
        ).scale(0.5)
        f96_1.set_color_by_tex_to_color_map(self.ft2c)

        f96_2 = TexMobject(
            "{AG",
            "\\over",
            "BG}",
            "<",
            "\\frac{2016\\frac{1}{6}}{66}"
        ).scale(0.5)
        f96_2.set_color_by_tex_to_color_map(self.ft2c)

        f96_3 = TexMobject(
            "{AB^2",
            "\\over",
            "BG^2}",
            "=",
            "{BG^2",
            "+",
            "AG^2",
            "\\over",
            "BG^2}",
            "<",
            "(\\frac{2016\\frac{1}{6}}{66})^2+1",
        ).scale(0.5)
        f96_3.set_color_by_tex_to_color_map(self.ft2c)

        f96_4 = TexMobject(
            "{AB",
            "\\over",
            "BG}",
            "<",
            "\\frac{2017\\frac{1}{4}}{66}",
        ).scale(0.5)
        f96_4.set_color_by_tex_to_color_map(self.ft2c)

        f96 = VGroup(f96_1,f96_2,f96_3,f96_4)
        fpi_1 = TexMobject(
            "{2",
            "r",
            "\\over",
            "a_{96}}",
            "<",
            "\\frac{2017\\frac{1}{4}}{66}",
            tex_to_color_map=self.t2c
        ).scale(0.8)
        fpi_2 = TexMobject(
            "{2",
            "r",
            "\\over",
            "96",
            "a_{96}}",
            "<",
            "\\frac{2017\\frac{1}{4}}{66\\times 96}",
            tex_to_color_map=self.t2c
        ).scale(0.8)
        fpi_3 = TexMobject(
            "\\frac{66\\times 96}{2017\\frac{1}{4}}",
            "<"
            "{96",
            "a_{96}",
            "\\over",
            "2",
            "r}",
            tex_to_color_map=self.t2c
        ).scale(0.8)
        fpi_4 = TexMobject(
            "3\\frac{10}{71}"
            "<",
            "\\frac{6336}{2017\\frac{1}{4}}",
            "<",
            "{96",
            "a_{96}",
            "\\over",
            "2",
            "r}",
            tex_to_color_map=self.t2c
        ).scale(0.8)
        fpi_5 = TexMobject(
            "3\\frac{10}{71}",
            "<",
            "{96",
            "a_{96}",
            "\\over",
            "2",
            "r}",
            "<",
            "\\pi",
            tex_to_color_map=self.t2c
        ).scale(0.8)
        fpi_6 = TexMobject(
            "3\\frac{10}{71}",
            "<",
            "\\pi",
            "<",
            "3\\frac{1}{7}",
            tex_to_color_map=self.t2c
        ).scale(0.8)
        fpi_7 = TexMobject(
            "3.1408",
            "<",
            "\\pi",
            "<",
            "3.1429",
            tex_to_color_map=self.t2c
        ).scale(0.8)
        fpi = VGroup(fpi_1,fpi_2,fpi_3,fpi_4,fpi_5,fpi_6,fpi_7)
        fpi.shift(DOWN)
        # fpi_7.next_to(fpi_6,direction=DOWN,buff=0.5)
        title = Text("内接正多边形",font="方正黑体简体")\
               .scale(0.3)\
               .next_to(in_geo,direction=DOWN,buff=0.3)
        captions = [
            "后面就省略证明三角形相似的过程",
            "直接得出等比性质后的关系",
            "遗憾的是",                 # 2
            "当阿基米德计算到正96边形时",   # 3
            "罗马士兵攻破城墙，残忍地杀害了他", # 4
            "但无疑他对圆周率的研究作出了巨大的贡献"   # 5
        ]
        caption_mob = VGroup(
            *[
                Text(cap,font="方正黑体简体").scale(0.4).to_edge(DOWN) for cap in captions
            ]
        )
        self.add(in_geo,title,tex)
        self.wait()
        self.play(
            *[Write(t) for t in table_tex1]
        )
        self.wait(1)
        for t1, t2 in zip(table_tex1, table_tex2):
            self.play(
                ReplacementTransform(t1.copy(), t2)
            )
        self.wait(1)

        self.play(
            *[Write(t) for t in table_tex3]
        )
        for t3, t4 in zip(table_tex3, table_tex4):
            self.play(
                ReplacementTransform(t3.copy(), t4)
            )
        self.wait()
        self.play(
            FadeOutAndShiftDown(table_tex1),
            FadeOutAndShiftDown(table_tex2),
            FadeInFrom(table_tex5, UP),
            Write(table_tex6[0]),
        )
        self.wait()
        self.play(
            ShowCreationThenFadeAround(tex[:5])
        )
        for t in table_tex6[1:]:
            self.play(ReplacementTransform(tex[:6].copy(),t))
            self.wait(0.1)
        self.wait()
        for i in range(1,6):
            self.play(
                FadeOut(table_tex6[i]),
                ReplacementTransform(table_tex3[i-1].copy(),table_tex6_1[i])
            )
            self.wait(0.1)
        self.wait()
        self.play(
            FadeOut(table_tex5),
            FadeOut(table_tex3),
            FadeOut(table_tex4),
            FadeOut(table_tex6[0]),
            ApplyFunction(
                lambda mob: mob.to_corner(UL) \
                    .shift(1.2 * DOWN + 1.2*LEFT) \
                    .scale(0.7),
                table_tex6_1
            )
        )
        for n in self.n:
            n.next_to(table_tex6_1,direction=DOWN,aligned_edge=LEFT,buff=0.3)
        self.play(Write(self.n[0]))
        indic_rec = ShowCreationThenDestructionAround(table_tex6_1[1]).get_rect()
        self.play(
            ShowCreationThenDestructionAround(table_tex6_1[1]),
            ShowCreation(indic_rec)
        )
        self.wait()
        self.play(
            Write(f6_1),
            Write(f6_2),
        )
        self.wait()
        self.play(
            f6_2.next_to, title, {"direction": DOWN, "buff": 0.4},
            f6_1.next_to, self.n[0], {"direction": DOWN, "buff": 0.4, "aligned_edge": LEFT},
        )
        self.wait(1)
        # AB AC AD AE AF AG BC BD AH DH CH BH
        # 0  1  2  3  4  5  6  7  8  9  10 11
        self.play(
            in_geo[1][0].set_color, BLUE_D,
            in_geo[1][8].set_color, BLUE_D,
            in_geo[1][11].set_color, BLUE_D,
            in_geo[1][7].set_color, YELLOW_C,
            in_geo[1][9].set_color, YELLOW_C,

            in_geo[1][10].set_color, YELLOW_C,
            in_geo[1][1].set_color, GREEN_SCREEN,
            in_geo[1][2].set_color, GREEN_SCREEN,
        )
        self.wait()
        f12_1.next_to(f6_1,direction=DOWN,aligned_edge=LEFT,buff=0.5)
        f12_2.next_to(f12_1,direction=RIGHT,buff=0.4)
        f12_3.next_to(f12_1,direction=DOWN,aligned_edge=LEFT,buff=0.5)
        f12_4.next_to(f12_3,direction=DOWN,aligned_edge=LEFT,buff=0.5)
        f12_5.next_to(f12_3,direction=DOWN,aligned_edge=LEFT,buff=0.5)
        f12_6.next_to(f12_3,direction=DOWN,aligned_edge=LEFT,buff=0.5)
        f12_7.next_to(f12_6,direction=DOWN,aligned_edge=LEFT,buff=0.5)
        f12_8.next_to(f12_6,direction=DOWN,aligned_edge=LEFT,buff=0.5)
        self.play(
            indic_rec.move_to, table_tex6_1[2],
            Write(f12_1),
            Transform(self.n[0],self.n[1])
        )
        for i in range(1,6):
            if i >= 4:
                self.play(ReplacementTransform(f12[i - 1], f12[i]))
            else:
                self.play(ReplacementTransform(f12[i-1].copy(),f12[i]))

            self.wait()
        self.play(Write(f12_7))
        self.wait()
        self.play(
            Transform(f12_7, f12_8),
            Write(caption_mob[0])
        )
        self.wait()
        self.play(
            Transform(caption_mob[0],caption_mob[1])
        )
        self.play(
            FadeOut(f12_1),
            FadeOut(f12_2),
            FadeOut(f12_3),
            FadeOut(caption_mob[0]),
            f12_7.next_to,f6_2,{"direction":DOWN,"aligned_edge":LEFT,"buff":0.4},
            f12[5].next_to,f6_1,{"direction":RIGHT,"buff":0.4}
        )
        self.wait()
        f = [f12,f24,f48,f96]
        for i,fn in zip(range(1,4),f[1:]):
            fn[0].next_to(f6_1,direction=DOWN,aligned_edge=LEFT,buff=0.5)
            fn[1].next_to(f6_1,direction=DOWN,aligned_edge=LEFT,buff=0.5)
            fn[2].next_to(fn[1],direction=DOWN,aligned_edge=LEFT,buff=0.5)
            fn[3].next_to(fn[1],direction=DOWN,aligned_edge=LEFT,buff=0.5)
            self.play(
                Write(fn[0]),
                indic_rec.move_to,table_tex6_1[i+2],
                Transform(self.n[0],self.n[i+1])
            )
            self.wait()
            if i == 1:
                self.play(
                    ShowCreationThenDestructionAround(f12[5]),
                    ShowCreationThenDestructionAround(f12_7),
                    ShowCreationThenDestructionAround(fn[0][4:9])
                )
            else:
                self.play(
                    ShowCreationThenDestructionAround(fn[0][4:9]),
                    ShowCreationThenDestructionAround(f[i-1][1]),
                    ShowCreationThenDestructionAround(f[i - 1][3]),
                )
            self.wait()
            self.play(ReplacementTransform(fn[0],fn[1]))
            self.wait(1)

            self.play(Write(fn[2]))
            self.wait()
            self.play(ReplacementTransform(fn[2],fn[3]))
            self.wait()
            if i != 3:
                if i == 1:
                    self.play(
                        fn[1].next_to,f12[5],{"direction":RIGHT,"buff":0.4},
                        fn[3].next_to,f12_7,{"direction":DOWN,"aligned_edge":LEFT,"buff":0.4}
                    )
                else:
                    self.play(
                        fn[1].next_to, f[i-1][1], {"direction": RIGHT, "buff" : 0.4},
                        fn[3].next_to, f[i-1][3], {"direction": DOWN, "aligned_edge": LEFT, "buff": 0.4}
                    )
            self.wait()
        self.play(
            ShowCreationThenDestructionAround(f96_4),
            ShowCreationThenDestructionAround(tex[:5]),
        )
        self.wait()
        for pi in fpi[:-1]:
            self.play(
                Transform(f96_4,pi)
            )
            self.wait()
        fad_ombjects = [mobject for mobject in self.mobjects if mobject is not fpi_6 or fpi_7]
        self.play(
            FadeOut(
                Group(*fad_ombjects),
            ),
            fpi_6.move_to, UP,
            fpi_6.scale, 1.2,
            Write(caption_mob[2])
        )
        fpi_7.scale(1.2)\
             .move_to(ORIGIN)
        self.wait()
        self.play(
            ReplacementTransform(fpi_6.copy(), fpi_7),
            Transform(caption_mob[2],caption_mob[3])
        )
        self.wait()
        self.play(
            Transform(caption_mob[2],caption_mob[4])
        )
        self.wait()
        self.play(
            Transform(caption_mob[2], caption_mob[5])
        )
        self.wait(4)





    def get_in_geo(self):
        sector = AnnularSector(
            fill_opacity=0,
            stroke_width=4,
            inner_radius=0,
            angle=TAU / 2,
        )
        # O A B C D E F G H
        # 0 1 2 3 4 5 6 7 8
        points = self.get_in_points()
        # 创建线段
        # AB AC AD AE AF AG BC BD AH DH CH BH
        # 12 13 14 15 16 17 23 24 18 48 38 28
        lines = VGroup()
        for start,end in [(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(2,3),(2,4),(1,8),(4,8),(3,8),(2,8)]:
            l = Line(np.array(points[start]),np.array(points[end]),stroke_width=4)
            lines.add(l)
        # 创建标注
        notes = ["O","A","B","C","D","E","F","G","H"]
        #        /   /   /   /   /   /   /   /   /
        #       0   1   2   3   4   5   6   7   8
        notes_mob = VGroup(
            *[
                TexMobject(note).scale(0.6) for note in notes
            ]
        )
        directions = [DOWN,DOWN,DOWN,UP,UL,UL,LEFT,DL,UR]
        buffs = [0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.3,0.1]
        for note,i,dir,buf in zip(notes_mob,range(9),directions,buffs):
            note.next_to(points[i],direction=dir,buff=buf)
        # self.add(sector,lines,notes_mob)
        arrow = Arrow(
            notes_mob[7],
            points[7],
            stroke_width=3,
        )
        in_geo = VGroup(sector,lines,notes_mob,arrow)
        return in_geo
    def get_in_points(self):
        # 顺序： O A B C D E F G H
        r = 2
        angle = 60*DEGREES
        coords = [(0,0,0),(2,0,0),(-2,0,0)]
        for _ in range(5):
            x = r*np.cos(angle)
            y = r*np.sin(angle)
            coords.append((-x,y,0))
            angle /= 2
        coords.append((-1.46,0.93,0))
        return coords



class Arcs(VGroup):

    CONFIG = {
        'colors': [RED, YELLOW, BLUE, PINK],
        'radius': 1,
        'start_angle': 0,
        'angle_list': [30 * DEGREES, 60 * DEGREES, 90 * DEGREES],
        'stroke_width': 40,

    }

    def __init__(self, **kwargs):

        VMobject.__init__(self, **kwargs)
        self.create_arcs()

    def create_arcs(self, **kwargs):
        angle = self.start_angle
        colors = color_gradient(self.colors, len(self.angle_list))
        for i in range(len(self.angle_list)):
            self.add(Arc(radius=self.radius, start_angle=angle, angle=self.angle_list[i], color=colors[i], stroke_width=self.stroke_width, **kwargs))
            angle += self.angle_list[i]

class Arcs_Test(Scene):

    def construct(self):

        arcs_01 = Arcs(stroke_width=80).shift(LEFT * 4.5)
        arcs_02 = Arcs(angle_list=np.array([10, 20, 30, 40, 50, 60, 70, 80]) * DEGREES, stroke_width=200)
        arcs_03 = Arcs(angle_list=np.array([10, 15, 20, 30]) * DEGREES, stroke_width=200).set_stroke(opacity=0.25).shift(RIGHT * 4)
        arcs_04 = Arcs(angle_list=np.array([10, 15, 20, 30]) * DEGREES, radius=2, stroke_width=10).shift(RIGHT * 4)

        self.play(ShowCreation(arcs_01))
        self.wait()
        self.play(ShowCreation(arcs_02))
        self.wait()
        self.play(ShowCreation(VGroup(arcs_03, arcs_04)))

        self.wait(4)

class Angle(VGroup):

    CONFIG = {
        'radius': 1,
        'color': RED,
        'opacity': 0.4,
        'stroke_width': 10,
        'below_180': True,
    }

    def __init__(self, A, O, B, **kwargs):

        VMobject.__init__(self, **kwargs)
        OA, OB = A-O, B-O
        if self.below_180:
            theta = np.angle(complex(*OA[:2])/complex(*OB[:2])) # angle of OB to OA
        else:
            theta = TAU + np.angle(complex(*OA[:2])/complex(*OB[:2]))

        self.add(Arc(start_angle=Line(O, B).get_angle(), angle=theta, radius=self.radius/2,
                     stroke_width=100 * self.radius, color=self.color, arc_center=O).set_stroke(opacity=self.opacity))
        self.add(Arc(start_angle=Line(O, B).get_angle(), angle=theta, radius=self.radius,
                     stroke_width=self.stroke_width, color=self.color, arc_center=O))

class Angles_tag(Scene):

    def construct(self):

        A = LEFT * 4.5 + DOWN * 2
        B = RIGHT * 6 + DOWN * 1
        C = UP * 2

        tri_abc = Polygon(A, B, C, color=WHITE)

        dot_A = Dot(A, color=RED, radius=0.15)
        angle_A = Angle(B, A, C, color=RED, radius=1.6)

        dot_B = Dot(B, color=YELLOW, radius=0.15)
        angle_B = Angle(A, B, C, color=YELLOW, radius=1.5)

        dot_C = Dot(C, color=BLUE, radius=0.15)
        angle_C = Angle(A, C, B, color=BLUE, radius=1.)

        self.add((tri_abc))
        self.wait()
        self.play(FadeInFromLarge(dot_A))
        self.play(ShowCreation(angle_A))
        self.wait()
        self.play(FadeInFromLarge(dot_B))
        self.play(ShowCreation(angle_B))
        self.wait()
        self.play(FadeInFromLarge(dot_C))
        self.play(ShowCreation(angle_C))

        self.wait(2)



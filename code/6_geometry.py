from manimlib.imports import *
import sys

sys.path.append('..')

class Demo(GraphScene):
    def construct(self):
        theta = ValueTracker(90*DEGREES)
        arrow = Arrow(np.array([-2,0,0]),np.array([2,0,0]))\
                .rotate(theta.get_value(),about_point=np.array([-2,0,0]))
        line = Line(arrow.get_start(),np.array([2,0,0]))
        arrow.add_updater(
            lambda mob:mob.set_angle(
                theta.get_value()
            )
        )
        arc = Arc(arc_center=arrow.get_start(),
                  radius=arrow.get_length(),
                  start_angle=line.get_angle(),
                  angle=arrow.get_angle()
        )
        self.play(
            *[
                ShowCreation(mob) for mob in [arrow,line]
            ]
        )
        arc.add_updater(
            lambda mob:mob.become(
                Arc(
                    arc_center=arrow.get_start(),
                    radius = arrow.get_length(),
                    start_angle=line.get,
                    angle = arrow.get_angle()
                )
            )
        )
        self.add(arc)
        self.play(theta.increment_value, 90*DEGREES)

class Demo1(Scene):
    CONFIG = {
        'x_min':-1,
        'x_max':1
    }
    def construct(self):
        # arc = Arc(
        #     arc_center=ORIGIN,
        #     radius=2,
        #     start_angle=
        # )
        pass

class Scene1(MovingCameraScene):
    # CONFIG = {
    #     'camera_config': {
    #         'background_color': WHITE,
    #     }
    # }
    def construct(self):
        captions = [
            "BE_1=\\frac{1}{2}AB",
            "BE_2=\\frac{1}{3}AB",
            "BE_{n-1}=\\frac{1}{n}AB",
            "BE_n=\\frac{1}{n+1}AB"
        ]
        captions_mob = VGroup(
            *[
                TexMobject(mob).scale(0.5) for mob in captions
            ]
        )
        captions_mob.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.4
        )
        captions_mob.move_to(np.array([-3,0,0]))
        text = [
            "A",        # 0
            "B",        # 1
            "C_1",      # 2
            "C_2",      # 3
            "C_{n-1}",  # 4
            "C_n",      # 5
            "D_1",      # 6
            "D_2",      # 7
            "D_{n-1}",  # 8
            "D_n",      # 9
            "E_1",      # 10
            "E_2",      # 11
            "E_{n-1}",  # 12
            "E_n",      # 13

        ]
        text_mob = VGroup(
            *[
                TexMobject(mob) for mob in text
            ]
        )
        # screen_grid = ScreenGrid()
        # self.add(screen_grid)
        dots_data = [
            ("a", -2, -2),
            ("b", 2, -2),
            ("c1", 2, 2),
            ("c2", 2, 0),
            ("cn1", 2, -0.67),
            ("cn", 2, -1),
            ("d1", 0, 0),
            ("d2", 0.67, -0.67),
            ("dn1", 1, -1),
            ("dn", 1.2, -1.2),
            ("e1", 0, -2),
            ("e2", 0.67, -2),
            ("en1", 1, -2),
            ("en", 1.2, -2),
            ("g", 2, 3),
        ]
        dots = {}
        for name, x, y in dots_data:
            d = SmallDot().move_to(np.array([x, y, 0]))
            dots[name] = d
        lines_data = [
            ('ae2',dots['a'],dots['e2'],Line,GREEN),
            ('e2en1',dots['e2'],dots['en1'],Line,GREEN),
            ('e2en1_',dots['e2'],dots['en1'],DashedLine,GREEN),
            ('en1b',dots['en1'],dots['b'],Line,GREEN),
            ('bcn',dots['b'],dots['cn'],Line,YELLOW),
            ('cncn1',dots['cn'],dots['cn1'],Line,YELLOW),
            ('cn1c2', dots['c2'], dots['cn1'], Line,YELLOW),
            ('cn1c2_', dots['c2'], dots['cn1'], DashedLine,YELLOW),

            ('c2g',dots['c2'],dots['g'],Line,YELLOW),
            ("ac1", dots["a"], dots["c1"],Line,BLUE),
            ("bd1", dots["b"], dots["d1"],Line,PINK),
            ("d1e1", dots["d1"], dots["e1"],DashedLine,"#AF601A"),
            ("ac2", dots["a"], dots["c2"],Line,"#AF601A"),
            ("d2e2", dots["d2"], dots["e2"],DashedLine,"#AF601A"),
            ("acn1", dots["a"], dots["cn1"],Line,BLUE),
            ("dn1en1", dots["dn1"], dots["en1"],DashedLine,'#AF601A'),
            ("acn", dots["a"], dots["cn"],Line,BLUE),
            ("dnen", dots["dn"], dots["en"],DashedLine,'#AF601A'),
        ]
        lines = {}
        for name, d1, d2,line_class,col in lines_data:
            line = line_class(d1.get_center(), d2.get_center(),color=col)
            lines[name] = line
        line_bc_mob = VGroup(lines['bcn'],lines['cncn1'],lines['cn1c2'],lines['cn1c2_'],lines['c2g'])
        line_ab_mob = VGroup(lines['ae2'],lines['e2en1'],lines['e2en1_'],lines['en1b'])
        text_data = [
            (0, dots["a"], DL, 0.2,0.5),
            (1, dots["b"], DR, 0.2,0.5),
            (2, dots["c1"], RIGHT, 0.1,0.5),
            (3, dots["c2"], RIGHT, 0.1,0.5),
            (4, dots["cn1"], RIGHT, 0.1,0.5),
            (5, dots["cn"], RIGHT, 0.1,0.5),
            (6, dots["d1"], UP, 0.1,0.5),
            (7, dots["d2"], UP, 0.1,0.5),
            (8, dots["dn1"], UP, 0.1,0.4),
            (9, dots["dn"], DOWN, 0.1,0.4),
            (10, dots["e1"], DOWN, 0.2,0.4),
            (11, dots["e2"], DOWN, 0.2,0.4),
            (12,dots['en1'],DOWN,0.2,0.3),
            (13, dots['en'], DOWN, 0.2, 0.3),

        ]
        for i, d, dir, buf,size in text_data:
            text_mob[i].scale(size)
            text_mob[i].next_to(d, direction=dir, buff=buf)
        arc_c = Arc(radius=4,
                    arc_center=dots['b'].get_center(),
                    start_angle=180 * DEGREES,
                    angle=-90*DEGREES,
                    color='#7FFF7F'

                    )
        arc_e = Arc(
            radius = 2,
            arc_center=dots['b'].get_center(),
            start_angle=180 * DEGREES,
            angle=-90 * DEGREES,
            color='#7FFF7F'
        )
        arc_e1 = Arc(
            radius=1.33,
            arc_center=dots['b'].get_center(),
            start_angle=180 * DEGREES,
            angle=-90 * DEGREES,
            color='#7FFF7F'
        )
        arc_e2 = Arc(
            radius=1,
            arc_center=dots['b'].get_center(),
            start_angle=180 * DEGREES,
            angle=-90 * DEGREES,
            color='#7FFF7F'
        )
        arc_angle = Arc(
            radius=0.5,
            arc_center=dots['b'].get_center(),
            start_angle=90*DEGREES,
            angle=45*DEGREES,
            color='#9400d3'
        )
        rec = Rectangle(height=0.25,width=0.25,fill_color=YELLOW,fill_opacity=0.5,stroke_opacity=0)\
              .move_to(dots['b'].get_center())\
              .shift(0.125*LEFT)\
              .shift(0.125*UP)
        note = TexMobject('45^\\circ')\
               .scale(0.4)\
               .next_to(arc_angle,direction=UP,buff=0.1)
        note1 = TexMobject("AD_1=C_1D_1").scale(0.5)\
                                         .next_to(dots['d1'],direction=LEFT,buff=0.2)


        # ------------------以上为变量定义---------------------------
        self.camera.frame.scale(0.7)
        text = TextMobject("方法一").scale(0.8)\
                                    .set_color(YELLOW)
        l = Line(LEFT, RIGHT, color=YELLOW).next_to(text, direction=DOWN, buff=0.1)
        self.play(FadeInFrom(text,UP),
                  FadeInFrom(l,UP)
        )
        self.wait()
        self.play(
            FadeOutAndShift(text,DOWN),
            FadeOutAndShift(l, DOWN),

        )
        self.add(line_ab_mob,line_bc_mob)
        self.wait()
        self.play(ShowCreation(rec))
        self.wait()
        self.play(Write(text_mob[0]),
                  Write(text_mob[1]),
                  ShowCreation(dots['a']),
                  ShowCreation(dots['b'])
                  )
        self.wait()
        self.play(CircleIndicate(dots['b']))
        self.wait(1)
        self.play(ShowCreation(arc_c))
        self.wait(1)
        self.play(
            ShowCreation(dots['c1']),
            Write(text_mob[2]),
            FadeOut(arc_c)
        )
        self.wait()
        self.play(ShowCreation(lines["ac1"]))
        self.wait()
        self.play(
            ShowCreation(dots['d1']),
            Write(text_mob[6])
        )
        self.wait()
        self.play(ShowCreationThenFadeOut(note1))
        self.wait()
        self.play(ShowCreation(lines["bd1"]))
        self.wait()
        self.play(ShowCreation(arc_angle))
        self.wait(1)
        self.play(Write(note))
        self.wait()
        self.play(ShowCreation(lines["d1e1"]))
        self.wait(1)
        self.play(
            ShowCreation(dots['e1']),
            Write(text_mob[10])
        )
        self.wait()
        self.play(Write(captions_mob[0]))
        self.wait()
        self.play(CircleIndicate(dots['b']))
        self.wait(1)
        self.play(ShowCreation(arc_e))
        self.wait(1)
        self.play(
            ShowCreation(dots['c2']),
            Write(text_mob[3]),
            FadeOut(arc_e)
        )
        self.wait()
        self.play(ShowCreation(lines['ac2']))
        self.wait()
        self.add(dots['d2'])
        self.wait(1)
        self.play(Write(text_mob[7]))
        self.wait()
        self.play(ShowCreation(lines['d2e2']))
        self.wait(1)
        self.play(
            ShowCreation(dots['e2']),
            Write(text_mob[11])
        )
        self.wait()
        self.play(Write(captions_mob[1]))
        self.wait()
        self.play(FadeOut(lines['cn1c2']))
        self.wait()
        self.play(CircleIndicate(dots['b']))
        self.wait(1)
        self.play(ShowCreation(arc_e1))
        self.wait(1)
        self.play(
            ShowCreation(dots['cn1']),
            Write(text_mob[4]),
            FadeOut(arc_e1)
        )
        self.wait()
        self.play(ShowCreation(lines['acn1']))
        self.wait()
        self.play(
            ShowCreation(dots['dn1']),
            Write(text_mob[8])
        )
        self.wait()
        self.play(ShowCreation(lines['dn1en1']))
        self.wait(1)
        self.play(
            ShowCreation(dots['en1']),
            Write(text_mob[12])
        )
        self.wait(1)
        self.play(FadeOut(lines['e2en1']))
        self.wait()
        self.play(Write(captions_mob[2]))
        self.wait()
        self.play(CircleIndicate(dots['b']))
        self.wait(1)
        self.play(ShowCreation(arc_e2))
        self.wait(1)
        self.play(
            ShowCreation(dots['cn']),
            FadeOut(arc_e2),
            Write(text_mob[5])
        )
        self.wait()
        self.play(ShowCreation(lines['acn']))
        self.wait()
        self.play(ShowCreation(dots['dn']))
        self.wait(1)
        self.play(Write(text_mob[9]))
        self.wait()
        self.play(ShowCreation(lines['dnen']))
        self.wait()
        self.play(
            ShowCreation(dots['en']),
            Write(text_mob[13])
        )
        self.wait()
        self.play(Write(captions_mob[3]))
        self.wait()
class Scene2(MovingCameraScene):
    CONFIG = {
        'x_min':-1,
        'x_max':1,
        'tick_frequency':2
    }
    def construct(self):
        # 所有点的定义
        dots_data = [
            ('a',-3,0),         # 0
            ('b',1,0),          # 1
            ('c1',-1,0),        # 2
            ('c2',-1.67,0),     # 3
            ('c3',-2,0),        # 4
            ('c4',-2.2,0),      # 5
            ('d',3,0),          # 6
            ('e',5,0),          # 7
            ('f',7,0),          # 8
            ('j1',-1,3.46),     # 9
            ('j2',-1.67,3.77),  # 10
            ('j3',-2,3.87),     # 11
            ('j4',-2.2,3.92),   # 12
            ('k1',-1,-3.46),    # 13
            ('k2',-1.67,-3.77), # 14
            ('k3',-2,-3.87),    # 15
            ('k4',-2.2,-3.92),  # 16
            ('g1',0,3.87),      # 17
            ('g2',0,5.2),       # 18
            ('g3',0,6.24),      # 19
            ('g4',0,7.14),      # 20
            ('h1', 0, -3.87),   # 21
            ('h2', 0, -5.2),    # 22
            ('h3', 0, -6.24),   # 23
            ('h4', 0, -7.14),   # 24
            ('i',9,0)           # 25
        ]
        dots = {}
        dots_mob = VGroup()
        for name,x,y in dots_data:
            d = Dot(radius=0.08).move_to(np.array([x,y,0]))
            dots[name] = d
            dots_mob.add(d)
        # 所有点标签定义
        tags = [
            "A",        # 0
            "B",        # 1
            "C_1",      # 2
            "C_2",      # 3
            "C_3",      # 4
            "C_4",      # 5
            "D",        # 6
            "E",        # 7
            "F",        # 8
        ]
        tags_mob = VGroup(
            *[
                TexMobject(mob) for mob in tags
            ]
        )
        tags_data = [
            (0,dots['a'],0.8,DL,0.1),
            (1,dots["b"],0.8,DR,0.1),
            (2, dots["c1"], 0.8, DR, 0.1),
            (3, dots["c2"], 0.7, DR, 0.1),
            (4, dots["c3"], 0.7, DR, 0.06),
            (5, dots["c4"], 0.7, DL, 0.08),
            (6, dots["d"], 0.8, DOWN, 0.1),
            (7, dots["e"], 0.8, DOWN, 0.1),
            (8, dots["f"], 0.8, DOWN, 0.1),
        ]
        for i,d,size,dir,buff in tags_data:
            tags_mob[i].scale(size)
            tags_mob[i].next_to(d,direction=dir,buff=buff)
        # 所有线段的定义
        lines_data = [
            ('af',dots['a'],dots['f'],Line,"#99CC33"),
            ('j1k1',dots['j1'],dots['k1'],DashedLine,"#66CCCC"),
            ('j2k2', dots['j2'], dots['k2'],DashedLine,"#FF99CC"),
            ('j3k3', dots['j3'], dots['k3'],DashedLine,"#FF9999"),
            ('j4k4', dots['j4'], dots['k4'],DashedLine,"#FF6666"),
            ('fg',dots['f'],dots['i'],DashedLine,"#99CC33"),
            ('bc1',dots['b'],dots['c1'],Line,"#66CC33"),
            ('dc2', dots['d'], dots['c2'], Line,"#66CC33"),
            ('ec3', dots['e'], dots['c3'], Line,"#66CC33"),
            ('fc4', dots['f'], dots['c4'], Line,"#66CC33"),
            ('bg1', dots['b'], dots['g1'], DashedLine,"#666699"),
            ('dg2', dots['d'], dots['g2'], DashedLine,"#FF9999"),
            ('eg3', dots['e'], dots['g3'], DashedLine,"#FFCC00"),
            ('fg4', dots['f'], dots['g4'], DashedLine,"#FF9900"),

        ]
        lines = {}
        lines_mob = VGroup()
        for name,d1,d2,line_class,col in lines_data:
            l = line_class(d1,d2,color=col)
            lines[name] = l
            lines_mob.add(l)
        # 圆的定义
        ca = Circle(radius=4).move_to(dots['a'])
        # 圆弧的定义
        arcs_data = [
            ('arc_h1g1',dots['g1'],dots['h1'],151.04,"#66CCCC",),
            ('arc_h2g2',dots['g2'],dots['h2'],120,"#FF99CC"),
            ('arc_h3g3',dots['g3'],dots['h3'],102.64,"#FF9999"),
            ('arc_h4g4',dots['g4'],dots['h4'],91.15,"#FFFF66"),

        ]
        arcs = {}
        for name,d1,d2,angle,col in arcs_data:
            arc = ArcBetweenPoints(d1.get_center(),d2.get_center(),angle=angle*DEGREES,color=col)
            arcs[name] = arc

        numberline_bc1 = NumberLine(x_min=-1,x_max=1,tick_frequency=1).next_to(dots['d'],direction=UP,buff=3)

        brace = Brace(numberline_bc1,direction=UP,buff=MED_SMALL_BUFF)
        # tip = TexMobject("BC_1").scale(0.8).next_to(brace,direction=UP,buff=0.1)
        tips = [
            "BC_1",
            "BC_1=BD=DE=EF",
        ]
        tips_mob = VGroup(
            *[
                TexMobject(mob) for mob in tips
            ]
        )
        tips_data = [
            (0,0.8, brace, UP, 0.1),
            (1,0.8,dots['d'],DOWN,2)
        ]
        for i,size,target,dir,buff in tips_data:
            tips_mob[i].scale(size)
            tips_mob[i].next_to(target,direction=dir,buff=buff)
        arc_bedf_data = [
            ('bd',dots['b'],2,30,-60),
            ('de', dots['d'], 2, 30, -60),
            ('ef', dots['e'], 2, 30, -60),

        ]
        arcs_bedf = {}
        arc_bedf_mob = VGroup()
        for name,d,r,start_angle,angle in arc_bedf_data:
            arc = Arc(arc_center=d.get_center(),radius=r,start_angle=start_angle*DEGREES,angle=angle*DEGREES)
            arcs_bedf[name] = arc
            arc_bedf_mob.add(arc)
        arrow = Arrow(numberline_bc1.get_start(), numberline_bc1.get_end(), buff=0) \
            .shift(1 * DOWN)
        arrow1 = Arrow(dots['b'].get_center(),arcs_bedf['bd'].get_start(),buff=0)
        notes = [
            "BC_1=\\frac{1}{2}AB",
            "BC_2=\\frac{1}{3}AB",
            "BC_3=\\frac{1}{4}AB",
            "BC_4=\\frac{1}{5}AB",
            "......"

        ]
        notes_mob = VGroup(
            *[
                TexMobject(mob).scale(0.7) for mob in notes
            ]
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.3
        ).next_to(dots['d'],direction=DOWN,buff=1.5)
        text = TextMobject("方法二").scale(1.5)\
                                    .set_color(YELLOW)
        l = Line(1.5*LEFT,1.5*RIGHT,color=YELLOW).next_to(text,direction=DOWN,buff=0.1)
        # ------------------------以上为各变量的定义--------------------------------------
        self.camera.frame.scale(1.7)
        self.play(
            *[FadeInFrom(mob,UP) for mob in [text,l]]
        )
        self.wait()
        self.play(
            *[FadeOutAndShiftDown(mob) for mob in [text,l]]
        )
        self.wait()
        self.play(ShowCreation(lines['af']))
        self.wait(1)
        self.play(
            ShowCreation(dots['a']),
            ShowCreation(dots['b']),
            Write(tags_mob[0]),
            Write(tags_mob[1])
        )
        self.wait()
        # TODO:得出def点前先画二等分点
        self.play(CircleIndicate(dots['a']))
        self.play(ShowCreation(ca))
        self.wait()
        self.play(CircleIndicate(dots['b']))
        self.play(ShowCreation(arcs['arc_h1g1']))
        self.wait(1)
        self.play(
            ShowCreation(dots['j1']),
            ShowCreation(dots['k1']),
            ShowCreation(lines['bg1'])
        )
        self.wait(1)
        self.play(ShowCreation(lines['j1k1']))
        self.wait(1)
        self.play(
            ShowCreation(dots['c1']),
            Write(tags_mob[2])
        )
        self.wait()
        # TODO:绘制def点
        self.play(ReplacementTransform(lines['bc1'],numberline_bc1))
        self.wait()
        self.play(FadeInFrom(brace,UP),FadeInFrom(tips_mob[0],UP))
        self.wait()
        self.play(ReplacementTransform(numberline_bc1.copy(),arrow))
        self.wait()
        self.play(CircleIndicate(dots['b']))
        self.wait(1)
        self.play(ShowCreation(arcs_bedf['bd']))
        self.wait()
        self.play(ReplacementTransform(arrow.copy(),arrow1))
        self.wait()
        self.play(
            ShowCreation(dots['d']),
            Write(tags_mob[6]),
            FadeOut(arcs_bedf['bd']),
            FadeOut(arrow1)
        )
        self.wait()
        self.play(
            *[
                ShowCreation(d) for d in [dots['e'],dots['f']]
            ]
        )
        self.wait(1)
        self.play(
            *[
                Write(tag) for tag in tags_mob[7:]
            ]
        )
        self.wait()
        self.play(
            ShowCreationThenFadeOut(tips_mob[1], run_time=7)
        )
        self.play(
            *[FadeOut(mob) for mob in [arrow,brace,numberline_bc1,tips_mob[0]]]
        )
        self.wait()


        self.play(CircleIndicate(dots['d']))

        self.play(ShowCreation(arcs['arc_h2g2']))
        self.wait(1)
        self.play(ShowCreation(lines['dg2']))
        self.wait(1)
        self.play(
            ShowCreation(dots['j2']),
            ShowCreation(dots['k2'])
        )
        self.wait(1)
        self.play(ShowCreation(lines['j2k2']))
        self.wait(1)
        self.play(
            ShowCreation(dots['c2']),
            Write(tags_mob[3])
        )
        self.wait()
        self.play(CircleIndicate(dots['e']))
        self.play(ShowCreation(arcs['arc_h3g3']))
        self.wait(1)
        self.play(ShowCreation(lines['eg3']))
        self.wait()
        self.play(
            ShowCreation(dots['j3']),
            ShowCreation(dots['k3'])
        )
        self.wait(1)
        self.play(ShowCreation(lines['j3k3']))
        self.wait(1)
        self.play(
            ShowCreation(dots['c3']),
            Write(tags_mob[4])
        )
        self.wait()
        self.play(CircleIndicate(dots['f']))
        self.play(ShowCreation(arcs['arc_h4g4']))
        self.wait(1)
        self.play(ShowCreation(lines['fg4']))
        self.wait()
        self.play(
            ShowCreation(dots['j4']),
            ShowCreation(dots['k4'])
        )
        self.wait(1)
        self.play(ShowCreation(lines['j4k4']))
        self.wait(1)
        self.play(
            ShowCreation(dots['c4']),
            Write(tags_mob[5])
        )
        self.wait()
        self.play(ShowCreation(lines['fg']))
        self.wait()
        self.play(Write(notes_mob))
class Scene3(MovingCameraScene):

    def construct(self):
        # 所有点的定义
        dots_data = [
            ('a',-4,0),
            ('b',4,0),
            ('c1',-1.33,0),
            ('c2',3.11,0),
            ('d',2.42,-2.87),
            ('a1',-2.08,0.57),
            ('a2',-0.17,1.15),
            ('a3',1.75,1.72),
            ('an1',3.66,2.3),
            ('an',5.58,2.87)
        ]
        dots = {}
        for name,x,y in dots_data:
            d = Dot(radius=0.09).move_to(np.array([x,y,0]))
            dots[name] = d
        # 所有标签的定义
        tex = [
            "A",        # 0
            "B",        # 1
            'C_1',      # 2
            'C_2',      # 3
            'D',        # 4
            'A_1',      # 5
            'A_2',      # 6
            'A_3',      # 7
            'A_{n-1}',  # 8
            'A_n'       # 9
        ]
        tags_mob = VGroup(
            *[
                TexMobject(mob) for mob in tex
            ]
        )
        tags_data = [
            (0,dots['a'],0.7,DOWN,0.2),
            (1,dots['b'],0.7,DOWN,0.2),
            (2, dots['c1'], 0.7, DOWN, 0.2),
            (3, dots['c2'], 0.7, DR, 0.1),
            (4, dots['d'], 0.7, RIGHT, 0.2),
            (5, dots['a1'], 0.7, UL, 0.2),
            (6, dots['a2'], 0.7, UL, 0.2),
            (7, dots['a3'], 0.7, UL, 0.2),
            (8, dots['an1'], 0.7, UL, 0.2),
            (9, dots['an'], 0.7, UL, 0.2),

        ]
        for i,d,size,dir,buff in tags_data:
            tags_mob[i].scale(size)
            tags_mob[i].next_to(d,direction=dir,buff=buff)

        # 多有的线的定义
        lines_data = [
            ('ab',dots['a'],dots['b'],Line,"#00FF00"),
            ('aa3',dots['a'],dots['a3'],Line,"#00BFFF"),
            ('a3an1',dots['a3'],dots['an1'],DashedLine,"#00BFFF"),
            ('an1an',dots['an1'],dots['an'],Line,"#00BFFF"),
            ('and',dots['an'],dots['d'],Line,"#FF00FF"),
            ('a1d',dots['a1'],dots['d'],Line,"#DC143C"),
            ('an1d',dots['an1'],dots['d'],Line,"#DC143C")
        ]
        lines = {}
        for name,d1,d2,line_class,col in lines_data:
            l = line_class(d1.get_center(),d2.get_center(),color=col)

            lines[name] = l
        # 所有的圆弧定义
        arcs_data = [
            ('arc_aa1',dots['a'],2,0,33.4),
            ('arc_a1a2',dots['a1'],2,0,33.4),
            ('arc_a2a3',dots['a2'],2,0,33.4),
            ('arc_a3an1', dots['a3'], 2,0,33.4),
            ('arc_an1an', dots['an1'], 2,0,33.4),
        ]
        arcs = {}
        for name,d,r,sta_angle,angle in arcs_data:
            r = Arc(arc_center=d.get_center(),radius=r,start_angle=sta_angle*DEGREES,angle=angle*DEGREES)
            arcs[name] = r
        cb = Circle(radius=3.28).move_to(dots['b'].get_center())

        theta = ValueTracker(0*DEGREES)
        numberline = NumberLine(x_min=-1,x_max=1).next_to(np.array([-3,0,0]),direction=DOWN,buff=1.5)
        brace = Brace(numberline,direction=DOWN,buff=0.1)
        notes = [
            "任意长度",
            "$AA_1=A_1A_2=A_2A_3=A_3A_{n-1}=A_{n-1}A_n$",
            "$AC_1=\\frac{2}{n+1}AB$",
            "$BC_2=\\frac{1}{2n-1}AB$",
            "过点A做任意射线",
        ]
        notes_mob = VGroup(
            *[TextMobject(mob).scale(0.7) for mob in notes]
        )
        notes_data = [
            (0,brace,DOWN,0.1),
            (1,ORIGIN,DOWN,3),
            (2,np.array([-3,0,0]),DOWN,1),
            (3,np.array([-3,0,0]),DOWN,2),
            (4,np.array([-3,0,0]),DOWN,1)
        ]
        for i,target,dir,buff in notes_data:
            notes_mob[i].next_to(target,direction=dir,buff=buff)
        arrow1 = Arrow(dots['a'].get_center(),arcs['arc_aa1'].get_start(),buff=0).next_to(numberline,direction=UP,buff=0.3)
        arrow = Arrow(dots['a'].get_center(),arcs['arc_aa1'].get_start(),buff=0)
        arrow.add_updater(
            lambda l:l.set_angle(
                theta.get_value()
            )
        )
        arcs['arc_aa1'].add_updater(
            lambda arc:arc.become(
                Arc(
                    arc_center=dots['a'].get_center(),
                    radius=arrow.get_length(),
                    start_angle=0*DEGREES,
                    angle=arrow.get_angle()
                )
            )
        )
        text = TextMobject("方法三").set_color(YELLOW)
        l = Line(LEFT,RIGHT,color=YELLOW).next_to(text,direction=DOWN,buff=0.1)
        #------------------------以上为各个变量定义---------------------------
        self.camera.frame.scale(1.2)
        self.play(
            *[
                FadeInFrom(mob,UP) for mob in [text,l]
            ]
        )
        self.wait()
        self.play(
            *[
                FadeOutAndShiftDown(mob) for mob in [text,l]
            ]
        )
        self.wait()
        self.play(ShowCreation(lines['ab']))
        self.wait(1)
        self.play(
            ShowCreation(dots['a']),
            ShowCreation(dots['b']),
            Write(tags_mob[0]),
            Write(tags_mob[1])
        )
        self.wait()
        self.play(Write(notes_mob[-1]))
        self.wait()
        self.play(
            ShowCreation(lines['aa3']),
            FadeOut(notes_mob[-1])
        )
        self.wait()
        self.play(ShowCreation(numberline))
        self.wait()
        self.play(
            FadeInFrom(brace,DOWN),
            FadeInFrom(notes_mob[0], DOWN),
        )
        self.wait(1)
        self.play(FadeInFrom(arrow1,UP))
        self.wait()
        self.play(ReplacementTransform(arrow1,arrow))
        self.wait(1)
        self.add(arcs['arc_aa1'])
        self.play(
            theta.increment_value,33.4*DEGREES
        )
        self.wait()
        self.play(
            ShowCreation(dots['a1']),
            Write(tags_mob[5]),
            FadeOut(arcs['arc_aa1']),
            FadeOut(arrow)
        )
        self.wait()
        self.play(CircleIndicate(dots['a1']))
        self.play(ShowCreation(arcs['arc_a1a2']))
        self.wait(1)
        self.play(
            ShowCreation(dots['a2']),
            Write(tags_mob[6]),
            FadeOut(arcs['arc_a1a2'])
        )
        self.wait()
        self.play(CircleIndicate(dots['a2']))
        self.play(ShowCreation(arcs['arc_a2a3']))
        self.wait(1)
        self.play(
            ShowCreation(dots['a3']),
            Write(tags_mob[7]),
            FadeOut(arcs['arc_a2a3'])
        )
        self.wait()

        self.play(ShowCreation(lines['a3an1']))
        self.wait()
        self.play(CircleIndicate(dots['a3']))
        self.play(ShowCreation(arcs['arc_a3an1']))
        self.wait(1)
        self.play(
            ShowCreation(dots['an1']),
            Write(tags_mob[8]),
            FadeOut(arcs['arc_a3an1'])
        )
        self.wait()

        self.play(ShowCreation(lines['an1an']))
        self.wait()
        self.play(CircleIndicate(dots['an1']))
        self.play(ShowCreation(arcs['arc_an1an']))
        self.play(
            ShowCreation(dots['an']),
            Write(tags_mob[9]),
            FadeOut(arcs['arc_an1an'])
        )
        self.wait()
        self.play(
            *[FadeOut(mob) for mob in [numberline,brace,notes_mob[0]]]
        )
        self.play(Write(notes_mob[1]))
        self.wait()
        self.play(
            ShowCreation(lines['and']),
            FadeOut(notes_mob[1])
        )
        self.wait()
        self.play(CircleIndicate(dots['b']))
        self.play(ShowCreation(cb))
        self.wait(1)
        self.play(
            ShowCreation(dots['d']),
            Write(tags_mob[4]),
            FadeOut(cb)
        )
        self.wait()
        self.play(
            ShowCreation(lines['an1d']),
            ShowCreation(lines['a1d']),
        )
        self.wait(1)
        self.play(
            ShowCreation(dots['c1']),
            ShowCreation(dots['c2']),
            Write(tags_mob[2]),
            Write(tags_mob[3]),
        )
        self.wait()
        self.play(
            Write(notes_mob[-3]),
            Write(notes_mob[-2]),
        )
        self.wait()
class Scene4(MovingCameraScene):

    def construct(self):
        # 所有点的定义
        dots_data = [
            ('a',-4,0),
            ('b',4,0),
            ('c1',0,0),
            ('c2',1.33,0),
            ('cn1',2,0),
            ('cn', 2.4, 0),
            ('d1',-2,1),
            ('d2',0,2),
            ('dn1',2,3),
            ('dn', 4, 4),
            ('f',2,-1),
        ]
        dots = {}
        for name,x,y in dots_data:
            d = Dot(radius=0.07).move_to(np.array([x,y,0]))
            dots[name] = d

        # 所有标签的定义
        tex = [
            'A',        # 0
            'B',        # 1
            'C_1',      # 2
            'C_2',      # 3
            'C_{n-1}',  # 4
            'C_n',      # 5
            'D_1',      # 6
            'D_2',      # 7
            'D_{n-1}',  # 8
            'D_n',      # 9
            'F',        # 10
        ]
        tags_mob = VGroup(
            *[
                TexMobject(mob) for mob in tex
            ]
        )
        tags_data = [
            (0,dots['a'],0.7,DOWN,0.2),
            (1, dots['b'], 0.7, DOWN, 0.2),
            (2, dots['c1'], 0.7, DOWN, 0.2),
            (3, dots['c2'], 0.6, DL, 0.1),
            (4, dots['cn1'], 0.6, UL, 0.1),
            (5, dots['cn'], 0.6, UR, 0.1),
            (6, dots['d1'], 0.7, UL, 0.1),
            (7, dots['d2'], 0.7, UL, 0.1),
            (8, dots['dn1'], 0.7, UL, 0.1),
            (9, dots['dn'], 0.7, UL, 0.1),
            (10, dots['f'], 0.7, DR, 0.1),

        ]
        for i,d,size,dir,buf in tags_data:
            tags_mob[i].scale(size)
            tags_mob[i].next_to(d,direction=dir,buff=buf)

        # 所有线的定义
        lines_data = [
            ('ab',dots['a'],dots['b'],Line,"#00FF00"),
            ('bf', dots['b'], dots['f'],Line,"#FFA500"),
            ('ad2', dots['a'], dots['d2'],Line,"#FF00FF"),
            ('d2dn1', dots['d2'], dots['dn1'],DashedLine,"#FF00FF"),
            ('dn1dn', dots['dn1'], dots['dn'],Line,"#FF00FF"),
            ('fd1', dots['f'], dots['d1'],Line,"#00FFFF"),
            ('fd2', dots['f'], dots['d2'],Line,"#00FFFF"),
            ('fdn1', dots['f'], dots['dn1'],Line,"#00FFFF"),
            ('fdn', dots['f'], dots['dn'],Line,"#00FFFF"),

        ]
        lines = {}
        for name,d1,d2,class_line,col in lines_data:
            l = class_line(d1.get_center(),d2.get_center(),color=col)
            lines[name] = l
        # 所有的圆弧定义
        arc_data = [
            ('ad1',dots['a'],2.24,0,50),
            ('d1d2', dots['d1'], 2.24, 0, 50),
            ('d2dn1', dots['d2'], 2.24, 0, 50),
            ('dn1dn', dots['dn1'], 2.24, 0, 50),
            ('bf',dots['b'],2.24,180,50),
        ]
        arcs = {}
        for name,d,r,start,angle in arc_data:
            arc = Arc(arc_center=d.get_center(),radius=r,start_angle=start*DEGREES,angle=angle*DEGREES)
            arcs[name] = arc
        theta = ValueTracker(0*DEGREES)
        arrow1 = Arrow(
            dots['a'],
            arcs['ad1'].get_start(),
            buff=0
        )
        arrow2 = Arrow(
            dots['b'],
            arcs['bf'].get_start(),
            buff=0
        )
        arrow1.add_updater(
            lambda l:l.set_angle(
                theta.get_value()
            )
        )
        arrow2.add_updater(
            lambda l: l.set_angle(
                theta.get_value()+180*DEGREES
            )
        )
        arcs['ad1'].add_updater(
            lambda arc:arc.become(
                Arc(
                    arc_center=dots['a'].get_center(),
                    radius=arrow1.get_length(),
                    start_angle=0*DEGREES,
                    angle=arrow1.get_angle()
                )
            )
        )
        arcs['bf'].add_updater(
            lambda arc: arc.become(
                Arc(
                    arc_center=dots['b'].get_center(),
                    radius=arrow2.get_length(),
                    start_angle=180 * DEGREES,
                    angle=theta.get_value()
                )
            )
        )
        brace = Brace(arrow1,direction=DOWN,buff=0.2)
        notes = [
            "分别过点A、B作两条平行的射线",              # 0
            "以任意长度为半径",                         # 1
            "$AD_1=BF$",                              # 2
            "$AD_1=D_1D_2=D_2D_{n-1}=D_{n-1}D_n=BF$", # 3
            "$BC_1=\\frac{1}{2}AB$",                  # 4
            "$BC_2=\\frac{1}{3}AB$",                  # 5
            "$BC_{n-1}=\\frac{1}{n}AB$",              # 6
            "$BC_n=\\frac{1}{n+1}AB$",                # 7

        ]
        notes_mob = VGroup(
            *[
                TextMobject(mob).scale(0.7) for mob in notes
            ]
        )
        notes_mob1 = VGroup(
            *[
                mob for mob in notes_mob[4:]
            ]
        )
        notes_mob1.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.4
        ).next_to(dots['c1'],direction=DOWN,buff=1.5)
        notes_data = [
            (0,dots['c1'],DOWN,2),
            (1,dots['c1'],DOWN,2),
            (2,dots['c1'],DOWN,2),
            (3,dots['c1'],DOWN,2),
            # (4, dots['c1'], DOWN, 2),
            # (5, dots['c1'], DOWN, 2.4),
            # (6, dots['c1'], DOWN, 2.8),
            # (7, dots['c1'], DOWN, 3.2),

        ]
        for i,target,dir,buff in notes_data:
            notes_mob[i].next_to(target,direction=dir,buff=buff)
        text = TextMobject("方法四").scale(1.1)\
                                    .set_color(YELLOW)
        l = Line(LEFT,RIGHT,color=YELLOW).next_to(text,direction=DOWN,buff=0.1)
# ----------------------以上为变量定义------------------------------------------
        self.camera.frame.scale(1.3)
        self.play(
            *[
                FadeInFrom(mob,UP) for mob in [text,l]
            ]
        )
        self.wait()
        self.play(
            *[
                FadeOutAndShiftDown(mob) for mob in [text,l]
            ]
        )
        self.wait()
        self.play(ShowCreation(lines['ab']))
        self.wait(1)
        for mob in [(dots['a'],tags_mob[0]),(dots['b'],tags_mob[1])]:
            self.play(
                ShowCreation(mob[0]),
                Write(mob[1])
            )
        self.play(Write(notes_mob[0]))
        self.wait()
        self.play(
            *[ShowCreation(l) for l in [lines['ad2'],lines['bf']]]
        )
        self.play(FadeOut(notes_mob[0]))
        self.play(
            ShowCreation(arrow1),
            ShowCreation(arrow2),
            ShowCreation(arcs['ad1']),
            ShowCreation(arcs['bf']),

        )
        self.play(Write(notes_mob[1]))
        self.wait()
        self.play(FadeOut(notes_mob[1]))
        self.wait()
        self.play(
            theta.increment_value,50*DEGREES
        )

        self.wait()
        self.play(
            ShowCreation(dots['d1']),
            ShowCreation(dots['f']),
            Write(tags_mob[10]),
            Write(tags_mob[6]),
            Write(notes_mob[2]),
            FadeOut(arcs['ad1']),
            FadeOut(arcs['bf']),
            FadeOut(arrow1),
            FadeOut(arrow2),

        )
        self.wait()

        self.play(CircleIndicate(dots['d1']))
        self.play(ShowCreation(arcs['d1d2']))
        self.wait(1)
        self.play(
            ShowCreation(dots['d2']),
            Write(tags_mob[7]),
            FadeOut(arcs['d1d2'])
        )
        self.wait()
        self.play(ShowCreation(lines['d2dn1']))
        self.wait(1)
        self.play(CircleIndicate(dots['d2']))
        self.play(ShowCreation(arcs['d2dn1']))
        self.wait(1)
        self.play(
            ShowCreation(dots['dn1']),
            Write(tags_mob[8]),
            FadeOut(arcs['d2dn1'])
        )
        self.wait()
        self.play(ShowCreation(lines['dn1dn']))
        self.wait(1)
        self.play(CircleIndicate(dots['dn1']))
        self.play(ShowCreation(arcs['dn1dn']))
        self.wait(1)
        self.play(
            ShowCreation(dots['dn']),
            Write(tags_mob[9]),
            FadeOut(arcs['dn1dn'])
        )
        self.wait()
        self.play(ReplacementTransform(notes_mob[2],notes_mob[3]))
        self.wait()
        self.play(FadeOut(notes_mob[3]))
        self.play(
            *[ShowCreation(l) for l in [lines['fd1'],lines['fd2'],lines['fdn1'],lines['fdn']]]
        )
        self.wait(1)
        self.play(
            *[
                ShowCreation(d) for d in [dots['c1'],dots['c2'],dots['cn1'],dots['cn']]
            ]
        )
        self.play(
            *[
                ShowCreation(tag) for tag in tags_mob[2:6]
            ]
        )
        self.wait()
        self.play(
            *[Write(note) for note in notes_mob1]
        )
class Scene5(GraphScene):

    def construct(self):
        dots_data = [
            ('a',-5,-2),        # 0
            ('b',5,-2),         # 1
            ('c0',-4,0),        # 2
            ('c1',-3,0),        # 3
            ('c2',-2,0),        # 4
            ('c3',-1,0),        # 5
            ('c4',0,0),         # 6
            ('c5',1,0),         # 7
            ('cn1',2,0),        # 8
            ('cn',3,0),         # 9
            ('cm',4,0),         # 10
            ('j',0,3),          # 11
            ('k',-3.33,-2),     # 12
            ('l',-1.67,-2),     # 13
            ('m',0,-2),         # 14
            ('n',1.67,-2),      # 15
            ('o',3.33,-2),      # 16
            ('p', -6, -3),      # 17
            ('q', -4, -3),      # 18
            ('r', -2, -3),      # 19
            ('s', 0, -3),       # 20
            ('t', 2, -3),       # 21
            ('u', 4, -3),       # 22
            ('v', 6, -3),       # 23
        ]
        dots = {}
        dots_mob = VGroup()
        for name,x,y in dots_data:
            d = Dot(radius=0.06).move_to(np.array([x,y,0]))
            dots[name] = d
            dots_mob.add(d)
        tex = [
            "A",    # 0
            "B",    # 1
            "C_1",    # 2
            "C_2",    # 3
            "C_3",    # 4
            "C_4",    # 5
            "C_5",    # 6
            "C_{n-1}",    # 7
            "C_n",    # 8
            "J",    # 9
            "K",    # 10
            "L",    # 11
            "M",    # 12
            "N",    # 13
            "O",    # 14
        ]
        tags_mob = VGroup(
            *[
                TexMobject(mob) for mob in tex
            ]
        )
        tag_data = [
            (0, dots['a'], 0.7, LEFT, 0.2),
            (1, dots['b'], 0.7, RIGHT, 0.2),
            (2, dots['c1'], 0.7, UL, 0.1),
            (3, dots['c2'], 0.7, DR, 0.1),
            (4, dots['c3'], 0.6, DR, 0.1),
            (5, dots['c4'], 0.6, DR, 0.1),
            (6, dots['c5'], 0.7, DR, 0.1),
            (7, dots['cn1'], 0.6, DR, 0.1),
            (8, dots['cn'], 0.7, UR, 0.1),
            (9, dots['j'], 0.7, LEFT, 0.1),
            (10, dots['k'], 0.7, DR, 0.1),
            (11, dots['l'], 0.7, DR, 0.1),
            (12, dots['m'], 0.7, DR, 0.1),
            (13, dots['n'], 0.7, DL, 0.1),
            (14, dots['o'], 0.7, DL, 0.1),

        ]
        for i,d,size,dir,buf in tag_data:
            tags_mob[i].scale(size)
            tags_mob[i].next_to(d,direction=dir,buff=buf)

        # 所有线的定义
        lines_data = [
            ('c0c5', dots['c0'], dots['c5'],Line,"#00FF00"),              # 0
            ('c5cn1', dots['c5'], dots['cn1'], DashedLine,"#00FF00"),     # 1
            ('cn1cm', dots['cn1'], dots['cm'], Line,"#00FF00"),           # 2
            ('ab', dots['a'], dots['b'],Line,"#FFA500"),                  # 3
            ('aj', dots['p'], dots['j'],Line,"#FFA500"),                  # 4
            ('kj', dots['q'], dots['j'],Line,"#FFA500"),                  # 5
            ('lj', dots['r'], dots['j'],Line,"#FFA500"),                  # 6
            ('mj', dots['s'], dots['j'],Line,"#FFA500"),                  # 7
            ('nj', dots['t'], dots['j'],Line,"#FFA500"),                  # 8
            ('oj', dots['u'], dots['j'],Line,"#FFA500"),                  # 9
            ('bj', dots['v'], dots['j'],Line,"#FFA500"),                  # 10
        ]
        lines = {}
        lines_mob = VGroup()
        for name, d1, d2,line_class,col in lines_data:
            l = line_class(d1.get_center(), d2.get_center(),color=col)
            lines[name] = l
            lines_mob.add(l)
        # 所有的圆弧定义
        arc_data = [
            ('c1c2', dots['c1'], 1, 30, -60),
            ('c2c3', dots['c2'], 1, 30, -60),
            ('c3c4', dots['c3'], 1, 30, -60),
            ('c4c5', dots['c4'], 1, 30, -60),
            ('c5cn1', dots['c5'], 1, 30, -60),
            ('cn1cn', dots['cn1'], 1, 30, -60),
        ]
        arcs = {}
        for name, d, r, start, angle in arc_data:
            arc = Arc(arc_center=d.get_center(), radius=r, start_angle=start * DEGREES, angle=angle * DEGREES)
            arcs[name] = arc
        theta = ValueTracker(30*DEGREES)
        arrow = Arrow(
            dots['c1'].get_center(),
            dots['c2'].get_center(),
            buff=0
        )
        arrow.add_updater(
            lambda mob:mob.set_angle(
                theta.get_value()
            )
        )
        arcs['c1c2'].add_updater(
            lambda mob:mob.become(
                Arc(
                    arc_center=dots['c1'].get_center(),
                    radius=arrow.get_length(),
                    start_angle=30*DEGREES,
                    angle=-(30*DEGREES-arrow.get_angle())
                )
            )
        )
        captions = [
            "作一条平行于AB的直线",              # 0
            "在直线上任取一点$C_1$",             # 1
            "以任意长度为半径",                  # 2
            "在直线上截取$n-1$段长度相等的线段",  # 3
            "K,L,M,N,......,O即为$n-1$等分点"   # 4
        ]
        captions_mob = VGroup(
            *[
                TextMobject(mob).scale(0.7)\
                                .to_edge(DOWN) for mob in captions
            ]
        )
        text = TextMobject("方法五").scale(0.8)\
                                    .set_color(YELLOW)
        l = Line(LEFT,RIGHT,color=YELLOW).next_to(text,DOWN,0.1)
#-----------------------------以上为变量定义--------------------------------------------------------------------
        self.play(
            *[
                FadeInFrom(mob,UP) for mob in [text,l]
            ]
        )
        self.wait()
        self.play(
            *[
                FadeOutAndShiftDown(mob) for mob in [text,l]
            ]
        )
        self.wait()
        self.play(
            ShowCreation(lines['ab'])
        )
        self.wait(1)
        self.play(
            ShowCreation(dots['a']),
            ShowCreation(dots['b']),
            Write(tags_mob[0]),
            Write(tags_mob[1]),
        )
        self.wait()
        self.play(Write(captions_mob[0]))
        self.wait()
        self.play(ShowCreation(lines['c0c5']))
        self.wait(1)
        self.play(ReplacementTransform(captions_mob[0],captions_mob[1]))
        self.wait()
        self.play(
            ShowCreation(dots['c1']),
            Write(tags_mob[2])
        )
        self.wait()
        self.play(CircleIndicate(dots['c1']))
        self.play(
            ShowCreation(arrow),
            ShowCreation(arcs['c1c2'])
        )
        self.play(ReplacementTransform(captions_mob[1],captions_mob[2]))

        self.wait()
        self.play(
            theta.increment_value,-60*DEGREES
        )
        self.wait()
        self.play(
            ShowCreation(dots['c2']),
            Write(tags_mob[3]),
            FadeOut(arcs['c1c2'],arrow),
            FadeOut(arrow)
        )
        self.wait()
        self.play(ReplacementTransform(captions_mob[2], captions_mob[3]))
        self.wait()
        self.play(CircleIndicate(dots['c2']))
        self.play(ShowCreation(arcs['c2c3']))
        self.wait(1)
        self.play(
            ShowCreation(dots['c3']),
            Write(tags_mob[4]),
            FadeOut(arcs['c2c3'])
        )
        self.wait()
        self.play(CircleIndicate(dots['c3']))
        self.play(ShowCreation(arcs['c3c4']))
        self.wait(1)
        self.play(
            ShowCreation(dots['c4']),
            Write(tags_mob[5]),
            FadeOut(arcs['c3c4'])
        )
        self.wait()
        self.play(CircleIndicate(dots['c4']))
        self.play(ShowCreation(arcs['c4c5']))
        self.wait(1)
        self.play(
            ShowCreation(dots['c5']),
            Write(tags_mob[6]),
            FadeOut(arcs['c4c5'])
        )
        self.wait()

        self.play(ShowCreation(lines['c5cn1']))
        self.wait()
        self.play(CircleIndicate(dots['c5']))
        self.play(ShowCreation(arcs['c5cn1']))
        self.wait(1)
        self.play(
            ShowCreation(dots['cn1']),
            Write(tags_mob[7]),
            FadeOut(arcs['c5cn1'])
        )
        self.wait()

        self.play(ShowCreation(lines['cn1cm']))
        self.wait()
        self.play(CircleIndicate(dots['cn1']))
        self.play(ShowCreation(arcs['cn1cn']))
        self.wait(1)
        self.play(
            ShowCreation(dots['cn']),
            Write(tags_mob[8]),
            FadeOut(arcs['cn1cn'])
        )
        self.play(FadeOut(captions_mob[3]))
        self.wait()

        self.play(
            *[ShowCreation(l) for l in [lines_mob[4],lines_mob[10]]]
        )
        self.wait(1)
        self.play(
            ShowCreation(dots['j']),
            Write(tags_mob[9])
        )
        self.wait()
        self.play(
            *[ShowCreation(l) for l in lines_mob[5:10]]
        )
        self.wait()
        self.play(
            *[ShowCreation(d) for d in dots_mob[12:17]]
        )
        self.wait()
        self.play(Write(tags_mob[10:]))
        self.wait()
        self.play(Write(captions_mob[-1]))
class Scene6(Scene):
    def construct(self):
        dot_data = [
            ('a',-5,-2),        # 0
            ('b', 5, -2),       # 1
            ('c', 5, 2),        # 2
            ('d', -5, 2),       # 3
            ('e1', 0, -2),      # 4
            ('e2', 1.67, -2),   # 5
            ('e3', 2.5, -2),    # 6
            ('e4', 3, -2),      # 7
            ('f1', 0, 0),       # 8
            ('f2', 1.67, -0.67),# 9
            ('f3', 2.5,-1),     # 10
            ('f4', 3, -1.2),    # 11
        ]
        dots = {}
        dot_mob = VGroup()
        for name,x,y in dot_data:
            d = Dot(radius=0.05).move_to(np.array([x,y,0]))
            dots[name] = d
            dot_mob.add(d)
        tex = [
            "A",    # 0
            "B",    # 1
            "C",    # 2
            "D",    # 3
            "E_1",  # 4
            "E_2",  # 5
            "E_3",  # 6
            "E_4",  # 7
            "F_1",  # 8
            "F_2",  # 9
            "F_3",  # 10
            "F_4",  # 11
        ]
        tags_mob = VGroup(
            *[
                TexMobject(mob) for mob in tex
            ]
        )
        tag_data = [
            (0, dots['a'], 0.7, DL, 0.1),       # 0
            (1, dots['b'], 0.7, DR, 0.1),       # 1
            (2, dots['c'], 0.7, UR, 0.1),       # 2
            (3, dots['d'], 0.7, UL, 0.1),       # 3
            (4, dots['e1'], 0.7, DOWN, 0.1),    # 4
            (5, dots['e2'], 0.7, DOWN, 0.1),    # 5
            (6, dots['e3'], 0.7, DOWN, 0.1),    # 6
            (7, dots['e4'], 0.7, DOWN, 0.1),    # 7
            (8, dots['f1'], 0.6, UP, 0.1),      # 8
            (9, dots['f2'], 0.6, UP, 0.1),      # 9
            (10, dots['f3'], 0.6, UP, 0.1),     # 10
            (11, dots['f4'], 0.6, UP, 0.1),     # 11
        ]
        for i, d, size, dir, buf in tag_data:
            tags_mob[i].scale(size)
            tags_mob[i].next_to(d, direction=dir, buff=buf)
        rectangle = Rectangle(height=4,width=10,color="#FF8C00")
        lines_data = [
            ('bd', dots['b'], dots['d'], Line,"#8A2BE2"),            # 0
            ('f1e1', dots['f1'], dots['e1'], DashedLine,"#00FFFF"),  # 1
            ('f2e2', dots['f2'], dots['e2'], DashedLine,"#00FFFF"),  # 2
            ('f3e3', dots['f3'], dots['e3'], DashedLine,"#00FFFF"),  # 3
            ('f4e4', dots['f4'], dots['e4'], DashedLine,"#00FFFF"),  # 4
            ('ca', dots['c'], dots['a'], Line,"#8A2BE2"),            # 5
            ('ce1', dots['c'], dots['e1'], Line,"#00FF00"),          # 6
            ('ce2', dots['c'], dots['e2'], Line,"#00FF00"),          # 7
            ('ce3', dots['c'], dots['e3'], Line,"#00FF00"),          # 8
            ('ce4', dots['c'], dots['e4'], Line,"#00FF00"),          # 9

        ]
        lines = {}
        lines_mob = VGroup()
        for name, d1, d2, line_class,col in lines_data:
            l = line_class(d1.get_center(), d2.get_center(),color=col)
            lines[name] = l
            lines_mob.add(l)
        captions = [
            "画一个矩形",
        ]
        captions_mob = VGroup(
            *[TextMobject(mob).scale(0.7)\
                              .to_edge(DOWN) for mob in captions
            ]
        )
        notes = [
            "\\frac{1}{2}",
            "\\frac{1}{3}",
            "\\frac{1}{4}",
            "\\frac{1}{5}",
        ]
        notes_mob = VGroup(
            *[
                TexMobject(mob).scale(0.8)\
                               .next_to(target,direction=DOWN,buff=0.3) for mob,target in zip(notes,tags_mob[4:8])
            ]
        )
        other = TexMobject("......").scale(0.7)\
                                    .next_to(tags_mob[7],direction=RIGHT,buff=0.2)
        other1 = other.deepcopy().next_to(notes_mob[-1],direction=RIGHT,buff=0.2)
        text = TextMobject("方法六").scale(0.8)\
                                    .set_color(YELLOW)
        l = Line(LEFT,RIGHT,color=YELLOW).next_to(text,DOWN,0.1)
        self.play(
            *[FadeInFrom(mob,UP) for mob in [text,l]]
        )
        self.wait()
        self.play(
            *[FadeOutAndShiftDown(mob) for mob in [text,l]]
        )
        self.wait()
        self.play(ShowCreationThenFadeOut(captions_mob[0],run_time=3),
                  ShowCreation(rectangle)
        )
        self.wait(1)
        self.play(
            *[Write(tag) for tag in tags_mob[:4]]
        )
        self.wait()

        self.play(ShowCreation(lines['bd']))
        self.wait()

        for l1,l2,d1,d2,f,e in zip(lines_mob[5:],lines_mob[1:5],dot_mob[8:],dot_mob[4:8],tags_mob[8:],tags_mob[4:8]):
            self.play(ShowCreation(l1))
            self.wait(1)
            self.play(
                ShowCreation(d1),
                Write(f)
            )
            self.wait()
            self.play(ShowCreation(l2))
            self.wait(1)
            self.play(
                ShowCreation(d2),
                Write(e)
            )
            self.wait()
        self.play(Write(other))
        self.wait()
        self.play(
            FadeInFrom(notes_mob,UP),
            Write(other1)
        )
        self.wait()

class Scene7(MovingCameraScene):
    def construct(self):
        self.camera.frame.scale(1.6)
        dot_data = [
            ('a', -4, -2),      # 0
            ('b', 4, -2),       # 1
            ('c', 4, 6),        # 2
            ('c1', 4, 3.66),    # 3
            ('c2', 4, 2.62),    # 4
            ('c3', 4, 2),       # 5
            ('c4',4,1.58),      # 6
            ('d1', 0, 2),       # 7
            ('d2', 1.33, 1.77), # 8
            ('d3', 2, 1.46),    # 9
            ('d4', 2.4, 1.2),   # 10
            ('f1', 0, -2),      # 11
            ('f2', 1.33, -2),   # 12
            ('f3', 2, -2),      # 13
            ('f4', 2.4, -2),    # 14

        ]
        dots = {}
        dots_mob = VGroup()
        for name, x, y in dot_data:
            d = Dot(radius=0.08).move_to(np.array([x, y, 0]))
            dots[name] = d
            dots_mob.add(d)
        tex = [
            "A",    # 0
            "B",    # 1
            "C",    # 2
            "C_1",  # 3
            "C_2",  # 4
            "C_3",  # 5
            "C_4",  # 6
            "F_1",  # 7
            "F_2",  # 8
            "F_3",  # 9
            "F_4",  # 10
        ]
        tags_mob = VGroup(
            *[
                TexMobject(mob) for mob in tex
            ]
        )
        tag_data = [
            (0, dots['a'], 0.9, DL, 0.1),       # 0
            (1, dots['b'], 0.9, DR, 0.1),       # 1
            (2, dots['c'], 0.9, RIGHT, 0.1),    # 2
            (3, dots['c1'], 0.9, RIGHT, 0.1),   # 3
            (4, dots['c2'], 0.9, RIGHT, 0.1),   # 4
            (5, dots['c3'], 0.9, RIGHT, 0.1),   # 5
            (6, dots['c4'], 0.9, RIGHT, 0.1),   # 6
            (7, dots['f1'], 0.9, DOWN, 0.1),    # 7
            (8, dots['f2'], 0.9, DOWN, 0.1),    # 8
            (9, dots['f3'], 0.9, DOWN, 0.1),    # 9
            (10, dots['f4'], 0.9, DOWN, 0.1),    # 10

        ]
        for i, d, size, dir, buf in tag_data:
            tags_mob[i].scale(size)
            tags_mob[i].next_to(d, direction=dir, buff=buf)
        lines_data = [
            ('ab', dots['a'], dots['b'], Line,"#0066CC"),             # 0
            ('bc', dots['b'], dots['c'], Line,"#99CC33"),             # 1
            ('ac', dots['a'], dots['c'], Line,"#33CC99"),             # 2
            ('ac1', dots['a'], dots['c1'], Line,"#33CC99"),           # 3
            ('ac2', dots['a'], dots['c2'], Line,"#33CC99"),           # 4
            ('ac3', dots['a'], dots['c3'], Line,"#33CC99"),           # 5
            ('ac4', dots['a'], dots['c4'], Line,"#33CC99"),           # 6
            ('d1f1', dots['d1'], dots['f1'], DashedLine,"#FF33CC"),   # 7
            ('d2f2', dots['d2'], dots['f2'], DashedLine,"#FF33CC"),   # 8
            ('d3f3', dots['d3'], dots['f3'], DashedLine,"#FF33CC"),   # 9
            ('d4f4', dots['d4'], dots['f4'], DashedLine,"#FF33CC"),   # 10

        ]
        lines = {}
        lines_mob = VGroup()
        for name, d1, d2, line_class,col in lines_data:
            l = line_class(d1.get_center(), d2.get_center(),color=col)
            lines[name] = l
            lines_mob.add(l)
        # 所有的圆弧定义
        arc_data = [
            ('ab', dots['a'], dots['b'], -180,"#FF6666"),
            ('d1c1', dots['d1'],dots['c1'],-45,"#CCFF99"),
            ('d2c2', dots['d2'], dots['c2'], -35.26,"#66CC66"),
            ('d3c3', dots['d3'], dots['c3'], -30,"#99CC66"),
            ('d4c4', dots['d4'], dots['c4'], -26.57,"#006600"),

        ]
        arcs = {}
        arcs_mob = VGroup()
        for name, d1, d2, angle,col in arc_data:
            arc = ArcBetweenPoints(d1.get_center(),d2.get_center(),angle=angle*DEGREES,color=col)
            arcs[name] = arc
            arcs_mob.add(arc)
        arrows_data = [
            ('bd1',dots['b'],dots['d1']),
            ('bd2',dots['b'],dots['d2']),
            ('bd3', dots['b'], dots['d3']),
            ('bd4', dots['b'], dots['d4']),
        ]
        arrows_mob = VGroup()
        for name,d1,d2 in arrows_data:
            arrow = Arrow(d1.get_center(),d2.get_center(),buff=0)
            arrows_mob.add(arrow)
        theta = ValueTracker(180*DEGREES)
        arrow_ab = Arrow(
            dots['f1'].get_center(),
            dots['a'].get_center(),
            buff=0
        )
        arrow_ab.add_updater(
            lambda l:l.set_angle(
                theta.get_value()
            )
        )
        arcs['ab'].add_updater(
            lambda arc:arc.become(
                Arc(
                    arc_center=dots['f1'].get_center(),
                    radius=arrow_ab.get_length(),
                    start_angle=180*DEGREES,
                    angle=theta.get_value()-180*DEGREES
                )
            )
        )
        captions = [
            "以AB为直径作半圆",
            "AB=BC,且AB垂直BC于点B",
        ]
        captions_mob = VGroup(
            *[
                TextMobject(mob).scale(0.9)\
                                .to_edge(DOWN) for mob in captions
            ]
        )
        notes = [
            "BF_1=\\frac{1}{2}AB",
            "BF_2=\\frac{1}{3}AB",
            "BF_3=\\frac{1}{4}AB",
            "BF_4=\\frac{1}{5}AB",
            "......"
        ]
        notes_mob = VGroup(
            *[
                TexMobject(mob).scale(0.9) for mob in notes
            ]
        )
        notes_mob.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.4
        ).next_to(lines['bc'],direction=RIGHT,buff=1.5)
        text = TextMobject("方法七").scale(1.4)\
                                    .set_color(YELLOW)
        l = Line(1.3*LEFT,1.3*RIGHT,color=YELLOW).next_to(text,DOWN,0.1)
        self.play(
            *[FadeInFrom(mob,UP) for mob in [text,l]]
        )
        self.wait()
        self.play(
            *[
                FadeOutAndShiftDown(mob) for mob in [text,l]
            ]
        )
        self.wait()
        self.play(Write(captions_mob[0]))
        self.play(
            ShowCreation(lines['ab']),
            ShowCreation(dots['a']),
            ShowCreation(dots['b']),
            Write(tags_mob[0]),
            Write(tags_mob[1]),

        )
        self.wait(1)
        self.play(CircleIndicate(dots['f1']))
        self.play(
            ShowCreation(arrow_ab),
            ShowCreation(arcs['ab'])
        )
        self.play(
            theta.increment_value,-180*DEGREES
        )
        arcs['ab'].clear_updaters()
        self.wait()
        self.play(FadeOut(arrow_ab))
        self.wait()
        self.play(ShowCreation(lines['bc']))
        self.wait(1)
        self.play(
            ShowCreation(dots['c']),
            Write(tags_mob[2])
        )
        self.wait()
        self.play(ReplacementTransform(captions_mob[0],captions_mob[1]))
        self.wait()
        self.play(FadeOutAndShift(captions_mob[1],DOWN))
        for l1,l2,arc,d,f,c,tagf,tagc,arrow in zip(lines_mob[2:7],lines_mob[7:],arcs_mob[1:],dots_mob[7:11],dots_mob[11:],dots_mob[3:7],tags_mob[7:],tags_mob[3:7],arrows_mob):
            self.play(ShowCreation(l1))
            self.wait(1)
            self.play(ShowCreation(d))
            self.wait()
            self.play(ShowCreation(l2))
            self.wait(1)
            self.play(
                ShowCreation(f),
                Write(tagf)
            )
            self.wait()
            self.play(CircleIndicate(dots['b']))
            self.play(ShowCreation(arc))
            self.wait(1)
            self.play(ShowCreationThenFadeOut(arrow,run_time=3))
            self.play(
                ShowCreation(c),
                Write(tagc)
            )
            self.wait()
        self.play(Write(notes_mob))
        self.wait()

class Scene8(Scene):
    def construct(self):
        dot_data = [
            ('a', -5, -2),          # 0
            ('b', 5, -2),            # 1
            ('c', 3, 3),            # 2
            ('d', -1.8, 0),         # 3
            ('e', 4.2, 0),          # 4
            ('f1', 0.75, -0.75),    # 5
            ('f2', -0.82, -1.09),   # 6
            ('f3', -1.71, -1.29),   # 7
            ('f4', -2.29, -1.41),   # 8
            ('g1', 0, -2),          # 9
            ('g2', -1.67, -2),      # 10
            ('g3', -2.5, -2),       # 11
            ('g4', -3, -2),         # 12
        ]
        dots = {}
        dots_mob = VGroup()
        for name, x, y in dot_data:
            d = Dot(radius=0.05).move_to(np.array([x, y, 0]))
            dots[name] = d
            dots_mob.add(d)
        tex = [
            "A",    # 0
            "B",    # 1
            "C",    # 2
            "D",    # 3
            "E",    # 4
            "G_1",  # 5
            "G_2",  # 6
            "G_3",  # 7
            "G_4",  # 8
        ]
        tags_mob = VGroup(
            *[
                TexMobject(mob) for mob in tex
            ]
        )
        tag_data = [
            (0, dots['a'], 0.7, DL, 0.1),       # 0
            (1, dots['b'], 0.7, DR, 0.1),       # 1
            (2, dots['c'], 0.7, RIGHT, 0.1),    # 2
            (3, dots['d'], 0.7, UL, 0.1),       # 3
            (4, dots['e'], 0.7, UR, 0.1),       # 4
            (5, dots['g1'], 0.7, DOWN, 0.1),    # 5
            (6, dots['g2'], 0.7, DOWN, 0.1),    # 6
            (7, dots['g3'], 0.7, DOWN, 0.1),    # 7
            (8, dots['g4'], 0.7, DOWN, 0.1),    # 8
        ]
        for i, d, size, dir, buf in tag_data:
            tags_mob[i].scale(size)
            tags_mob[i].next_to(d, direction=dir, buff=buf)
        lines_data = [
            ('ab', dots['a'], dots['b'], Line,"#99CC00"),         # 0
            ('bc', dots['b'], dots['c'], Line,"#FFCC00"),         # 1
            ('ac', dots['a'], dots['c'], Line,"#FF9900"),         # 2
            ('ae', dots['a'], dots['e'], Line,"#00CC00"),         # 3
            ('de', dots['d'], dots['e'], Line,"#6666CC"),         # 4
            ('db', dots['d'], dots['b'], Line,"#990066"),         # 5
            ('dg1', dots['d'], dots['g1'], Line,"#6699FF"),       # 6
            ('dg2', dots['d'], dots['g2'], Line,"#6699FF"),       # 7
            ('dg3', dots['d'], dots['g3'], Line,"#6699FF"),       # 8
            ('cg1', dots['c'], dots['g1'], DashedLine,"#9933CC"), # 9
            ('cg2', dots['c'], dots['g2'], DashedLine,"#9933CC"), # 10
            ('cg3', dots['c'], dots['g3'], DashedLine,"#9933CC"), # 11
            ('cg4', dots['c'], dots['g4'], DashedLine,"#9933CC"), # 12
        ]
        lines = {}
        lines_mob = VGroup()
        for name, d1, d2, line_class,col in lines_data:
            l = line_class(d1.get_center(), d2.get_center(),color=col)
            lines[name] = l
            lines_mob.add(l)
        captions = [
            "画一个三角形",
            "DE平行于AB",
        ]
        captions_mob = VGroup(
            *[
                TextMobject(mob).scale(0.7)\
                                .to_edge(DOWN) for mob in captions
            ]
        )
        notes = [
            "\\frac{1}{2}",
            "\\frac{1}{3}",
            "\\frac{1}{4}",
            "\\frac{1}{5}",
        ]
        notes_mob = VGroup(
            *[
                TexMobject(mob).scale(0.8)\
                               .next_to(target,direction=DOWN,buff=0.5) for mob,target in zip(notes,tags_mob[5:])
            ]
        )
        other = TexMobject("......").next_to(tags_mob[-1],direction=LEFT,buff=0.3)
        other1 = other.deepcopy()\
                      .next_to(notes_mob[-1],direction=LEFT,buff=0.3)
        text = TextMobject("方法八").scale(0.8)\
                                    .set_color(YELLOW)
        l = Line(LEFT,RIGHT,color=YELLOW).next_to(text,DOWN,0.1)
        self.play(
            *[FadeInFrom(mob,UP) for mob in [text,l]]
        )
        self.wait()
        self.play(
            *[FadeOutAndShiftDown(mob) for mob in [text,l]]
        )
        self.wait()
        self.play(Write(captions_mob[0]))
        self.wait()
        self.play(
            *[ShowCreation(l) for l in lines_mob[:3]]
        )
        self.wait()
        self.play(
            *[ShowCreation(d) for d in dots_mob[:3]]
        )
        self.play(
            *[Write(t) for t in tags_mob[:3]]
        )
        self.wait()
        self.play(ShowCreation(lines['de']))
        self.wait(1)
        self.play(
            ShowCreation(dots['d']),
            ShowCreation(dots['e']),
            Write(tags_mob[3]),
            Write(tags_mob[4]),
        )
        self.wait()
        self.play(ReplacementTransform(captions_mob[0],captions_mob[1]))
        self.wait()
        self.play(
            ShowCreation(lines['ae']),
            FadeOut(captions_mob[1])
        )
        self.wait(1)
        for l1,l2,d1,d2,t in zip(lines_mob[5:9],lines_mob[9:],dots_mob[5:9],dots_mob[9:],tags_mob[5:]):
            self.play(ShowCreation(l1))
            self.wait(1)
            self.play(ShowCreation(d1))
            self.wait()
            self.play(ShowCreation(l2))
            self.wait(1)
            self.play(
                ShowCreation(d2),
                Write(t)
            )
            self.wait()
        self.play(
            FadeInFrom(notes_mob,UP),
            Write(other),
            Write(other1)
        )
        self.wait()
class Scene9(MovingCameraScene):
    def construct(self):
        dot_data = [
            ('a', -6, -2),          # 0
            ('b', 6, -2),           # 1
            ('c', 0, -2),           # 2
            ('d', -3.8, -0.53),     # 3
            ('d1', -1.6, 0.93),     # 4
            ('d2', 0.6, 2.4),       # 5
            ('dn1', 2.8, 3.87),     # 6
            ('dn', 5.01, 5.34),     # 7
            ('e', -4.9, -1.27),     # 8
            ('f', -1.27, -1.51),    # 9
            ('g', 0.56, -1.18),     # 10
            ('h', 1.99, -0.93),     # 11
            ('i', -5.51, -2.27),    # 12
            ('j', -4, -2),          # 13
        ]
        dots = {}
        dots_mob = VGroup()
        for name, x, y in dot_data:
            d = Dot(radius=0.08).move_to(np.array([x, y, 0]))
            dots[name] = d
            dots_mob.add(d)
        tex = [
            "A",        # 0
            "B",        # 1
            "C",        # 2
            "D",        # 3
            "D_1",      # 4
            "D_2",      # 5
            "D_{n-1}",  # 6
            "D_n",      # 7
            "E",        # 8
            "F",        # 9
            "G",        # 10
            "J",        # 11
        ]
        tags_mob = VGroup(
            *[
                TexMobject(mob) for mob in tex
            ]
        )
        tag_data = [
            (0, dots['a'], 0.9, DL, 0.1),   # 0
            (1, dots['b'], 0.9, DR, 0.1),   # 1
            (2, dots['c'], 0.9, DOWN, 0.1), # 2
            (3, dots['d'], 0.9, LEFT, 0.1), # 3
            (4, dots['d1'], 0.9, UL, 0.1),  # 4
            (5, dots['d2'], 0.9, UL, 0.1),  # 5
            (6, dots['dn1'], 0.9, UL, 0.1), # 6
            (7, dots['dn'], 0.9, UL, 0.1),  # 7
            (8, dots['e'], 0.9, UL, 0.1),   # 8
            (9, dots['f'], 0.9, UP, 0.1),   # 9
            (10, dots['g'], 0.9, UP, 0.1),  # 10
            (11, dots['j'], 0.9, DOWN, 0.1),# 11
        ]
        for i, d, size, dir, buf in tag_data:
            tags_mob[i].scale(size)
            tags_mob[i].next_to(d, direction=dir, buff=buf)
        lines_data = [
            ('ab', dots['a'], dots['b'], Line,"#0066CC"),         # 0
            ('ad', dots['a'], dots['d'], Line,"#99CC33"),         # 1
            ('dd2', dots['d'], dots['d2'], Line,"#99CC33"),       # 2
            ('d2dn1', dots['d2'], dots['dn1'], DashedLine,"#99CC33"),   # 3
            ('dn1dn', dots['dn1'], dots['dn'], Line,"#99CC33"),   # 4
            ('be', dots['b'], dots['e'], Line,"#FFCC33"),         # 5
            ('cd', dots['c'], dots['d'], Line,"#FF0033"),         # 6
            ('bd', dots['b'], dots['d'], Line,"#99CC00"),         # 7
            ('cdn', dots['c'], dots['dn'], Line,"#FF6600"),       # 8
            ('hi', dots['h'], dots['i'], DashedLine,"#66CC99"),   # 9
        ]
        lines = {}
        lines_mob = VGroup()
        for name, d1, d2, line_class,col in lines_data:
            l = line_class(d1.get_center(), d2.get_center(),color=col)
            lines[name] = l
            lines_mob.add(l)

        arc_data = [
            ('dd1', dots['d'], 0, 68),
            ('d1d2', dots['d1'], 0, 68),
            ('d2dn1', dots['d2'], 0, 68),
            ('dn1dn', dots['dn1'], 0, 68),
        ]
        arcs = {}
        arcs_mob = VGroup()
        for name, d,start_angle,angle in arc_data:
            arc = Arc(arc_center=d.get_center(),radius=2.65, start_angle=start_angle*DEGREES,angle=angle * DEGREES)
            arcs[name] = arc
            arcs_mob.add(arc)
        theta = ValueTracker(0*DEGREES)
        arrow = Arrow(
            dots['d'].get_center(),
            arcs['dd1'].get_start(),
            buff=0
        )
        arrow.add_updater(
            lambda mob:mob.set_angle(
                theta.get_value()
            )
        )
        arcs['dd1'].add_updater(
            lambda mob:mob.become(
                Arc(
                    arc_center=dots['d'].get_center(),
                    radius=arrow.get_length(),
                    start_angle=0*DEGREES,
                    angle=arrow.get_angle()
                )
            )
        )
        captions = [
            "过A点作一条射线",
            "在射线上任取一点",
            "$DD_n=nAD$",
            "C、E分别是AB、AD的中点",
            "则$AJ=\\frac{1}{n+2}AB$"
        ]
        captions_mob = VGroup(
            *[
                TextMobject(mob).scale(0.9)\
                                .to_edge(DOWN) for mob in captions
            ]
        )
        text = TextMobject("方法九").scale(1.3)\
                                    .set_color(YELLOW)
        l = Line(1.2*LEFT,1.2*RIGHT,color=YELLOW).next_to(text,DOWN,0.1)
        self.camera.frame.scale(1.5)
        self.play(
            *[FadeInFrom(mob,UP) for mob in [text,l]]
        )
        self.wait()
        self.play(
            *[FadeOutAndShiftDown(mob) for mob in [text,l]]
        )
        self.wait()
        self.play(ShowCreation(lines['ab']))
        self.wait(1)
        self.play(
            ShowCreation(dots['a']),
            ShowCreation(dots['b']),
            Write(tags_mob[0]),
            Write(tags_mob[1]),
        )
        self.wait()
        self.play(Write(captions_mob[0]))
        self.wait()
        self.play(ShowCreation(lines['ad']))
        self.wait()
        self.play(ReplacementTransform(captions_mob[0], captions_mob[1]))
        self.wait(1)
        self.play(
            ShowCreation(dots['d']),
            Write(tags_mob[3]),
            FadeOut(captions_mob[1])
        )
        self.wait()
        self.play(ShowCreation(lines['dd2']))
        self.wait()

        self.play(
            ShowCreation(arrow),
            ShowCreation(arcs['dd1'])
        )
        self.play(
            theta.increment_value,68*DEGREES
        )
        self.play(
            ShowCreation(dots['d1']),
            Write(tags_mob[4]),
            FadeOut(arcs['dd1']),
            FadeOut(arrow)
        )
        self.wait()
        self.play(CircleIndicate(dots['d1']))
        self.play(ShowCreation(arcs['d1d2']))
        self.wait(1)
        self.play(
            ShowCreation(dots['d2']),
            Write(tags_mob[5]),
            FadeOut(arcs['d1d2'])
        )
        self.wait()
        self.play(ShowCreation(lines['d2dn1']))
        self.wait()
        self.play(CircleIndicate(dots['d2']))
        self.play(ShowCreation(arcs['d2dn1']))
        self.wait(1)
        self.play(
            ShowCreation(dots['dn1']),
            Write(tags_mob[6]),
            FadeOut(arcs['d2dn1'])
        )
        self.wait()
        self.play(ShowCreation(lines['dn1dn']))
        self.wait()
        self.play(CircleIndicate(dots['dn1']))
        self.play(ShowCreation(arcs['dn1dn']))
        self.wait(1)
        self.play(
            ShowCreation(dots['dn']),
            Write(tags_mob[7]),
            FadeOut(arcs['dn1dn'])
        )
        self.wait()
        self.play(Write(captions_mob[2]))
        self.wait()
        self.play(
            ShowCreation(dots['e']),
            Write(tags_mob[8]),
            ShowCreation(dots['c']),
            Write(tags_mob[2])
        )
        self.wait()
        self.play(ReplacementTransform(captions_mob[2], captions_mob[3]))
        self.wait()
        self.play(
            ShowCreation(lines['be']),
            ShowCreation(lines['cd']),
        )
        self.wait(1)
        self.play(
            ShowCreation(dots['f']),
            Write(tags_mob[9])
        )
        self.wait()
        self.play(
            ShowCreation(lines['bd']),
            ShowCreation(lines['cdn'])
        )
        self.wait(1)
        self.play(
            ShowCreation(dots['g']),
            Write(tags_mob[10])
        )
        self.wait()
        self.play(ShowCreation(lines['hi']))
        self.wait(1)
        self.play(
            ShowCreation(dots['j']),
            Write(tags_mob[11])
        )
        self.wait()
        self.play(ReplacementTransform(captions_mob[3],captions_mob[4]))
        self.wait()
class Scene10(MovingCameraScene):
    def construct(self):
        dot_data = [
            ('a', -7, -2),      # 0
            ('b', -3, -2),      # 1
            ('b1', 1, -2),      # 2
            ('b2', 5, -2),      # 3
            ('bn1', 9, -2),     # 4
            ('bn', 13, -2),     # 5
            ('c', -3, 2),       # 6
            ('d1', -5, -2),     # 7
            ('d2', -4.33, -2),  # 8
            ('d3', -4, -2),     # 9
            ('h', 1, 0),        # 10
            ('i', 1, 0.67),     # 11
            ('j', 1, 1),        # 12
            ('e', 1, 4),        # 13

        ]
        dots = {}
        dots_mob = VGroup()
        for name, x, y in dot_data:
            d = Dot(radius=0.1).move_to(np.array([x, y, 0]))
            dots[name] = d
            dots_mob.add(d)
        tex = [
            "A",        # 0
            "B",        # 1
            "B_1",      # 2
            "B_2",      # 3
            "B_{n-1}",  # 4
            "B_n",      # 5
            "C",        # 6
            "D_2",      # 7
            "D_{n-1}",  # 8
            "D_n",      # 9
            "H",        # 10
            "I",        # 11
            "J",        # 12
        ]
        tags_mob = VGroup(
            *[
                TexMobject(mob) for mob in tex
            ]
        )
        tag_data = [
            (0, dots['a'], 0.9, DOWN, 0.1),     # 0
            (1, dots['b'], 0.9, DOWN, 0.1),     # 1
            (2, dots['b1'], 0.9, DOWN, 0.1),    # 2
            (3, dots['b2'], 0.9, DOWN, 0.1),    # 3
            (4, dots['bn1'], 0.9, DOWN, 0.1),   # 4
            (5, dots['bn'], 0.9, DOWN, 0.1),    # 5
            (6, dots['c'], 0.9, UP, 0.1),       # 6
            (7, dots['d1'], 0.9, DL, 0.1),      # 7
            (8, dots['d2'], 0.9, UP, 0.1),      # 8
            (9, dots['d3'], 0.9, UR, 0.1),      # 9
            (10, dots['h'], 0.9, RIGHT, 0.1),   # 10
            (11, dots['i'], 0.9, LEFT, 0.1),      # 11
            (12, dots['j'], 0.9, UL, 0.1),      # 12

        ]
        for i, d, size, dir, buf in tag_data:
            tags_mob[i].scale(size)
            tags_mob[i].next_to(d, direction=dir, buff=buf)
        lines_data = [
            ('ab', dots['a'], dots['b'], Line,"#FFCC33"),             # 0
            ('bc', dots['b'], dots['c'], Line,"#FFCC33"),             # 1
            ('bb2', dots['b'], dots['b2'], Line,"#FFCC33"),           # 2
            ('b2bn1', dots['b2'], dots['bn1'], DashedLine,"#FFCC33"), # 3
            ('bn1bn', dots['bn1'], dots['bn'], Line,"#FFCC33"),       # 4
            ('b1e', dots['b1'], dots['e'], Line,"#FF0033"),           # 5
            ('b2c', dots['b2'], dots['c'], Line,"#99CC33"),           # 6
            ('bn1c', dots['bn1'], dots['c'], Line,"#99CC33"),         # 7
            ('bnc', dots['bn'], dots['c'], Line,"#99CC33"),           # 8
        ]
        lines = {}
        lines_mob = VGroup()
        for name, d1, d2, line_class,col in lines_data:
            l = line_class(d1.get_center(), d2.get_center(),stroke_width=2,color=col)
            lines[name] = l
            lines_mob.add(l)
        arc_data = [
            ('bb1', dots['b'], 4, 20, -40,"#CC3333"),
            ('b1b2', dots['b1'], 4, 20, -40,"#CC3333"),
            ('b2bn1', dots['b2'], 4, 20, -40,"#CC3333"),
            ('bn1bn', dots['bn1'], 4, 20, -40,"#CC3333"),
            ('hd1', dots['c'], 4.47, -8, -130,"#0099FF"),
            ('id2', dots['c'], 4.22, -8, -130,"#CCFF66"),
            ('fd3', dots['c'], 4.12, -8, -130,"#6699FF"),
        ]
        arcs = {}
        arcs_mob = VGroup()
        for name, d, r, start_angle, angle,col in arc_data:
            arc = Arc(arc_center=d.get_center(),
                      radius=r,
                      start_angle=start_angle * DEGREES,
                      angle=angle * DEGREES,
                      stroke_width=2,
                      color=col
            )
            arcs[name] = arc
            arcs_mob.add(arc)
        theta = ValueTracker(-8*DEGREES)
        arrows_data = [
            (dots['c'],arcs['hd1'].get_start()),
            (dots['c'], arcs['id2'].get_start()),
            (dots['c'], arcs['fd3'].get_start()),
        ]
        arrows_mob = VGroup()
        for start,end in arrows_data:
            arrow = Arrow(start.get_center(),end,buff=0,stroke_width=2)
            arrows_mob.add(arrow)
        def update_arrow(mob):
            mob.set_angle(theta.get_value())

        for arrow in arrows_mob:
            arrow.add_updater(update_arrow)
        col = ["#0099FF","#CCFF66","#6699FF"]
        for arc,arrow,color in zip(arcs_mob[4:],arrows_mob,col):
            arc.add_updater(
                lambda mob:mob.become(
                    Arc(
                        arc_center=dots['c'].get_center(),
                        radius=arrow.get_length(),
                        start_angle=-8*DEGREES,
                        angle=theta.get_value()+8*DEGREES,
                        stroke_width=2,
                        color=color
                    )
                )
            )

        rec1 = Rectangle(height=0.25, width=0.25, fill_color=YELLOW, fill_opacity=0.5, stroke_opacity=0) \
            .move_to(dots['b'].get_center()) \
            .shift(0.125 * RIGHT) \
            .shift(0.125 * UP)
        rec2 = Rectangle(height=0.25, width=0.25, fill_color=YELLOW, fill_opacity=0.5, stroke_opacity=0) \
            .move_to(dots['b1'].get_center()) \
            .shift(0.125 * RIGHT) \
            .shift(0.125 * UP)
        captions = [
            "$AB=BC$",
            "$AB=BB_1=B_1B_2=B_2B_{n-1}=B_{n-1}B_n$",
            "$D_2$",
            "......",
            "$D_{n-1}$",
            "$D_n$",
            "$\\frac{1}{2}$",
            "......",
            "$\\frac{1}{n-1}$",
            "$\\frac{1}{n}$",

        ]
        captions_mob = VGroup(
            VGroup(
                *[
                    TextMobject(mob).scale(1.3) \
                        .shift(4*DOWN) for mob in captions[:2]
                ]
            ),
            VGroup(
                *[
                    TextMobject(mob).scale(1.3) for mob in captions[2:6]
                ]
            ).arrange(
                RIGHT,
                aligned_edge=DOWN,
                buff=0.8
            ),
            VGroup(
                *[
                    TextMobject(mob).scale(1.3) for mob in captions[6:]
                ]
            )

        )

        captions_mob[1].shift(4*DOWN)
        # captions_mob[2].next_to(captions_mob[1],direction=DOWN,buff=0.3)
        for i in range(4):
            captions_mob[2][i].next_to(captions_mob[1][i],direction=DOWN,buff=1)
        captions_mob[2][1].shift(0.4*DOWN)
        text = TextMobject("方法十").scale(1.8)\
                                    .set_color(YELLOW)
        l = Line(1.7*LEFT,1.7*RIGHT,color=YELLOW).next_to(text,DOWN,0.1)

        self.camera.frame.scale(2)
        self.play(
            *[
                FadeInFrom(mob,UP) for mob in [text,l]
            ]
        )
        self.wait()
        self.play(
            *[
                FadeOutAndShiftDown(mob) for mob in [text,l]
            ]
        )
        self.wait()
        self.play(ShowCreation(lines['ab']))
        self.wait(1)
        self.play(
            ShowCreation(dots['a']),
            ShowCreation(dots['b']),
            Write(tags_mob[0]),
            Write(tags_mob[1]),
        )
        self.wait()
        self.play(ShowCreation(lines['bc']))
        self.wait(1)
        self.play(
            ShowCreation(dots['c']),
            Write(tags_mob[6]),
            Write(captions_mob[0][0])
        )
        self.wait()
        self.play(ShowCreation(lines['bb2']))
        self.wait(1)
        self.play(ShowCreation(rec1))
        self.play(ShowCreation(arcs['bb1']))
        self.wait(1)
        self.play(
            ShowCreation(dots['b1']),
            Write(tags_mob[2]),
            FadeOut(arcs['bb1'])
        )
        self.wait()
        self.play(ShowCreation(arcs['b1b2']))
        self.wait(1)
        self.play(
            ShowCreation(dots['b2']),
            Write(tags_mob[3]),
            FadeOut(arcs['b1b2'])
        )
        self.wait()
        self.play(ShowCreation(lines['b2bn1']))
        self.wait()
        self.play(ShowCreation(arcs['b2bn1']))
        self.wait(1)
        self.play(
            ShowCreation(dots['bn1']),
            Write(tags_mob[4]),
            FadeOut(arcs['b2bn1'])
        )
        self.wait()
        self.play(ShowCreation(lines['bn1bn']))
        self.wait()
        self.play(ShowCreation(arcs['bn1bn']))
        self.wait(1)
        self.play(
            ShowCreation(dots['bn']),
            Write(tags_mob[5]),
            ReplacementTransform(captions_mob[0][0],captions_mob[0][1]),
            FadeOut(arcs['bn1bn'])
        )
        self.wait()
        self.play(ShowCreation(lines['b1e']),FadeOut(captions_mob[0][1]))
        self.wait(1)
        self.play(ShowCreation(rec2))
        for l,d1,d2,arc,tag1,tag2,arrow in zip(lines_mob[6:],dots_mob[10:13],dots_mob[7:10],arcs_mob[4:],tags_mob[10:],tags_mob[7:10],arrows_mob):
            self.play(ShowCreation(l))
            self.wait()
            self.play(
                ShowCreation(d1),
                Write(tag1)
            )
            self.wait()
            self.play(
                ShowCreation(arrow),
                ShowCreation(arc),
            )
            self.play(theta.increment_value,-130*DEGREES)
            # self.play(ShowCreation(arc))
            self.wait()
            arc.clear_updaters()
            arrow.clear_updaters()
            self.play(
                ShowCreation(d2),
                Write(tag2),
                FadeOut(arrow)
            )
            self.wait()
            theta = ValueTracker(-8*DEGREES)
        self.play(Write(captions_mob[1]))
        self.wait()
        self.play(FadeInFrom(captions_mob[2]))
class CodeLine(Text):
    CONFIG = {
        't2c': {
            'x': average_color(BLUE, PINK),
            'y': average_color(BLUE, PINK),
            'z': average_color(BLUE, PINK),
            'RIGHT': ORANGE,
            'LEFT': ORANGE,
            'DOWN': ORANGE,
            'UP': ORANGE,
            'IN': ORANGE,
            'OUT': ORANGE,
            'ORIGIN': ORANGE,
            'DL': ORANGE,
            'DR': ORANGE,
            'UL': ORANGE,
            'UR': ORANGE,
            'TOP': ORANGE,
            'BOTTOM': ORANGE,
            'LEFT_SIDE': ORANGE,
            'RIGHT_SIDE': ORANGE,
            'manim': GOLD,
            'constants.py': GOLD,
            'FRAME_HEIGHT': BLUE_D,
            'FRAME_WIDTH': BLUE_D,
            'PIXEL_HEIGHT': RED_B,
            'PIXEL_WIDTH': RED_B,
            'np': BLACK,
            'array': BLUE_D,
            'ndarray': BLUE,
            'FadeIn': average_color(RED, ORANGE),
            'move_to': BLUE_D,
            'shift': BLUE_D,
            'arrange': BLUE_D,
            'VGroup': BLUE_D,
            'VMobject': BLUE_D,
            'ImageMobject': BLUE_D,
            'list': BLUE_D,
            'append': BLUE_D,
            'remove': BLUE_D,
            'next_to': BLUE_D,
            'to_corner': BLUE_D,
            'to_edge': BLUE_D,
            'align_to': BLUE_D,
            'scale': BLUE_D,
            'rotate': BLUE_D,
            'flip': BLUE_D,
            'add': BLUE_D,
            'add_to_back': BLUE_D,
            'vector': ORANGE,
            'play': BLUE_D,
            'set_width': BLUE_D,
            'set_stroke': BLUE_D,
            'aligned_edge': RED,
            'center': RED,
            ">>>": RED,
            'coor_mask': RED,
            'point_or_mobject': RED,
            'python': GOLD,
            '0': average_color(BLUE, PINK),
            '1': average_color(BLUE, PINK),
            '2': average_color(BLUE, PINK),
            '3': average_color(BLUE, PINK),
            '4': average_color(BLUE, PINK),
            '5': average_color(BLUE, PINK),
            '6': average_color(BLUE, PINK),
            '7': average_color(BLUE, PINK),
            '8': average_color(BLUE, PINK),
            '9': average_color(BLUE, PINK),
            'True': average_color(BLUE, PINK),
            '2D': RED_B,
            '3D': RED_B,
            'self': PINK,
            'mob': RED_D,
            'mob1': RED_D,
            'mob2': RED_D,
            'mob3': RED_D,
            'mob0': RED_D,
            "~": "#EBEBEB",
            "vg2": DARK_GRAY,
        },
        'font': 'Consolas',
        'size': 0.36,
        'color': DARK_GRAY,
        'plot_depth': 2,
    }

    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


class Grid(VGroup):
    CONFIG = {
        "height": 6.0,
        "width": 6.0,
    }

    def __init__(self, rows, columns, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        x_step = self.width / self.columns
        y_step = self.height / self.rows

        for x in np.arange(0, self.width + x_step, x_step):
            self.add(Line(
                [x - self.width / 2., -self.height / 2., 0],
                [x - self.width / 2., self.height / 2., 0],
            ))
        for y in np.arange(0, self.height + y_step, y_step):
            self.add(Line(
                [-self.width / 2., y - self.height / 2., 0],
                [self.width / 2., y - self.height / 2., 0]
            ))


class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": FRAME_Y_RADIUS * 2,
        "width": 14,
        "grid_stroke": 0.5,
        "grid_color": WHITE,
        "axis_color": RED,
        "axis_stroke": 2,
        "labels_scale": 0.25,
        "labels_buff": 0,
        "number_decimals": 2
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(self.grid_color, self.grid_stroke)

        vector_ii = ORIGIN + np.array((- self.width / 2, - self.height / 2, 0))
        vector_si = ORIGIN + np.array((- self.width / 2, self.height / 2, 0))
        vector_sd = ORIGIN + np.array((self.width / 2, self.height / 2, 0))

        axes_x = Line(LEFT * self.width / 2, RIGHT * self.width / 2)
        axes_y = Line(DOWN * self.height / 2, UP * self.height / 2)

        axes = VGroup(axes_x, axes_y).set_stroke(self.axis_color, self.axis_stroke)

        divisions_x = self.width / columns
        divisions_y = self.height / rows

        directions_buff_x = [UP, DOWN]
        directions_buff_y = [RIGHT, LEFT]
        dd_buff = [directions_buff_x, directions_buff_y]
        vectors_init_x = [vector_ii, vector_si]
        vectors_init_y = [vector_si, vector_sd]
        vectors_init = [vectors_init_x, vectors_init_y]
        divisions = [divisions_x, divisions_y]
        orientations = [RIGHT, DOWN]
        labels = VGroup()
        set_changes = zip([columns, rows], divisions, orientations, [0, 1], vectors_init, dd_buff)
        for c_and_r, division, orientation, coord, vi_c, d_buff in set_changes:
            for i in range(1, c_and_r):
                for v_i, directions_buff in zip(vi_c, d_buff):
                    ubication = v_i + orientation * division * i
                    coord_point = round(ubication[coord], self.number_decimals)
                    label = Text(f"{coord_point}", font="Arial", stroke_width=0).scale(self.labels_scale)
                    label.next_to(ubication, directions_buff, buff=self.labels_buff)
                    labels.add(label)

        self.add(grid, axes, labels)

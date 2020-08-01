from manimlib.imports import *
import sys

sys.path.append('..')


class Catalog(GraphScene):

    def construct(self):
        # 创建目录
        catalog = [
            "目录",
            "$\\lim_{x \\to \\infty}({e^{-x}+\\frac{1}{x}})$",
            "$\\lim_{x\\to \\infty}{\\frac{\\sin x}{x}}$",
            "$\\lim_{x \\to 1}({2x-1})$"
        ]
        catalog_mob = VGroup(
            *[
                TextMobject(mob).scale(0.8) for mob in catalog
            ]
        )
        catalog_mob.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.4
        )
        for cat in catalog_mob[1:]:
            cat.set_color(BLUE)
        self.play(Write(catalog_mob))
        self.wait()
        # 导入手指svg
        finger = ImageMobject(r"C:\Manim\manim\docs\source\assets\raster_images\finger.png") \
            .scale(0.4) \
            .move_to(catalog_mob[1].get_center() + 2.8 * LEFT + 0.25 * DOWN)
        self.play(FadeInFrom(finger, UP))


class ThreeTheorems(GraphScene, MovingCameraScene):

    def construct(self):
        # 字幕设置
        captions = [
            "两个无穷小的和还是无穷小吗？",  # 0
            "这好像是废话",  # 1
            "但要怎么证明这一点呢？",  # 2
            "要用无穷小的定义来证明γ是无穷小",  # 3
            "既然ε是任意的正数,那么ε/2当然也是任意的正数",  # 4
            "只是为了方便说明",  # 5
            "说明γ也是无穷小",  # 6
            "有界函数与无穷小的乘积会是无穷小吗？",  # 7
            "知道有界和无穷小的定义之后就很简单了",  # 8
            "这里针对的是自变量趋于某个值的无穷小",  # 9
            "自变量趋于无穷的无穷小同理",  # 10
            "我们可能顺手就这样得出极限值",  # 11
            "但凭什么2x可以在极限里分出来呢？",  # 12
            "这也需要证明",  # 13
            "这其实是一个定理",  # 14
            "函数f(x)存在极限的充分必要条件",  # 15
            "是函数等于极限值加上一个无穷小量",  # 16
            "如果极限符号里面是加法、减法、除法、幂运算呢？"   # 17
        ]
        captions_mob = VGroup(
            *[
                CodeLine(cap, font="思源黑体 CN Bold", color=WHITE, size=0.36).to_edge(DOWN) for cap in captions
            ]
        )
        # 定理1：有限个无穷小的和也是无穷小
        pros1 = [
            "假设$\\alpha$和$\\beta$是$x \\rightarrow \\infty$的无穷小",  # 0
            "而$\\gamma=\\alpha+\\beta$",  # 1

            "$\\because \\alpha$是$x \\rightarrow \\infty$的无穷小",  # 2
            "那么$\\forall \\frac{\\varepsilon}{2}>0,\\exists X_1>0$",  # 3
            # {\\varepsilon \\over 2}
            "当$\\left|x\\right|>X_1$时,$\\left|\\alpha\\right|<{\\varepsilon \\over 2}$",  # 4

            "$\\because \\beta$是$x \\rightarrow \\infty$的无穷小",  # 5
            "那么$\\forall \\frac{\\varepsilon}{2}>0,\\exists X_2>0$",  # 6

            "当$\\left|x\\right|>X_2$时,$\\left|\\beta\\right|<{\\varepsilon \\over 2}$",  # 7

            "取$X=max\\{X_1,X_2\\}$,当$\\left|x\\right|>X$时",  # 8
            # 9
            "$\\left|\\alpha\\right|<\\frac{\\varepsilon}{2},\\left|\\beta\\right|<{\\varepsilon \\over 2}$同时成立",
            # 10
            "即$\\left|\\gamma\\right|=\\left|\\alpha+\\gamma\\right|\\leq\\left|\\alpha\\right|+\\left|\\beta\\right|<{\\varepsilon \\over 2}+{\\varepsilon \\over 2}=\\varepsilon$"
        ]
        # 对定理1的文字进行分组处理
        pros1_mob = VGroup(
            *[
                TextMobject(mob).scale(0.6) for mob in pros1
            ]
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.2
        )

        # 定理2：有界函数和无穷小的乘积是无穷小
        pros2 = [
            "设函数$u$在$x_0$的一个邻域$\\mathring{U}(x_0,\\sigma_1)$内有界",  # 0
            "即$\\exists M>0$,当$x \\in\\mathring{U}(x_0,\\sigma_1)$时",  # 1
            "$\\left|u\\right|\\leq M$",  # 2
            "设$\\alpha$是$x\\rightarrow x_0$的无穷小",  # 3
            "即$\\forall \\varepsilon>0,\\exists \\sigma_2>0$",  # 4
            "当$0<\\left|x-x_0\\right|<\\sigma_2$时,$\\left|\\alpha\\right|<\\frac{\\varepsilon}{M}$",  # 5
            "取$\\sigma=max\\{\\sigma_1,\\sigma_2\\}$,当$0<\\left|x-x_0\\right|<\\sigma$时",  # 6
            "$\\left|\\alpha\\right|<\\frac{\\varepsilon}{M},\\left|u\\right|<M$同时成立",  # 7
            # 8
            "$\\therefore \\left|u\\alpha\\right|=\\left|u\\right|\\cdot\\left|\\alpha\\right|<M\\cdot\\frac{\\varepsilon}{M}=\\varepsilon$",
            "说明$u\\alpha$也是无穷小",  # 9
        ]
        pros2_mob = VGroup(
            *[
                TextMobject(mob).scale(0.6) for mob in pros2
            ]
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.2
        )

        # 定理3：极限里的函数可以拆出来
        pros3 = [
            "$\\because \\lim{f(x)}=A,\\lim{g(x)}=B$",  # 0
            "$\\therefore f(x)=A+\\alpha,g(x)=B+\\beta$",  # 1
            "$\\alpha ,\\beta$分别是$f(x),g(x)$的无穷小量",     # 2
            "$\\therefore f(x)\\cdot g(x)=(A+\\alpha)(B+\\beta)=AB+A\\beta+B\\alpha+\\alpha\\beta$",  # 3
            "$\\therefore \\lim{[f(x)g(x)]}=\\lim{[AB]+A\\beta+B\\alpha+\\alpha\\beta}=AB$"  # 4
        ]
        pros3_mob = VGroup(
            *[
                TextMobject(mob).scale(0.7) for mob in pros3
            ]
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.2
        )
        # 目录
        catalog_text = TexMobject("Catalog").scale(0.9)
        catalog_formula1 = TexMobject(
            "\\lim_",  # 0
            "{x \\to \\infty}",  # 1
            "(",  # 2
            "e^{-x}",  # 3
            "+",  # 4
            "{1",  # 5
            "\\over",  # 6
            "x}",  # 7
            ")",  # 8
        ).scale(0.8)
        catalog_formula2 = TexMobject(
            "\\lim_",  # 0
            "{x \\to \\infty}",  # 1
            "{\\sin x",  # 2
            "\\over",  # 3
            "x}",  # 4
        ).scale(0.8)
        catalog_formula3 = TexMobject(
            "\\lim_{x\\to 1}",  # 0
            "(",  # 1
            "2",  # 2
            "\\cdot",  # 3
            "x",  # 4
            ")",  # 5
        )

        formula1 = TexMobject(
            "\\lim_",  # 0
            "{x \\to \\infty}",  # 1
            "(",  # 2
            "e^{-x}",  # 3
            "+",  # 4
            "{1",  # 5
            "\\over",  # 6
            "x}",  # 7
            ")",  # 8
            # "=",                    # 9
            # "0"                     # 10
        )
        for i, color in [(3, "#FF00FF"), (5, RED), (6, RED), (7, RED)]:
            formula1[i].set_color(color)
        formula2 = TexMobject(
            "\\lim_",  # 0
            "{x \\to \\infty}",  # 1
            "{\\sin x",  # 2
            "\\over",  # 3
            "x}",  # 4
            "=",                    # 5
            "0"                     # 6
        )
        for i, color in [(2, "#00FFFF"), (4, RED)]:
            formula2[i].set_color(color)
        formula3 = TexMobject(
            "\\lim_{x\\to 1}",  # 0
            "{(",  # 1
            "2",  # 2
            "\\cdot",  # 3
            "x",  # 4
            ")}",  # 5
            "=",  # 6
            "\\lim_{x\\to 1}",  # 7
            "{2}",  # 8
            "\\cdot",  # 9
            "\\lim_{x\\to 1}",  # 10
            "{x}",  # 11
            "=",  # 12
            "2",  # 13
            "\\cdot",  # 14
            "1",  # 15
            "=",  # 16
            "2"  # 17
        )
        for i, color in [(2, "#00FFFF"), (4, RED), (8, "#00FFFF"), (11, RED), (13, "#00FFFF"), (15, RED)]:
            formula3[i].set_color(color)
        catalog_mob = VGroup(catalog_text, catalog_formula1, catalog_formula2, catalog_formula3) \
            .arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.3
        )
        catalog_data = [(0, "#FF00FF"), (1, YELLOW), (2, YELLOW), (3, YELLOW)]
        for i, color in catalog_data:
            catalog_mob[i].set_color(color)
        # 注释语句
        notes1 = [
            "当$x \\rightarrow \\infty$",  # 0
            "无穷小",  # 1
            "无穷小",  # 2
        ]
        notes1_mob = VGroup(*[TextMobject(mob).scale(0.7) for mob in notes1]) \
            .arrange(
            RIGHT,
            aligned_edge=DOWN,
            buff=0.6)
        notes2 = [
            "$\\left|\\sin x\\right|\\leq 1$,有界",
            "${1\\over x}$",
            "无穷小"
        ]
        notes2_mob = VGroup(
            *[TextMobject(mob) for mob in notes2]
        )
        notes2_mob[1].scale(1.5)
        title = [
            "有限个无穷小的和也是无穷小",
            "有界函数与无穷小的乘积是无穷小"
        ]
        # ----------------------以上是对证明过程的文字、字幕的设置----------------------------------#
        # 目录的边框
        self.play(Write(catalog_mob),
                  AnimationOnSurroundingRectangle(catalog_mob, surrounding_rectangle_config={"color": "#00FF00"})
                  )
        self.wait()
        # 导入手指png
        finger = ImageMobject(r"C:\Manim\manim\docs\source\assets\raster_images\finger.png") \
            .scale(0.4) \
            .next_to(catalog_mob[0], direction=LEFT, buff=0.2) \
            .shift(0.2 * DOWN)
        self.play(FadeInFrom(finger, UP))

        self.wait()
        # TODO:目录的透明度设置  √
        self.play(
            finger.shift, 1 * DOWN,
            catalog_mob[2:].set_opacity, 0.5
        )
        self.wait()
        # 存储摄像机最原始的机位
        self.camera.frame.save_state()
        self.play(
            self.camera.frame.move_to, 9 * RIGHT
        )
        self.wait()
        # 移动pros1到画面中间位置
        pros1_mob.move_to(self.camera.get_frame_center()) \
            .shift(3 * LEFT)
        other1 = TextMobject("证：") \
            .scale(0.6) \
            .next_to(pros1_mob[0], direction=LEFT, buff=0.2)
        # 移动字幕
        captions_mob[0].move_to(self.camera.get_frame_center()) \
            .shift(3.4 * DOWN)
        for cap in captions_mob[1:7]:
            cap.move_to(captions_mob[0])
        # TODO:对式子搞动画
        formula1.move_to(self.camera.get_frame_center()) \
            .shift(UP)
        self.play(Write(formula1))
        self.wait()
        self.play(
            ShowCreationThenFadeAround(formula1[3]),
            ShowCreationThenFadeAround(formula1[5:8])

        )
        self.wait(1)
        notes1_mob.next_to(formula1, direction=DOWN, buff=1) \
            .shift(0.7 * LEFT)
        other2 = TextMobject("0 + 0 = 0 ?")\
                .next_to(notes1_mob[1:], direction=DOWN, buff=0.7)\
                .set_color(RED)
        self.wait()
        self.play(FadeInFrom(notes1_mob, UP))
        self.wait()

        # 生成两个箭头
        arrow1 = Arrow(formula1[3].get_center(), notes1_mob[1].get_center(), buff=0.2)
        arrow2 = Arrow(formula1[7].get_center(), notes1_mob[2].get_center(), buff=0.2)
        # self.add(arrow1, arrow2)
        self.play(GrowArrow(arrow1),GrowArrow(arrow2))
        self.wait()
        self.play(FadeInFrom(other2, UP))
        self.wait()
        # TODO:字幕处理
        self.play(Write(captions_mob[0]))
        self.wait()
        for cap in captions_mob[1:3]:
            self.play(Transform(captions_mob[0], cap))
            self.wait()
        self.play(
            formula1.next_to, pros1_mob[0], {"direction": RIGHT, "buff": 2},
            FadeOutAndShiftDown(notes1_mob),
            FadeOutAndShiftDown(other2),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOutAndShift(captions_mob[0], DOWN)

        )
        arrow1.remove()
        arrow2.remove()

        self.wait()
        self.play(Write(other1), Write(pros1_mob[0]))
        self.wait(1)
        self.play(
            ShowCreationThenFadeAround(formula1[3]),
            ShowCreationThenFadeAround(formula1[5:8])
        )
        self.wait()
        self.play(Write(pros1_mob[1]))
        self.wait(1)
        self.play(ShowCreationThenFadeAround(formula1[3:8]))
        self.wait()
        self.play(Write(captions_mob[3]))
        self.wait()
        for i in range(2, 5):
            self.play(Write(pros1_mob[i]), Write(pros1_mob[i + 3]))
            self.wait(3)
        self.play(ReplacementTransform(captions_mob[3], captions_mob[4]))
        self.wait()
        self.play(ReplacementTransform(captions_mob[4], captions_mob[5]))
        self.wait()
        for p in pros1_mob[8:]:
            self.play(Write(p))
            self.wait()
        self.play(ReplacementTransform(captions_mob[5], captions_mob[6]))
        self.wait()
        self.play(
            Restore(self.camera.frame),
            FadeOutAndShift(pros1_mob, RIGHT),
            FadeOutAndShift(other1)
        )
        self.wait()
        # 手指下移
        self.play(
            finger.shift, 1.2 * DOWN,
            catalog_mob[1].set_opacity, 0.5,
            catalog_mob[2].set_opacity, 1
        )
        self.wait()
        self.play(
            self.camera.frame.move_to, 8 * UP
        )
        # 移动pros2 formula2
        pros2_mob.move_to(self.camera.get_frame_center()) \
            .shift(3 * LEFT)
        other3 = other1.deepcopy() \
            .next_to(pros2_mob[0], direction=LEFT, buff=0.2)
        formula2.move_to(self.camera.get_frame_center())
        captions_mob[7].move_to(self.camera.get_frame_center()) \
            .shift(3.4 * DOWN)
        for i in range(8, 11):
            captions_mob[i].move_to(captions_mob[7])

        # TODO:对式子搞动画
        self.wait(1)
        self.play(Write(formula2[:5]))
        self.wait()
        notes2_mob[0].next_to(formula2[2], direction=UP, buff=1)
        notes2_mob[1].next_to(formula2[4], direction=DL, buff=1)
        notes2_mob[2].next_to(formula2[4], direction=DR, buff=1)
        # 创建三个箭头
        arrow1 = Arrow(formula2[2].get_center(), notes2_mob[0].get_center(), buff=0.4)
        arrow2 = Arrow(formula2[4].get_center(), notes2_mob[1].get_center(), buff=0.4)
        arrow3 = Arrow(notes2_mob[1].get_center(), notes2_mob[2].get_center(), buff=0.7)

        self.play(FadeInFrom(notes2_mob[0], UP), FadeInFrom(notes2_mob[1], LEFT), FadeInFrom(notes2_mob[2], RIGHT))
        self.wait()
        # self.add(arrow1, arrow2, arrow3)
        self.play(GrowArrow(arrow1),GrowArrow(arrow2),GrowArrow(arrow3))
        self.wait()
        self.play(Write(captions_mob[7]))
        self.wait()
        self.play(
            FadeOutAndShiftDown(notes2_mob),
            FadeOut(arrow1),
            FadeOut(arrow2),
            FadeOut(arrow3),
        )
        arrow1.remove()
        arrow2.remove()
        arrow3.remove()
        other4 = TextMobject("$0\\cdot 1 = 0 ?$")\
                .next_to(formula2,direction=DOWN,buff=1)\
                .set_color(RED)

        self.wait(1)
        self.play(GrowFromCenter(other4))
        self.wait()
        self.play(formula2[:5].next_to, pros2_mob[0], {"direction": RIGHT, "buff": 2},
        FadeOutAndShiftDown(captions_mob[7]),
        FadeOutAndShiftDown(other4)
        )
        self.wait()
        self.play(Write(other3), Write(pros2_mob[0]))
        self.wait()
        for p in pros2_mob[1:4]:
            self.play(Write(p))
            self.wait()
        self.play(Write(captions_mob[9]))
        self.wait()
        self.play(ReplacementTransform(captions_mob[9], captions_mob[10]))
        self.wait()
        for p in pros2_mob[4:]:
            self.play(Write(p))
            self.wait()
        formula2[5:].next_to(formula2[:5],direction=RIGHT,buff=0.2)
        self.play(Write(formula2[5:]))
        self.wait()
        self.play(Indicate(formula2[6]))
        self.wait()
        self.play(Restore(self.camera.frame))
        self.wait()
        # 手指下移
        self.play(
            finger.shift, 0.9 * DOWN,
            catalog_mob[2].set_opacity, 0.5,
            catalog_mob[3].set_opacity, 1

        )
        self.wait()
        self.play(
            self.camera.frame.move_to, 8 * DOWN
        )
        # 移动pros3_mob
        pros3_mob.move_to(self.camera.get_frame_center())
        other4 = other1.deepcopy() \
            .next_to(pros3_mob[0], direction=LEFT, buff=0.2)
        captions_mob[11].move_to(self.camera.get_frame_center())\
                        .shift(3.4*DOWN)
        for i in range(12,18):
            captions_mob[i].move_to(captions_mob[11])

        formula3.move_to(self.camera.get_frame_center())
        self.wait(1)
        self.play(Write(formula3[:7]))
        self.wait()
        self.play(
            ShowCreationThenFadeAround(formula3[2]),
            ShowCreationThenFadeAround(formula3[4]),
        )
        self.wait()
        self.play(
            ReplacementTransform(formula3[0].copy(), formula3[7]),
            ReplacementTransform(formula3[0].copy(), formula3[10]),
            ReplacementTransform(formula3[2].copy(), formula3[8]),
            ReplacementTransform(formula3[3].copy(), formula3[9]),
            ReplacementTransform(formula3[4].copy(), formula3[11]),
        )
        self.wait()
        self.play(Write(formula3[12:]))
        self.wait()
        self.play(Write(captions_mob[11]))
        self.wait()
        self.play(ReplacementTransform(captions_mob[11],captions_mob[12]))
        self.wait()
        self.play(ReplacementTransform(captions_mob[12],captions_mob[13]))
        self.wait()
        self.play(FadeOutAndShiftDown(formula3),FadeOutAndShiftDown(captions_mob[13]))
        self.wait()
        self.play(Write(pros3_mob[0]), Write(other4))
        self.wait()
        self.play(Write(pros3_mob[1]))
        self.wait()
        self.play(Write(pros3_mob[2]))
        self.wait()
        self.play(Write(captions_mob[14]))
        self.wait()
        for i in range(15,17):
            self.play(Transform(captions_mob[14],captions_mob[i]))
            self.wait()
        for p in pros3_mob[ 3:]:
            self.play(Write(p))
            self.wait()
        self.play(Transform(captions_mob[14],captions_mob[17]))
        self.wait(3)
        self.play(Restore(self.camera.frame))

        self.wait()
        self.play(self.camera.frame.move_to, 12 * LEFT)
        fav = SVGMobject(r'C:\Manim\manim\docs\source\assets\raster_images\good.svg').scale(0.5)
        col = SVGMobject(r'C:\Manim\manim\docs\source\assets\raster_images\favo.svg').scale(0.5)
        share = SVGMobject(r'C:\Manim\manim\docs\source\assets\raster_images\share.svg').scale(0.5)
        fin = ImageMobject(r'C:\Manim\manim\docs\source\assets\raster_images\手指.png').scale(0.8)
        end_title = TextMobject("码字不易,留个赞吧！")
        con = VGroup(fav, col, share)
        con.arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.8
        ).move_to(self.camera.get_frame_center())
        self.play(DrawBorderThenFill(con))
        self.wait()
        self.play(
            con[0].next_to,con[1],{"direction":LEFT,"buff":0.8},
            con[2].next_to,con[1],{"direction":RIGHT,"buff":0.8}
        )
        # self.play(con.arrange, RIGHT, {"aligned_edge": DOWN, "buff": 0.8,"center":self.camera.get_frame_center()})
        self.wait()
        fin.next_to(col, direction=DOWN, buff=1)
        # self.play(ShowCreation(fin))
        # self.wait(0.1)
        self.play(fin.shift, 1.5 * UP + 1.5 * LEFT)
        self.wait(0.5)
        self.play(con.set_color, "#FB7299", run_time=0.5)
        self.wait(0.5)
        self.play(
            *[
                Flash(obj, color=YELLOW, flash_radius=1) for obj in con
            ]
        )
        end_title.next_to(con[1], direction=UP, buff=0.5)
        self.play(Write(end_title))

class Demo(Scene):

    def construct(self):
        cat_text = VGroup(
            TextMobject("$0 + 0 = 0$")\
                .set_color_by_gradient((BLUE,GREEN))\
                .scale(1.2),
            TextMobject("$0 \\cdot 1 = 0$")\
                .set_color_by_gradient((BLUE,GREEN))\
                .scale(1.2),
            TextMobject("$(1 \\cdot 2) = 1 \\cdot 2$")\
                .set_color_by_gradient((BLUE,GREEN))\
                .scale(1.2)
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.5
        )
        q = TextMobject("?"*20)\
            .next_to(cat_text[0],direction=UP,buff=0.5)\
            .shift(0.2*RIGHT)\
            .set_color(YELLOW)
        q_1 = q.deepcopy()\
               .next_to(cat_text[2],direction=DOWN,buff=0.5)\
               .shift(0.1*LEFT)
        title = TextMobject("证明")\
                .scale(1.2)\
                .set_color(RED)\
                .next_to(q,direction=UP,buff=0.5)
        self.add(cat_text,q,title,q_1)

    def debugTex(self, texm):
        for i, j in zip(range(100), texm):
            tex_id = TexMobject(str(i)).scale(0.5).set_color(PURPLE)
            tex_id.move_to(j)
            self.add(tex_id)


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

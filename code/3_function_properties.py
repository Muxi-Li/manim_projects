from manimlib.imports import *
import sys
sys.path.append('..')


class FunctionProperty1(GraphScene):
    CONFIG = {
        "property_1": "性质一:",
        "property_2:": "函数的极限具有唯一性",
        "other": "这里分两种极限进行证明",
        "prove_0": "证：",
        "prove_1": "假设$\\lim _{ x\\rightarrow { x }_{ 0 } }{ f(x) } =A,\\lim _{ x\\rightarrow { x }_{ 0 } }{ f(x) } =B$,且$A<B$",
        "prove_2": "对于$\\lim _{ x\\rightarrow { x }_{ 0 } }{ f(x) } =A$",
        "prove_3": "$\\forall \\varepsilon >0$,取$\\varepsilon = \\frac{B-A}{2}$",
        "prove_4": "$\exists \\delta_1>0 $,当$\\left| x-{ x }_{ 0 } \\right| <{ \\delta  }_{ 1 }$时",
        "prove_5": "$\\left|f(x)-A\\right|<\\varepsilon=\\frac{B-A}{2}$",
        "prove_6": "即$\\frac{3A-B}{2}<f(x)<\\frac{A+B}{2}$.......(1)",
        "prove_7": "对于$\\lim _{ x\\rightarrow { x }_{ 0 } }{ f(x) } =B$",
        "prove_8": "$\exists \\delta_2>0 $,当$\\left| x-{ x }_{ 0 } \\right| <{ \\delta  }_{ 2 }$时",
        "prove_9": "$\\left|f(x)-B\\right|<\\varepsilon=\\frac{B-A}{2}$",
        "prove_10": "即$\\frac{A+B}{2}<f(x)<\\frac{3B-A}{2}$......(2)",
        "prove_11": "当$\\delta=min\\{\\delta_1,\\delta_2\\}$时,(1)(2)同时成立,矛盾",
        "prove_12": "$\\therefore $当$x \\rightarrow x_0$时,极限有唯一值",

    }

    def construct(self):
        property_1 = TextMobject("性质一:").scale(0.8)
        property_2 = TextMobject("如果函数存在极限,那么极限具有唯一性").scale(0.8)
        other = TextMobject("这里分两种极限进行证明").scale(0.8)
        prove_0 = TextMobject(self.prove_0).scale(0.8)

        prove_1 = TextMobject("假设", "$\\lim _{ x\\rightarrow { x }_{ 0 } }{ f(x) } =A$",
                              ",$\\lim _{ x\\rightarrow { x }_{ 0 } }{ f(x) } =B$", ",且$A<B$")
        prove_2 = TextMobject(
            "对于", "$\\lim _{ x\\rightarrow { x }_{ 0 } }{ f(x) } =A$")
        prove_3 = TextMobject("$\\forall \\varepsilon >0$,取",
                              "$\\varepsilon = \\frac{B-A}{2}$")
        prove_4 = TextMobject(
            "$\exists \\delta_1>0 $,当$\\left| x-{ x }_{ 0 } \\right| <{ \\delta  }_{ 1 }$时")
        prove_5 = TextMobject("$\\left|f(x)-A\\right|<$",
                              "$\\varepsilon$", "$=\\frac{B-A}{2}$")
        prove_6 = TextMobject(
            "即", "$\\frac{3A-B}{2}<f(x)<\\frac{A+B}{2}$",".......(1)")
        prove_7 = TextMobject(
            "对于$\\lim _{ x\\rightarrow { x }_{ 0 } }{ f(x) } =B$")
        prove_8 = TextMobject(
            "$\exists \\delta_2>0 $,当$\\left| x-{ x }_{ 0 } \\right| <{ \\delta  }_{ 2 }$时")
        prove_9 = TextMobject("$\\left|f(x)-B\\right|<\\varepsilon=\\frac{B-A}{2}$")
        prove_10 = TextMobject("即","$\\frac{A+B}{2}<f(x)<\\frac{3B-A}{2}$","......(2)")
        prove_11 = TextMobject("当$\\delta=min\\{\\delta_1,\\delta_2\\}$时,(1)(2)同时成立,矛盾")
        prove_12 = TextMobject("$\\therefore $当$x \\rightarrow x_0$时,极限有唯一值")

        prove_1_1 = TextMobject(
            "假设$\\lim _{ x\\rightarrow \\infty }{ f(x) } =A,\\lim _{ x\\rightarrow \\infty }{ f(x) } =B$,且$A<B$")
        prove_2_1 = TextMobject(
            "对于$\\lim _{ x\\rightarrow \\infty }{ f(x) } =A$")
        prove_3_1 = TextMobject(
            "$\\forall \\varepsilon >0$,取$\\varepsilon = \\frac{B-A}{2}$")
        prove_4_1 = TextMobject(
            "$\exists X_1>0 $,当$\\left| x \\right| > X_1$时")
        prove_5_1 = TextMobject(
            "$\\left|f(x)-A\\right|<\\varepsilon=\\frac{B-A}{2}$")
        prove_6_1 = TextMobject(
            "即","$\\frac{3A-B}{2}<f(x)<\\frac{A+B}{2}$",".......(1)")
        prove_7_1 = TextMobject("对于$\\lim _{ x\\rightarrow \\infty }{f(x)}=B$")
        prove_8_1 = TextMobject(
            "$\\exists X_2>0 $,当$\\left| x \\right| > X_2$时")
        prove_9_1 = TextMobject(
            "$\\left|f(x)-B\\right|<\\varepsilon=\\frac{B-A}{2}$")
        prove_10_1 = TextMobject(
            "即","$\\frac{A+B}{2}<f(x)<\\frac{3B-A}{2}$","......(2)")
        prove_11_1 = TextMobject("当$X=max\\{X_1,X_2\\}$时,(1)(2)同时成立,矛盾")
        prove_12_1 = TextMobject(
            "$\\therefore $当$x \\rightarrow \\infty$时,极限有唯一值")
        rectangle = Rectangle(height=0.03, width=40,
                              color=RED).set_fill(RED, 0.9)
        property_1.to_edge(UL)
        rectangle.next_to(property_1, direction=DOWN)
        self.wait()
        self.play(FadeInFrom(property_1, UP), Write(property_2))
        self.wait(3)
        self.play(
            # FadeOutAndShift(property_1, DOWN),
            FadeInFrom(rectangle, UP),
            property_2.to_edge, UP
        )
        self.wait(3)
        self.play(Write(other))
        prove_0.to_edge(UL)
        prove_0.shift(DOWN)
        self.wait()
        self.play(ReplacementTransform(other, prove_0))
        self.wait(3)
        prove_1.scale(0.7)
        prove_1.next_to(prove_0, direction=RIGHT, buff=SMALL_BUFF)
        prove_1_1.scale(0.7)
        prove_1_1.next_to(prove_0, direction=RIGHT, buff=SMALL_BUFF)
        prove_list = [prove_1, prove_2, prove_3, prove_4, prove_5,
                      prove_6, prove_7, prove_8, prove_9, prove_10, prove_11, prove_12]
        prove1_list = [prove_1_1, prove_2_1, prove_3_1, prove_4_1, prove_5_1, prove_6_1,
                       prove_7_1, prove_8_1, prove_9_1, prove_10_1, prove_11_1, prove_12_1]
        for i in range(1, 12):
            prove_list[i].scale(0.7)
            prove1_list[i].scale(0.7)
            prove_list[i].next_to(
                prove_list[i-1], direction=DOWN, aligned_edge=LEFT, buff=0.2)
            prove1_list[i].next_to(
                prove1_list[i-1], direction=DOWN, aligned_edge=LEFT, buff=0.2)

        # prove_1:"假设$\\lim _{ x\\rightarrow { x }_{ 0 } }{ f(x) } =A,\\lim _{ x\\rightarrow { x }_{ 0 } }{ f(x) } =B$,且$A<B$",
        # 显示prove_1
        self.play(FadeInFrom(prove_1, UP))

        # prove_2:"对于", "$\\lim _{ x\\rightarrow { x }_{ 0 } }{ f(x) } =A$"
        # 显示prove_2
        self.wait()
        self.play(Write(prove_2[0]))
        self.wait()
        self.play(ReplacementTransform(prove_1[1].copy(), prove_2[1]))
        self.wait(3)

        # prove_3:"$\\forall \\varepsilon >0$,取","$\\varepsilon = \\frac{B-A}{2}$"
        # 显示prove_3
        self.play(FadeInFrom(prove_3, UP))
        self.wait(3)

        # prove_4:"$\exists \\delta_1>0 $,当$\\left| x-{ x }_{ 0 } \\right| <{ \\delta  }_{ 1 }$时"
        # 显示：prove_4
        self.play(ReplacementTransform(prove_3.copy(), prove_4))
        self.wait(3)

        # prove_5:"$\\left|f(x)-A\\right|<$","$\\varepsilon$","$=\\frac{B-A}{2}$"
        # 显示prove_5
        self.play(Write(prove_5[:2]))
        self.wait()
        self.play(ShowPassingFlashAround(prove_5[1]),
                  ShowPassingFlashAround(prove_3[1]), 
                  prove_5[1].set_color,YELLOW,
                  prove_3[1].set_color,YELLOW,
                  )
        # self.play(prove_5[1].set_color,RED,
        #           prove_3[1].set_color,RED,)
        self.wait()
        prove_5[2].set_color(YELLOW)
        self.play(FadeInFrom(prove_5[2], UP))
        self.wait(3)

        # prove_6:"即", "$\\frac{3A-B}{2}$", "$<f(x)$", "<", "$\\frac{A+B}{2}$.......(1)"
        # 显示prove_6
        self.play(ReplacementTransform(prove_5.copy(),prove_6))
        self.wait(3)

        # prove_7:"对于$\\lim _{ x\\rightarrow { x }_{ 0 } }{ f(x) } =B$"
        # 显示prove_7
        for prove in prove_list[6:10]:
            self.play(FadeInFrom(prove,UP))
            self.wait()
        self.wait(3)
        self.play(
            ShowPassingFlashAround(prove_6[1]),
            ShowPassingFlashAround(prove_10[1]), 
            prove_6[1].set_color,RED,
            prove_10[1].set_color,RED,
        )

        self.wait()
        prove_11.next_to(prove_6, direction=RIGHT, buff=0.5)
        prove_12.next_to(prove_11, direction=DOWN, aligned_edge=LEFT, buff=0.2)

        self.play(
            ReplacementTransform(prove_10.copy(), prove_11),
        )
        self.wait()
        self.play(ReplacementTransform(prove_11.copy(), prove_12))
        
        self.wait(3)
        self.play(
            *[FadeOutAndShift(prove) for prove in prove_list]
        )

        for prove in prove1_list[:10]:
            self.play(FadeInFrom(prove,UP))
            self.wait()
        prove_11_1.next_to(prove_6_1, direction=RIGHT, buff=0.5)
        prove_12_1.next_to(prove_11_1, direction=DOWN, aligned_edge=LEFT, buff=0.2)
        self.play(
            ReplacementTransform(prove_10_1.copy(), prove_11_1),
        )
        self.wait()
        self.play(
            ShowCreationThenFadeAround(prove_6_1[1]),
            ShowCreationThenFadeAround(prove_10_1[1]), 
            prove_6_1[1].set_color,RED,
            prove_10_1[1].set_color,RED,
        )
        self.wait(3)
        self.play(ReplacementTransform(prove_11_1.copy(), prove_12_1))



        # self.wait()
        # self.play(
        #     *[FadeInFrom(prove, UP) for prove in prove1_list],
        #     run_time=4
        # )


class FunctionProperty2(GraphScene):
    CONFIG = {
        "property_1": "性质二：局部有界性",
        "property_2": "如果$\\lim _{ x\\rightarrow { x }_{ 0 } }{ f(x) } =A,\\exists M>0,\\sigma >0$",
        "property_3": "当$0<\\left|x-x_0\\right|<\\sigma$时,$\\left|f(x)\\right|\\leqslant M$",
        "prove_1": "证：",
        "prove_2": "$\\because \\lim _{ x\\rightarrow { x }_{ 0 } }{ f(x) } =A$",
        "prove_3": "$\\therefore \\forall \\varepsilon>0,\\exists \\sigma>0$",
        "prove_4": "当$0<\\left|x-x_0\\right|<\\sigma$时",
        "prove_5": "有$\\left|f(x)-A\\right|<\\varepsilon$",
        # "prove_6": "则$\\left|f(x)\\right|=\\left|f(x)-A+A\\right|\\leqslant$","$\\left|f(x)-A\\right|+\\left|A\\right|$","<","$\\left|A\\right|+\\varepsilon$",
        "prove_7": "令$M=\\left|A\\right|+\\varepsilon$,则$f(x)<M$"
    }

    def construct(self):
        property_1 = TextMobject(self.property_1).scale(0.8)
        property_2 = TextMobject(self.property_2).scale(0.8)
        property_3 = TextMobject(self.property_3).scale(0.8)
        prove_1 = TextMobject(self.prove_1).scale(0.7)
        prove_2 = TextMobject(self.prove_2)
        prove_3 = TextMobject(self.prove_3)
        prove_4 = TextMobject(self.prove_4)
        prove_5 = TextMobject("有","$\\left|f(x)-A\\right|<\\varepsilon$")
        prove_6 = TextMobject("则$\\left|f(x)\\right|=\\left|f(x)-A+A\\right|\\leqslant$","$\\left|f(x)-A\\right|$","$+\\left|A\\right|$","<","$\\left|A\\right|+\\varepsilon$")
        prove_7 = TextMobject(self.prove_7)
        property_1.to_edge(UL)
        rectangle = Rectangle(height=0.03, width=40,
                              color=RED).set_fill(RED, 0.9)
        rectangle.next_to(property_1, direction=DOWN)
        self.wait()
        self.play(
            FadeInFrom(property_1, UP),
            FadeInFrom(rectangle, UP),
        )
        self.wait()
        property_3.next_to(property_2, direction=DOWN,
                           aligned_edge=LEFT, buff=0.3)
        rectangle1 = Rectangle(height=1.3, width=0.03,
                               color=PINK).set_fill(RED, 0.9)
        rectangle1.next_to(property_2, direction=UP,
                           buff=SMALL_BUFF, aligned_edge=LEFT)
        rectangle1.shift(1.4*DOWN)
        self.play(FadeInFrom(rectangle1, UP))
        self.wait()
        self.play(rectangle1.shift, 7.3*RIGHT, Write(property_2, rate_func=running_start),
                  Write(property_3, rate_func=running_start), run_time=1)
        self.wait(4)
        self.play(
            rectangle1.shift, 7.3*LEFT,
            FadeOutAndShift(property_2, LEFT),
            FadeOutAndShift(property_3, LEFT),
            run_time=0.5
        )
        self.wait(0.5)
        self.play(FadeOutAndShift(rectangle1, DOWN))
        self.wait()
        prove_list = [prove_1, prove_2, prove_3,
                      prove_4, prove_5, prove_6, prove_7]
        prove_1.to_edge(UL)
        prove_1.shift(1*DOWN)
        self.play(Write(prove_1))
        prove_2.scale(0.7)
        prove_2.next_to(prove_1, direction=RIGHT, buff=0.2)
        for i in range(2, 7):
            prove_list[i].scale(0.7)
            prove_list[i].next_to(
                prove_list[i-1], direction=DOWN, aligned_edge=LEFT, buff=0.3)
        self.wait()
        for prove in prove_list[1:5]:
            self.play(FadeInFrom(prove,UP))
            self.wait()
        self.play(FadeInFrom(prove_6[:3],UP))
        introduction = TextMobject("绝对值不等式")\
            .scale(0.7)\
            .next_to(prove_6[1:3],direction=UP,buff=0.2)\
            .set_color(RED)
        self.play(
            ShowCreationThenFadeAround(prove_6[1:3]),
            FadeInFrom(introduction,UP),
            run_time=3
        )
        self.wait()
        
        self.play(FadeOutAndShift(introduction,DOWN))
        self.wait()
        self.play(AnimationOnSurroundingRectangle(prove_6[1]),AnimationOnSurroundingRectangle(prove_5[1]))
        self.wait()
        self.play(FadeInFrom(prove_6[3:],UP))

        # self.play(FadeOutAndShift(introduction))
        self.wait()
        self.play(FadeInFrom(prove_7,UP))
        
        # self.play(
        #     *[FadeInFrom(prove, UP) for prove in prove_list[1:]]
        # )


class FunctionProperty3(GraphScene):
    CONFIG = {
        "property_1": "性质三：局部保号性",
        "property_2": "如果$\\lim _{ x\\rightarrow { x }_{ 0 } }{ f(x) } =A>0$,且$A>0$(或$A<0$)",
        "property_3": "那么存在常数$\\sigma>0$,当$0<\\left|x-x_0\\right|$时",
        "property_4": "有$f(x)>0$或$f(x)<0$",
        "prove_1": "证：",
        "prove_2": "$\\because \\lim _{ x\\rightarrow { x }_{ 0 } }{ f(x) } =A$",
        "prove_3": "$\\therefore \\forall \\varepsilon>0$,取$\\varepsilon=\\frac{A}{2}>0$",
        "prove_4": "则$\\exists \\sigma>0$,当$0<\\left|x-x_0\\right|<\\sigma$时",
        "prove_5": "有$\\left|f(x)-A\\right|<\\varepsilon=\\frac{A}{2}$",
        "prove_6": "即$f(x)>\\frac{A}{2}>0$",
        "prove_7": "A<0的情况同上"
    }

    def construct(self):
        property_1 = TextMobject(self.property_1).scale(0.8)
        property_2 = TextMobject(self.property_2).scale(0.8)
        property_3 = TextMobject(self.property_3).scale(0.8)
        property_4 = TextMobject(self.property_4).scale(0.8)
        prove_1 = TextMobject(self.prove_1).scale(0.7)
        prove_2 = TextMobject(self.prove_2)

        prove_3 = TextMobject(self.prove_3)
        prove_4 = TextMobject(self.prove_4)
        prove_5 = TextMobject(self.prove_5)
        prove_6 = TextMobject(self.prove_6)
        prove_7 = TextMobject(self.prove_7)
        property_1.to_edge(UL)
        rectangle = Rectangle(height=0.03, width=40,
                              color=RED).set_fill(RED, 0.9)
        rectangle.next_to(property_1, direction=DOWN)
        self.wait()
        self.play(
            FadeInFrom(property_1, UP),
            FadeInFrom(rectangle, UP),
        )
        self.wait()
        property_2.shift(1*UP)
        property_3.next_to(property_2, direction=DOWN,
                           aligned_edge=LEFT, buff=0.3)
        property_4.next_to(property_3, direction=DOWN,
                           aligned_edge=LEFT, buff=0.3)
        rectangle1 = Rectangle(height=2, width=0.03,
                               color=PINK).set_fill(RED, 0.9)
        rectangle1.next_to(property_2, direction=UP,
                           buff=SMALL_BUFF, aligned_edge=LEFT)
        rectangle1.shift(2.1*DOWN)
        self.play(FadeInFrom(rectangle1, UP))
        self.wait()
        self.play(rectangle1.shift, 8.9*RIGHT, Write(property_2, rate_func=running_start),
                  Write(property_3, rate_func=running_start), Write(property_4, rate_func=running_start), run_time=1)
        self.wait(3)
        self.play(
            rectangle1.shift, 8.9*LEFT,
            FadeOutAndShift(property_2, LEFT),
            FadeOutAndShift(property_3, LEFT),
            FadeOutAndShift(property_4, LEFT),
            run_time=0.5
        )
        self.wait(0.5)
        self.play(FadeOutAndShift(rectangle1, DOWN))
        self.wait()
        prove_list = [prove_1, prove_2, prove_3,
                      prove_4, prove_5, prove_6, prove_7]
        prove_1.to_edge(UL)
        prove_1.shift(1*DOWN)
        self.play(Write(prove_1))
        prove_2.scale(0.7)
        prove_2.next_to(prove_1, direction=RIGHT, buff=0.2)
        for i in range(2, 7):
            prove_list[i].scale(0.7)
            prove_list[i].next_to(
                prove_list[i-1], direction=DOWN, aligned_edge=LEFT, buff=0.3)
        self.wait()
        for prove in prove_list[1:]:
            self.play(FadeInFrom(prove,UP))
            self.wait()
        # self.play(
        #     *[FadeInFrom(prove, UP) for prove in prove_list[1:]]
        # )

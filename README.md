# MyAnimationWithManim

## 写在前面

本着遇到各种坑再寻找解决方法的原则，总结了我遇到了各种坑的解决方法，可能有些方法并不是很好。这些方法有很多是总结其他作者的，后面会一一列出。

---

## `GraphScene`类

### 坐标轴设置问题

我们要显示函数图像，首先要设置坐标轴，才能让函数图像在坐标轴上显示出来。

以下是一般的设置方法：（CONFIG里的参数如果默认的话可以不用定义）

```python
class Plot1(GraphScene):
    CONFIG = {
        "x_min": -1,		# 横坐标最小值
        "x_max": 10,		# 横坐标最大值
        "x_axis_width": 9,	# 整个画面的宽度是14，可以设置x轴所占的宽度
        "x_tick_frequency": 1,	  # x轴刻度间隔
        "x_leftmost_tick": None,  # 从最小刻度开始绘制tick，如果不是None，则最小刻度那里没有tick
        # 感觉可以改写源代码，让最小刻度的tick在需要的值开始
        "x_labeled_nums": None,	  # 横坐标刻度值，传入列表
        "x_axis_label": "$x$",	  # 就是横坐标的label，一般是x
        "y_min": -1,			  # 纵坐标的最小值
        "y_max": 10,			  # 纵坐标的最大值
        "y_axis_height": 6,		  # 纵坐标轴所占的画面高度，画面全高为6
        "y_tick_frequency": 1,	  # y轴刻度值间隔
        "y_bottom_tick": None,    # 跟x_leftmost_tick一样
        "y_labeled_nums": None,	  # 是否显示纵坐标数字刻度
        "y_axis_label": "$y$",	  # y轴的label，一般为y
        "axes_color": GREY,		  # 坐标轴的颜色
        "graph_origin": 2.5 * DOWN + 4 * LEFT,			# 原点的位置，注意是绝对坐标
        "exclude_zero_label": True,						# 是否显示原点的label
        "default_graph_colors": [BLUE, GREEN, YELLOW],	# 图像颜色
        "default_derivative_color": GREEN,				# 这是啥？
        "default_input_color": YELLOW,					# 这也是啥？
        "default_riemann_start_color": BLUE,			# 这是啥？
        "default_riemann_end_color": GREEN,				# 黎曼是啥？
        "area_opacity": 0.8,							# 在显示面积积分的时候显示的颜色透明度
        "num_rects": 50,								# 这是啥？
        
    }
    def construct(self):
        self.setup_axes(animate=True)	# 是否显示坐标轴动画
        graph = self.get_graph(lambda x : x**2,  	# 函数表达式，可以另写在def中
                                    color = GREEN,	# 函数图像颜色
                                    x_min = 2, 		# 图像的最小值
                                    x_max = 4		# 图像的最大值
                                    )
        self.play(
        	ShowCreation(graph),
            run_time = 2
        )
        self.wait()
```

输出结果：

<img src="./img/1.png" alt="graph" style="zoom: 33%;" />

以上都是`manim`默认设置的`graph`，但有时我们需要**定制**适合自己的坐标系。这里主要展示我平时制作视频时遇到的问题。

#### **1.显示坐标轴刻度值，并且间隔为2**

```python
# 只需改改CONFIG中的参数即可
"x_tick_frequency": 2,
"x_labeled_nums": range(-1,11,2),
"y_tick_frequency": 2,
"y_labeled_nums": range(-1,11,2),
```

输出结果：

<img src="./img/2.png" alt="graph" style="zoom:50%;" />

由于横纵坐标的最大值为10，而间隔为2，所以最终不会显示10的`tick`。

解决方法是：要么改变`x_tick_frequency`和`y_tick_frequency`，要么改变`x_max`和`y_max`使最大值有对应的`tick`。

```python
"x_max":11,
"y_max":11,
"x_tick_frequency": 2,
"x_labeled_nums": range(-1,12,2),
"y_tick_frequency": 2,
"y_labeled_nums": range(-1,12,2),
```

输出结果：

<img src="./img/3.png" alt="graph" style="zoom:50%;" />

#### **2.至少其中一个坐标轴的原点不是从0开始**

视频中的画面是有大小的，有时候我们只需要查看函数图像从某一个值开始的情况，比如x>20的情况，这时候画面可能并不会显示函数图像，就如上面的设置，横坐标到11就差不多到边界了。以前曾天真的scale()坐标系，真是太痛苦了。

```python
class PlotGraph(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 20,
        "x_max" : 7,
        "x_min" : 4,
        "y_tick_frequency" : 5, 
        "x_tick_frequency" : 1,
        "axes_color" : BLUE,
        "y_labeled_nums": range(30,60,10),
        "x_labeled_nums": list(np.arange(4, 8)),
        # "x_label_decimal":1,
        "graph_origin": 3 * DOWN + 6 * LEFT,
        "x_label_direction":DOWN,
        "y_label_direction":RIGHT,
        "x_axis_label": None,
        "x_axis_width":10
    }

    def construct(self):
        self.setup_axes(animate=False) 
        # 移动坐标轴，暂时还想不出为什么会这样移动，得研究源码才知道，先记住然后运用再说
        self.x_axis.shift(LEFT*abs(self.y_axis[0].points[0]-self.x_axis[0].points[0]))
        self.y_axis.shift(DOWN*abs(self.y_axis[0].points[0]-self.x_axis[0].points[0]))
        # 对x、ylabel进行移动，这里可以看出self.x_axis[0]应该是numberline
        self.x_axis_label_mob.next_to(self.x_axis[0].get_end(),UP)
        self.y_axis_label_mob.next_to(self.y_axis[0].get_end(),UP)
        p=Dot().move_to(self.coords_to_point(self.x_min, self.y_min))
        self.add(p)
        graph = self.get_graph(lambda x : x**2, 
                                    color = GREEN,
                                    x_min = 5, 
                                    x_max = 7
                                    )

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()
```

输出结果：**图片的xlabel是正常显示的。**

<img src="./img/4.png" style="zoom:50%;" />

发现不管怎么设置横纵坐标的起始值，运用这种移动方式都可以满足要求，例如下面：

```python
# 修改上面一些值
"x_min":5,
"x_max":8,
"y_min":30,
"y_max":60,
"x_labeled_nums": list(np.arange(5, 9)),
"y_labeled_nums":range(40,70,10),
graph = self.get_graph(lambda x : 6*x,
                                    color = GREEN,
                                    x_min = 5, 
                                    x_max = 8
                                    )
```

输出结果：

<img src="./img/5.png" alt="graph" style="zoom:50%;" />

#### **3.具有小数刻度值的坐标轴**

这里不知道是不是我安装的版本旧还是作者没有更新这个问题，所以我就改了了一下源代码，来满足我的需求。

在改代码之前，我们首先要知道，`graph`在初始化的时候，生成两个坐标轴：`x_axis`、`y_axis`，这两个其实是`Numberline`，然后y轴旋转90度就得到我们看到的坐标系。其中的刻度小数位数可以在`number_line.py`中修改：

```python
CONFIG = {
    # ......
    "decimal_number_config": {
            "num_decimal_places": 0,
        },
    # ......
}
```

可以看到默认的刻度值是0位小数的，我们可以在定义`Numberline`的时候引入一个数，具体的做法如下：

```python
# graph_scene.py
# 在graph_scene.py的CONFIG配置中添加两个变量
"x_label_decimal":0,	# 0是默认是没有小数的
"y_label_decimal":0,
# 在def setup_axes()中作如下修改
x_axis = NumberLine(
            x_min=self.x_min,
            x_max=self.x_max,
            unit_size=self.space_unit_to_x,
            tick_frequency=self.x_tick_frequency,
            leftmost_tick=self.x_leftmost_tick,
            numbers_with_elongated_ticks=self.x_labeled_nums,
            color=self.axes_color,
    		# 添加了下面一行
            decimal_number_config={"num_decimal_places": self.x_label_decimal}
        )
 y_axis = NumberLine(
            x_min=self.y_min,
            x_max=self.y_max,
            unit_size=self.space_unit_to_y,
            tick_frequency=self.y_tick_frequency,
            leftmost_tick=self.y_bottom_tick,
            numbers_with_elongated_ticks=self.y_labeled_nums,
            color=self.axes_color,
            line_to_number_vect=LEFT,
            label_direction=LEFT,
     		# 添加了下面一行
            decimal_number_config={"num_decimal_places": self.y_label_decimal}
        )
```

那我们在写代码的时候是怎样的的呢？

```python
class Plot1(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 5, 
        "x_tick_frequency" : 0.5, 
        "axes_color" : BLUE, 
        "y_labeled_nums": range(0,60,10),
        "x_labeled_nums": list(np.arange(2, 7.0+0.5, 0.5)),
        "x_label_decimal":1,	# 这里设置x轴刻度值小数位数
        "y_label_direction": RIGHT,
        "x_label_direction": UP,
        "y_label_decimal":3		# 这里设置y轴刻度值小数位数
    }
    def construct(self):
        self.setup_axes(animate=True)
        graph = self.get_graph(lambda x : x**2,  
                                    color = GREEN,
                                    x_min = 2, 
                                    x_max = 4
                                    )
        self.play(
        	ShowCreation(graph),
            run_time = 2
        )
        self.wait()
```

输出结果：

<img src="./img/6.png" style="zoom:50%;" />

#### **4.自定义setup_axes()函数**

上面有关`graph`的变量赋值都是通过`CONFIG`实现的，但可以自己写一个`setup_axes()`实现这个效果。原则上说，`graph_scene.py`中`CONFIG`中定义的变量都可以在`setup_axes`中实现。

```python
class Plot2(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        # "x_min" : 0,	# 假设注释这个，在自己的setup_axes()中定义
        "y_tick_frequency" : 5,
        "axes_color" : BLUE,
        "x_axis_label" : "$t$",
        "y_axis_label" : "$f(t)$",
    }
    def construct(self):
        self.setup_axes()	# 调用setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)
        self.play(
        	ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        # 一定要加这一句，先初始坐标系，再更改其他的东西
        GraphScene.setup_axes(self) 
        # Parametters of labels
        #   For x
        self.x_min=-1	# 横轴最小值
        self.x_axis.label_direction = DOWN #DOWN is default
        self.y_axis.label_direction = RIGHT
		# 添加坐标轴刻度值
        self.x_axis.add_numbers(*range(
                                        2,
                                        7+1,
                                        1
                                    ))
        self.y_axis.add_numbers(*range(
                                        20,
                                        50+20,
                                        5
                                    ))
        # 显示生成坐标轴的动画
        self.play(
            ShowCreation(self.x_axis),
            ShowCreation(self.y_axis)
        )
```

输出结果：

<img src="./img/7.png" style="zoom:50%;" />

自定义坐标轴还是挺重要的，因为有时候我们需要在同一个画面中显示两个坐标系，需要定义不同的参数。

#### **5.自定义刻度值**

前面的刻度值都是整数或者小数，但我们有时候不想要，比如想要分数的刻度值，咋办呢？

```python
class Plot5(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 0.5,
        "axes_color" : BLUE,
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        values_x = [
            "\\frac{1}{2}",
            "\\frac{3}{2}",
            "\\frac{5}{2}",
            "\\frac{7}{2}",
            "\\frac{9}{2}",
            "\\frac{11}{2}",
            "\\frac{13}{2}",
        ]
        self.x_axis_labels = VGroup()  # Create a group named x_axis_labels
        for x_val,position in zip(values_x,np.arange(0.5,7,1)):
            tex = TexMobject(x_val).scale(0.7)
            tex.next_to(self.coords_to_point(position, 0), DOWN)
            self.x_axis_labels.add(tex)
        self.play(
            Write(self.x_axis_labels),
            Write(self.x_axis),
            Write(self.y_axis)
        )
```

输出结果：

<img src="./img/8.png" style="zoom:50%;" />

这里也可以自定义刻度值来实现**小数刻度值**的情况。

```python
class Plot7(GraphScene):
    CONFIG = {
        "y_max" : 50,
        "y_min" : 0,
        "x_max" : 7,
        "x_min" : 0,
        "y_tick_frequency" : 10,
        "x_tick_frequency" : 0.5,
        "axes_color" : BLUE,
    }
    def construct(self):
        self.setup_axes()
        graph = self.get_graph(lambda x : x**2, color = GREEN)

        self.play(
            ShowCreation(graph),
            run_time = 2
        )
        self.wait()

    def setup_axes(self):
        GraphScene.setup_axes(self)
        self.x_axis.label_direction = UP
        # Additional parametters
        init_val_x = 0
        step_x = 0.5
        end_val_x = 7
        # Position of labels
        values_decimal_x=Range(init_val_x,end_val_x,step_x)
        # List of labels 注意这里
        list_x=[*["%.1f"%i for i in values_decimal_x]]
        # List touples of (posición,etiqueta)
        values_x = [
            (i,j)
            for i,j in zip(values_decimal_x,list_x)
        ]
        self.x_axis_labels = VGroup()
        for x_val, x_tex in values_x:
            tex = TexMobject(x_tex)
            tex.scale(0.7)
            tex.next_to(self.coords_to_point(x_val, 0), DOWN)
            self.x_axis_labels.add(tex)
        self.play(
            Write(self.x_axis_labels),
            Write(self.x_axis),
            Write(self.y_axis)
        )

```

输出结果：

<img src="./img/9.png" style="zoom:50%;" />

所以自定制刻度值是非常灵活的，可以实现在坐标轴上只显示几个点的刻度值。

### `GraphScene`的一些相关函数

这里再补充一下`graphScene`类的一些函数。

* `setup_axes(self, animate=False)`

> 功能

建立坐标轴。

> parameters

`animate`: `True`表示显示生成坐标轴动画，`False`则表示不显示，直接出现画好的坐标轴。



* `coords_to_point(self, x, y)`

> 功能

根据坐标获取图像中的点。

> parameters

`x`：横坐标。

`y`：纵坐标



* `point_to_coords(self, point)`

> 功能

在图像上返回一个点的坐标

> parameters

`point`：函数图像上某一点。

> return

`[x,y]`



* `input_to_graph_point(self, x, graph)`

> 功能

根据横坐标获取图像上的一个点。

> parameters

`x`：横坐标值

`graph`：生成的函数图像

> return

`point`



* `angle_of_tangent(self, x, graph, dx=0.01)`

> 功能

返回横坐标对应点的斜率的角度。

> parameters

`x`：横坐标值。

`graph`：函数图像。

`dx=0.01`：计算斜率肯定需要两个点，这是两个点的横坐标间隔，默认为0.01。



* `slope_of_tangent(self, *args, **kwargs)`

> 功能

返回一个点的斜率

> parameters

跟`angle_of_tangent`传一样的参数即可。



* `get_derivative_graph(self, graph, dx=0.01, **kwargs)`

> 功能

获取一个函数的微分图像，比如`y=x**2`，那么它的导函数就是`y=2*x`，画出这个导函数的图像。

> parameters

`graph`：已经生成的graph。

`dx`：微小量。



* `get_graph_label(self,graph,label="f(x)",x_val=None,direction=RIGHT,buff=MED_SMALL_BUFF,color=None)`

> 功能

返回函数图像添加`label`，默认是`f(x)`。

> parameters

`graph`：已经生成的函数图像。

`label`：函数标签，默认是`f(x)`。

`x_val`：添加`label`的横坐标。

`direction`：方向。

`buff`：距离。

`color`：标签的颜色。



* `get_riemann_rectangles(self,graph,x_min=None,x_max=None,dx=0.1,input_sample_type="left",stroke_width=1,stroke_color=BLACK,fill_opacity=1,start_color=None,end_color=None,show_signed_area=True,width_scale_factor)`

> 功能

返回函数图像黎曼积分的矩形，就是面积积分的矩形。

> parameters

`graph`：生成的函数图像。

`x_min`：显示矩形的开始位置。

`x_max`：显示矩形的结束位置。

`dx`：其实就是矩形的宽度，当宽度越小时，积分越能近似函数图像的面积积分。

`input_sample_type`：取样点，有`left`、`center`、`right`三个值，应该是求矩形高的时候有关，因为三个值对应的函数值不同，代表的矩形高也不同。

`stroke_width`：矩形边的线宽。

`stroke_color`：矩形线的颜色。

`fill_opacity`：矩形填充的透明度。

`start_color`：填充颜色的起始颜色，涉及到颜色渐变。

`end_color`：填充颜色的结束颜色。

`show_signed_area`：跟积分正负有关，`True`，区分显示负积分的矩形，`False`，不区分显示负积分的矩形。

`width_scale_factor`：还不知道用处是啥，可能自己暂时用不上。

* `get_area(self, graph, t_min, t_max)`

> 功能

求面积积分。相当于前面的`get_riemann_rectangles()`当`dx`很小的情况。

> parameters

`graph`：已经生成的函数图像。

`t_min`：面积积分横坐标开始位置。

`t_max`：面积积分横坐标结束位置。

* `transform_between_riemann_rects(self, curr_rects, new_rects, **kwargs)`

> 功能

将两个`get_riemann_rectangles`矩形`transform`变换。

> parameters

`curr_rects`：旧的矩形。

`new_rects`：新的矩形。

* `get_vertical_line_to_graph(self,x,graph,line_class,**line_kwargs)`

> 功能

获取某个横坐标对应的竖直的线。

> parameters

`x`：横坐标。

`graph`：已经画好的函数图像。

`line_class`：直线线类型，有`Line`（实线）、`Dashline`（虚线）。

`line_kwargs`：其他一些直线的参数。

* `get_vertical_lines_to_graph(self,graph,x_min=None,x_max=None,num_lines=20,**kwargs)`

> 功能

返回`(x_min,x_max)`内的所有竖直线`(VGroup)`，竖直线默认数量为20。

> parameters

`graph`：函数图像。

`x_min`：横坐标最小值。

`x_max`：横坐标最大值。

`num_lines`：竖直线数量。

* `get_secant_slope_group(x,graph,dx=None,dx_line_color=None,df_line_color=None,dx_label=None,df_label=None,include_secant_line=True,secant_line_color=None,secant_line_length=10)`

> 功能

返回一条割线，感觉很有用。

> parameters

`x`：一个点的横坐标。

`graph`：函数图像。

`dx`：画割线肯定要两个点，横坐标`x`确定第一个点，`x+dx`确定另一个点。

`dx_line_color`：线的颜色，具体看图。

`df_line_color`：线的颜色，具体看图。

`dx_label`：具体看图。

`df_label`：具体看图。

`include_secant_line`：True表示显示割线，反之不显示。

`secant_line_color`：割线的颜色。

`secant_line_length`：割线的长度，默认长10。

```python
class MyGraph(GraphScene):
    CONFIG = {
        "x_min": -1,
        "x_max": 10,
        "x_axis_width": 9,
        "x_tick_frequency": 1,
        "x_leftmost_tick": 2,  # Change if different from x_min
        "x_labeled_nums": range(-1,11),
        "x_axis_label": "$x$",
        "y_min": -1,
        "y_max": 10,
        "y_axis_height": 6,
        "y_tick_frequency": 1,
        "y_bottom_tick": None,  # Change if different from y_min
        "y_labeled_nums": range(-1,11),
        "y_axis_label": "$y$",
        "axes_color": GREY,
        "graph_origin": 2.5 * DOWN + 4 * LEFT,
        "exclude_zero_label": True,
        "default_graph_colors": [BLUE, GREEN, YELLOW],
        "default_derivative_color": GREEN,
        "default_input_color": YELLOW,
        "default_riemann_start_color": BLUE,
        "default_riemann_end_color": GREEN,
        "area_opacity": 0.8,
        "num_rects": 50,

    }
    def construct(self):
        self.setup_axes(animate=True)
        p1 = Dot().move_to(self.coords_to_point(1, 1))
        p2 = Dot().move_to(self.coords_to_point(3, 9))
        self.add(p1, p2)
        graph1 = self.get_graph(
            lambda x:x**2,
            x_min=-1,
            x_max=4,
            color=BLUE,
        )
        self.play(ShowCreation(graph1))
        self.wait()
        slope_mob = self.get_secant_slope_group(
            x=1,
            graph=graph1,
            dx=2,
            dx_line_color=YELLOW,
            df_line_color=RED,
            dx_label="dx",
            df_label="dy",
            secant_line_color=PINK

        )

        self.play(ShowCreation(slope_mob))
        self.wait()
```

输出结果：

<img src="./img/10.png" style="zoom:50%;" />

* `animate_secant_slope_group_change()`

> 功能

`update`割线效果。

> parameters

`secant_slope_group`：前面`get_secant_slope_group`生成的割线和`label`，是一个`group`。

`target_dx`：最终`dx`。

`target_x`：最终的`x`。

`run_time=3`：运动时长。

`added_anims`：搞不懂。

`**anim_kwargs`：其他一些关键字参数。

---

## `TexMobject` &`TextMobject`&`Text`

对于文字操作，我们更多的时候，是考虑文字对齐、上色美化问题。

#### 文字上色

1. **`TexMobject`:  分开字符，分别上色**

```python
class MyFormula(Scene):
    def construct(self):
        tex = TexMobject("\\lim_",             # 0
                          "{h",                 # 1
                          "\\rightarrow","0}",  # 2
                          "{f",                 # 3
                          "\\left(",            # 4
                          "x",                  # 5
                          "+",                  # 6
                          "h",                  # 7
                          "\\right)",           # 8
                          "-",                  # 9
                          "f",                  # 10
                          "\\left(",            # 11
                          "h",                  # 12
                          "\\right)",           # 13
                          "\\over",             # 14
                          "h}"                  # 15
        ).scale(0.7)
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        text[8].set_color(TEAL)
        text[9].set_color(GOLD)
        text[10].set_color(GRAY)
        text[11].set_color("#F8C471")
        text[12].set_color("#D0D3D4")
        text[13].set_color("#512E5F")
        text[14].set_color("#273746")
        text[15].set_color("#E6B0AA")
        text[16].set_color("#2ECC71")
        self.play(Write(text))
        self.wait(2)
```

输出结果：

<img src="./img/11.png" style="zoom:50%;" />

这里对于有分数的上色推荐使用`\\over`而不是用`\\frac{}{}`，后者可能会出现意想不到的问题。

这里可以进一步优化（**推荐**）：

```python
class MyFormula(Scene):
    def construct(self):
        tex = TexMobject("\\lim_",              # 0
                          "{h",                 # 1
                          "\\rightarrow",		# 2
                          "0}",  				# 3
                          "{f",                 # 4
                          "\\left(",            # 5
                          "x",                  # 6
                          "+",                  # 7
                          "h",                  # 8
                          "\\right)",           # 9
                          "-",                  # 10
                          "f",                  # 11
                          "\\left(",            # 12
                          "h",                  # 13
                          "\\right)",           # 14
                          "\\over",             # 15
                          "h}"                  # 16
        ).scale(1.2)
        # 这里设置color_data非常灵活，不必拘泥于此
        color_data = [
            RED,
            BLUE,
            GREEN,
            YELLOW,
            PINK,
            ORANGE,
            PURPLE,
            MAROON,
            TEAL,
            GOLD,
            GRAY,
            "#F8C471",
            "#D0D3D4",
            "#512E5F",
            "#273746",
            "#E6B0AA",
            "#2ECC71"
        ]
        for i,color in zip(range(17),color_data):
            tex[i].set_color(color)
        self.play(Write(tex))
        self.wait(2)
```

输出结果：

<img src="./img/12.png" style="zoom:50%;" />

2. **`TexMobject`：使用`set_color_by_tex_to_color_map(t2c)`函数**

```python
class MyFormula(Scene):
    CONFIG = {
        "t2c":{
            "\\lim_":RED,
            "{h":BLUE,
            "\\rightarrow":GREEN,
            "0}":YELLOW,
            "{f":PINK,
            "\\left(":ORANGE,
            "x":PURPLE,
             "+":MAROON,
             "h":TEAL,
             "\\right)":GOLD,
             "-":GRAY,
             "f":"#F8C471",
             "\\left(":"#D0D3D4",
             "h":"#512E5F",
             "\\right)":"#273746",
             "\\over":"#E6B0AA",
             "h}":"#2ECC71"

    }
    }
    def construct(self):
        tex = TexMobject("\\lim_",              # 0
                          "{h",                 # 1
                          "\\rightarrow",       # 2
                          "0}",                 # 3
                          "{f",                 # 4
                          "\\left(",            # 5
                          "x",                  # 6
                          "+",                  # 7
                          "h",                  # 8
                          "\\right)",           # 9
                          "-",                  # 10
                          "f",                  # 11
                          "\\left(",            # 12
                          "h",                  # 13
                          "\\right)",           # 14
                          "\\over",             # 15
                          "h}"                  # 16
        ).scale(1.2)
        tex.set_color_by_tex_to_color_map(self.t2c)
        self.add(tex)
```

输出结果：

<img src="./img/13.png" style="zoom:50%;" />

显而易见，使用`t2c`字典，使相同字符有一样的颜色，有优势也有弊端。

这里为什么没提到`TextMobject`呢？主要是`TextMobject`有中文的时候我非常讨厌上色，拆分很烦，就不想那么复杂，反正上色的话跟上面提到的差不多，而且还不如用`Text`。

3. **`Text`:  使用set_color_by_t2c(t2c)函数**

`Text`类是用来显示不同中文字体的类，个人非常喜欢，如果你的版本里的`Text`有`bug`的话，可以去`manim`的`GitHub`上看别人提交的`Pull requests`，有修复`Text`的方法。

```python
class Demo(Scene):
    CONFIG = {
        't2c':{
            'a': RED,
            'b': YELLOW,
            'c': GREEN,
            '你': PURPLE,
            '好': MAROON,
            ',': TEAL
        }
    }
    def construct(self):
        text = Text("abc,你好",font="思源黑体")
        text.set_color_by_t2c(self.t2c)
        self.add(text)
```

输出结果：

<img src="./img/14.png" style="zoom:50%;" />

对中文也这样，太棒了！！！

#### 字体对齐  

1. **next_to()**

```python
class Demo(Scene):
    def construct(self):
        tex1 = TexMobject("a").scale(0.8)
        tex2 = TexMobject("ab").scale(0.8)
        tex3 = TexMobject("abc").scale(0.8)
        tex4 = TexMobject("abcd").scale(0.8)
        tex5 = TexMobject("abcde").scale(0.8)
        tex6 = TexMobject("abcdef").scale(0.8)
        # 改变aligned_edge左对齐
        tex1.shift(2*UP)
        tex2.next_to(tex1,direction=DOWN,buff=0.3,aligned_edge=LEFT)
        tex3.next_to(tex2, direction=DOWN, buff=0.3, aligned_edge=LEFT)
        tex4.next_to(tex3, direction=DOWN, buff=0.3, aligned_edge=LEFT)
        tex5.next_to(tex4, direction=DOWN, buff=0.3, aligned_edge=LEFT)
        tex6.next_to(tex5, direction=DOWN, buff=0.3, aligned_edge=LEFT)
        self.add(tex1,tex2,tex3,tex4,tex5,tex6)
```

输出结果：

<img src="./img/15.png" style="zoom:50%;" />

默认的情况下是中间对齐，如：上面代码不添加`aligned_edge=LEFT`，则效果如下：

<img src="./img/16.png" style="zoom:50%;" />

2. **arrange()**

使用`VGroup()`的`arrange()`函数，这个函数的本质是`next_to()`。非常方便，个人推荐。

```python
class Demo(Scene):
    def construct(self):
        tex = [
            "a",
            "ab",
            "abc",
            "abcd",
            "abcde",
            "abcdef"
        ]
        tex_mob = VGroup(
            *[TexMobject(mob).scale(0.8) for mob in tex]
        )
        tex_mob.arrange(
            direction=DOWN,		# next_to()	的direction形参
            aligned_edge=LEFT,	# 左对齐
            buff=0.3
        )
        self.add(tex_mob)
```

输出结果：

<img src="./img/17.png" style="zoom:50%;" />

还可以有第三种方法，那就是`latex`语法对齐，但我还没系统的学`latex`，所以就不写了，也少用。

---

## `update()`函数

### 一般用法

```python
class AddUpdater1(Scene):
    def construct(self):
        dot = Dot()
        text = TextMobject("Label")\
               .next_to(dot,RIGHT,buff=SMALL_BUFF)

        self.add(dot,text)

        # Update function
        def update_text(obj):
            obj.next_to(dot,RIGHT,buff=SMALL_BUFF)

        # Add update function to the objects
        text.add_updater(update_text)

        # Add the object again
        self.add(text)

        self.play(dot.shift,UP*2)

        # Remove update function
        text.remove_updater(update_text)

        self.wait()
```

输出结果：

![](./video/2.gif)

使用` text.add_updater(update_text)`将`label`与点绑定在一起，一起运动。

### 使用`dt`参数

```python
class UpdateDemo1(GraphScene):
    CONFIG = {
        "t_offset": -3,
        "x_max": 3,
        "x_min": -3,
        "y_min": -9,
        "y_max": 9,
        "x_tick_frequency": 1,
        "y_tick_frequency": 1,
        "axes_color": "BLUE",
        "graph_origin": ORIGIN

    }
    def construct(self):

        # 创建一个坐标系
        self.setup_axes(animate=False)
        graph = self.get_graph(self.func, x_min=-3, x_max=3, color=RED)
        self.play(ShowCreation(graph))
        self.wait()
        # 创建一个点，点在图像上移动
        dot = Dot().move_to(self.coords_to_point(-3, self.func(-3)))
        self.add(dot)
        self.wait()
        def update_dot(mob, dt):
            # dt就是帧速率，一帧等于多少秒
            rate = 0.5*dt	# 设置速度
            mob.move_to(self.coords_to_point(self.t_offset +
                                             rate, self.func(self.t_offset+rate)))
            # self.t_offset是起始值
            self.t_offset += rate
        dot.add_updater(update_dot)

        # 创建两条虚线,随着dot移动
        line1 = DashedLine(start=self.coords_to_point(-3, 0),
                           end=self.coords_to_point(-3, self.func(-3)))
        line2 = DashedLine(start=self.coords_to_point(-3, self.func(-3)),
                           end=self.coords_to_point(0, self.func(-3)))
        self.add(line1, line2)

        def update_line1(mob):
            l = DashedLine(
                start=self.coords_to_point(self.t_offset, 0), 											end=self.coords_to_point(
                self.t_offset, self.func(self.t_offset))
            )
            mob.become(l)

        def update_line2(mob):
            l = DashedLine(
                start=self.coords_to_point(self.t_offset, self.func(
                self.t_offset)), 
                end=self.coords_to_point(0, self.func(self.t_offset)))
            mob.become(l)
        line1.add_updater(update_line1)
        line2.add_updater(update_line2)
		# 一定要加下面这句
        self.add(dot, line1, line2)
        self.wait(12)	# 这里控制运动时间
        dot.remove_updater(update_dot)
        # 去掉关联
        line1.remove_updater(update_line1)
        line2.remove_updater(update_line2)

    def func(self, x):
        return x**2
```





<img src="./video/1.gif" style="zoom: 80%;" />

按照我的理解就是：点是父级，两条虚线是子集，点的坐标通过`dt`参数实现每前进一帧时改变它的坐标，从而达到运动效果，两条虚线通过`become()`函数实现不断的刷新，与点的位置相关联。
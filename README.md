# MyAnimationWithManim

## 写在前面

本着遇到各种坑再寻找解决方法的原则，总结了我遇到了各种坑的解决方法，可能有些方法并不是很好。

## 问题一：坐标系的设置

我们要显示函数图像，首先要设置坐标轴，才能让函数图像在坐标轴上显示出来。

以下是一般的设置方法：

```python
class Plot1(GraphScene):
    CONFIG = {
        "x_min": -1,		# 横坐标最小值
        "x_max": 10,		# 横坐标最大值
        "x_axis_width": 9,	# 整个画面的宽度是14，可以设置x轴所占的宽度
        "x_tick_frequency": 1,	  # x轴刻度间隔
        "x_leftmost_tick": None,  # None的话显示tick，设想：可不可以显示其他类型的tick？
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

[graph](./img/1.png)

以上都是`manim`默认设置的`graph`，但有时我们需要**定制**适合自己的坐标系。

1. 显示坐标轴刻度值，并且间隔为2

```python
# 只需改改CONFIG中的参数即可
"x_tick_frequency": 2,
"x_labeled_nums": range(-1,11,2),
"y_tick_frequency": 2,
"y_labeled_nums": range(-1,11,2),
```

输出结果：

[graph](./img/2.png)

由于横纵坐标的最大值为10，而间隔为2，所以最终不会显示10的`tick`，解决方法是：要么改变`x_tick_frequency`和`y_tick_frequency`，要么改变`x_max`和`y_max`使最大值有对应的`tick`。

```python
"x_max":11,
"y_max":11,
"x_tick_frequency": 2,
"x_labeled_nums": range(-1,12,2),
"y_tick_frequency": 2,
"y_labeled_nums": range(-1,12,2),
```

输出结果：

[graph](./img/3.png)


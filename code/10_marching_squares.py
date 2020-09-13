from manimlib.imports import *



class MetaballsGrid(VGroup):
    CONFIG = {
        "side_length": 0.4,
        "height": 6,
        "width": 10
    }

    def __init__(self, **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)
        rows = int(self.height / self.side_length)
        columns = int(self.width / self.side_length)
        squares = VGroup(
            *[Square(side_length=self.side_length, stroke_width=1) for _ in range(rows * columns)])
        squares.arrange_in_grid(n_rows=rows, n_cols=columns, buff=0)
        dots = VGroup(*[Dot(point=squa.get_center(), radius=0.02) for squa in squares])
        self.add(squares, dots)


class MetaballScene(Scene):
    CONFIG = {
        "height":6,
        "width":10,
    }
    def construct(self):
        grid = MetaballsGrid(side_length=0.2)
        rec = Rectangle(height=self.height,width=self.width,color=PURPLE)
        title = TexMobject("Metaballs",color=YELLOW).next_to(rec,UP,0.2)
        self.c1 = Circle(radius=0.5, velocity=(RIGHT * 2 + UP) * 2e-2)
        self.c2 = Circle(radius=0.8, velocity=(LEFT * 2 + UP) * 2e-2)
        self.c3 = Circle(radius=1.0, velocity=(RIGHT * 1.5 + 0.3 * DOWN) * 2e-2)
        self.c4 = Circle(radius=1.0, velocity=(LEFT * 2.5 + 1.2 * DOWN) * 2e-2)
        for c in [self.c1, self.c2, self.c3, self.c4]:
            c.add_updater(self.update_circle)
        grid.add_updater(self.update_grid)
        self.add(grid,rec,title,self.c1,self.c2,self.c3,self.c4)
        self.wait(63)

    def update_circle(self, mob, dt):
        velocity = mob.velocity
        mob.shift(velocity)
        if abs(mob.get_center()[1]) > (self.height - mob.get_height()) / 2:
            velocity[1] *= -1
        if abs(mob.get_center()[0]) > (self.width - mob.get_width()) / 2:
            velocity[0] *= -1
        mob.velocity = velocity

    def update_grid(self, mob):
        for squa in mob[0]:
            center = squa.get_center()
            f = self.get_f(center)
            if f > 1:
                squa.set_fill(GREEN_SCREEN, opacity=1)
            else:
                squa.set_fill(opacity=0)

    def get_f(self, center):
        x,y = center[:2]
        x1, y1 = self.c1.get_center()[:2]
        x2, y2 = self.c2.get_center()[:2]
        x3, y3 = self.c3.get_center()[:2]
        x4, y4 = self.c4.get_center()[:2]
        cir_data = [(x1, y1, 0.5), (x2, y2, 0.8), (x3, y3, 1.0), (x4, y4, 1.0)]
        return sum([ri ** 2 / ((x - xi) ** 2 + (y - yi) ** 2) for xi, yi, ri in cir_data])

    def func(self, x, y, xi, yi, r):
        return r ** 2 / ((x - xi) ** 2 + (y - yi) ** 2)


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
        self.x_step = x_step
        self.y_step = y_step
    def get_points(self):
        points = []
        x_step = self.x_step
        y_step = self.y_step
        for y in np.arange(-self.height/2, self.height/2 + y_step, y_step):
            for x in np.arange(-self.width/2, self.width/2 + x_step, x_step):
                points.append((x,y,0))
        return np.array(points)


class ScreenGrid(VGroup):
    CONFIG = {
        "rows": 8,
        "columns": 14,
        "height": 6,
        "width": 10,
        "grid_stroke": 0.7,
        "grid_color": WHITE,
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        rows = self.rows
        columns = self.columns
        grid = Grid(width=self.width, height=self.height, rows=rows, columns=columns)
        grid.set_stroke(color=self.grid_color, width=self.grid_stroke)
        self.add(grid)
        self.grid = grid

    def get_points(self):
        points = self.grid.get_points()
        return points


class MarchingSquares(Scene):
    CONFIG = {
        "screen_grid_config": {
            "rows": 12,
            "columns": 20,
        },
    }

    def construct(self):
        self.func_dict = {
            0: self.f0,
            1: self.f1,
            2: self.f2,
            3: self.f3,
            4: self.f4,
            5: self.f5,
            6: self.f6,
            7: self.f7,
            8: self.f8,
            9: self.f9,
            10: self.f10,
            11: self.f11,
            12: self.f12,
            13: self.f13,
            14: self.f14,
            15: self.f15,
        }
        rec = Rectangle(height=6,width=10,color=PURPLE)
        title = TexMobject("Marching Squares",color=YELLOW).next_to(rec,UP,0.2)
        rows = self.screen_grid_config["rows"] + 1
        columns = self.screen_grid_config["columns"] + 1
        screen_grid = ScreenGrid(**self.screen_grid_config)
        self.points = screen_grid.get_points().reshape([rows, columns, 3])
        self.corners = self.get_corners()
        self.c1 = Circle(radius=0.5, velocity=(RIGHT * 2 + UP) * 2e-2)
        self.c2 = Circle(radius=0.8, velocity=(LEFT * 2 + UP) * 2e-2)
        self.c3 = Circle(radius=1.0, velocity=(RIGHT * 1.5 + 0.3 * DOWN) * 2e-2)
        self.c4 = Circle(radius=1.0, velocity=(LEFT * 2.5 + 1.2 * DOWN) * 2e-2)

        for c in [self.c1, self.c2, self.c3, self.c4]:
            c.add_updater(self.update_circle)
        self.corners.add_updater(self.update_corners, index=0)
        self.corners.add_updater(self.update_boundary, index=1)
        self.add(screen_grid,self.corners, self.c1, self.c2, self.c3, self.c4,rec,title)
        self.wait(99)

    def get_corners(self):
        corners = VGroup(
            *[VGroup(
                *[Dot(radius=0.05, point=p, color=BLACK) for p in po]
            ) for po in self.points]
        )
        corners.set_plot_depth(1)
        return corners

    def update_circle(self, mob, dt):
        velocity = mob.velocity
        mob.shift(velocity)
        if abs(mob.get_center()[1]) > (6 - mob.get_height()) / 2:
            velocity[1] *= -1
        if abs(mob.get_center()[0]) > (10 - mob.get_width()) / 2:
            velocity[0] *= -1
        # mob.set_color(BLACK)
        mob.velocity = velocity

    def update_corners(self, corners):
        rows = self.screen_grid_config["rows"] + 1
        columns = self.screen_grid_config["columns"] + 1
        for i in range(rows):
            for j in range(columns):
                cen = corners[i][j].get_center()
                f = self.get_space(cen)
                if f >= 1:
                    corners[i][j].signal = '1'
                    corners[i][j].set_color(RED_C)
                else:
                    corners[i][j].signal = '0'
                    corners[i][j].set_color(WHITE)
                corners[i][j].f = f


    def update_boundary(self, corners):
        if not hasattr(self, "boundary"):
            setattr(self, "boundary", VGroup())
            return self
        self.remove(self.boundary)
        rows = self.screen_grid_config["rows"] + 1
        columns = self.screen_grid_config["columns"] + 1
        boundary = VGroup()
        for i in range(rows - 1):
            for j in range(columns - 1):
                ul = corners[i][j]
                ur = corners[i][j + 1]
                dl = corners[i + 1][j]
                dr = corners[i + 1][j + 1]
                tem = (ul.signal, ur.signal, dr.signal, dl.signal)
                n = self.get_f(tem)
                l = self.get_boundary(n, i, j)
                if l:
                    boundary.add(l)
        self.boundary = boundary
        self.add(boundary)

    def get_f(self, tem):
        config = ''
        return int(config.join(tem), 2)

    def get_space(self, cen):
        x_list = [cen[0]] * 4
        y_list = [cen[1]] * 4
        xi_list = [c.get_center()[0] for c in [self.c1, self.c2, self.c3, self.c4]]
        yi_list = [c.get_center()[1] for c in [self.c1, self.c2, self.c3, self.c4]]
        r_list = [0.5, 0.8, 1.0, 1.0]
        return sum(list(map(self.func, x_list, y_list, xi_list, yi_list, r_list)))

    def func(self, x, y, xi, yi, r):
        return r ** 2 / ((x - xi) ** 2 + (y - yi) ** 2)

    def get_boundary(self, n, i, j):
        f = self.func_dict[n]
        l = f(i, j)
        return l

    def average(self, s, t):
        return (s + t) / 2

    def get_liner_inter_func(self, s, t, n):
        sy = self.points[s[0], s[1], n]
        ty = self.points[t[0], t[1], n]
        fs = self.corners[s[0]][s[1]].f
        ft = self.corners[t[0]][t[1]].f
        return sy + (ty - sy) * (1 - fs) / (ft - fs)

    def liner_interpolation(self, s, t):
        if s[0] == t[0]:
            x = self.get_liner_inter_func(s, t, 0)
            y = self.points[s[0], s[1], 1]
        elif s[1] == t[1]:
            x = self.points[s[0], s[1], 0]
            y = self.get_liner_inter_func(s, t, 1)
        return np.array([x, y, 0])

    def f0(self, i, j):
        return None

    def f1(self, i, j):
        start = self.liner_interpolation((i, j), (i + 1, j))
        end = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
        # start = self.average(self.points[i, j], self.points[i + 1, j])
        # end = self.average(self.points[i + 1, j], self.points[i + 1, j + 1])
        l = Line(start, end, stroke_width=1.5).set_color(GREEN_SCREEN)
        return l

    def f2(self, i, j):
        # start = self.average(self.points[i, j + 1], self.points[i + 1, j + 1])
        # end = self.average(self.points[i + 1, j], self.points[i + 1, j + 1])
        start = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
        end = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
        l = Line(start, end, stroke_width=1.5).set_color(GREEN_SCREEN)
        return l

    def f3(self, i, j):
        # start = self.average(self.points[i, j], self.points[i + 1, j])
        # end = self.average(self.points[i, j + 1], self.points[i + 1, j + 1])
        start = self.liner_interpolation((i, j), (i + 1, j))
        end = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
        l = Line(start, end, stroke_width=1.5).set_color(GREEN_SCREEN)
        return l

    def f4(self, i, j):
        # start = self.average(self.points[i, j], self.points[i, j + 1])
        # end = self.average(self.points[i, j + 1], self.points[i + 1, j + 1])
        start = self.liner_interpolation((i, j), (i, j + 1))
        end = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
        l = Line(start, end, stroke_width=1.5).set_color(GREEN_SCREEN)
        return l

    def f5(self, i, j):
        # start1 = self.average(self.points[i, j], self.points[i, j + 1])
        # end1 = self.average(self.points[i, j], self.points[i + 1, j])
        start1 = self.liner_interpolation((i, j), (i, j + 1))
        end1 = self.liner_interpolation((i, j), (i + 1, j))
        # start2 = self.average(self.points[i, j + 1], self.points[i + 1, j + 1])
        # end2 = self.average(self.points[i + 1, j], self.points[i + 1, j + 1])
        start2 = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
        end2 = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
        l1 = Line(start1, end1, stroke_width=1.5).set_color(GREEN_SCREEN)
        l2 = Line(start2, end2, stroke_width=1.5).set_color(GREEN_SCREEN)
        return VGroup(l1, l2)

    def f6(self, i, j):
        # start = self.average(self.points[i, j], self.points[i, j + 1])
        # end = self.average(self.points[i + 1, j], self.points[i + 1, j + 1])
        start = self.liner_interpolation((i, j), (i, j + 1))
        end = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
        l = Line(start, end, stroke_width=1.5).set_color(GREEN_SCREEN)
        return l

    def f7(self, i, j):
        # start = self.average(self.points[i, j], self.points[i, j + 1])
        # end = self.average(self.points[i, j], self.points[i + 1, j])
        start = self.liner_interpolation((i, j), (i, j + 1))
        end = self.liner_interpolation((i, j), (i + 1, j))
        l = Line(start, end, stroke_width=1.5).set_color(GREEN_SCREEN)
        return l

    def f8(self, i, j):
        # start = self.average(self.points[i, j], self.points[i, j + 1])
        # end = self.average(self.points[i, j], self.points[i + 1, j])
        start = self.liner_interpolation((i, j), (i, j + 1))
        end = self.liner_interpolation((i, j), (i + 1, j))
        l = Line(start, end, stroke_width=1.5).set_color(GREEN_SCREEN)
        return l

    def f9(self, i, j):
        # start = self.average(self.points[i, j], self.points[i, j + 1])
        # end = self.average(self.points[i + 1, j], self.points[i + 1, j + 1])
        start = self.liner_interpolation((i, j), (i, j + 1))
        end = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
        l = Line(start, end, stroke_width=1.5).set_color(GREEN_SCREEN)
        return l

    def f10(self, i, j):
        # start1 = self.average(self.points[i, j], self.points[i, j + 1])
        # end1 = self.average(self.points[i, j + 1], self.points[i + 1, j + 1])
        start1 = self.liner_interpolation((i, j), (i, j + 1))
        end1 = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
        # start2 = self.average(self.points[i, j], self.points[i + 1, j])
        # end2 = self.average(self.points[i + 1, j], self.points[i + 1, j + 1])
        start2 = self.liner_interpolation((i, j), (i + 1, j))
        end2 = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
        l1 = Line(start1, end1, stroke_width=1.5).set_color(GREEN_SCREEN)
        l2 = Line(start2, end2, stroke_width=1.5).set_color(GREEN_SCREEN)
        return VGroup(l1, l2)

    def f11(self, i, j):
        # start = self.average(self.points[i, j], self.points[i, j + 1])
        # end = self.average(self.points[i, j + 1], self.points[i + 1, j + 1])
        start = self.liner_interpolation((i, j), (i, j + 1))
        end = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
        l = Line(start, end, stroke_width=1.5).set_color(GREEN_SCREEN)
        return l

    def f12(self, i, j):
        # start = self.average(self.points[i, j], self.points[i + 1, j])
        # end = self.average(self.points[i, j + 1], self.points[i + 1, j + 1])
        start = self.liner_interpolation((i, j), (i + 1, j))
        end = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
        l = Line(start, end, stroke_width=1.5).set_color(GREEN_SCREEN)
        return l

    def f13(self, i, j):
        # start = self.average(self.points[i, j + 1], self.points[i + 1, j + 1])
        # end = self.average(self.points[i + 1, j], self.points[i + 1, j + 1])
        start = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
        end = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
        l = Line(start, end, stroke_width=1.5).set_color(GREEN_SCREEN)
        return l

    def f14(self, i, j):
        # start = self.average(self.points[i, j], self.points[i + 1, j])
        # end = self.average(self.points[i + 1, j], self.points[i + 1, j + 1])
        start = self.liner_interpolation((i, j), (i + 1, j))
        end = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
        l = Line(start, end, stroke_width=1.5).set_color(GREEN_SCREEN)
        return l

    def f15(self, i, j):
        return None


class MarchingSquaresAdvance(Scene):
    CONFIG = {
        "rows": 12,
        "columns": 20,
        "height": 6,
        "width": 10,
    }

    def construct(self):
        # screen_grid = ScreenGrid(rows=self.rows,columns=self.columns)
        self.set_coords()
        self.mpoints = Mobject()
        rec = Rectangle(height=6, width=10, color=PURPLE)
        title = TexMobject("Metaballs", color=YELLOW).next_to(rec, UP, 0.2)
        self.c1 = Circle(radius=0.5, color=BLACK,velocity=(RIGHT * 2 + UP) * 2e-2)
        self.c2 = Circle(radius=0.8, color=BLACK,velocity=(LEFT * 2 + UP) * 2e-2)
        self.c3 = Circle(radius=1.0, color=BLACK,velocity=(RIGHT * 1.5 + 0.3 * DOWN) * 2e-2)
        self.c4 = Circle(radius=1.0, color=BLACK,velocity=(LEFT * 2.5 + 1.2 * DOWN) * 2e-2)
        for c in [self.c1, self.c2, self.c3, self.c4]:
            c.add_updater(self.update_circle)
        self.mpoints.add_updater(self.update_mpoints, index=0)
        self.mpoints.add_updater(self.update_boundary, index=1)
        self.add(self.c1, self.c2, self.c3, self.c4, rec, title,self.mpoints)
        self.wait(33)

    def set_coords(self):
        rows = self.rows
        columns = self.columns
        width = self.width
        height = self.height
        x_step = width / columns
        y_step = height / rows
        x_coords = np.arange(-width / 2, width / 2 + x_step, x_step)
        y_coords = np.arange(-height / 2, height / 2 + y_step, y_step)
        self.x_coords = x_coords
        self.y_coords = y_coords

    def update_circle(self, mob, dt):
        velocity = mob.velocity
        mob.shift(velocity)
        if abs(mob.get_center()[1]) > (self.height - mob.get_height()) / 2:
            velocity[1] *= -1
        if abs(mob.get_center()[0]) > (self.width - mob.get_width()) / 2:
            velocity[0] *= -1
        mob.velocity = velocity
        mob.set_color(BLACK)

    def get_f(self, x, y):
        x1, y1 = self.c1.get_center()[:2]
        x2, y2 = self.c2.get_center()[:2]
        x3, y3 = self.c3.get_center()[:2]
        x4, y4 = self.c4.get_center()[:2]
        cir_data = [(x1, y1, 0.5), (x2, y2, 0.8), (x3, y3, 1.0), (x4, y4, 1.0)]
        return sum([ri ** 2 / ((x - xi) ** 2 + (y - yi) ** 2) for xi, yi, ri in cir_data])

    def get_fs(self):
        rows = self.rows + 1
        columns = self.columns + 1
        x_coords = self.x_coords
        y_coords = self.y_coords
        fs = np.array([self.get_f(x_coords[j], y_coords[i]) for i in range(rows) for j in range(columns)])
        return fs


    def update_mpoints(self, mob):
        rows = self.rows + 1
        columns = self.columns + 1
        fs = self.get_fs()
        fs = fs.reshape([rows, columns])
        lig_index = np.array([(i, j) for i in range(rows) for j in range(columns) if fs[i, j] >= 1])
        self.lig_index = lig_index
        self.fs = fs

    def get_corners(self, i, j):
        return [(i - 1, j - 1), (i - 1, j), (i, j), (i, j - 1)]

    def get_cor_f(self, i, j):
        ul = self.fs[i, j]
        ur = self.fs[i, j + 1]
        dr = self.fs[i + 1, j + 1]
        dl = self.fs[i + 1, j]
        n = 0
        for i, f in enumerate([ul, ur, dr, dl]):
            if f >= 1:
                n += 2 ** (3 - i)
        return n

    def update_boundary(self, mob):
        if not hasattr(self, "boundary"):
            setattr(self, "boundary", VGroup())
            return self
        self.remove(self.boundary)
        rows = self.rows + 1
        columns = self.columns + 1
        boundary = VGroup()
        corners = np.array([self.get_corners(i, j) for i, j in self.lig_index]).reshape([-1, 2])
        for i, j in corners:
            if i > (rows - 2) or i < 0 or j > (columns - 2) or j < 0:
                continue
            n = self.get_cor_f(i, j)
            l = None
            if n == 0:
                pass
            elif n == 1:
                start = self.liner_interpolation((i, j), (i + 1, j))
                end = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
                l = Line(start, end, stroke_width=1.5,color=GREEN_SCREEN)
            elif n == 2:
                start = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
                end = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
                l = Line(start, end, stroke_width=1.5,color=GREEN_SCREEN)
            elif n == 3:
                start = self.liner_interpolation((i, j), (i + 1, j))
                end = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
                l = Line(start, end, stroke_width=1.5,color=GREEN_SCREEN)
            elif n == 4:
                start = self.liner_interpolation((i, j), (i, j + 1))
                end = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
                l = Line(start, end, stroke_width=1.5,color=GREEN_SCREEN)
            elif n == 5:
                start1 = self.liner_interpolation((i, j), (i, j + 1))
                end1 = self.liner_interpolation((i, j), (i + 1, j))
                start2 = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
                end2 = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
                l1 = Line(start1, end1, stroke_width=1.5,color=GREEN_SCREEN)
                l2 = Line(start2, end2, stroke_width=1.5,color=GREEN_SCREEN)
                l = VGroup(l1, l2)
            elif n == 6:
                start = self.liner_interpolation((i, j), (i, j + 1))
                end = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
                l = Line(start, end, stroke_width=1.5,color=GREEN_SCREEN)
            elif n == 7:
                start = self.liner_interpolation((i, j), (i, j + 1))
                end = self.liner_interpolation((i, j), (i + 1, j))
                l = Line(start, end, stroke_width=1.5,color=GREEN_SCREEN)
            elif n == 8:
                start = self.liner_interpolation((i, j), (i, j + 1))
                end = self.liner_interpolation((i, j), (i + 1, j))
                l = Line(start, end, stroke_width=1.5,color=GREEN_SCREEN)
            elif n == 9:
                start = self.liner_interpolation((i, j), (i, j + 1))
                end = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
                l = Line(start, end, stroke_width=1.5,color=GREEN_SCREEN)
            elif n == 10:
                start1 = self.liner_interpolation((i, j), (i, j + 1))
                end1 = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
                start2 = self.liner_interpolation((i, j), (i + 1, j))
                end2 = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
                l1 = Line(start1, end1, stroke_width=1.5,color=GREEN_SCREEN)
                l2 = Line(start2, end2, stroke_width=1.5,color=GREEN_SCREEN)
                l = VGroup(l1, l2)
            elif n == 11:
                start = self.liner_interpolation((i, j), (i, j + 1))
                end = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
                l = Line(start, end, stroke_width=1.5,color=GREEN_SCREEN)
            elif n == 12:
                start = self.liner_interpolation((i, j), (i + 1, j))
                end = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
                l = Line(start, end, stroke_width=1.5,color=GREEN_SCREEN)
            elif n == 13:
                start = self.liner_interpolation((i, j + 1), (i + 1, j + 1))
                end = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
                l = Line(start, end, stroke_width=1.5,color=GREEN_SCREEN)
            elif n == 14:
                start = self.liner_interpolation((i, j), (i + 1, j))
                end = self.liner_interpolation((i + 1, j), (i + 1, j + 1))
                l = Line(start, end, stroke_width=1.5,color=GREEN_SCREEN)
            else:
                pass
            if l:
                boundary.add(l)
        self.boundary = boundary
        self.add(boundary)

    def average(self, s, t):
        return (s + t) / 2

    def liner_inter_func(self, s, t, n):
        if n == 0:
            sy = self.y_coords[s[n]]
            ty = self.y_coords[t[n]]
        else:
            sy = self.x_coords[s[n]]
            ty = self.x_coords[t[n]]
        fs = self.fs[s[0], s[1]]
        ft = self.fs[t[0], t[1]]
        return sy + (ty - sy) * (1 - fs) / (ft - fs)

    def liner_interpolation(self, s, t):
        if s[0] == t[0]:
            x = self.liner_inter_func(s, t, 1)
            y = self.y_coords[s[0]]
        elif s[1] == t[1]:
            x = self.x_coords[s[1]]
            y = self.liner_inter_func(s, t, 0)
        return np.array([x, y, 0])

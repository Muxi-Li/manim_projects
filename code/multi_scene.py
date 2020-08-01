from manimlib.animation.transform import ApplyMethod
from manimlib.camera.moving_camera import MovingCamera
from manimlib.camera.multi_camera import MultiCamera
from manimlib.constants import *
from manimlib.mobject.types.image_mobject import ImageMobjectFromCamera
from manimlib.scene.moving_camera_scene import *
from manimlib.scene.zoomed_scene import *
from manimlib.utils.simple_functions import fdiv

class MultiScene(ZoomedScene):
    CONFIG = {
        "camera_class": MultiCamera,
        "zoomed_display_height": 3,
        "zoomed_display_width": 3,
        "zoomed_display_center": None,
        "zoomed_display_corner": UP + RIGHT,
        "zoomed_display_corner_buff": DEFAULT_MOBJECT_TO_EDGE_BUFFER,
        "zoomed_camera_config": {
            "default_frame_stroke_width": 2,
            "background_opacity": 1,
        },
        "zoomed_camera_image_mobject_config": {},
        "zoomed_camera_frame_starting_position": ORIGIN,
        "zoom_factor": 0.15,
        "image_frame_stroke_width": 3,
        "zoom_activated": False,
        "camera_numbers":2,
    }
    def setup(self):
        ZoomedScene.setup(self)
        self.add_zoomed_cameras()
        self.add_zoomed_displays()
        # self.zoomed_camera和self.zoomed_display在ZoomedScene.setup(self)时生成
        # self.zoomed_cameras.append(self.zoomed_camera)
        # self.zoomed_displays.append(self.zoomed_display)


    def add_zoomed_camera(self):
        zoomed_camera = MovingCamera(**self.zoomed_camera_config)
        zoomed_camera.frame.move_to(self.zoomed_camera_frame_starting_position)
        zoomed_camera.frame.stretch_to_fit_height(self.zoomed_display_height)
        zoomed_camera.frame.stretch_to_fit_width(self.zoomed_display_width)
        zoomed_camera.frame.scale(self.zoom_factor)
        return zoomed_camera
    def add_zoomed_cameras(self):
        zoomed_cameras = []
        for i in range(self.camera_numbers):
            zoomed_camera = self.add_zoomed_camera()
            zoomed_cameras.append(zoomed_camera)
        self.zoomed_cameras = zoomed_cameras
    def add_zoomed_display(self,zoomed_camera):
        zoomed_display = ImageMobjectFromCamera(
            zoomed_camera, **self.zoomed_camera_image_mobject_config
        )
        zoomed_display.stretch_to_fit_height(self.zoomed_display_height)
        zoomed_display.stretch_to_fit_width(self.zoomed_display_width)
        zoomed_display.add_display_frame()
        # position
        if self.zoomed_display_center is not None:
            zoomed_display.move_to(self.zoomed_display_center)
        else:
            zoomed_display.to_corner(
                self.zoomed_display_corner,
                buff=self.zoomed_display_corner_buff
            )
        return zoomed_display
    def add_zoomed_displays(self):
        zoomed_displays = []
        for zoomed_camera in self.zoomed_cameras:
            zoomed_display = self.add_zoomed_display(zoomed_camera)
            zoomed_displays.append(zoomed_display)
        self.zoomed_displays = zoomed_displays

    def activate_zooming(self, animate=False):
        self.zoom_activated = True
        for zoomed_camera,zoomed_display in zip(self.zoomed_cameras,self.zoomed_displays):
            self.camera.add_image_mobject_from_camera(zoomed_display)
            self.add_foreground_mobjects(
                zoomed_camera.frame,
                # zoomed_display,
            )


    def get_zoomed_display_pop_out_animation(self, **kwargs):
    apply_methods = []
    for zoomed_camera, zoomed_display in zip(self.zoomed_cameras,self.zoomed_displays):
        zoomed_display.save_state(use_deepcopy=True)
        zoomed_display.replace(zoomed_camera.frame, stretch=True)
        apply_method = ApplyMethod(zoomed_display.restore)
        apply_methods.append(apply_method)
    return apply_methods
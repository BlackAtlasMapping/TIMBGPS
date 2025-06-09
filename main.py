from manim import *


class WriteRTK(Scene):
    def construct(self):
        rtk = Text("RTK")
        rtk_expanded = Text("Real-Time Kinematic Positioning")

        self.play(Write(rtk))
        self.wait(1)
        self.play(Transform(rtk, rtk_expanded))
        self.wait(3)

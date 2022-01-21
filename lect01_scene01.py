import manim


class NameOfAnimatino(manim.Scene):
    def construct(self):
        box = manim.Rectangle(stroke_color=manim.GREEN_C, stroke_opacity=0.7, fill_color=manim.RED_B,
                              height=1, width=1)
        self.add(box)
        self.play(box.animate.shift(manim.RIGHT * 2), run_time=2)
        self.play(box.animate.shift(manim.UP * 3), run_time=2)
        self.play(box.animate.shift(manim.DOWN * 5 + manim.LEFT * 5), run_time=2)
        self.play(box.animate.shift(manim.UP * 1.5 + manim.RIGHT * 1), run_time=2)
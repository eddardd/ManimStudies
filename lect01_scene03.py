import manim


class Updaters(manim.Scene):
    def construct(self):
        rectangle = manim.RoundedRectangle(stroke_width=8, stroke_color=manim.WHITE, fill_color=manim.BLUE_B,
                                           width=4.5, height=2).shift(manim.UP * 3 + manim.LEFT * 4)
        mathtext = manim.MathTex("\\frac{3}{4}=0.75").set_color_by_gradient(manim.GREEN, manim.PINK).set_height(1.5)
        mathtext.move_to(manim.rectangle.get_center())
        mathtext.add_updater(lambda x: x.move_to(rectangle.get_center()))

        self.play(manim.FadeIn(rectangle))
        self.play(manim.Write(mathtext))
        self.play(rectangle.animate.shift(manim.RIGHT * 1.5 + manim.DOWN * 5), run_time=6)
        self.wait()

        mathtext.clear_update()
        self.play(rectangle.animate.shift(manim.LEFT * 2 + manim.UP * 1), run_time=6)

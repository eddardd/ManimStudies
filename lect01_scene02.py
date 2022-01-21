import manim


class FittingObjects(manim.Scene):
    def construct(self):
        axes = manim.Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1],
                          x_length=6, y_length=6)
        axes.to_edge(manim.LEFT, buff=0.5)

        circle = manim.Circle(stroke_width=6, stroke_color=manim.YELLOW, fill_color=manim.RED_C,
                              fill_opacity=0.8)
        circle.set_width(2).to_edge(manim.DR, buff=0)

        triangle = manim.Triangle(stroke_color=manim.ORANGE, stroke_width=10,
                                  fill_color=manim.GREY).set_height(2).shift(manim.DOWN * 3 + manim.RIGHT * 3)
        
        self.play(manim.Write(axes))
        self.play(manim.DrawBorderThenFill(circle))
        self.play(circle.animate.set_width(1))
        self.play(manim.Transform(circle, triangle), run_time=3)

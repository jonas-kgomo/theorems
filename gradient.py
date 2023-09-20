from manim import *

class FillByValueExample(ThreeDScene):
    def construct(self):
        resolution_fa = 50
        self.set_camera_orientation(phi=75 * DEGREES, theta=-160 * DEGREES)
        axes = ThreeDAxes(x_range=(0, 5, 1), y_range=(0, 5, 1), z_range=(-1, 1, 0.5))
        
        def param_surface(u, v):
            x = u
            y = v
            z = np.sin(x) * np.cos(y)
            return z
        
        surface_plane = Surface(
            lambda u, v: axes.c2p(u, v, param_surface(u, v)),
            resolution=(resolution_fa, resolution_fa),
            v_range=[0, 5],
            u_range=[0, 5],
        )
        surface_plane.set_style(fill_opacity=1, fill_color=BLUE)
        surface_plane.set_fill_by_value(axes=axes, colorscale=[(BLUE, -1), (BLUE, 0), (BLUE, 1)], axis=2)
        
        curve = ParametricFunction(lambda u: axes.c2p(u, u, param_surface(u, u)), color=WHITE, t_range=[0, 5])
        dot = Sphere(radius=0.1, color=RED).move_to(curve.get_start())  # Create a ball-like dot at the start of the curve
        
        self.add(axes, surface_plane, curve, dot)  # Add the curve and dot to the scene
        
        self.play(MoveAlongPath(dot, curve), run_time=3)  # Move the dot along the curve
        
   
         
        self.wait()
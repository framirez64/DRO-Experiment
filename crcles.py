from psychopy import visual

# Object class for circles (template)
class Circle:
    def __init__(self, win, name, category, pos):
        self.win = win
        self.name = name
        self.category = category
        self.pos = pos

        # Attributes based on given circle type
        self.categories = {
            'DRO': {'size': [1.0, 1.0], 'lineColor': 'white', 'fillColor': 'black', 'depth': 0.0},
            'Red': {'size': [1.0, 1.0], 'lineColor': 'white', 'fillColor': [1.0000, -1.0000, -1.0000], 'depth': -1.0}
        }

        # Get attributes for the given category
        category_attributes = self.categories.get(category, {})

        self.stim = visual.ShapeStim(
            win=self.win, name=self.name,
            size=category_attributes.get('size', [1.0, 1.0]),
            vertices='circle', ori=0.0, pos=self.pos, anchor='center',
            lineWidth=1.0, colorSpace='rgb',
            lineColor=category_attributes.get('lineColor', 'white'),
            fillColor=category_attributes.get('fillColor', 'black'),
            opacity=1.0, depth=category_attributes.get('depth', 0.0),
            interpolate=True)

    def draw(self):
        self.stim.draw()


class CircleManager:
    def __init__(self, win):
        self.win = win
        self.circles = []

    def add_circle(self, name, category, pos):
        circle = Circle(self.win, name, category, pos)
        self.circles.append(circle)

    def draw(self):
        for circle in self.circles:
            circle.draw()


# Example usage:
win = visual.Window([1080, 900])  # Your window initialization here
circle_manager = CircleManager(win)

# Add circles with different categories
circle_manager.add_circle('DROCircle', 'DRO', [0, 0])
circle_manager.add_circle('RedCircle', 'Red', [1, 1])

# In your draw loop:
circle_manager.draw()
win.flip()

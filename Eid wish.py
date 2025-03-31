import tkinter as tk
import random
import math

def sequence_gen(text, delay, final_delay):
    seq = [(text[:i], delay) for i in range(1, len(text) + 1)]
    seq[-1] = (seq[-1][0], final_delay)
    return seq

class EidMubarakApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Eid Mubarak")
        self.root.geometry("800x600")
        self.root.configure(bg='#0a3d62')

        self.canvas = tk.Canvas(root, width=800, height=600, bg='#0a3d62', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.load_moon_image()
        self.greeting_text = self.canvas.create_text(400, 250, text="", font=("Arial", 40, "bold"), fill="gold", justify=tk.CENTER)
        self.secondary_text = self.canvas.create_text(400, 320, text="", font=("Arial", 20), fill="white", justify=tk.CENTER)

        self.stars = []
        self.create_stars(50)

        self.lanterns = []
        self.create_lanterns(5)

        self.greeting_sequence = sequence_gen("Eid Mubarak", 0.1, 0.5)
        self.secondary_sequence = sequence_gen("May Allah bless you and your family with happiness and prosperity", 0.1, 2)

        self.current_greeting_step = 0
        self.current_secondary_step = 0

        self.animate_greeting()
        self.animate_stars()
        self.animate_lanterns()

        self.fireworks = []
        self.root.bind("<Button-1>", self.create_firework)

    def load_moon_image(self):
        self.canvas.create_oval(100, 100, 200, 200, fill="#f5f6fa", outline="")
        self.canvas.create_oval(85, 100, 185, 200, fill="#0a3d62", outline="")

    def create_stars(self, num_stars):
        for _ in range(num_stars):
            x = random.randint(0, 800)
            y = random.randint(0, 300)
            size = random.uniform(0.5, 3)
            star = self.canvas.create_oval(x, y, x+size, y+size, fill="white", outline="")
            self.stars.append((star, size, x, y))

    def create_lanterns(self, count):
        lantern_colors = ['#e74c3c', '#e67e22', '#f1c40f', '#2ecc71', '#3498db']
        for i in range(count):
            x = 100 + i * 150
            y = 450
            color = lantern_colors[i % len(lantern_colors)]
            body = self.canvas.create_oval(x-20, y-40, x+20, y+40, fill=color, outline="gold", width=2)
            light = self.canvas.create_oval(x-15, y-30, x+15, y+30, fill="", outline="")
            self.lanterns.append((body, light, x, y, color))

    def animate_greeting(self):
        if self.current_greeting_step < len(self.greeting_sequence):
            text, delay = self.greeting_sequence[self.current_greeting_step]
            self.canvas.itemconfig(self.greeting_text, text=text)
            self.current_greeting_step += 1
            self.root.after(int(delay * 1000), self.animate_greeting)
        else:
            self.animate_secondary_text()

    def animate_secondary_text(self):
        if self.current_secondary_step < len(self.secondary_sequence):
            text, delay = self.secondary_sequence[self.current_secondary_step]
            self.canvas.itemconfig(self.secondary_text, text=text)
            self.current_secondary_step += 1
            self.root.after(int(delay * 1000), self.animate_secondary_text)

    def animate_stars(self):
        for star, size, x, y in self.stars:
            twinkle = random.random() * 0.5 + 0.5
            self.canvas.itemconfig(star, fill=self.rgb_to_hex(255, 255, 255, twinkle))
        self.root.after(500, self.animate_stars)

    def animate_lanterns(self):
        for i, (body, light, x, y, color) in enumerate(self.lanterns):
            r, g, b = self.hex_to_rgb(color)
            intensity = 0.7 + 0.3 * math.sin(self.root.winfo_height() / 100 + i)
            glow_color = self.rgb_to_hex(
                min(255, int(r * 1.5 * intensity)),
                min(255, int(g * 1.5 * intensity)),
                min(255, int(b * 1.5 * intensity))
            )
            self.canvas.itemconfig(light, outline=glow_color)
        self.root.after(100, self.animate_lanterns)

    def create_firework(self, event):
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'white']
        color = random.choice(colors)
        particles = []

        for _ in range(20):
            angle = random.uniform(0, math.pi * 2)
            speed = random.uniform(2, 6)
            size = random.uniform(1, 3)
            particle = {
                'x': event.x,
                'y': event.y,
                'dx': math.sin(angle) * speed,
                'dy': math.cos(angle) * speed,
                'size': size,
                'age': 0,
                'lifetime': random.uniform(1, 2),
                'id': None,
                'color': color
            }
            particle['id'] = self.canvas.create_oval(event.x - size, event.y - size, event.x + size, event.y + size, fill=color, outline="")
            particles.append(particle)

        self.fireworks.append(particles)
        self.animate_fireworks()

    def animate_fireworks(self):
        for firework in self.fireworks[:]:
            for particle in firework[:]:
                particle['x'] += particle['dx']
                particle['y'] += particle['dy'] + 0.1
                particle['dy'] += 0.1
                particle['age'] += 0.02

                alpha = 1 - (particle['age'] / max(0.1, particle['lifetime']))
                if alpha <= 0:
                    self.canvas.delete(particle['id'])
                    firework.remove(particle)
                else:
                    r, g, b = self.hex_to_rgb(particle['color'])
                    faded_color = self.rgb_to_hex(r, g, b, alpha)
                    self.canvas.itemconfig(particle['id'], fill=faded_color)
            if not firework:
                self.fireworks.remove(firework)
        if self.fireworks:
            self.root.after(20, self.animate_fireworks)

    @staticmethod
    def hex_to_rgb(hex_color):
        return tuple(int(hex_color[i:i+2], 16) for i in (1, 3, 5))

    @staticmethod
    def rgb_to_hex(r, g, b, alpha=1.0):
        return f'#{int(r * alpha):02x}{int(g * alpha):02x}{int(b * alpha):02x}'

if __name__ == '__main__':
    root = tk.Tk()
    app = EidMubarakApp(root)
    root.mainloop()

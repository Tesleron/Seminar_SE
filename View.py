import tkinter as tk
import math


def yp(n, m, k):
    # 0<n     n elements in the circle
    # 1<=m<=n    reduce the m element after the current existing element
    # 1<=k<=n k elements remain in the circle at the end of process
    print("n =", n, " m =", m, " k =", k)
    l = [i for i in range(1, n+1)]
    i = 0
    if (len(l) > k):
        i = (i + m) % len(l)
        l.remove(l[i])
        return l
    if m == 1 and k==1:
     print("n =", n, "survive by algorithm =", l, \
           "survive by formula =", \
           int(2 * (n - math.pow(2, math.floor(math.log(n, 2)))) + 1))
    else:
        print("n =", n, "survive by algorithm =", l)

        
class CircleNumbers:
    def __init__(self, master):
        self.master = master
        master.title("Circle of Numbers")
        master.geometry("700x500")
        master.resizable(False, False)
        master.wm_attributes("-topmost", 1)

        # Create a frame to hold the slider and button
        frame = tk.Frame(master)
        frame.pack(side=tk.RIGHT, padx=50)

        # Create the "Speed" label
        self.labelSurvivors = tk.Label(frame, text="Number:")
        self.labelSurvivors.pack(pady=2)

        # Create the slider
        self.sliderPeople = tk.Scale(frame, from_=0, to=42, orient=tk.HORIZONTAL, command=self.draw_circle)
        self.sliderPeople.pack(pady=10)

        # Create the "Speed" label
        self.labelSpeed = tk.Label(frame, text="Speed:")
        self.labelSpeed.pack(pady=2)

        # Create the slider
        self.sliderSpeed = tk.Scale(frame, from_=0, to=42, orient=tk.HORIZONTAL)
        self.sliderSpeed.pack(pady=2)

        # Create the "Speed" label
        self.labelJumps = tk.Label(frame, text="Jumps:")
        self.labelJumps.pack(pady=2)

        # Create the slider
        self.sliderJumps = tk.Scale(frame, from_=0, to=42, orient=tk.HORIZONTAL)
        self.sliderJumps.pack(pady=2)

        # Create the "Speed" label
        self.labelStartFrom = tk.Label(frame, text="Start from:")
        self.labelStartFrom.pack(pady=2)

        # Create the slider
        self.sliderStartFrom = tk.Scale(frame, from_=0, to=42, orient=tk.HORIZONTAL)
        self.sliderStartFrom.pack(pady=2)

        # Create the "Speed" label
        self.labelSurvivors = tk.Label(frame, text="Survivors:")
        self.labelSurvivors.pack(pady=2)

        # Create the slider
        self.sliderSurvivors = tk.Scale(frame, from_=0, to=42, orient=tk.HORIZONTAL)
        self.sliderSurvivors.pack(pady=2)

        # Create a frame named "checkBoxFrame"
        checkBoxFrame = tk.Frame(frame)
        checkBoxFrame.pack()

        # Create a checkbox
        checkbox_var = tk.BooleanVar()
        checkbox = tk.Checkbutton(checkBoxFrame, text="Clockwise", variable=checkbox_var)
        checkbox.pack(side=tk.LEFT)

        # Create the canvas for the circle
        self.canvas = tk.Canvas(master, width=450, height=450)
        self.canvas.pack()

        # Calculate the center coordinates of the root window
        root_width = root.winfo_width()
        root_height = root.winfo_height()
        canvas_width = 400
        canvas_height = 400
        x = (root_width - canvas_width) // 2
        y = (root_height - canvas_height) // 2

        # Place the canvas at the center of the root window
        self.canvas.place(x=x, y=y)

        # Create the "PLAY" button
        self.button = tk.Button(frame, text="Start", command=self.start_timer)
        self.button.pack(pady=2)

        # Create the "PLAY" button
        self.button = tk.Button(frame, text="Restart", command=self.start_timer)
        self.button.pack(pady=2)

        # Initialize variables
        self.numbers = []
        self.circle_size = 150  # radius of the circle
        self.circle_center = (200, 250)  # center of the circle
        self.timer = None

    def start_timer(self):
        self.cancel_timer()
        n = int(self.sliderPeople.get())
        self.draw_circle(n)
        self.timer = self.master.after(3000, self.remove_numbers)

    def draw_circle(self, n):
        self.clear_circle()
        n = int(n)
        # Calculate the positions of the numbers in the circle
        angle_increment = 2 * math.pi / n
        for i in range(n):
            angle = i * angle_increment
            x = self.circle_center[0] + self.circle_size * math.cos(angle)
            y = self.circle_center[1] + self.circle_size * math.sin(angle)
            number_label = self.canvas.create_text(x, y, text=str(i+1))
            self.numbers.append(number_label)

    def remove_numbers(self):
        if len(self.numbers) > 1:
            n = len(self.numbers)
            m = 2
            k = 1
            i = 0
            order = yp(n, m, k)
            number_to_remove = self.numbers[i]
            self.canvas.delete(number_to_remove)
            self.numbers.remove(number_to_remove)
            i+=1
            self.timer = self.master.after(3000, self.remove_numbers)

    def clear_circle(self):
        for number_label in self.numbers:
            self.canvas.delete(number_label)
        self.numbers = []

    def cancel_timer(self):
        if self.timer is not None:
            self.master.after_cancel(self.timer)
            self.timer = None


root = tk.Tk()
app = CircleNumbers(root)

# Center the UI elements more vertically
app.labelSurvivors.pack_configure(anchor=tk.CENTER)
app.sliderSurvivors.pack_configure(anchor=tk.CENTER)
app.sliderSpeed.pack_configure(anchor=tk.CENTER)
app.button.pack_configure(anchor=tk.CENTER)
app.canvas.pack_configure(anchor=tk.CENTER)

root.mainloop()
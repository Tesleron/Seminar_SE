import tkinter as tk
import math
import time
import threading


def yp(n, m, k, view, interval, i = 0):
    # 0<n     n elements in the circle
    # 1<=m<=n    reduce the m element after the current existing element
    # 1<=k<=n k elements remain in the circle at the end of process
    print("n =", n, " m =", m, " k =", k)
    l = [i for i in range(1, n+1)]
    while (len(l) > k and view.active):
        i = (i + m) % len(l)
        j = len(l) - i
        if view.checkbox_var.get() is False:
            view.remove_numbers(l[i])
            l.remove(l[i])
        else:
            view.remove_numbers(l[j])
            l.remove(l[j])
        view.master.update()
        time.sleep(interval)
        # removal from gui
    if m == 1 and k==1 and view.active:
     print("n =", n, "survive by algorithm =", l, \
           "survive by formula =", \
           int(2 * (n - math.pow(2, math.floor(math.log(n, 2)))) + 1))
    elif view.active:
        print("n =", n, "survive by algorithm =", l)
    else:
        print("Game canceled")

        
class CircleNumbers:
    def __init__(self, master):
        self.master = master
        self.active = True
        master.title("Circle of Numbers")
        master.geometry("700x500")
        master.resizable(False, False)
        master.wm_attributes("-topmost", 1)

        # Create a frame to hold the slider and button
        frame = tk.Frame(master)
        frame.pack(side=tk.RIGHT, padx=50)

        # Create the "Speed" label
        self.labelSurvivors = tk.Label(frame, text="People:")
        self.labelSurvivors.pack(pady=2)

        # Create the slider
        self.sliderPeople = tk.Scale(frame, from_=0, to=42, orient=tk.HORIZONTAL, command=self.draw_circle)
        self.sliderPeople.pack(pady=10)

        # Create the "Speed" label
        self.labelSpeed = tk.Label(frame, text="Speed:")
        self.labelSpeed.pack(pady=2)

        # Create the slider
        self.sliderSpeed = tk.Scale(frame, from_=1, to=3, orient=tk.HORIZONTAL)
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
        self.sliderStartFrom = tk.Scale(frame, from_=1, to=42, orient=tk.HORIZONTAL)
        self.sliderStartFrom.pack(pady=2)

        # Create the "Speed" label
        self.labelSurvivors = tk.Label(frame, text="Survivors:")
        self.labelSurvivors.pack(pady=2)

        # Create the slider
        self.sliderSurvivors = tk.Scale(frame, from_=1, to=42, orient=tk.HORIZONTAL)
        self.sliderSurvivors.pack(pady=2)

        # Create a frame named "checkBoxFrame"
        checkBoxFrame = tk.Frame(frame)
        checkBoxFrame.pack()

        # Create a checkbox
        self.checkbox_var = tk.BooleanVar()
        checkbox = tk.Checkbutton(checkBoxFrame, text="Anti-Clockwise", variable=self.checkbox_var)
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
        self.playButton = tk.Button(frame, text="Start", command=self.start_timer, state='disabled')
        self.playButton.pack(pady=2)

        # Create the "PLAY" button
        self.button = tk.Button(frame, text="Restart", command=self.clear_circle)
        self.button.pack(pady=2)

        # Initialize variables
        self.numbers = {}
        self.circle_size = 150  # radius of the circle
        self.circle_center = (200, 250)  # center of the circle
        self.timer = None

    def start_timer(self):
        n = int(self.sliderPeople.get())
        m = int(self.sliderJumps.get())
        k = int(self.sliderSurvivors.get())
        i = int(self.sliderStartFrom.get())
        interval = int(self.sliderSpeed.get())
        yp(n, m, k, self, interval, i)

    def draw_circle(self, n):
        self.clear_circle()
        self.active = True
        n = int(n)
        self.sliderStartFrom.config(to=n)
        self.sliderSurvivors.config(to=n)
        self.sliderJumps.config(to=n)
        if n>=1:
            self.playButton.config(state='active')
        else:
            self.playButton.config(state='disabled')
            return
        # Calculate the positions of the numbers in the circle
        angle_increment = 2 * math.pi / n
        for i in range(n):
            angle = i * angle_increment
            x = self.circle_center[0] + self.circle_size * math.cos(angle)
            y = self.circle_center[1] + self.circle_size * math.sin(angle)
            number_label = self.canvas.create_text(x, y, text=str(i+1))
            self.numbers[i+1] = number_label

    def remove_numbers(self, number_to_remove):
        self.canvas.delete(self.numbers[number_to_remove])
        del self.numbers[number_to_remove]
                   
    def clear_circle(self):
        self.active = False
        for number_label in self.numbers.values():
            self.canvas.delete(number_label)
        self.numbers = {}

root = tk.Tk()
app = CircleNumbers(root)

# Center the UI elements more vertically
app.labelSurvivors.pack_configure(anchor=tk.CENTER)
app.sliderSurvivors.pack_configure(anchor=tk.CENTER)
app.sliderSpeed.pack_configure(anchor=tk.CENTER)
app.button.pack_configure(anchor=tk.CENTER)
app.canvas.pack_configure(anchor=tk.CENTER)

root.mainloop()
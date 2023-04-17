import tkinter as tk
import math
import time
import textwrap
from PIL import Image, ImageTk
import pyttsx3

# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()

def yp(n, m, k, view, interval, i = 0):
    message = ""
    # 0<n     n elements in the circle
    # 1<=m<=n    reduce the m element after the current existing element
    # 1<=k<=n k elements remain in the circle at the end of process
    # print("n =", n, " m =", m, " k =", k)
    if view.checkbox_var.get() is True:
        i = n - i - 1
    l = [i for i in range(1, n+1)]
    while (len(l) > k and view.active):
        view.playButton.config(state='disabled')
        i = (i + m) % len(l)
        j = len(l) - i - 1
        if view.checkbox_var.get() is False:
            view.remove_numbers(l[i])
            l.remove(l[i])
        else:
            # print(f"l is \n{l}\nj is\n{j}\nl[j] is \n{l[j]}\nview.numbers is\n{view.numbers}\n")
            view.remove_numbers(l[j])
            l.remove(l[j])
        view.master.update()
        time.sleep(interval/2)
    view.playButton.config(state='active')
    if m == 1 and k==1 and view.active and view.checkbox_var.get() is False:
     message = "n = " + str(n) + " survive by algorithm = " + str(l) + ", survive by formula = " + str(int(2 * (n - math.pow(2, math.floor(math.log(n, 2)))) + 1))
     view.display_endgame_msg(message)
    #  print("n =", n, "survive by algorithm =", l, \
    #        "survive by formula =", \
    #        int(2 * (n - math.pow(2, math.floor(math.log(n, 2)))) + 1))
    elif view.active:
        message = "n = " + str(n) + " survive by algorithm = " + str(l)
        view.display_endgame_msg(message)
        # print("n =", n, "survive by algorithm =", l)
    else:
        pass
    engine.say(message)
        # say method on the engine that passing input text to be spoken
    
    # run and wait method, it processes the voice commands.
    engine.runAndWait()
        # print("Game canceled")

        
class CircleNumbers:
    def __init__(self, master):
        self.master = master
        self.active = True
        master.title("YP_Problem")
        master.geometry("900x650")
        master.resizable(False, False)
        master.wm_attributes("-topmost", 1)

        # Create a frame to hold the slider and button
        frame = tk.Frame(master)
        frame.pack(side=tk.RIGHT, padx=50)

        # Create the "People" label
        self.labelSurvivors = tk.Label(frame, text="People:")
        self.labelSurvivors.pack(pady=2)

        # Create the slider
        self.sliderPeople = tk.Scale(frame, from_=1, to=50, orient=tk.HORIZONTAL, command=self.draw_circle)
        self.sliderPeople.pack(pady=10)

        # Create the "Speed" label
        self.labelSpeed = tk.Label(frame, text="Speed:")
        self.labelSpeed.pack(pady=2)

        # Create the slider
        self.sliderSpeed = tk.Scale(frame, from_=1, to=3, orient=tk.HORIZONTAL)
        self.sliderSpeed.pack(pady=2)

        # Create the "Jumps" label
        self.labelJumps = tk.Label(frame, text="Jumps:")
        self.labelJumps.pack(pady=2)

        # Create the slider
        self.sliderJumps = tk.Scale(frame, from_=1, to=42, orient=tk.HORIZONTAL)
        self.sliderJumps.pack(pady=2)

        # Create the "Start from" label
        self.labelStartFrom = tk.Label(frame, text="Start from:")
        self.labelStartFrom.pack(pady=2)

        # Create the slider
        self.sliderStartFrom = tk.Scale(frame, from_=1, to=42, orient=tk.HORIZONTAL)
        self.sliderStartFrom.pack(pady=2)

        # Create the "Survivors" label
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
        self.canvas = tk.Canvas(master, width=900, height=600)
        self.canvas.pack()
        self.canvas.image_refs = []
        
        # Calculate the center coordinates of the root window
        root_width = root.winfo_width()
        root_height = root.winfo_height()
        canvas_width = 900
        canvas_height = 600
        x = (root_width - canvas_width) // 2
        y = (root_height - canvas_height) // 2

        # Place the canvas at the center of the root window
        self.canvas.place(x=x, y=y)

        # Create the "PLAY" button
        self.playButton = tk.Button(frame, text="Start", command=self.start_timer, state='disabled')
        self.playButton.pack(pady=2)

        # # Create the "Restart" button
        # self.button = tk.Button(frame, text="Restart", command=lambda: self.clear_circle(True))
        # self.button.pack(pady=2)
        
        self.endgame_text = tk.Label(self.master, text="", font=("Arial", 12))
        self.endgame_text.place(relx = 0.0, rely = 1.0, anchor ='sw')

        # Initialize variables
        self.numbers = {}
        self.images = {}
        self.circle_size = 280  # radius of the circle
        self.circle_size_imgs = 255  # radius of the images circle
        self.circle_center = (350, 300)  # center of the circle
        self.timer = None

    def start_timer(self):
        n = int(self.sliderPeople.get())
        m = int(self.sliderJumps.get())
        k = int(self.sliderSurvivors.get())
        i = int(self.sliderStartFrom.get() - 1)
        interval = int(self.sliderSpeed.get())
        self.draw_circle(n)
        yp(n, m, k, self, interval, i)

    def draw_circle(self, n):
        self.clear_circle(False)
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
        
        self.draw_outer_circle(n)
        self.draw_inner_circle(n)
            
    def draw_outer_circle(self, n):
        # Calculate the positions of the numbers in the circle
        angle_increment = 2 * math.pi / n
        for i in range(n):
            angle = i * angle_increment - math.pi / 2 
            x = self.circle_center[0] + self.circle_size * math.cos(angle)
            y = self.circle_center[1] + self.circle_size * math.sin(angle)
            
            number_label = self.canvas.create_text(x, y, text=str(i+1))
            self.numbers[i+1] = number_label
            
            
    def draw_inner_circle(self, n):
        # Calculate the positions of the numbers in the circle
        angle_increment = 2 * math.pi / n
        for i in range(n):
            angle = i * angle_increment - math.pi / 2
            x_img = self.circle_center[0] + self.circle_size_imgs * math.cos(angle)
            y_img = self.circle_center[1] + self.circle_size_imgs * math.sin(angle)
            img = Image.open("Seminar_SE\glad.png")
            photo = ImageTk.PhotoImage(img)
            self.canvas.image_refs.append(photo)
            photo_output = self.canvas.create_image(x_img, y_img, image=photo)
            self.images[i+1] = photo_output
            
            

    def remove_numbers(self, number_to_remove):
        self.canvas.delete(self.numbers[number_to_remove])
        self.canvas.delete(self.images[number_to_remove])
        del self.numbers[number_to_remove]
        del self.images[number_to_remove]
                   
    def clear_circle(self, from_restart):
        if (from_restart):
            self.sliderPeople.set(0)
        self.endgame_text.config(text = "")
        self.active = False
        for number_label in self.numbers.values():
            self.canvas.delete(number_label)
        self.numbers = {}
        self.images = {}
        self.canvas.image_refs = []
        self.canvas.delete('all')
        
    def display_endgame_msg(self, message):
        message = textwrap.fill(message, width=100)
        self.endgame_text.config(text = message)   

root = tk.Tk()
app = CircleNumbers(root)

# Center the UI elements more vertically
app.labelSurvivors.pack_configure(anchor=tk.CENTER)
app.sliderSurvivors.pack_configure(anchor=tk.CENTER)
app.sliderSpeed.pack_configure(anchor=tk.CENTER)
#app.button.pack_configure(anchor=tk.CENTER)
app.canvas.pack_configure(anchor=tk.CENTER)

root.mainloop()
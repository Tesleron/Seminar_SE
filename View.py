import tkinter as tk
import math 

class CircleNumbers:
    def init(self, master):
        self.master = master
        master.title("Circle of Numbers")
        master.geometry("500x500")

        # Create the UI elements
        self.label = tk.Label(master, text="Select a number:")
        self.label.pack()
        self.slider = tk.Scale(master, from_=0, to=42, orient=tk.HORIZONTAL, command=self.draw_circle)
        self.slider.pack()

        # Initialize variables
        self.numbers = []
        self.circle_size = 175  # radius of the circle
        self.circle_center = (250, 250)  # center of the circle
        self.timer = None

    def draw_circle(self, n):
        # Clear any existing numbers and cancel the timer
        self.clear_circle()
        self.cancel_timer()

        # Get the current slider value as an integer
        n = int(n)

        # Calculate the positions of the numbers in the circle
        angle_increment = 2 * math.pi / n
        for i in range(n):
            angle = i * angle_increment
            x = self.circle_center[0] + self.circle_size * math.cos(angle)
            y = self.circle_center[1] + self.circle_size * math.sin(angle)
            number_label = tk.Label(self.master, text=str(i))
            number_label.place(x=x, y=y)
            self.numbers.append(number_label)

        # Start the timer to remove numbers
        self.timer = self.master.after(3000, self.remove_numbers)

    def remove_numbers(self):
        if len(self.numbers) > 1:
            number_to_remove = self.numbers.pop(0)
            number_to_remove.destroy()
            self.timer = self.master.after(3000, self.remove_numbers)

    def clear_circle(self):
        for number_label in self.numbers:
            number_label.destroy()
        self.numbers = []

    def cancel_timer(self):
        if self.timer is not None:
            self.master.after_cancel(self.timer)
            self.timer = None


root = tk.Tk()
app = CircleNumbers(root)
root.mainloop()

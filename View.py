import tkinter as tk
import math
import textwrap
from PIL import Image, ImageTk
from Logic import yp
from pygame import mixer

# init function to get an engine instance for the speech synthesis

class CircleNumbers:
    def __init__(self, master):
        self.master = master
        self.active = True
        master.title("YP_Problem")
        master.geometry("900x650")
        master.resizable(False, False)
        master.wm_attributes("-topmost", 1)
        # Instantiate mixer
        mixer.init()
        # Load audio file
        mixer.music.load('fall.wav')
        print("music started playing....")
        # Set preferred volume
        mixer.music.set_volume(0.2)
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
        """
        Start a timer with given parameters.

        :param self (object): The instance of the class that this method belongs to.
        :return: None
        """
        # Get values from sliders
        n = int(self.sliderPeople.get())  # Number of people
        m = int(self.sliderJumps.get())  # Number of jumps
        k = int(self.sliderSurvivors.get())  # Number of survivors
        i = int(self.sliderStartFrom.get() - 1)  # Starting index (0-based)
        interval = int(self.sliderSpeed.get())  # Time interval

        # Draw circles based on the number of people
        self.draw_circle(n)

        # Call yp() function with given parameters to start the timer
        yp(n, m, k, self, interval, i)

    def draw_circle(self, n):
        """
        Draw a circle with given number of people.

        :param self (object): The instance of the class that this method belongs to.
        :param n (int): Number of people.
        :return: None
        """
        self.clear_circle(False)  # Clear previous circles
        self.active = True  # Set "active" flag to True
        n = int(n)  # Convert n to integer
        self.sliderStartFrom.config(to=n)  # Update "Start From" slider's maximum value
        self.sliderSurvivors.config(to=n)  # Update "Survivors" slider's maximum value
        self.sliderJumps.config(to=n)  # Update "Jumps" slider's maximum value
        if n >= 1:
            self.playButton.config(state='active')  # Enable "Play" button if n is greater than or equal to 1
        else:
            self.playButton.config(state='disabled')  # Disable "Play" button if n is less than 1
            return
        self.draw_outer_circle(n)  # Draw outer circle
        self.draw_inner_circle(n)  # Draw inner circle
            
    def draw_outer_circle(self, n):
        """
        Draw the outer circle with numbers positioned evenly on the circumference.

        :param self (object): The instance of the class that this method belongs to.
        :param n (int): Number of people.
        :return: None
        """
        # Calculate the angle increment between each number on the circumference
        angle_increment = 2 * math.pi / n

        # Loop through each number and calculate its position on the circumference
        for i in range(n):
            angle = i * angle_increment - math.pi / 2  # Calculate the angle for each number
            x = self.circle_center[0] + self.circle_size * math.cos(angle)  # Calculate x-coordinate
            y = self.circle_center[1] + self.circle_size * math.sin(angle)  # Calculate y-coordinate

            number_label = self.canvas.create_text(x, y, text=str(i+1))  # Create a text label for the number
            self.numbers[i+1] = number_label  # Store the text label in a dictionary with the number as the key
                
    def draw_inner_circle(self, n):
        """
        Draw the inner circle with images positioned evenly on the circumference.

        :param self (object): The instance of the class that this method belongs to.
        :param n (int): Number of people.
        :return: None
        """
        # Calculate the angle increment between each image on the circumference
        angle_increment = 2 * math.pi / n

        # Loop through each image and calculate its position on the circumference
        for i in range(n):
            angle = i * angle_increment - math.pi / 2  # Calculate the angle for each image
            x_img = self.circle_center[0] + self.circle_size_imgs * math.cos(angle)  # Calculate x-coordinate
            y_img = self.circle_center[1] + self.circle_size_imgs * math.sin(angle)  # Calculate y-coordinate

            img = Image.open("./glad.png")  # Open the image file
            photo = ImageTk.PhotoImage(img)  # Create a PhotoImage object from the image
            self.canvas.image_refs.append(photo)  # Append the PhotoImage object to a list for reference
            photo_output = self.canvas.create_image(x_img, y_img, image=photo)  # Create an image item on the canvas
            self.images[i+1] = photo_output  # Store the image item in a dictionary with the image number as the key
                
        
    def remove_numbers(self, number_to_remove):
        """
        Remove a number label and image from the canvas.

        :param self (object): The instance of the class that this method belongs to.
        :param number_to_remove (int): The number to remove.
        :return: None
        """
        self.canvas.delete(self.numbers[number_to_remove])  # Delete the number label from the canvas
        self.canvas.delete(self.images[number_to_remove])  # Delete the image from the canvas
        # Play the music
        mixer.music.play()
        del self.numbers[number_to_remove]  # Remove the number from the numbers dictionary
        del self.images[number_to_remove]  # Remove the image from the images dictionary


    def clear_circle(self, from_restart):
        """
        Clear the canvas and reset the game state.

        :param self (object): The instance of the class that this method belongs to.
        :param from_restart (bool): Whether the clear is called from a game restart.
        :return: None
        """
        if from_restart:
            self.sliderPeople.set(0)  # Reset the slider value to 0 if called from a game restart
        self.endgame_text.config(text="")  # Clear the endgame text on the canvas
        self.active = False  # Set the game state to inactive
        for number_label in self.numbers.values():
            self.canvas.delete(number_label)  # Delete all number labels from the canvas
        self.numbers = {}  # Clear the numbers dictionary
        self.images = {}  # Clear the images dictionary
        self.canvas.image_refs = []  # Clear the image references list
        self.canvas.delete('all')  # Delete all items from the canvas
        
    def display_endgame_msg(self, message):
        """
        Display the endgame message on the canvas.

        :param self (object): The instance of the class that this method belongs to.
        :param message (str): The endgame message to display on the canvas.
        :return: None
        """
        message = textwrap.fill(message, width=100)  # Format the message to fit within 100 characters per line
        self.endgame_text.config(text=message)  # Set the endgame text on the canvas to the formatted message  

root = tk.Tk()
app = CircleNumbers(root)

# Center the UI elements more vertically
app.labelSurvivors.pack_configure(anchor=tk.CENTER)
app.sliderSurvivors.pack_configure(anchor=tk.CENTER)
app.sliderSpeed.pack_configure(anchor=tk.CENTER)
app.canvas.pack_configure(anchor=tk.CENTER)

root.mainloop()
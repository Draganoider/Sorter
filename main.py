import tkinter as tk
import numpy as np
import time
import pygame

# Initialize pygame
pygame.init()

# Constants
NUM_BARS = 200
BAR_WIDTH = 600 / NUM_BARS
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 400

# Load beep sound
pygame.mixer.init()
beep_sound = pygame.mixer.Sound("sound93.wav")  # Replace "beep.wav" with the path to your sound file

class SortingVisualizer:
    def __init__(self, master, data):
        self.master = master
        self.master.title("Sorting Visualizer")

        self.data = data
        self.canvas = tk.Canvas(self.master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
        self.canvas.pack()

    def draw_bars(self):
        self.canvas.delete("all")
        for i, value in enumerate(self.data):
            x1, y1 = i * BAR_WIDTH, CANVAS_HEIGHT
            x2, y2 = (i + 1) * BAR_WIDTH, CANVAS_HEIGHT - value * 4
            self.canvas.create_rectangle(x1, y1, x2, y2, fill='blue')

        self.master.update()
        ##time.sleep(0.1)  # Adjust sleep time to control animation speed

    def play_beep(self):
        beep_sound.play()

    def bubble_sort(self):
        n = len(self.data)

        for i in range(n):
            for j in range(0, n - i - 1):
                if self.data[j] > self.data[j + 1]:
                    # Swap the elements if they are in the wrong order
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    # Draw the current state for visualization
                    self.draw_bars()
                    # Play a beep sound after each swap
                    #

            self.play_beep()


def main():
    root = tk.Tk()

    # Generate random data
    data_to_sort = np.random.randint(1, 100, NUM_BARS)

    visualizer = SortingVisualizer(root, data_to_sort)

    # Display the initial state
    visualizer.draw_bars()

    # Run the Bubble Sort algorithm and visualize the process
    visualizer.bubble_sort()

    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
import random

# Game window
WIDTH, HEIGHT = 400, 600
root = tk.Tk()
root.title("Flappy Bird (Tkinter Edition)")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="skyblue")
canvas.pack()

# Bird
bird_size = 20
bird = canvas.create_oval(50, HEIGHT//2 - bird_size, 50 + bird_size, HEIGHT//2, fill="yellow")
bird_velocity = 0
gravity = 0.50
flap_strength = -10

# Pipes
pipe_width = 60
pipe_gap = 150
pipes = []
pipe_speed = 3

score = 0
score_text = canvas.create_text(WIDTH//2, 30, text=f"Score: {score}", font=("Arial", 20), fill="white")

def flap(event):
    global bird_velocity
    bird_velocity = flap_strength

root.bind("<space>", flap)

def create_pipe():
    gap_y = random.randint(100, HEIGHT - 100)
    top_pipe = canvas.create_rectangle(WIDTH, 0, WIDTH + pipe_width, gap_y - pipe_gap//2, fill="green")
    bottom_pipe = canvas.create_rectangle(WIDTH, gap_y + pipe_gap//2, WIDTH + pipe_width, HEIGHT, fill="green")
    pipes.append((top_pipe, bottom_pipe))

def move_pipes():
    global score
    for top, bottom in pipes:
        canvas.move(top, -pipe_speed, 0)
        canvas.move(bottom, -pipe_speed, 0)
        if canvas.coords(top)[2] < 0:
            canvas.delete(top)
            canvas.delete(bottom)
            pipes.remove((top, bottom))
            score += 1
            canvas.itemconfig(score_text, text=f"Score: {score}")

def check_collision():
    bird_coords = canvas.coords(bird)
    if bird_coords[1] <= 0 or bird_coords[3] >= HEIGHT:
        return True
    for top, bottom in pipes:
        if overlap(bird_coords, canvas.coords(top)) or overlap(bird_coords, canvas.coords(bottom)):
            return True
    return False

def overlap(a, b):
    return not (a[2] < b[0] or a[0] > b[2] or a[3] < b[1] or a[1] > b[3])

def game_loop():
    global bird_velocity
    bird_velocity += gravity
    canvas.move(bird, 0, bird_velocity)
    move_pipes()
    if check_collision():
        canvas.create_text(WIDTH//2, HEIGHT//2, text="Game Over", font=("Arial", 30), fill="red")
        return
    if random.randint(1, 100) == 1:
        create_pipe()
    root.after(30, game_loop)

create_pipe()
game_loop()
root.mainloop()

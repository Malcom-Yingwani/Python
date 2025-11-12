import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.

while True:
    # Make a random walk.
    # rw = RandomWalk()
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use("classic")
    
    # fig, ax = plt.subplots()
    # fig, ax = plt.subplots(figsize = (15, 9))
    fig, ax = plt.subplots(figsize = (10, 6), dpi = 128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c = point_numbers, cmap = plt.cm.Blues, edgecolors = "none", s=1) # edge colors removes the outline around each point
    ax.set_aspect("equal")
    
    # Emphasise the first and last points.
    ax.scatter(0, 0, c = "green", edgecolors = "none", s = 100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c = "red", edgecolors = "none", s = 100)
    
    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n): " )
    if keep_running == "n":
        break
    
# =====================================================================================================
# Chat GPT SUMMARY
# =====================================================================================================
# Purpose:
#   - Visualizes random walks using matplotlib and the RandomWalk class.
# =====================================================================================================
# Core Functionality:
#   - Continuously generates and displays new random walks until the user quits.
#   - Each walk consists of 50,000 points filled by rw.fill_walk().
# =====================================================================================================
# Visualization:
#   - Plots the random walk using a blue color gradient (cmap=Blues).
#   - Highlights the start (green) and end (red) points.
#   - Uses equal aspect ratio and hides axes for a cleaner look.
# =====================================================================================================
# User Interaction:
#   - After each plot, prompts “Make another walk? (y/n)” to continue or exit.
# =====================================================================================================

{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOpdwDQJyIFBv2dFVmFNaK/",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/mohamedafzal1245/Autonomous-Vehicles-And-Robotics/blob/main/project.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "QCLzTzlv3t-r"
      },
      "outputs": [],
      "source": [
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "\n",
        "# Vehicle class\n",
        "class Vehicle:\n",
        "    def __init__(self, start, goal, obstacles):\n",
        "        \"\"\" Initialize the vehicle, its path, and obstacles \"\"\"\n",
        "        self.position = np.array(start, dtype=float)\n",
        "        self.goal = np.array(goal, dtype=float)\n",
        "        self.path = [self.position.copy()]\n",
        "        self.obstacles = obstacles\n",
        "        self.speed = 1.0\n",
        "\n",
        "    def move(self):\n",
        "        \"\"\" Move the vehicle towards the goal while avoiding obstacles \"\"\"\n",
        "        direction = self.goal - self.position\n",
        "        distance = np.linalg.norm(direction)\n",
        "\n",
        "        # Check if the vehicle has reached its goal\n",
        "        if distance < 1:\n",
        "            return False\n",
        "\n",
        "        # Normalize the direction vector\n",
        "        direction = direction / distance\n",
        "\n",
        "        # Obstacle avoidance logic\n",
        "        for obs in self.obstacles:\n",
        "            vec_to_obs = obs - self.position\n",
        "            dist = np.linalg.norm(vec_to_obs)\n",
        "\n",
        "            if dist < 5:  # Avoid if too close\n",
        "                direction += (self.position - obs) / (dist + 1e-5)  # Prevent division by zero\n",
        "\n",
        "        # Normalize the new direction vector\n",
        "        direction = direction / np.linalg.norm(direction)\n",
        "\n",
        "        # Move the vehicle\n",
        "        self.position += direction * self.speed\n",
        "        self.path.append(self.position.copy())\n",
        "\n",
        "        return True\n",
        "\n",
        "    def run(self):\n",
        "        \"\"\" Keep moving until the goal is reached \"\"\"\n",
        "        while self.move():\n",
        "            pass\n",
        "\n",
        "\n",
        "# Define start, goal, and obstacles\n",
        "start = (10, 10)\n",
        "goal = (90, 90)\n",
        "\n",
        "obstacles = np.array([\n",
        "    [40, 40],\n",
        "    [50, 50],\n",
        "    [60, 60],\n",
        "    [45, 60],\n",
        "    [70, 40]\n",
        "])\n",
        "\n",
        "# Run simulation\n",
        "vehicle = Vehicle(start, goal, obstacles)\n",
        "vehicle.run()\n",
        "\n",
        "# Plot the result\n",
        "path = np.array(vehicle.path)\n",
        "\n",
        "plt.figure(figsize=(8, 8))\n",
        "plt.plot(path[:, 0], path[:, 1], label=\"Path\", linewidth=2)\n",
        "plt.scatter(*zip(*obstacles), c='red', label=\"Obstacles\")\n",
        "plt.scatter(*start, c='blue', label=\"Start\", s=100)\n",
        "plt.scatter(*goal, c='green', label=\"Goal\", s=100)\n",
        "plt.legend()\n",
        "plt.grid(True)\n",
        "plt.title(\"Autonomous Vehicle Path Planning with Obstacle Avoidance\")\n",
        "plt.xlabel(\"X\")\n",
        "plt.ylabel(\"Y\")\n",
        "plt.show()"
      ]
    }
  ]
}
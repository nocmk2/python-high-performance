from matplotlib import pyplot as plt
from matplotlib import animation
from Particle import Particle
from ParticleSimulator import ParticleSimulator

def visualize(simulator):
    X = [p.x for p in simulator.particles]
    Y = [p.y for p in simulator.particles]

    fig = plt.figure()
    ax = plt.subplot(111, aspect='equal')
    line, = ax.plot(X, Y, 'ro')

    # Axis limits 
    plt.xlim(-1, 1)
    plt.ylim(-1, 1)

    # It will be run when the animation starts
    def init():
       line.set_data([], [])
       return line, # The comma is important!
    def animate(i):
       # We let the particle evolve for 0.01 time units
       simulator.evolve(0.01)
       X = [p.x for p in simulator.particles]
       Y = [p.y for p in simulator.particles]
       line.set_data(X, Y)
       return line,
    # Call the animate function each 10 ms
    anim = animation.FuncAnimation(fig,
                                  animate,
                                  init_func=init,
                                  blit=True,
                                  interval=10)
    plt.show()


def test_visualize():
   particles = [Particle(0.3, 0.5, 1),Particle(0.0, -0.5, -1),Particle(-0.1, -0.4, 3)]
   simulator = ParticleSimulator(particles)
   visualize(simulator)

if __name__ == '__main__':
    test_visualize()

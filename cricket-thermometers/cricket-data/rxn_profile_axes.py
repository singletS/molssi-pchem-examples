import matplotlib.pyplot as plt

with plt.xkcd():
    fig, ax = plt.subplots()
    fig.set_size_inches(8,6)
    # We need to draw the canvas, otherwise the labels won't be positioned and
    # won't have values yet.
    fig.canvas.draw()

    xlabels = ['' for item in ax.get_xticklabels()]
    xlabels[0] = 'Reactants'
    xlabels[-1] = 'Products'

    ylabels = ['' for item in ax.get_yticklabels()]

    ax.set_xticklabels(xlabels)
    ax.set_yticklabels(ylabels)

    plt.xlabel('Reaction Progress')
    plt.ylabel('Energy')
    #plt.show()
    plt.savefig('rxn-profile-axes.png')

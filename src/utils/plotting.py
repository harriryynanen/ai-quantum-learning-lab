import matplotlib.pyplot as plt


def plot_loss_distribution(losses, title="Monte Carlo loss distribution"):
    plt.hist(losses, bins=30)
    plt.xlabel("Portfolio loss")
    plt.ylabel("Frequency")
    plt.title(title)
    plt.show()

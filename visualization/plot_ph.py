import pandas as pd
import matplotlib.pyplot as plt


def plot_ph():

    df = pd.read_csv("data/patients.csv")

    plt.figure()

    plt.plot(df["day"], df["pH"])

    plt.xlabel("Days")
    plt.ylabel("pH")
    plt.title("Evolution of pH over 43 days (Simulated Patient)")

    plt.axhspan(6, 6.5, color='#30D158', alpha=0.2, label="Healthy")
    plt.axhspan(6.5, 7.2, color='#FFA94D', alpha=0.2, label="Risk of infection")
    plt.axhspan(7.2, 8, color='#FF6B6B', alpha=0.2, label="Infection")

    plt.legend()
    plt.savefig("visualization/ph_plot.png", dpi=300, bbox_inches="tight")
    plt.show()
import pandas as pd
import matplotlib.pyplot as plt


def plot_spo2():

    df = pd.read_csv("data/patients.csv")

    plt.figure()

    plt.plot(df["day"], df["SpO2"])

    plt.xlabel("Days")
    plt.ylabel("SpO2")
    plt.title("Oxygen Saturation Over 43 Days (Simulated Patient)")

    plt.axhspan(94, 100, color='#30D158', alpha=0.2, label="Healthy")
    plt.axhspan(90, 94, color='#FFA94D', alpha=0.2, label="Risk")
    plt.axhspan(70, 90, color='#FF6B6B', alpha=0.2, label="Critical")

    plt.legend()
    plt.savefig("visualization/SpO2_plot.png", dpi=300)
    plt.show()
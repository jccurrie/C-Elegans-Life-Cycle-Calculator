import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from c_elegans_model import TIME_FORMAT
import os


OUTPUT_DIR = "life_cycle_graphs"  # Directory to save files
os.makedirs(OUTPUT_DIR, exist_ok=True)  # Ensure the directory exists


def display_life_cycle(life_cycle_data):
    """
    Prints the calculated life cycle times for each temperature.
    """
    for temp, data in life_cycle_data.items():
        print(f"\n=== Life Cycle at {temp} ===")
        for stage, time in zip(data["Stages"], data["Times"]):
            print(f"Stage: {stage.ljust(5)} - Time: {time}")


def plot_life_cycle(life_cycle_data):
    """
    Generates a Seaborn plot for C. elegans life cycle and saves it as an image file.
    """
    worm_data = []
    for temp, data in life_cycle_data.items():
        for stage, time in zip(data["Stages"], data["Times"]):
            worm_data.append({"Temperature": temp, "Stage": stage, "Time": time})

    df = pd.DataFrame(worm_data)
    df["Time"] = pd.to_datetime(df["Time"], format=TIME_FORMAT)

    sns.set_theme(style="whitegrid")

    temp_order = ["15C", "20C", "25C"]
    pastel_palette = sns.color_palette("pastel")
    custom_palette = {
        "15C": pastel_palette[0],
        "20C": pastel_palette[4],
        "25C": pastel_palette[3],
    }

    fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharex=True)

    for ax, temp in zip(axes, temp_order):
        temp_df = df[df["Temperature"] == temp]
        sns.lineplot(
            x="Stage",
            y="Time",
            data=temp_df,
            marker="o",
            linewidth=2,
            markersize=8,
            color=custom_palette[temp],
            ax=ax,
        )

        ax.set_title(f"{temp}", fontsize=14)
        ax.set_xlabel("Life Stages")
        ax.set_ylabel("Time")

        y_ticks = np.sort(temp_df["Time"].unique())
        ax.set_yticks(y_ticks)
        ax.yaxis.set_major_formatter(mdates.DateFormatter("%m/%d %I:%M %p"))

        ax.tick_params(axis="x", rotation=30)
        ax.yaxis.grid(True, linestyle="--", linewidth=0.5)

    plt.suptitle("C. Elegans Life Cycle Stages at Different Temperatures", fontsize=16)
    plt.tight_layout()

    # Save plot to a file
    file_path = os.path.join(OUTPUT_DIR, "c_elegans_life_cycle.png")
    plt.savefig(file_path, format="png")
    plt.close()

    return file_path

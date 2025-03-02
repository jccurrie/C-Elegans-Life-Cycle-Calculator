from datetime import datetime, timedelta
from matplotlib import ticker
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# C. Elegans Life Stages
STAGES = ["EGG", "L1", "L2", "L3", "L4", "ADULT"]

# Date-Time Format
TIME_FORMAT = "%m/%d/%Y %I:%M %p"

# Worm Stages and Times at Different Storage Temperatures
WORM_LIFE_CYCLE = {
    "25C": {"Stages": STAGES, "Times": []},
    "20C": {"Stages": STAGES, "Times": []},
    "15C": {"Stages": STAGES, "Times": []},
}

# Time intervals for different temperatures (in hours)
TIME_INTERVALS = {
    "L1": {"25C": 8, "20C": 10.4, "15C": 16.8},
    "L2": {"25C": 20, "20C": 26, "15C": 42},
    "L3": {"25C": 27, "20C": 35.1, "15C": 56.7},
    "L4": {"25C": 34, "20C": 44.2, "15C": 71.4},
    "ADULT": {"25C": 43, "20C": 55.9, "15C": 90.3},
}


def get_user_input():
    """
    Prompts user for the starting date/time and returns a formatted datetime object.
    """
    while True:
        date_str = input("Enter the starting date (MM/DD/YYYY HH:MM AM/PM): ")
        try:
            return datetime.strptime(date_str, TIME_FORMAT)
        except ValueError:
            print(
                "❌ Invalid format! Please enter the date in 'MM/DD/YYYY HH:MM AM/PM' format."
            )


def calculate_life_cycle(start_time: str):
    """
    Calculates the life cycle times based on storage temperature and stage.
    """
    for temp in WORM_LIFE_CYCLE:
        WORM_LIFE_CYCLE[temp]["Times"].append(start_time.strftime(TIME_FORMAT))

    for stage in STAGES[1:]:  # Skip 'EGG' as it's the starting point
        for temp in WORM_LIFE_CYCLE:
            new_time = start_time + timedelta(hours=TIME_INTERVALS[stage][temp])
            WORM_LIFE_CYCLE[temp]["Times"].append(new_time.strftime(TIME_FORMAT))


def display_life_cycle():
    """
    Prints the calculated life cycle times for each temperature.
    """
    for temp, data in WORM_LIFE_CYCLE.items():
        print(f"\n=== Life Cycle at {temp} ===")
        for stage, time in zip(data["Stages"], data["Times"]):
            print(f"Stage: {stage.ljust(5)} - Time: {time}")


def plot_life_cycle():
    """
    Generates subplots of the life cycle stages at different temperatures using Seaborn.
    """
    # Convert data into a DataFrame
    worm_data = []
    for temp, data in WORM_LIFE_CYCLE.items():
        for stage, time in zip(data["Stages"], data["Times"]):
            worm_data.append({"Temperature": temp, "Stage": stage, "Time": time})

    df = pd.DataFrame(worm_data)
    df["Time"] = pd.to_datetime(df["Time"], format=TIME_FORMAT)

    # Set Seaborn theme
    sns.set_theme(style="whitegrid")

    # Define temperature order and custom color palette
    temp_order = ["15C", "20C", "25C"]
    pastel_palette = sns.color_palette("pastel")
    custom_palette = {
        "15C": pastel_palette[0],
        "20C": pastel_palette[4],
        "25C": pastel_palette[3],
    }

    # Create subplots
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

        # Set custom y-ticks per subplot
        y_ticks = np.sort(temp_df["Time"].unique())
        ax.set_yticks(y_ticks)
        ax.yaxis.set_major_formatter(mdates.DateFormatter("%m/%d %I:%M %p"))

        ax.tick_params(axis="x", rotation=30)
        ax.yaxis.grid(True, linestyle="--", linewidth=0.5)

    plt.suptitle("C. Elegans Life Cycle Stages at Different Temperatures", fontsize=16)
    plt.tight_layout()
    plt.show()


def main():
    start_time = get_user_input()
    print(f"\nCycle Start Date: {start_time.strftime('%B %d, %Y %I:%M %p')}")
    calculate_life_cycle(start_time)
    display_life_cycle()
    plot_life_cycle()


if __name__ == "__main__":
    main()

# 0 Easy test time: 02/25/2025 08:00 AM

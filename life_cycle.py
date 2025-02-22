from datetime import datetime, timedelta
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
    Generates a line plot of the life cycle stages at different temperatures using Seaborn.
    """
    # Create a DataFrame that will be easier for Seaborn to plot
    worm_data = []
    for temp, data in WORM_LIFE_CYCLE.items():
        for stage, time in zip(data["Stages"], data["Times"]):
            worm_data.append({"Temperature": temp, "Stage": stage, "Time": time})

    df = pd.DataFrame(worm_data)

    # Convert 'Time' to datetime objects to ensure proper sorting
    df["Time"] = pd.to_datetime(df["Time"], format=TIME_FORMAT)

    # Set Seaborn theme
    sns.set_theme(style="whitegrid")

    # Define the correct order for the legend
    hue_order = ["15C", "20C", "25C"]

    # Use Seaborn's pastel palette and assign colors
    pastel_palette = sns.color_palette("pastel")

    # Custom color mapping using pastel colors
    custom_palette = {
        "15C": pastel_palette[0],
        "20C": pastel_palette[4],
        "25C": pastel_palette[3],
    }

    # Plotting time on the y-axis
    sns.lineplot(
        x="Stage",
        y="Time",
        hue="Temperature",
        data=df,
        marker="o",
        linewidth=2,
        markersize=8,
        hue_order=hue_order,
        palette=custom_palette,
    )

    # Format the plot
    plt.title("C. Elegans Life Cycle Stages at Different Temperatures", fontsize=16)
    plt.xlabel("Life Stages", fontsize=12)
    plt.ylabel("Time", fontsize=12)

    # Get all the unique times across all stages and temperatures for y-axis ticks
    all_times = df["Time"].unique()

    # Sort the times using numpy
    all_times = np.sort(all_times)

    # Set a time threshold (e.g., 3 hours) to group times
    time_threshold = pd.Timedelta(hours=3)

    # Group times into 3-hour windows and calculate the average time within each window
    averaged_times = []
    current_group = [all_times[0]]

    for current_time in all_times[1:]:
        # Check if the current time is within the threshold of the last time in the group
        if current_time - current_group[-1] <= time_threshold:
            current_group.append(current_time)
        else:
            # Calculate the average time for the current group
            # Convert datetime to integer (nanoseconds) for averaging
            avg_time = pd.to_datetime(np.mean(np.array(current_group).astype(np.int64)))
            averaged_times.append(avg_time)
            
            # Start a new group with the current time
            current_group = [current_time]

    # Don't forget to add the last group
    if current_group:
        avg_time = pd.to_datetime(np.mean(np.array(current_group).astype(np.int64)))
        averaged_times.append(avg_time)

    # Set the y-axis ticks to the averaged times
    plt.gca().set_yticks(averaged_times)

    # Format the y-axis to display times properly
    plt.gca().yaxis.set_major_formatter(mdates.DateFormatter("%m/%d/%Y %I:%M %p"))

    # Show the legend and tighten the layout
    plt.legend(title="Temperature")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Optional: Add gridlines for better readability
    plt.gca().yaxis.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.show()


def main():
    start_time = get_user_input()
    print(f"\nCycle Start Date: {start_time.strftime('%B %d, %Y %I:%M %p')}")
    calculate_life_cycle(start_time)
    display_life_cycle()
    plot_life_cycle()


if __name__ == "__main__":
    main()

# Easy test time: 02/25/2025 08:00 AM

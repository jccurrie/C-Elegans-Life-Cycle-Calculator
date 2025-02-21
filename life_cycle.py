from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt

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
    """Prompts user for the starting date/time and returns a formatted datetime object."""
    date_str = input("Enter the starting date (MM/DD/YYYY HH:MM AM/PM): ")
    return datetime.strptime(date_str, TIME_FORMAT)


def calculate_life_cycle(start_time):
    """Calculates the life cycle times based on storage temperature and stage."""
    for temp in WORM_LIFE_CYCLE:
        WORM_LIFE_CYCLE[temp]["Times"].append(start_time.strftime(TIME_FORMAT))

    for stage in STAGES[1:]:  # Skip 'EGG' as it's the starting point
        for temp in WORM_LIFE_CYCLE:
            new_time = start_time + timedelta(hours=TIME_INTERVALS[stage][temp])
            WORM_LIFE_CYCLE[temp]["Times"].append(new_time.strftime(TIME_FORMAT))


def display_life_cycle():
    """Prints the calculated life cycle times for each temperature."""
    for temp, data in WORM_LIFE_CYCLE.items():
        print(f"\n=== Life Cycle at {temp} ===")
        for stage, time in zip(data["Stages"], data["Times"]):
            print(f"Stage: {stage.ljust(5)} - Time: {time}")


def plot_life_cycle():
    """Generates a line plot of the life cycle stages at different temperatures."""
    df = pd.DataFrame(WORM_LIFE_CYCLE)
    fig, axes = plt.subplots(3, figsize=(12, 9), sharex=True)
    fig.suptitle("C. Elegans Life Cycle Stages")

    colors = {"25C": "b", "20C": "r", "15C": "g"}
    for ax, temp in zip(axes, WORM_LIFE_CYCLE.keys()):
        ax.plot(
            df[temp]["Stages"],
            df[temp]["Times"],
            color=colors[temp],
            marker="o",
            label=f"{temp}",
        )
        ax.legend(loc="upper left")
        ax.set_ylabel("Time")

    plt.xlabel("Life Stages")
    plt.xticks(rotation=45)
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()


def main():
    start_time = get_user_input()
    print(f"\nCycle Start Date: {start_time.strftime('%B %d, %Y %I:%M %p')}")
    calculate_life_cycle(start_time)
    display_life_cycle()
    plot_life_cycle()


if __name__ == "__main__":
    main()

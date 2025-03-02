# C. Elegans Life Cycle Tracker

This project calculates and visualizes the life cycle stages of _C. elegans_ (Caenorhabditis elegans) at different storage temperatures. The program allows users to input a start time, and it calculates the timing of various life stages (Egg, L1, L2, L3, L4, and Adult) based on specific temperature conditions.

## Version

- **Current Version**: `1.1.2`

## Features

- _Life Cycle Calculation:_ Computes the time taken to reach each life stage based on input temperature and start time.
- _Visualization:_ Generates plots that display the life cycle stages at different temperatures using Seaborn and Matplotlib.
- _Temperature Variability:_ Takes into account three different storage temperatures (15°C, 20°C, 25°C).
- _User Interface:_ Simple date-time input via NiceGUI, with error handling for invalid inputs.

## Requirements

- `Python` >= 3.10
- `nicegui`: For building a GUI interface.
- `seaborn`: For plotting life cycle data.
- `matplotlib`: For visualization.
- `pandas`: For data handling.
- `numpy`: For numerical computations.

## Installation

Clone the repository:
```git clone https://github.com/yourusername/C-Elegans-Life-Cycle-Calculator.git```

Navigate into the project folder:
```cd C-Elegans-Life-Cycle-Calculator```

Install all dependencies using requirements.txt:
```pip install -r requirements.txt```

## Usage

1. Start the application by running `main.py`.
2. The program will prompt you to input the starting date and time.
3. The program will calculate the life cycle stages and display the results, including a graphical visualization of the life cycle stages at the specified temperatures.

## Output Example

```
Cycle Start Date: February 21, 2025 08:00 AM

=== Life Cycle at 25C ===
Stage: EGG   - Time: 02/21/2025 08:00 AM
Stage: L1    - Time: 02/21/2025 04:00 PM
Stage: L2    - Time: 02/22/2025 12:00 AM
...
```

A graph will also be displayed, showing the life cycle progression for each temperature.

## License

This project is licensed under the MIT License.

## Contributing

Pull requests are welcome! If you have suggestions or find any issues, feel free to open an issue or submit a PR.

## Author

Julian Currie

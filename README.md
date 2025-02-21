# C. Elegans Life Cycle Tracker

This Python script calculates and visualizes the life cycle stages of *C. Elegans* at different storage temperatures (15°C, 20°C, and 25°C). It allows users to input a starting date and time, then estimates the transition times between developmental stages based on known time intervals.

## Features

- User input for the start date and time.
- Calculation of life cycle stages at 15°C, 20°C, and 25°C.
- Console output of calculated stage transition times.
- Visualization of life cycle progression with a line plot using Matplotlib.

## Requirements

This script requires the following Python libraries:

- `datetime`
- `pandas`
- `matplotlib`

To install the required libraries, run:

```bash
pip install pandas matplotlib
```

## Usage

Run the script using Python:

```bash
python script.py
```

When prompted, enter the starting date and time in the following format:

```
MM/DD/YYYY HH:MM AM/PM
```

Example input:

```
02/21/2025 08:00 AM
```

The script will output the estimated times for each life stage transition and display a plot comparing life cycles at different temperatures.

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


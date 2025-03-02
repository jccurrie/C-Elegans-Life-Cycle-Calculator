from nicegui import ui
from input_handler import get_user_input
from life_cycle_calculator import calculate_life_cycle
from life_cycle_graph_display import display_life_cycle, plot_life_cycle


def on_start_time_selected(start_time):
    """Callback function to calculate and display the life cycle with the graph."""
    print(f"\nCycle Start Date: {start_time.strftime('%B %d, %Y %I:%M %p')}")

    life_cycle_data = calculate_life_cycle(start_time)
    display_life_cycle(life_cycle_data)

    # Generate the Seaborn plot
    file_path = plot_life_cycle(life_cycle_data)

    # Display the graph on the page
    ui.label("C. Elegans Life Cycle Plot")
    ui.image(file_path).classes("rounded-lg shadow-lg")  # Display saved image

    # Download Button
    ui.button("Download Graph", on_click=lambda: ui.download(file_path)).classes(
        "mt-4 bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md"
    )


# Start NiceGUI app
get_user_input(on_start_time_selected)
ui.run(title="C. Elegans Life Cycle", port=8080)

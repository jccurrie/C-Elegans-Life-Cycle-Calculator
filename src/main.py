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

    # Update the graph display dynamically
    graph_display.set_source(file_path)

    # Show the download button
    download_button.classes(remove="hidden")


# Define layout
with ui.row().classes("w-full h-screen grid grid-cols-5 gap-4 p-4"):

    # Left Panel (Date Picker) - 1/5 width
    with ui.column().classes(
        "col-span-1 border-r border-gray-300 p-4 flex items-center justify-center"
    ):
        get_user_input(on_start_time_selected)

    # Right Panel (Graph Display) - 4/5 width
    with ui.column().classes("col-span-4 flex flex-col items-center justify-center"):
        ui.label("C. Elegans Life Cycle Plot").classes("text-lg font-bold mb-4")
        graph_display = ui.image("").classes(
            "w-4/5 max-h-[80vh] rounded-lg shadow-lg"
        )  # Bigger Graph

        # Download Button (Hidden Initially)
        download_button = ui.button(
            "Download Graph",
            on_click=lambda: (
                ui.download(graph_display.source) if graph_display.source else None
            ),
        ).classes("mt-4 bg-blue-500 text-white px-4 py-2 rounded-lg shadow-md hidden")


# Start NiceGUI app
ui.run(title="C. Elegans Life Cycle", port=8080)

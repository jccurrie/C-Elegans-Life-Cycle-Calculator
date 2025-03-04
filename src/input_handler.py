from nicegui import ui
from datetime import datetime
from c_elegans_model import TIME_FORMAT


def get_user_input(callback):
    """
    Displays a NiceGUI datetime picker and passes the selected time to the callback function.
    """

    def on_submit():
        if not date_picker.value or not time_picker.value:
            ui.notify("Invalid format! Please select both date and time.")
            return

        try:
            # Convert NiceGUI date (YYYY-MM-DD) to MM/DD/YYYY
            date_obj = datetime.strptime(date_picker.value, "%Y-%m-%d")
            formatted_date = date_obj.strftime("%m/%d/%Y")

            # Convert NiceGUI time (HH:MM in 24-hour format) to 12-hour format with AM/PM
            time_obj = datetime.strptime(time_picker.value, "%H:%M")
            formatted_time = time_obj.strftime("%I:%M %p")

            # Combine and parse into final datetime object
            selected_datetime = f"{formatted_date} {formatted_time}"
            start_time = datetime.strptime(selected_datetime, TIME_FORMAT)

            callback(start_time)  # Pass selected time to main
            ui.notify(f"Start time selected: {start_time.strftime(TIME_FORMAT)}")

        except ValueError as e:
            ui.notify(f"Error parsing date/time: {e}")

    with ui.row().classes("flex items-center justify-center"):  # Align date & time pickers in one row
        ui.label("Select starting Date & Time").classes("text-lg font-bold mb-4")
        date_picker = ui.date()
        time_picker = ui.time()
        ui.button("Submit", on_click=on_submit).classes("mt-2 w-1/2 bg-blue-500 text-white rounded-lg shadow-md")

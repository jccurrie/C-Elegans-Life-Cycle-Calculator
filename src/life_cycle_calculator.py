from datetime import timedelta
from c_elegans_model import STAGES, TIME_FORMAT, TIME_INTERVALS, WORM_LIFE_CYCLE


def calculate_life_cycle(start_time: str):
    """
    Calculates the life cycle times based on storage temperature and stage.
    """
    for temperature in WORM_LIFE_CYCLE:
        WORM_LIFE_CYCLE[temperature]["Times"].append(start_time.strftime(TIME_FORMAT))

    for stage in STAGES[
        1:
    ]:  # Skips the'EGG' life cycle stage as it's the starting point.
        for temperature in WORM_LIFE_CYCLE:
            new_time = start_time + timedelta(hours=TIME_INTERVALS[stage][temperature])
            WORM_LIFE_CYCLE[temperature]["Times"].append(new_time.strftime(TIME_FORMAT))

    return WORM_LIFE_CYCLE

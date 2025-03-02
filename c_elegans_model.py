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

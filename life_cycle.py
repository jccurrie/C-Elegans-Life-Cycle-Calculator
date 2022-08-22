#LIFE CYCLE OF C.ELEGANS
from datetime import datetime
from datetime import timedelta
starting_day = input("What is your starting Date? ( in MM/DD/YYYY HH:mm ): ")
stages = ["L2", "L3", "L4"]

def calcCycle(starting_day, stages):
    starting_day_ref = datetime.strptime(starting_day,"%m/%d/%Y %H:%M")
    print("Your cycle start date is : "+starting_day_ref.strftime('%B/%d/%Y %H:%M'))
    for stage in stages:
        if stage == "L2":
                temp25 = starting_day_ref + timedelta(hours=12)
                temp20 = starting_day_ref + timedelta(hours=15.6)
                temp15 = starting_day_ref + timedelta(hours=25.2)
                print("\n")
                print("L1 at temperature: ( 25c ) becomes L2 at: " + str(temp25))
                print("L1 at temperature: ( 20c ) becomes L2 at: " + str(temp20))
                print("L1 at temperature: ( 15c ) becomes L2 at: " + str(temp15))
                print("\n")

        elif stage == "L3":
                temp25 = starting_day_ref + timedelta(hours=19)
                temp20 = starting_day_ref + timedelta(hours=24.7)
                temp15 = starting_day_ref + timedelta(hours=39.9)
                print("L1 at temperature: ( 25c ) becomes L3 at: " + str(temp25))
                print("L1 at temperature: ( 20c ) becomes L3 at: " + str(temp20))
                print("L1 at temperature: ( 15c ) becomes L3 at: " + str(temp15))
                print("\n")

        elif stage == "L4":
                temp25 = starting_day_ref + timedelta(hours=26)
                temp20 = starting_day_ref + timedelta(hours=33.8)
                temp15 = starting_day_ref + timedelta(hours=54.6)
                print("L1 at temperature: ( 25c ) becomes L4 at: " + str(temp25))
                print("L1 at temperature: ( 20c ) becomes L4 at: " + str(temp20))
                print("L1 at temperature: ( 15c ) becomes L4 at: " + str(temp15))
                print("\n")

    return 0

calcCycle(starting_day,stages)
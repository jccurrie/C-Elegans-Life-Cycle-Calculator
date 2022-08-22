#LIFE CYCLE OF C.ELEGANS
from datetime import datetime
from datetime import timedelta

STAGES = ["EGG", "L1", "L2", "L3", "L4", "ADULT"]
TIME_FRAME = '%B %d %Y %I:%M %p'

starting_day = input("What is your starting Date? ( in MM DD YYYY HH:mm ): ")

def calcCycle(starting_day, STAGES):
        starting_day_ref = datetime.strptime(starting_day,"%m %d %Y %I:%M")
        print("Your cycle start date is : "+starting_day_ref.strftime('%B %d %Y %I:%M'))
        for stage in STAGES:
                if stage == "L1":
                        temp25 = starting_day_ref + timedelta(hours=8)
                        temp20 = starting_day_ref + timedelta(hours=10.4)
                        temp15 = starting_day_ref + timedelta(hours=16.8)
                        print("\n")
                        print("Egg at temperature: ( 25c ) becomes L1 at: " + str(temp25.strftime(TIME_FRAME)))
                        print("Egg at temperature: ( 20c ) becomes L1 at: " + str(temp20.strftime(TIME_FRAME)))
                        print("Egg at temperature: ( 15c ) becomes L1 at: " + str(temp15.strftime(TIME_FRAME)))
                        print("\n")

                if stage == "L2":
                        temp25 = starting_day_ref + timedelta(hours=20)
                        temp20 = starting_day_ref + timedelta(hours=26)
                        temp15 = starting_day_ref + timedelta(hours=42)
                        print("Egg at temperature: ( 25c ) becomes L2 at: " + str(temp25.strftime(TIME_FRAME)))
                        print("Egg at temperature: ( 20c ) becomes L2 at: " + str(temp20.strftime(TIME_FRAME)))
                        print("Egg at temperature: ( 15c ) becomes L2 at: " + str(temp15.strftime(TIME_FRAME)))
                        print("\n")

                elif stage == "L3":
                        temp25 = starting_day_ref + timedelta(hours=27)
                        temp20 = starting_day_ref + timedelta(hours=35.1)
                        temp15 = starting_day_ref + timedelta(hours=56.7)
                        print("Egg at temperature: ( 25c ) becomes L3 at: " + str(temp25.strftime(TIME_FRAME)))
                        print("Egg at temperature: ( 20c ) becomes L3 at: " + str(temp20.strftime(TIME_FRAME)))
                        print("Egg at temperature: ( 15c ) becomes L3 at: " + str(temp15.strftime(TIME_FRAME)))
                        print("\n")

                elif stage == "L4":
                        temp25 = starting_day_ref + timedelta(hours=34)
                        temp20 = starting_day_ref + timedelta(hours=44.2)
                        temp15 = starting_day_ref + timedelta(hours=71.4)
                        print("Egg at temperature: ( 25c ) becomes L4 at: " + str(temp25.strftime(TIME_FRAME)))
                        print("Egg at temperature: ( 20c ) becomes L4 at: " + str(temp20.strftime(TIME_FRAME)))
                        print("Egg at temperature: ( 15c ) becomes L4 at: " + str(temp15.strftime(TIME_FRAME)))
                        print("\n")

                elif stage == "ADULT":
                        temp25 = starting_day_ref + timedelta(hours=43)
                        temp20 = starting_day_ref + timedelta(hours=55.9)
                        temp15 = starting_day_ref + timedelta(hours=90.3)
                        print("Egg at temperature: ( 25c ) becomes ADULT at: " + str(temp25.strftime(TIME_FRAME)))
                        print("Egg at temperature: ( 20c ) becomes ADULT at: " + str(temp20.strftime(TIME_FRAME)))
                        print("Egg at temperature: ( 15c ) becomes ADULT at: " + str(temp15.strftime(TIME_FRAME)))
                        print("\n")

calcCycle(starting_day, STAGES)
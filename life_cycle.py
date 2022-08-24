from datetime import datetime
from datetime import timedelta
import pandas as pd
import matplotlib.pyplot as plt

'''C.Elegans life stages'''
STAGES = ["EGG", "L1", "L2", "L3", "L4", "ADULT"]

'''String format for time'''
TIME_FRAME = '%m %d %Y %I:%M %p'

'''Dictionary of worm Stages and Times at different storage temperatures 25Celcius,20Celcius,15Celcius'''
WORM = {
        'Temp' : {
                '25Celcius' : {
                        'Stage' : STAGES,
                        'Time' : []
                        },
                '20Celcius' : {
                        'Stage' : STAGES,
                        'Time' : []
                        },
                '15Celcius' : {
                        'Stage' : STAGES,
                        'Time' : []
                        }
                }
        }

def main():
        starting_day = getUserInput()
        calculate_cycle(starting_day, STAGES)
        printWorm()
        print("\n**************************\n")
        gen_dataframe()

'''Prompts user for input and returns string'''
def getUserInput():
        print("\n")
        starting_day = input("What is your starting Date? ( in MM DD YYYY HH:mm ): ")
        return starting_day

'''Caclulates life cycle based on storage temperature and stage.'''
def calculate_cycle(starting_day, STAGES):

        starting_day_ref = datetime.strptime(starting_day,"%m %d %Y %I:%M")
        print("Your cycle start date is : "+starting_day_ref.strftime('%B %d %Y %I:%M'))

        for stage in STAGES:
                if stage == "EGG":
                        WORM['Temp']['25Celcius']['Time'].append((starting_day_ref).strftime(TIME_FRAME))
                        WORM['Temp']['20Celcius']['Time'].append((starting_day_ref).strftime(TIME_FRAME))
                        WORM['Temp']['15Celcius']['Time'].append((starting_day_ref).strftime(TIME_FRAME))

                elif stage == "L1":
                        new_time25 = (starting_day_ref + timedelta(hours=8))
                        new_time20 = (starting_day_ref + timedelta(hours=10.4))
                        new_time15 = (starting_day_ref + timedelta(hours=16.8))

                        WORM['Temp']['25Celcius']['Time'].append(str(new_time25.strftime(TIME_FRAME)))
                        WORM['Temp']['20Celcius']['Time'].append(str(new_time20.strftime(TIME_FRAME)))
                        WORM['Temp']['15Celcius']['Time'].append(str(new_time15.strftime(TIME_FRAME)))           

                elif stage == "L2":
                        new_time25 = (starting_day_ref + timedelta(hours=20))
                        new_time20 = (starting_day_ref + timedelta(hours=26))
                        new_time15 = (starting_day_ref + timedelta(hours=42))

                        WORM['Temp']['25Celcius']['Time'].append(str(new_time25.strftime(TIME_FRAME)))
                        WORM['Temp']['20Celcius']['Time'].append(str(new_time20.strftime(TIME_FRAME)))
                        WORM['Temp']['15Celcius']['Time'].append(str(new_time15.strftime(TIME_FRAME)))       

                elif stage == "L3":
                        new_time25 = (starting_day_ref + timedelta(hours=27))
                        new_time20 = (starting_day_ref + timedelta(hours=35.1))
                        new_time15 = (starting_day_ref + timedelta(hours=56.7))

                        WORM['Temp']['25Celcius']['Time'].append(str(new_time25.strftime(TIME_FRAME)))
                        WORM['Temp']['20Celcius']['Time'].append(str(new_time20.strftime(TIME_FRAME)))
                        WORM['Temp']['15Celcius']['Time'].append(str(new_time15.strftime(TIME_FRAME)))       
                        
                elif stage == "L4":
                        new_time25 = (starting_day_ref + timedelta(hours=34))
                        new_time20 = (starting_day_ref + timedelta(hours=44.2))
                        new_time15 = (starting_day_ref + timedelta(hours=71.4))

                        WORM['Temp']['25Celcius']['Time'].append(str(new_time25.strftime(TIME_FRAME)))
                        WORM['Temp']['20Celcius']['Time'].append(str(new_time20.strftime(TIME_FRAME)))
                        WORM['Temp']['15Celcius']['Time'].append(str(new_time15.strftime(TIME_FRAME)))       

                elif stage == "ADULT":
                        new_time25 = (starting_day_ref + timedelta(hours=43))
                        new_time20 = (starting_day_ref + timedelta(hours=55.9))
                        new_time15 = (starting_day_ref + timedelta(hours=90.3))

                        WORM['Temp']['25Celcius']['Time'].append(str(new_time25.strftime(TIME_FRAME)))
                        WORM['Temp']['20Celcius']['Time'].append(str(new_time20.strftime(TIME_FRAME)))
                        WORM['Temp']['15Celcius']['Time'].append(str(new_time15.strftime(TIME_FRAME)))       

def printWorm():
        # For temp in worm
        for temp in WORM['Temp']:
                print("\n**************************\n")
                print("At STORAGE TEMP: ", temp)
                # for stage in temp
                for stage_time in WORM['Temp'][temp]:
                        # for each index in stage and time in temp
                        for i in range(len(WORM['Temp'][temp]['Stage'])):
                                if stage_time == "Stage":
                                        print("STAGE: ", str(WORM['Temp'][temp]['Stage'][i]).ljust(5), "= TIME: ", str(WORM['Temp'][temp]['Time'][i]).ljust(5))
                                else:
                                        break

def gen_dataframe():
        df = pd.DataFrame.from_dict(WORM)
        fig, (ax1, ax2, ax3) = plt.subplots(3,figsize=(12,9))
        fig.suptitle('C.Elegans Life Cycle Calculation')
        ax1.plot(df['Temp']['25Celcius']['Stage'],df['Temp']['25Celcius']['Time'], c='b', marker='o', label='25 Celcius')
        ax2.plot(df['Temp']['20Celcius']['Stage'],df['Temp']['20Celcius']['Time'], c='r', marker='o', label='20 Celcius')
        ax3.plot(df['Temp']['15Celcius']['Stage'],df['Temp']['15Celcius']['Time'], c='g', marker='o', label='15 Celcius')
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper left')
        ax3.legend(loc='upper left')
        
        plt.show()

if __name__ == "__main__":
        main()



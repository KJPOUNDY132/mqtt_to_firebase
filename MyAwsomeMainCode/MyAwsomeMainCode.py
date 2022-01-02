import time
import os
from time import sleep
import read_
import send_
import sys
from multiprocessing import Process
import json


def main():

        p1 = Process(target = read_.main)
        p1.start()
        p2 = Process(target = send_.main)
        p2.start()



if __name__ == "__main__":
    try: 
        print("This Code writed by YigidOS")
        main()
    except KeyboardInterrupt:
        print("\nPrograms was stopped")  
        sys.exit()








#Authored by mostly nick :)
import os
import sys

def terminate_process():
    print("Terminating process...")
    os._exit(1)  # 0 is usually used for successful termination, non-zero for errors

if __name__ == "__main__":
    terminate_process()
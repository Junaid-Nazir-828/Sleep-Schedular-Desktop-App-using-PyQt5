# import os
# os.system("Rundll32.exe Powrprof.dll,SetSuspendState Sleep")

# from datetime import datetime
# time_now = datetime.datetime.now()
# print(time_now.hour)
# print(type(time_now.hour)) # int

# import os

# def get_machine_name():
#     return os.getlogin()

if __name__ == '__main__':
    # print(get_machine_name())
    # print(type(get_machine_name())) # str

    # ab = ''
    # if ab:
    #     print('not empt')
    # else:
    #     print('empty')
    # current_time = datetime.now().strftime('%H:%M')
    # print(type(current_time))
    import psutil

    # Get the names of all running processes
    process_names = [proc.name() for proc in psutil.process_iter(['name'])]

    # Print the names of the processes
    if 'Sleepy.exe' in process_names:
        print('yes')


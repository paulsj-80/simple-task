import time

from clearml import Task
task = Task.init(project_name='examples', task_name='hello world3')

#while True:
for i in range(3):
    print("mupse")
    time.sleep(1)



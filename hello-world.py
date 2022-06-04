import time

from clearml import Task
task = Task.init(project_name='examples', task_name='hello world3')

logger = task.get_logger()

while True:
#for i in range(3):
    #print("mupse")
    logger.report_text("some message!")
    time.sleep(1)



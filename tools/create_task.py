import os
from datetime import datetime

TASK_DIR = "../memory/long_term/tasks"


def create_task(title, description):
    os.makedirs(TASK_DIR, exist_ok=True)

    filename = f"{datetime.now().timestamp()}.txt"
    path = os.path.join(TASK_DIR, filename)

    content = f"""TITLE: {title}
    DESCRIPTION: {description}
    STATUS: TODO"""

    with open(path, "w") as f:
        f.write(content)

    return path

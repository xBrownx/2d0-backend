from src.globals import *

class Tasks:
    def __init__(self, db):
        self.db = db

    def get_user_tasks(self, username):
        task_ids = self.db.execute_query_fetchall(USER_TASKS_QUERY, (username,))
        tasks = self.db.execute_query_fetchall(TASKS_QUERY, task_ids)
        return self.get_task_objects_from_result(tasks)

    def get_task_objects_from_result(self, result):
        task_objects = []
        for task in result:
            task_objects.append({
                TASK_ID: task["task_id"],
                TASK_GROUP_ID: task["group_id"],
                TASK_TIMESTAMP: task["created_timestamp"],
                TASK_NAME: task["task_name"],
                TASK_DESC: task["task_description"],
                TASK_DUE_DATE: task["due_date"],
                TASK_IS_REPEAT: task["is_repeat"],
                TASK_REPEAT_FREQ: task["repeat_frequency"],
                TASK_REPEAT_FREQ_UNIT: task["repeat_frequency_unit"],
                TASK_IS_COMPLETE: task["is_complete"],
                TASK_COMPLETE_TIMESTAMP: task["completed_timestamps"],
                TASK_ASSIGNED_BY: task["assigned_by"],
                TASK_ASSIGNED_TO: self.get_users_assigned_to_task(task["task_id"])
            })
        return task_objects

    def get_users_assigned_to_task(self, task_id):
        return []

    def delete_task(self):
        pass
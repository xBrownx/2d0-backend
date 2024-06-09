from src.globals import *
import time
import uuid
class Groups:

    def __init__(self, db):
        self.db = db

    def get_user_groups(self, username):
        print("groups.get_user_groups")
        group_ids = self.db.execute_query_fetchall(USER_GROUPS_QUERY, (username,))
        group_ids = tuple(group_ids.flat)
        print(group_ids)
        groups = self.db.execute_query_fetchall(GROUPS_QUERY, group_ids)
        print(groups)
        return self.get_group_objects_from_result(groups)

    def register_group(self, group):
        print("groups.register_group")
        query_args = (
            group[GROUP_ID],
            group[GROUP_NAME],
            group[GROUP_OWNER],
            group[GROUP_TIMESTAMP]
        )
        return self.register_user_in_group(group[GROUP_OWNER], group[GROUP_ID]) if (
            self.db.execute_query_fetch_none(REGISTER_GROUP_QUERY, query_args)) \
            else False

    def register_personal_group(self, username):
        print("groups.register_personal_group")
        group_id = str(uuid.uuid4())
        query_args = (
            group_id,
            PERSONAL,
            username,
            round(time.time() * 1000)
        )
        return self.register_user_in_group(username, group_id) if (
            self.db.execute_query_fetch_none(REGISTER_GROUP_QUERY, query_args)) \
            else False

    def register_user_in_group(self, username, group_id):
        query_args = (username, group_id)
        return True if self.db.execute_query_fetch_none(REGISTER_USER_GROUP_QUERY, query_args) else False

    @staticmethod
    def get_group_objects_from_result(result):
        print("groups.get_group_objects_from_result")
        group_objects = []
        for group in result:
            group_objects.append({
                GROUP_ID: group[0],
                GROUP_NAME: group[1],
                GROUP_OWNER: group[2],
                GROUP_TIMESTAMP: group[3]
            })
        return group_objects

    def delete_group(self):
        print("groups.delete_group")
        pass

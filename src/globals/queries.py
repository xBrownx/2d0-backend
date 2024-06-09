AUTH_TOKEN_QUERY =          "SELECT * FROM user_tokens " \
                            "WHERE username = %s " \
                            "AND device_id = %s " \
                            "AND token = %s"

AUTH_LOGIN_QUERY =          "SELECT * FROM users " \
                            "WHERE username = %s " \
                            "AND password = %s"

AUTH_REGISTER_QUERY =       "INSERT INTO users (username, mobile_number, password) " \
                            "VALUES (%s, %s, %s);"

AUTH_USER_EXISTS_QUERY =    "SELECT * FROM users WHERE mobile_number = %s"

AUTH_CREATE_TOKEN_QUERY =   "INSERT INTO user_tokens (username, device_id, token) " \
                            "VALUES (%s, %s, %s);"

AUTH_DELETE_TOKEN_QUERY =   "DELETE FROM user_tokens " \
                            "WHERE username = %s " \
                            "AND device_id = %s " \
                            "AND token = %s;"

USER_GROUPS_QUERY =         "SELECT group_id FROM user_groups WHERE username = %s"

GROUPS_QUERY =              "SELECT * FROM groups WHERE group_id IN (%s)"

REGISTER_GROUP_QUERY =      "INSERT INTO groups (group_id, group_name, group_owner, created_timestamp) " \
                            "VALUES (%s, %s, %s, %s);"

REGISTER_USER_GROUP_QUERY = "INSERT INTO user_groups (username, group_id)" \
                            "VALUES(%s, %s)"

USER_TASKS_QUERY =          "SELECT task_id FROM user_tasks WHERE username = %s"

TASKS_QUERY =               "SELECT * FROM tasks WHERE task_id IN (%s)"

TASK_USERS_QUERY =          "SELECT username FROM user_tasks WHERE task_id = %s"

USER_FRIENDS_QUERY =        "SELECT * FROM user_friends WHERE username = %s"

FRIENDS_QUERY =             "SELECT * FROM users WHERE username IN (%s)"

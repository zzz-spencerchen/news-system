import sys
sys.path.append("..")
from db.mysql_db import pool

class RoleDao():
    def search_list(self):
        try:
            con=pool.get_connection()
            cursor=con.cursor()
            sql="select id, role from t_role"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()


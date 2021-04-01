import sys
sys.path.append("..")
from db.mysql_db import pool

class UserDao():
    def login(self, username, password):
        try:
            con=pool.get_connection()
            cursor=con.cursor()
            sql="select count(*) from t_user where username=%s " \
                "and AES_DECRYPT(UNHEX(password), 'hash')=%s"

            cursor.execute(sql,[username, password])
            count = cursor.fetchone()[0]
            if count == 1:
                return True
            else:
                return False

        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()


    def search_user_role(self, username):
        try:
            con=pool.get_connection()
            cursor=con.cursor()
            sql="select r.role from t_user u join t_role r on u.role_id=r.id " \
                "where u.username=%s"
            cursor.execute(sql, [username])
            role=cursor.fetchone()[0]
            return role
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()


    def add_user(self, username, password, email, role_id):
        try:
            con=pool.get_connection()
            con.start_transaction()
            cursor=con.cursor()
            sql="insert into t_user (username, password, email, role_id) " \
                "values (%s, HEX(AES_ENCRYPT(%s, 'hash')), %s, %s);"
            cursor.execute(sql, [username, password, email, role_id])
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()


    def search_count_page(self):
        try:
            con=pool.get_connection()
            cursor=con.cursor()
            sql="select CEIL(count(*)/10) from t_user"
            cursor.execute(sql)
            count_page=cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()


    def search_user_list(self, page):
        try:
            con=pool.get_connection()
            cursor=con.cursor()
            sql="select u.id, u.username, r.role from t_user u join t_role r " \
                "ON u.role_id=r.id " \
                "order by u.id ASC " \
                "limit %s,%s"
            cursor.execute(sql, [(page-1)*10, 10])
            result=cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()


    def update_user(self, id, username, password, email, role_id):
        try:
            con=pool.get_connection()
            con.start_transaction()
            cursor=con.cursor()
            sql="update t_user set username=%s, " \
                "password=HEX(AES_ENCRYPT(%s, 'hash')), " \
                "email=%s, role_id=%s " \
                "where id=%s"
            cursor.execute(sql, [username, password, email, role_id, id])
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()


    def delete_by_id(self,id):
        try:
            con=pool.get_connection()
            con.start_transaction()
            cursor=con.cursor()
            sql="delete from t_user where id=%s"
            cursor.execute(sql, [id])
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()
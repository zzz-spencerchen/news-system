import sys
sys.path.append("..")
from db.mysql_db import pool

class NewsDao():
    def search_unreview_list(self, page):
        try:
            con=pool.get_connection()
            cursor=con.cursor()
            sql="select n.id, n.title, t.type, u.username " \
                "from t_news n join t_type t on n.type_id=t.id " \
                "join t_user u on n.editor_id=u.id " \
                "where n.status=%s " \
                "order by n.create_time desc " \
                "limit %s,%s"
            cursor.execute(sql, ['unfinished', (page-1)*10, 10])
            result = cursor.fetchall()
            return result

        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()


    def search_unreview_count_page(self):
        try:
            con=pool.get_connection()
            cursor=con.cursor()
            sql="select CEIL(count(*)/10) From t_news where status=%s"
            cursor.execute(sql,['unfinished'])
            count_page=cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()


    def update_unreview_news(self, id):
        try:
            con=pool.get_connection()
            con.start_transaction()
            cursor=con.cursor()
            sql="update t_news set status=%s where id=%s"
            cursor.execute(sql, ['valid', id])
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()


    # search all news report
    def search_list(self, page):
        try:
            con=pool.get_connection()
            cursor=con.cursor()
            sql="select n.id, n.title, t.type, u.username " \
                "from t_news n join t_type t on n.type_id=t.id " \
                "join t_user u on n.editor_id=u.id " \
                "order by n.create_time desc " \
                "limit %s,%s"
            cursor.execute(sql, [(page-1)*10, 10])
            result = cursor.fetchall()
            return result
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()


    def search_count_page(self):
        try:
            con=pool.get_connection()
            cursor=con.cursor()
            sql="select CEIL(count(*)/10) From t_news"
            cursor.execute(sql)
            count_page=cursor.fetchone()[0]
            return count_page
        except Exception as e:
            print(e)
        finally:
            if 'con' in dir():
                con.close()


    def delete_by_id(self, id):
        try:
            con=pool.get_connection()
            con.start_transaction()
            cursor=con.cursor()
            sql="delete from t_news where id=%s"
            cursor.execute(sql, [id])
            con.commit()
        except Exception as e:
            if 'con' in dir():
                con.rollback()
            print(e)
        finally:
            if 'con' in dir():
                con.close()
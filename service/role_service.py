import sys
sys.path.append("..")
from db.role_dao import RoleDao


class RoleService():
    __role_Dao = RoleDao()

    def search_list(self):
        result = self.__role_Dao.search_list()
        return result
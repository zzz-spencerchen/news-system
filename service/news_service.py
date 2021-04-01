import sys
sys.path.append("..")
from db.news_dao import NewsDao

class NewsService():
    __news_dao=NewsDao()

    def search_unreview_list(self, page):
        result = self.__news_dao.search_unreview_list(page)
        return result


    def search_unreview_count_page(self):
        count_page=self.__news_dao.search_unreview_count_page()
        return count_page


    def update_unreview_news(self, id):
        self.__news_dao.update_unreview_news(id)


    def search_list(self, page):
        result = self.__news_dao.search_list(page)
        return result


    def search_count_page(self):
        result = self.__news_dao.search_count_page()
        return result


    def delete_by_id(self, id):
        self.__news_dao.delete_by_id(id)

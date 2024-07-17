from abc import ABC, abstractmethod

class AbstractAPI(ABC):
    @abstractmethod
    def get_response(self, text, per_page):
        """Получает ответ от API по заданному тексту и количеству вакансий на странице"""
        pass

    @abstractmethod
    def get_vacancies(self, text, per_page):
        """Получает вакансии по заданному тексту и количеству вакансий на странице"""
        pass

    @abstractmethod
    def get_filtered_vacancies(self, text, per_page):
        """Получает отфильтрованные вакансии по заданному тексту и количеству вакансий на странице"""
        pass

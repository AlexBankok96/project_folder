import requests

from project_folder.src.api import AbstractAPI


class HeadHunterAPI(AbstractAPI):
    BASE_URL = "https://api.hh.ru/vacancies"

    def get_response(self, text, per_page=100):
        """Получает ответ от API по заданному тексту и количеству вакансий на странице"""
        params = {
            "text": text,
            "per_page": per_page,
            "area": 113  # Россия
        }
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()

    def get_vacancies(self, text, per_page=100):
        """Получает вакансии по заданному тексту и количеству вакансий на странице"""
        data = self.get_response(text, per_page)
        return data["items"]

    def get_filtered_vacancies(self, text, per_page=100):
        """Получает отфильтрованные вакансии по заданному тексту и количеству вакансий на странице"""
        vacancies = self.get_vacancies(text, per_page)
        return [vac for vac in vacancies if "salary" in vac and vac["salary"] is not None]

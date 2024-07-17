import json
import requests
from src.headhunter import HeadHunterAPI
from src.vacancy import Vacancy
from src.json_saver import JSONSaver


def user_interaction():
    """Функция для взаимодействия с пользователем"""
    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words_input = input("Введите ключевые слова для фильтрации вакансий (разделяйте пробелами): ")

    # Разбиваем строку ключевых слов на список
    filter_words = filter_words_input.split() if filter_words_input else []

    # Получение вакансий с hh.ru
    hh_vacancies = hh_api.get_vacancies(search_query)

    # Преобразование набора данных из JSON в список объектов Vacancy
    vacancy_objects = [Vacancy.from_dict(vac) for vac in hh_vacancies]

    # Фильтрация вакансий по ключевым словам в описании, если они указаны
    if filter_words:
        filtered_vacancies = [vac for vac in vacancy_objects if
                              vac.description and any(word in vac.description for word in filter_words)]
    else:
        filtered_vacancies = vacancy_objects

    # Сортировка вакансий по зарплате
    sorted_vacancies = sorted(filtered_vacancies, key=lambda vac: vac.salary if vac.salary else 0, reverse=True)

    # Получение топ N вакансий по зарплате
    top_vacancies = sorted_vacancies[:top_n]

    # Сохранение вакансий в JSON файл
    json_saver = JSONSaver()
    for vac in top_vacancies:
        json_saver.add_vacancy(vac)

    # Вывод топ N вакансий
    for i, vac in enumerate(top_vacancies, 1):
        print(f"{i}. {vac}")


if __name__ == "__main__":
    user_interaction()

import os
import json
import pytest

from project_folder.src.json_saver import JSONSaver
from project_folder.src.vacancy import Vacancy

# Путь к временному JSON файлу для тестов
TEST_JSON_FILE = "tests/test_vacancies.json"


@pytest.fixture
def json_saver():
    """Фикстура для инициализации JSONSaver перед каждым тестом."""
    return JSONSaver(TEST_JSON_FILE)


def setup_module(module):
    """Setup before module execution."""
    # Создаем пустой JSON файл для тестирования
    with open(TEST_JSON_FILE, 'w', encoding='utf-8') as file:
        json.dump([], file)


def teardown_module(module):
    """Teardown after module execution."""
    # Удаляем временный JSON файл после тестирования
    if os.path.exists(TEST_JSON_FILE):
        os.remove(TEST_JSON_FILE)


def test_add_and_load_vacancy(json_saver):
    vacancy = Vacancy("Software Engineer", "https://hh.ru/vacancy/1", 100000, "Python, Django")
    json_saver.add_vacancy(vacancy)

    # Проверяем, что вакансия была добавлена и загружена корректно
    loaded_vacancies = json_saver.load_vacancies()
    assert len(loaded_vacancies) == 1
    assert loaded_vacancies[0]["title"] == "Software Engineer"
    assert loaded_vacancies[0]["url"] == "https://hh.ru/vacancy/1"
    assert loaded_vacancies[0]["salary"] == 100000
    assert loaded_vacancies[0]["description"] == "Python, Django"


def test_delete_vacancy(json_saver):
    vacancy1 = Vacancy("Backend Developer", "https://hh.ru/vacancy/1", 120000, "Python, Django")
    vacancy2 = Vacancy("Frontend Developer", "https://hh.ru/vacancy/2", 100000, "JavaScript, React")

    json_saver.add_vacancy(vacancy1)
    json_saver.add_vacancy(vacancy2)

    # Удаляем одну вакансию
    json_saver.delete_vacancy(vacancy1)

    # Проверяем, что вакансия была удалена
    loaded_vacancies = json_saver.load_vacancies()
    assert len(loaded_vacancies) == 1
    assert loaded_vacancies[0]["title"] == "Frontend Developer"


if __name__ == "__main__":
    pytest.main()

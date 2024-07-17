import pytest

from project_folder.src.vacancy import Vacancy


def test_vacancy_from_dict():
    vac_dict = {
        "name": "Software Engineer",
        "alternate_url": "https://hh.ru/vacancy/12345",
        "salary": {
            "from": 100000,
            "to": 150000
        },
        "snippet": {
            "requirement": "Experience with Python"
        }
    }
    vacancy = Vacancy.from_dict(vac_dict)
    assert vacancy.title == "Software Engineer"
    assert vacancy.url == "https://hh.ru/vacancy/12345"
    assert vacancy.salary == 100000  # проверяем начальную зарплату, без перевода в строку
    assert vacancy.description == "Experience with Python"


def test_vacancy_lt_comparison():
    vac1 = Vacancy("Backend Developer", "https://hh.ru/vacancy/1", 120000, "Python, Django")
    vac2 = Vacancy("Frontend Developer", "https://hh.ru/vacancy/2", 100000, "JavaScript, React")
    vac3 = Vacancy("Full-stack Developer", "https://hh.ru/vacancy/3", 150000, "Python, JavaScript")

    assert vac1 < vac2  # Backend Developer (120000) < Frontend Developer (100000)
    assert not vac1 < vac3  # Backend Developer (120000) >= Full-stack Developer (150000)


if __name__ == "__main__":
    pytest.main()
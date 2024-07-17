import pytest

from project_folder.src.headhunter import HeadHunterAPI


@pytest.fixture
def hh_api():
    """Фикстура для создания экземпляра HeadHunterAPI."""
    return HeadHunterAPI()

def test_get_vacancies(hh_api):
    """Тест получения вакансий с помощью HeadHunterAPI."""
    vacancies = hh_api.get_vacancies("developer", 5)
    assert len(vacancies) > 0

def test_get_filtered_vacancies(hh_api):
    """Тест получения отфильтрованных вакансий с помощью HeadHunterAPI."""
    filtered_vacancies = hh_api.get_filtered_vacancies("developer", 5)
    assert len(filtered_vacancies) > 0
    for vacancy in filtered_vacancies:
        assert "salary" in vacancy and vacancy["salary"]

if __name__ == "__main__":
    pytest.main()

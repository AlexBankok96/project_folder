class Vacancy:
    def __init__(self, title, url, salary, description):
        """Инициализирует вакансию с заданными параметрами"""
        self.title = title
        self.url = url
        self.salary = salary
        self.description = description

    def __lt__(self, other):
        """Сравнивает вакансии по зарплате"""
        return self.salary < other.salary

    def __repr__(self):
        """Возвращает строковое представление вакансии"""
        formatted_salary = f"{self.salary:,}" if self.salary else "Не указана"
        return f"Vacancy({self.title}, {formatted_salary})"

    @staticmethod
    def from_dict(vac_dict):
        """Создает объект Vacancy из словаря"""
        title = vac_dict["name"]
        url = vac_dict["alternate_url"]
        salary = vac_dict["salary"]["from"] if vac_dict["salary"] else 0
        description = vac_dict["snippet"]["requirement"]
        return Vacancy(title, url, salary, description)

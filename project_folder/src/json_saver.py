import json
import os
import logging

class JSONSaver:
    def __init__(self, filename='data/vacancies.json'):
        """Инициализирует JSONSaver с заданным именем файла"""
        self.filename = filename
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)

    def add_vacancy(self, vacancy):
        """Добавляет вакансию в JSON-файл"""
        vacancies = self.load_vacancies()
        vacancies.append(vacancy.__dict__)
        self.save_vacancies(vacancies)
        print(f"Добавлена вакансия: {vacancy.title}")  # Добавлен временный print для отладки

    def delete_vacancy(self, vacancy):
        """Удаляет вакансию из JSON-файла"""
        vacancies = self.load_vacancies()
        vacancies = [vac for vac in vacancies if vac["url"] != vacancy.url]
        self.save_vacancies(vacancies)

    def load_vacancies(self):
        """Загружает вакансии из JSON-файла"""
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError as e:
                print(f"Ошибка при загрузке JSON из файла: {e}")
                return []

    def save_vacancies(self, vacancies):
        """Сохраняет вакансии в JSON-файл"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(vacancies, file, ensure_ascii=False, indent=4)
                logging.info(f"Сохранено {len(vacancies)} вакансий в файл {self.filename}")
        except Exception as e:
            logging.error(f"Ошибка при сохранении вакансий: {e}")

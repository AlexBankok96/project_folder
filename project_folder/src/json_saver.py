import json
import os
import logging
from project_folder.src.file_handler import AbstractFileHandler


class JSONSaver(AbstractFileHandler):
    def __init__(self, filename='data/vacancies.json'):
        """Инициализирует JSONSaver с заданным именем файла"""
        self.filename = filename
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)

    def load(self):
        """Загружает вакансии из JSON-файла"""
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, 'r', encoding='utf-8') as file:
            try:
                return json.load(file)
            except json.decoder.JSONDecodeError as e:
                print(f"Ошибка при загрузке JSON из файла: {e}")
                return []

    def save(self, vacancies):
        """Сохраняет вакансии в JSON-файл"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(vacancies, file, ensure_ascii=False, indent=4)
                logging.info(f"Сохранено {len(vacancies)} вакансий в файл {self.filename}")
        except Exception as e:
            logging.error(f"Ошибка при сохранении вакансий: {e}")

    def add_vacancy(self, vacancy):
        """Добавляет вакансию в JSON-файл"""
        vacancies = self.load()
        vacancies.append(vacancy.__dict__)
        self.save(vacancies)
        print(f"Добавлена вакансия: {vacancy.title}")

    def delete_vacancy(self, vacancy):
        """Удаляет вакансию из JSON-файла"""
        vacancies = self.load()
        vacancies = [vac for vac in vacancies if vac["url"] != vacancy.url]
        self.save(vacancies)

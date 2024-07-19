from abc import ABC, abstractmethod

class AbstractFileHandler(ABC):
    @abstractmethod
    def load(self):
        """Загружает данные из файла"""
        pass

    @abstractmethod
    def save(self, data):
        """Сохраняет данные в файл"""
        pass
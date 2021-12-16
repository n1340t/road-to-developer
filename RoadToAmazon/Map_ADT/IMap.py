# https://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/8-List/list-map.html
from abc import ABC, abstractmethod


class IMap(ABC):
    @abstractmethod
    def size(self) -> int:
        raise NotImplementedError()

    @abstractmethod
    def isEmpty(self) -> bool:
        raise NotImplementedError()

    @abstractmethod
    def put(self, k: str, v: str):
        raise NotImplementedError()

    @abstractmethod
    def get(self, k: str) -> str:
        raise NotADirectoryError()

    @abstractmethod
    def remove(self, k: str) -> str:
        raise NotImplementedError()

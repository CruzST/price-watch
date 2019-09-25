from abc import ABCMeta, abstractmethod
from typing import List, TypeVar, Type, Dict, Union

from common.database import Database

# T must be a model or one of its subclasses
T = TypeVar('T', bound='Model')

class Model(metaclass=ABCMeta):
    # collection and _id will be string in the subclass
    collection: str
    _id: str

    # Avoid Warning
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def json(self) -> Dict:
        raise NotImplementedError

    @classmethod
    def all(cls: Type[T]) -> List[T]:
        items_from_db = Database.find(cls.collection, {})
        # create and return a list of items obtained from the query
        return [cls(**item) for item in items_from_db]

    @classmethod
    def get_by_id(cls: Type[T], _id: str) -> T:
        return cls.find_one_by("_id", _id)

    @classmethod
    def find_one_by(cls: Type[T], attribute: str, value: Union[str, Dict]) -> T:
        return cls(**Database.find_one(cls.collection, {attribute: value}))

    @classmethod
    def find_many_by(cls: Type[T], attribute: str, value: Union[str, Dict]) -> List[T]:
        return [cls(**item) for item in Database.find(cls.collection, {attribute: value})]

    def save_to_mongo(self):
        # upsert data
        Database.update(self.collection, {"_id": self._id}, self.json())

    def remove_from_mongo(self):
        Database.remove(self.collection, {"_id": self._id})


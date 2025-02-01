from typing import Generator, Tuple, Hashable

class HashMap[T]:
    def __init__(self, capacity=16, load_factor=0.75) -> None:
        self.capacity = capacity
        self.load_factor = load_factor
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]
        
    def _hash(self, key: Hashable) -> int:
        return hash(key) % self.capacity
    
    def _resize(self) -> None:
        self.capacity *= 2
        new_table = [[] for _ in range(self.capacity)]
        for bucket in self.table:
            for k, v in bucket:
                h = self._hash(k) # Пересчитываем хеш для новой таблицы
                new_table[h].append((k, v)) # Копирование элементов в новую таблицу
        self.table = new_table
        
    def put(self, key: Hashable, value: T) -> None:
        """Добавление элемента"""
        if (self.size + 1) / self.capacity > self.load_factor:
            self._resize()
            
        h = self._hash(key)
        bucket = self.table[h]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Обновление значения
                return
        
        bucket.append((key, value)) # Добавление нового элемента (метод цепочек)
        self.size += 1
        
    def get(self, key: Hashable) -> T:
        """Получение значения по ключу"""
        h = self._hash(key)
        bucket = self.table[h]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError(key)
    
    def remove(self, key: Hashable) -> None:
        """Удаление элемента по ключу"""
        h = self._hash(key)
        bucket = self.table[h]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.size -= 1
                return
        raise KeyError(key)
    
    def __len__(self) -> int:
        return self.size
    
    def __contains__(self, key: Hashable) -> bool:
        h = self._hash(key)
        return any(k == key for k, _ in self.table[h])
    
    def keys(self) -> Generator[Hashable, None, None]:
        """Генератор ключей"""
        for bucket in self.table:
            for k, _ in bucket:
                yield k

    def items(self) -> Generator[Tuple[Hashable, T], None, None]:
        """Генератор пар ключ-значение"""
        for bucket in self.table:
            yield from bucket
            
    
class AssociativeArray[T]:
    def __init__(self) -> None:
        self.map = HashMap[T]()
        
    def __setitem__(self, key: Hashable, value: T) -> None:
        self.map.put(key, value)
        
    def __getitem__(self, key: Hashable) -> T:
        return self.map.get(key)
    
    def __delitem__(self, key: Hashable) -> None:
        self.map.remove(key)
        
    def __len__(self) -> int:
        return len(self.map)
    
    def __contains__(self, key: Hashable) -> bool:
        return key in self.map
    
    def __str__(self) -> str:
        return "{" + ", ".join([f"{k}: {v}" for k, v in self.map.items()]) + "}"
    
    def __iter__(self) -> Generator[Hashable, None, None]:
        yield from self.map.keys()
        
    def keys(self) -> Generator[Hashable, None, None]:
        """Генератор ключей"""
        yield from self.map.keys()
        
    def items(self) -> Generator[Tuple[Hashable, T], None, None]:
        """Генератор пар ключ-значение"""
        yield from self.map.items()

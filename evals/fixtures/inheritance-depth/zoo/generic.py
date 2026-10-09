from typing import Generic, TypeVar

T = TypeVar("T")


class Repository(Generic[T]):
    pass


class SqlRepository(Repository[T]):
    pass


class CachedRepository(SqlRepository[T]):
    pass


class AuditedRepository(CachedRepository[int]):
    pass

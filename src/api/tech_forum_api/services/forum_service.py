from typing import Optional, List

from injector import inject, singleton
from sqlutils import Service

from tech_forum_api.cache import cache
from tech_forum_api.converters.forum_converter import ForumConverter
from tech_forum_api.models.forum import Forum
from tech_forum_api.persistence.dto.forum_dto import ForumDTO
from tech_forum_api.persistence.repositories.forum_repository import ForumRepository


@singleton
class ForumService(Service[Forum, ForumDTO, ForumRepository]):

    @inject
    def __init__(self, repo: ForumRepository) -> None:
        super().__init__(repo)
        self._converter = ForumConverter()

    @property
    def __repo(self) -> ForumRepository:
        return self._repo

    def get_by_id(self, uid: int) -> Optional[Forum]:
        return super().get_by_id(uid)

    def _convert(self, entity: ForumDTO) -> Optional[Forum]:
        if not entity:
            return None

        return self._converter.convert(entity)

    @staticmethod
    def _clear_cache() -> None:
        # cache.delete_memoized(ForumService.get_by_id)
        pass
        #TODO dont remember update cache

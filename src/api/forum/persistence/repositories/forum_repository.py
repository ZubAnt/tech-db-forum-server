from typing import Optional, List, Any, Dict

from injector import inject
from sqlutils import DataContext, Repository, create_one

from forum.persistence.dto.forum_dto import ForumDTO


class ForumRepository(Repository[ForumDTO]):

    @inject
    def __init__(self, context: DataContext) -> None:
        self._context = context

    def get_by_id(self, uid: int) -> Optional[ForumDTO]:
        data = self._context.callproc('get_forum_by_id', [uid])
        return create_one(ForumDTO, data)

    def get_by_slug(self, slug: str) -> Optional[ForumDTO]:
        data = self._context.callproc('get_forum_by_slug', [slug])
        return create_one(ForumDTO, data)

    def get_by_slug_setup(self, slug: str) -> Optional[ForumDTO]:

        data = self._context.callproc('get_forum_by_slug_ret_uid', [slug])
        return create_one(ForumDTO, data)

    def increment_threads(self, uid: int) -> None:
        self._context.callproc('forum_increment_threads', [uid])

    def increment_posts(self, uid: int) -> None:
        self._context.callproc('forum_increment_posts', [uid])

    def increment_posts_by_number(self, uid: int, number: int) -> None:
        self._context.callproc('forum_increment_posts_by_number', [uid, number])

    def get_count(self) -> int:
        data = self._context.callproc('get_forums_count', [])
        if data is None or len(data) == 0:
            return 0
        result_dict = data[0]
        return result_dict.get('forums_count')

    def clear(self):
        self._context.callproc('clear_forums', [])

    def get_all(self) -> List[ForumDTO]:
        raise NotImplementedError

    def add(self, params: Dict[str, Any]) -> Dict[str, Any]:
        self._context.callproc('add_forum', [params['slug'], params['user_id'], params['nickname'], params['title']])
        data = params
        data.update({
            'user': params['nickname'],
            'threads': 0,
            'posts': 0
        })
        data.pop('user_id')
        data.pop('nickname')
        return data

    def add_many(self, entities: List[ForumDTO]):
        raise NotImplementedError

    def update(self, entity: ForumDTO):
        raise NotImplementedError

    def delete(self, uid: int) -> None:
        raise NotImplementedError

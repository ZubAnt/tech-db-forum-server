from typing import Optional, Any, Dict

from injector import inject, singleton
from sqlutils import DataContext, return_one


@singleton
class ForumRepository(object):

    @inject
    def __init__(self, context: DataContext) -> None:
        self._context = context

    def is_exists_by_slug(self, slug: str) -> Optional[Dict[str, Any]]:
        data = self._context.callproc('is_exists_by_slug', [slug])
        return return_one(data)

    def get_by_id(self, uid: int) -> Optional[Dict[str, Any]]:
        data = self._context.callproc('get_forum_by_id', [uid])
        return return_one(data)

    def get_by_slug(self, slug: str) -> Optional[Dict[str, Any]]:
        data = self._context.callproc('get_forum_by_slug', [slug])
        return return_one(data)

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

    def add(self, params: Dict[str, Any]) -> Dict[str, Any]:
        self._context.callproc('add_forum', [params['slug'],  params['user_id'], params['user'], params['title']])
        data = params
        data.update({
            'threads': 0,
            'posts': 0
        })
        return data

    def clear(self):
        self._context.callproc('clear_forums', [])

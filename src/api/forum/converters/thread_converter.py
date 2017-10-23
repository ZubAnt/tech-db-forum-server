from sqlutils import Converter
from forum.models.user import User
from forum.models.forum import Forum
from forum.models.thread import Thread
from forum.persistence.dto.thread_dto import ThreadDTO


class ThreadConverter(Converter[Thread, ThreadDTO]):

    def convert(self, entity: ThreadDTO) -> Thread:
        return Thread(uid=entity.uid).fill(
            slug=entity.slug,
            forum=Forum(entity.forum_id),
            author=User(entity.user_id),
            created=entity.created,
            message=entity.message,
            title=entity.title
        )
from datetime import datetime

from sqlutils import Model
from tech_forum_api.models.user import User
from tech_forum_api.models.forum import Forum
from tech_forum_api.models.thread import Thread


class Post(Model):

    def __init__(self, uid: int) -> None:
        super().__init__(uid)

        self._thread: Thread = None
        self._forum: Forum = None
        self._user: User = None
        self._parent: Post = None
        self._message: str = None
        self._created: datetime = None
        self._is_edited: bool = None

    @property
    def thread(self) -> Thread:
        return self._thread

    @property
    def forum(self) -> Forum:
        return self._forum

    @property
    def user(self) -> User:
        return self._user

    @property
    def parent(self) -> "Post":
        return self._parent

    @property
    def created(self) -> datetime:
        return self._created

    @property
    def is_edited(self) -> bool:
        return self._is_edited

    def fill(self, thread: Thread, forum: Forum, user: User, parent: "Post",
             message: str, created: datetime, is_edited: bool) -> "Post":
        self._thread = thread
        self._forum = forum
        self._user = user
        self._parent = parent
        self._message = message
        self._created = created
        self._is_edited = is_edited
        self._filled()
        return self

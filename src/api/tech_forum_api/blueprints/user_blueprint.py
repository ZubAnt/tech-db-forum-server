import logging

from flask import Blueprint, abort, request, Response
from injector import inject, singleton

from apiutils import BaseBlueprint

from tech_forum_api.serializers.user_serializer import UserSerializer
from tech_forum_api.services.user_service import UserService
logging.basicConfig(level=logging.INFO)


@singleton
class UserBlueprint(BaseBlueprint[UserService]):

    @inject
    def __init__(self, service: UserService) -> None:
        super().__init__(service)

    @property
    def _name(self) -> str:
        return 'users'

    @property
    def _serializer(self) -> UserSerializer:
        return UserSerializer()

    def _create_blueprint(self) -> Blueprint:
        blueprint = Blueprint(self._name, __name__)

        @blueprint.route('/<uid>', methods=['GET'])
        def _get_by_id(uid: str):
            logging.exception(uid)
            return self._get_by_id(int(uid))

        @blueprint.route('/<nickname>/create', methods=['POST'])
        def _add(nickname: str):
            data = {'nickname': nickname}
            return self._add(data)

        @blueprint.route('/', methods=['PUT'])
        def _update():
            return self._update()

        @blueprint.route('/<uid>', methods=['DELETE'])
        def _delete(uid: str):
            return self._delete(uid)

        return blueprint

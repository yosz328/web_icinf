import connexion
import six

from swagger_server.models.fotos import Fotos  # noqa: E501
from swagger_server.models.mensaje import Mensaje  # noqa: E501
from swagger_server import util
from facebook_request import facebook_send
from facebook_photo_request import facebook_send_photo


def addphoto(body):  # noqa: E501
    """envia post con foto

     # noqa: E501

    :param body: foto que sera enviada
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = connexion.request.get_json() # noqa: E501
        print(body['url'])
        print(body['caption'])
        response = facebook_send_photo(body['caption'],body['url'])
    return response


def addpost(body):  # noqa: E501
    """envia un Post

     # noqa: E501

    :param body: post que sera enviado
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = connexion.request.get_json()  # noqa: E501
        print(body)
        response = facebook_send(body["message"])


    return response

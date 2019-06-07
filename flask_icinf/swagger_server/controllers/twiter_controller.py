import connexion
import six

from swagger_server.models.mensaje import Mensaje  # noqa: E501
from swagger_server import util


def addtweet(body):  # noqa: E501
    """envia un tweet

     # noqa: E501

    :param body: tweet que sera enviado
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Mensaje.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'

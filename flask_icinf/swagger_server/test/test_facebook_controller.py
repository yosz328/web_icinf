# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.mensaje import Mensaje  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFacebookController(BaseTestCase):
    """FacebookController integration test stubs"""

    def test_addpost(self):
        """Test case for addpost

        envia un Post
        """
        body = Mensaje()
        response = self.client.open(
            '/icinf/fbpost',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

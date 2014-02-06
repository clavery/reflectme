import json

from . import ReflectMeTest


class PathTests(ReflectMeTest):

    def setUp(self):
        super(PathTests, self).setUp()

    def tearDown(self):
        super(PathTests, self).tearDown()

    def create_test_path(self):
        data = dict(
            location='test_path',
            response='{"ok":"100"}',
            content_type='application/json')

        return self.client.post('/?create',data=data, follow_redirects=True)

    def test_missing_path(self):
        res = self.client.get('/doesnotexist')
        assert res.status_code == 404

    def test_create_path(self):
        res = self.create_test_path()
        assert res.status_code == 200
        assert 'test_path' in res.data

    def test_path_response(self):
        self.create_test_path()

        res = self.client.get('/test_path')

        assert res.status_code == 200
        assert res.content_type == 'application/json'
        res_data = json.loads(res.data)
        assert res_data.get('ok') == '100'

    def test_path_response_recording(self):
        self.create_test_path()

        visit = self.client.get('/test_path')
        assert visit.status_code == 200

        res = self.client.get('/inspect/test_path')

        assert 'Record Count: 1' in res.data
        assert 'User-Agenet' in res.data


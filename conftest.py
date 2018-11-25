import os
# import tempfile

import pytest

from app import app


@pytest.fixture
def client():
    # db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config.from_object(os.environ['APP_SETTINGS'])
    client = app.test_client()

    # with app.app_context() as context:
        # context.init_db()

    yield client

    # os.close(db_fd)
    # os.unlink(app.config['DATABASE'])

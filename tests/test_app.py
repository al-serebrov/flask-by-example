def test_header(client):
    """Start with a blank database."""

    rv = client.get('/')
    assert b'Hello World' in rv.data

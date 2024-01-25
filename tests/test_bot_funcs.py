from unittest.mock import MagicMock

import pytest

from src.main import MyClient


@pytest.fixture
def mocked_discord_client(monkeypatch):
    mocked_client = MagicMock(spec=MyClient)

    monkeypatch.setattr(mocked_client, 'run', MagicMock())

    return mocked_client


def test_on_ready_called(mocked_discord_client):
    client = mocked_discord_client()

    client.on_ready()

    assert client.on_ready.called


def test_on_message_called(mocked_discord_client):
    client = mocked_discord_client()

    client.on_message('Mocked')

    assert client.on_message.called

import inspect

import pytest

from src.main import bot
from tests import test_bot_commands


def _get_functions(module):
    return [
        name for name, obj in inspect.getmembers(module) if
        inspect.isfunction(obj) and name.startswith(
            'test_',
        ) and name.endswith('_command')
    ]


@pytest.mark.asyncio
async def test_all_commands_have_tests():
    list_commands = [
        f'test_{command.name}_command' for command in bot.walk_application_commands()
    ]

    list_test_functions = _get_functions(test_bot_commands)

    list_missing_on_test = list(set(list_commands) - set(list_test_functions))

    assert list_missing_on_test == [
    ], f'Test not found for command(s): {list_missing_on_test}'

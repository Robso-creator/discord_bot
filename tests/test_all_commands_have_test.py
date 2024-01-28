import inspect

from src.main import bot
from src.main import server_id
from tests import test_bot_commands


def _get_functions(module):
    return [name for name, obj in inspect.getmembers(module) if inspect.isfunction(obj) and name.startswith('test_') and name.endswith('_command')]


def test_all_commands_have_tests():
    list_commands = [
        f'test_{command.name}_command' for command in bot.tree.walk_commands(guild=server_id)
    ]
    list_test_functions = _get_functions(test_bot_commands)

    list_missing_on_test = list(set(list_commands) - set(list_test_functions))

    assert list_missing_on_test == [
    ], f'Test not found for command(s): {list_missing_on_test}'

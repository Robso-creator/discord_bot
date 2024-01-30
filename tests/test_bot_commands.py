from src.main import bot
from src.main import server_id


def test_hello_command():
    command_name = 'hello'
    command_description = 'teste de descrição'

    test_command = next(
        (
            c for c in bot.tree.walk_commands(
                guild=server_id,
            ) if c.name == command_name
        ),
        None,
    )

    assert test_command is not None, f"command '{command_name}' not found"
    assert test_command.callback.__name__ == command_name, 'function name is different from the command name'
    assert test_command.description == command_description, 'command description is different from the expected'


def test_help_command():
    command_name = 'help'
    command_description = 'teste de descrição'

    test_command = next(
        (
            c for c in bot.tree.walk_commands(
                guild=server_id,
            ) if c.name == command_name
        ),
        None,
    )

    assert test_command is not None, f"command '{command_name}' not found"
    assert test_command.callback.__name__ == command_name, 'function name is different from the command name'
    assert test_command.description == command_description, 'command description is different from the expected'

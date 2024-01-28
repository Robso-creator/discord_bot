from src.main import bot
from src.main import server_id


def test_hello_command():
    command_name = 'hello'
    command_description = 'teste de descrição'

    hello_command = next(
        (
            c for c in bot.tree.walk_commands(
                guild=server_id,
            ) if c.name == command_name
        ),
        None,
    )

    assert hello_command is not None, f"command '{command_name}' not found"
    assert hello_command.callback.__name__ == command_name, 'function name is different from the command name'
    assert hello_command.description == command_description, 'command description is different from the expected'

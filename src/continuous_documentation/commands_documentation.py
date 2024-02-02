from src.main import bot
from src.main import server_id

string_template = """# Documentação dos comandos do Bot

Esta documentação fornece informações detalhadas sobre os comandos disponíveis no Bot Discord.
Em vez de depender de um README estático, esta documentação é construída automáticamente no deploy
usando código Python.
Isso nos permite manter a dinamicidade do mapeamento dos comandos, garantindo que
as informações estejam sempre atualizadas.

> Para visualizar o código responsável por gerar esta documentação dinâmica,
> clique [aqui](../src/continuous_documentation/commands_documentation.py)

## Informações sobre os comandos

Hoje temos **{COMMANDS_COUNT}** comandos.

Mostramos na tabela abaixo quais são eles e suas informações de forma sintetizada.

ID |Nome do Comando| Descrição | Aceita Parametros |
---|---------------|-----------|-------------------|
{COMMANDS_TABLE}

## Comandos de forma detalhada

{COMMANDS_DETAILED}

"""


def docs_dags_self_documentation():
    final_path = './docs/commands.md'

    with open(final_path, 'w') as file:
        all_commands = [
            _command for _command in bot.tree.walk_commands(guild=server_id)
        ]
        commands_count = len(all_commands)
        commands_table = ''
        commands_detailed = ''
        for e, command in enumerate(all_commands, 1):
            dict_command = command.to_dict()
            accept_commands = '✅' if len(dict_command['options']) > 0 else '❌'
            command_name = dict_command['name']
            command_description = dict_command['description']

            _command_table = f'{e} | [{command_name}](#{command_name}) | {command_description} | {accept_commands}\n'
            commands_table += _command_table

            params = '**Parâmetros**:\n\n'
            for param in dict_command['options']:
                param_name = param['name']
                param_description = param['description']
                param_required = '❌' if param['required'] is False else '✅'

                if len(dict_command['options']) > 0:
                    params += (
                        f'- Nome: {param_name};\n- Descrição: {param_description};\n- Obrigatório: {param_required}.'
                    )

            _command_detail = f'### {command_name}\n - Descrição: {command_description}\n\n{params}'
            commands_detailed += _command_detail
            commands_detailed += '\n___\n'  # horizontal line

        commands_documentation = string_template.format(
            COMMANDS_COUNT=commands_count,
            COMMANDS_TABLE=commands_table,
            COMMANDS_DETAILED=commands_detailed,
        )
        file.write(commands_documentation)


if __name__ == '__main__':
    docs_dags_self_documentation()

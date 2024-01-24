<!--

Antes de abrir um PR, garanta que seu código cumpre os seguintes checks:

- Revise seu código e faça QA dele como se fosse o usuário final. Garanta que ele faz tudo o que foi descrito no JIRA.
- Dê rebase (ou faça um merge) da branch de destino com a sua e corrija conflitos.
- Verifique se não esqueceu nenhum comentário, typos ou byebugs no código.
- DRY (Don’t repeat yourself).
- KISS (Keep it simple).
- YAGNI (You ain’t gonna need it) - Não faça coisas antecipadamente se você não precisa delas ainda.

Caso tenha realizado todos os checks acima, continue e lembre-se de apagar seções que não fazem
sentido para esse PR ou adicionar novas seções conforme necessário.

-->

# Main contribution in this PR

Describe as an item list what are the main contributions found in this PR.

- [x] Add a new method...
- [x] Fix bugs related to...

# Github issue

If this references a Github Issue, please provide it here. Note that github automatically creates a link to an Issue if
it is referenced by number with a leading '#'.

Issue #1


## Screenshots


## How to test

<!--

The description of a test scenario (at least the happy flow) can help other developers who are not familiar with it.
with the part of the code that was modified in this PR but want to see everything working before approving.
This section might include step-by-step instructions on how to get to exactly where in the flow your code is changing.
Ideally this would already be in JIRA so it can be copied and pasted here.

Description example:
- Login with the user `foo` from the company `bar` configured with the `foobar` option
- Click on the `X` button on the interface
- Wait for the system to return `Y`

-->

## Emojis

Emojis can be added to review comments to separate blocking and non-blocking comments.

Example: Compliments, small suggestions or questions that don't block a merge.

> 🟢 Liked the refactor!

> 🟡 Why was this value removed?

Example: Blocking feedbacks must be addressed before a merge.

> 🔴 This change will break an important system flow

### Examples

| Type | Examples | Description |
| --- | --- | --- |
| Blocking | 🔴 ❌ 🚨 | Red emojis |
| Non-blocking | 🟡 💡 🤔 💭 | Yellow emojis, pensive, etc |
| Compliment | 🟢 💚 😍 👍 🙌 | Green emojis, hearts, positives, etc |

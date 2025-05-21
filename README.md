# 🐍 Curso Python 3 - Do Zero ao Avançado (Udemy)

Repositório com os códigos, exercícios, desafios e anotações realizadas durante o curso:

🔗 [Python 3 - Do Zero ao Avançado (Udemy)](https://www.udemy.com/course/python-3-do-zero-ao-avancado/)

---

## 📚 Progresso das Aulas

| Aula | Tópico                                                             | Status         |
|------|--------------------------------------------------------------------|----------------|
| 01   | Comentários e DocStrings                                           | ✅ Concluída    |
| 02   | A função print, argumentos e quebra de linha                       | ✅ Concluída    |
| 03   | Tipagem, strings e aspas                                           | ✅ Concluída    |
| 04   | Tipos de dados int e float (números)                               | ✅ Concluída    |
| 05   | Tipo de dados bool (boolean) - True ou False                       | ✅ Concluída    |
| 06   | Coerção de tipos (converter um tipo em outro)                      | ✅ Concluída    |
| 07   | Introdução às variáveis em Python                                  | ✅ Concluída    |
| 08   | Exercício com variáveis e tipos de dados                           | ✅ Concluída    |
| 09   | Introdução aos operadores aritméticos (matemática)                 | ✅ Concluída    |
| 10   | Concatenação (+) e repetição (*) com operadores aritméticos        | ✅ Concluída    |
| 11   | Precedência de operadores aritméticos                              | ✅ Concluída    |
| 12   | Exercício: Cálculo do IMC                                          | ✅ Concluída    |
| 13   | Introdução às f-strings (formatação de strings)                    | ✅ Concluída    |
| 14   | Formatação de strings com o método `format()`                      | ✅ Concluída    |
| 15   | Usando a função input para coletar dados do usuário                | ✅ Concluída    |
| 16   | Blocos de código + if / elif / else (condicionais)                 | ✅ Concluída    |
| 17   | if, elif e else: fluxo do interpretador                            | ✅ Concluída    |
| 18   | Debugger do VS Code / Windsurf                                     | ✅ Concluída    |
| 19   | Operadores relacionais (de comparação)                             | ✅ Concluída    |
| 20   | Exercício com if e operadores de comparação                        | ✅ Concluída    |
| 21   | Operador lógico `and`                                              | ✅ Concluída    |
| 22   | Operador lógico `or`                                               | ✅ Concluída    |
| 23   | Operador lógico `not`                                              | ✅ Concluída    |
| 24   | Operadores `in` e `not in`                                         | ✅ Concluída    |
| 25   | Interpolação de strings com `%`                                    | ✅ Concluída    |
| 26   | Formatação de strings com f-strings                                | ✅ Concluída    |
| 27   | Fatiamento de strings e a função `len()`                           | ✅ Concluída    |
| 28   | 🧩 Exercício de revisão geral (strings, operadores, inputs)        | ✅ Concluída    |

---

## 💻 Tecnologias utilizadas

- Python 3.13
- Windsurf Editor (alternativa ao VS Code)
- Git e GitHub

---

## 🧠 Anotações Importantes

- `input()` sempre retorna string
- `int("10")` converte string para inteiro
- `print()` pode usar `sep` e `end`
- Operadores: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Operadores lógicos: `and`, `or`, `not`
- Condicionais: `if`, `elif`, `else`
- Loops: `for`, `while`, `break`, `continue`
- Funções: `def`, parâmetros, retorno
- Lambda: funções anônimas
- Debugger: permite pausar e inspecionar o código passo a passo
- Windsurf cria `.vscode/launch.json` automaticamente ao depurar

---

## 🧩 Desafios e Exercícios Resolvidos

| Aula | Descrição do Exercício                           | Arquivo     |
|------|--------------------------------------------------|-------------|
| 08   | Exercício com variáveis e tipos de dados         | `aula8.py`  |
| 12   | Cálculo do IMC com entrada do usuário            | `aula12.py` |
| 20   | Condicional com `if`, `elif`, operadores         | `aula20.py` |
| 28   | Exercício de revisão geral (strings, inputs...)  | `aula28.py` |

---

## ❓ Dúvidas que tive (e como resolvi)

- **Por que `print('1' + 1)` dá erro?**  
  → Porque está somando string com inteiro. Use `print('1' + str(1))`.

- **Como usar f-strings?**  
  → Coloque um `f` antes da string e use `{}`:  
  `print(f"Olá, {nome}")`.

- **Como importar funções de outro arquivo?**  
  → `from nome_arquivo import funcao`

  ## 🧩 Extensões instaladas no Windsurf

- Python
- Code Runner
- Material Icon Theme
- Dracula Official
- GitLens (opcional)

---

## ⚙️ Configurações do Windsurf (`settings.json`)

{
  "workbench.colorTheme": "Dracula Theme",
  "code-runner.clearPreviousOutput": true,
  "code-runner.runInTerminal": true,
  "code-runner.ignoreSelection": true,
  "code-runner.executorMap": {
    "python": "cls ; & 'python' -u \"$fullFileName\""
  },
  "files.encoding": "utf8",
  "workbench.iconTheme": "material-icon-theme",
  "python.defaultInterpreterPath": "python",
  "git.autofetch": true
}

---

## ✍️ Observações Pessoais

- Curso bem didático e direto ao ponto
- Crio um novo arquivo por aula com testes e exemplos
- O debug me ajudou muito a entender o fluxo do código
- Este repositório é meu “caderno de estudos digital” com versionamento

---
# Decola T14 Dinâmica Técnica Coletiva

## Preparação do ambiente

1. **Criar o ambiente virtual**

```bash
$ python3 -m venv .venv
```

2. **Ativar o ambiente virtual**

```bash
$ source .venv/bin/activate
```

3. **Instalar as dependências no ambiente virtual**

```bash
$ python3 -m pip install -r requirements.txt
```

## Rodando os testes

Para executar todos os testes

```bash
$ python3 -m pytest
```

Para executar os testes relacionados a apenas um desafio (_para o desafio 1, por exemplo_)

```bash
$ python3 -m pytest tests/test_problem1.py
```
---

## Entrega do desafio

Após clonar o repositório, desenvolva as soluções em uma _branch_ com o número do seu grupo. O número do seu grupo é dado pelo número da breakout room em que vocês estão. Exemplos:
- Grupo 1: _branch_ `grupo-1`
- Grupo 2: _branch_ `grupo-2`
- Grupo 3: _branch_ `grupo-3`
- Grupo 4: _branch_ `grupo-4`
- ...

Ao final, faça o _push_ com as alterações

---

## Desafios

São 3 desafios ao todo.

Para cada desafio, temos um arquivo no qual você desenvolverá sua solução:
- `problems/problem1.py`
- `problems/problem2.py`
- `problems/problem3.py`

A solução deve ser realizada dentro da função `solve()` que está presente do arquivo

### 👉 Desafio 1

**Entrada**: 
> - `number`, do tipo `int`
> - `iterations`, do tipo `int`

**Desafio**:
> Execute a seguinte lógica pelo número de vezes indicado em `iterations`:
> - Se `number` não terminar em zero, subtraia `1` de `number`. Caso contrário, divida `number` por `10`
> 
> Retorne o valor final de `number`, que deve ser um numero inteiro.

### 👉 Desafio 2

**Entrada**: 
> - `brackets`, do tipo `str`

**Desafio**:
> A entrada `brackets` será uma sequência dos caracteres:
> - `(` : abertura de parênteses;
> - `)` : fechamento de parênteses. 
> 
> Verifique se, para cada abertura de parênteses, há um fechamento correspondente. Além disso, não deve haver um fechamento sem uma abertura correspondente. 
> 
> Retorne `True` se a entrada atende as condições, e `False` caso contrário.

### 👉 Desafio 3

**Entrada**: 
> - `students`, do tipo `list`

**Desafio**:
> A entrada `students` será uma lista de tuplas, sendo que cada tupla contém um par de inteiros.
> 
> Cada tupla representa os horários de entrada e saída de uma pessoa estudante em uma sala de estudos. Por exemplo, a tupla `(5, 9)` indica que essa pessoa estudante esteve na sala a partir do horário `5` até o horário `9`.
>
> Se temos outra tupla `(7, 13)`, outra pessoa estudante esteve na sala a partir do horário `7` até o horário `13`. Portanto, entre os horários `7` e `9` tivemos **2** pessoas estudantes simultaneamente na sala de estudos. 
> 
> Retorne o número máximo de pessoas estudantes que estiveram na sala de estudos simultaneamente.

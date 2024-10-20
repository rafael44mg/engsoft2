trab2 - Rafael Galimberti/
│
├── library/
│   ├── __init__.py
│   ├── book.py
│   ├── factory.py
│   └── loan.py
│
├── tests/
│   ├── __init__.py
│   └── test_factory.py
│
└── README.txt


#################################################

# Sistema de Gestão de Biblioteca

Este projeto implementa um sistema básico de gerenciamento de biblioteca, 
permitindo o cadastro de livros e o controle de empréstimos, 
utilizando o padrão de projeto **Factory Method**.

## Padrão de Projeto Utilizado: Factory Method

O padrão **Factory Method** foi aplicado na criação de livros e no gerenciamento de empréstimos. 
A classe `LibraryFactory` define a interface de criação, enquanto a classe `ConcreteLibraryFactory` 
implementa o método de criação de livros e empréstimos.

## Como executar os testes

Para rodar os testes unitários, execute:

```bash
python -m unittest discover -s tests

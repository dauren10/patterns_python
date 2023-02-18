"""
Задача поиска строк по образцу может быть решена посредством создания интерпретатора, определяющего грамматику языка.
 "Клиент" строит предложение в виде абстрактного синтаксического дерева, в узлах которого находятся объекты классов
   "ТерминальноеВыражение" и "НетерминальноеВыражение" (рекурсивное), затем "Клиент" инициализирует контекст и вызывает операцию Разобрать(Контекст). На каждом узле типа "НетерминальноеВыражение" определяется операция Разобрать для каждого подвыражения. Для класса "НетерминальноеВыражение" операция Разобрать определяет базу рекурсии. "АбстрактноеВыражение" определяет абстрактную операцию Разобрать, общую для всех узлов в абстрактном синтаксическом дереве.
 "Контекст" содержит информацию, глобальную по отношению к интерпретатору. 
"""

import abc


class AbstractExpression(metaclass=abc.ABCMeta):
    """
    Declare an abstract Interpret operation that is common to all nodes
    in the abstract syntax tree.
    """

    @abc.abstractmethod
    def interpret(self):
        pass


class NonterminalExpression(AbstractExpression):
    """
    Implement an Interpret operation for nonterminal symbols in the grammar.
    """

    def __init__(self, expression):
        self._expression = expression

    def interpret(self):
        self._expression.interpret()


class TerminalExpression(AbstractExpression):
    """
    Implement an Interpret operation associated with terminal symbols in
    the grammar.
    """

    def interpret(self):
        pass


def main():
    abstract_syntax_tree = NonterminalExpression(TerminalExpression())
    abstract_syntax_tree.interpret()


if __name__ == "__main__":
    main()

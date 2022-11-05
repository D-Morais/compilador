import ply.lex as lex
from teste import arquivo_de_teste


class MyLexer(object):

    palavras_reservadas = {
        'char': 'CHAR',
        'int': 'INT',
        'float': 'FLOAT'
    }

    # Lista de tokens + palavras reservadas.
    tokens = ['ID', 'PONTO_E_VIRGULA', 'VIRGULA'] + list(palavras_reservadas.values())


    # Lista de expressões regulares simples.
    t_PONTO_E_VIRGULA = r'\;'
    t_VIRGULA = '\,'
    t_CHAR = 'char'
    t_INT = 'int'

    """
    Comando token.value.lower() serve para verificar se a entrada é uma palavra reservada,
    se for ela não pode ser um ID. 
     
    O ID é baseado na linguagem C, logo pode começar com
    letras minúsculas, maiúsculas ou _, e após podem ter letras
    minúsculas ou maiúsculas, _ e/ou números.
    """
    def t_ID(self, token):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        token.type = self.palavras_reservadas.get(token.value.lower(), 'ID')
        return token


    # Conta o número de linhas.
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)


    # Ignora espaços em brancos e tabulação.
    t_ignore = ' \t'


    # Método para captura e apresentação de erros.
    def t_error(self, token):
        print(f'LexToken ({token.type.upper()}, valor: {token.value[0]}, linha: {token.lineno}, posição: {token.lexpos})')
        token.lexer.skip(1)


    # Construa o lexer
    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    # Teste a saida
    def test(self, dados):
        self.lexer.input(dados)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(f'LexToken ({tok.type}, valor: {tok.value}, linha: {tok.lineno}, posição: {tok.lexpos})')


# Construa o lexer e experimente
lexico = MyLexer()

# Constroi o lexer
lexico.build()

# Aqui é inserido os dados para teste da ferramenta.
entrada = arquivo_de_teste()
lexico.test(entrada)

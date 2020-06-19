from blackpythonpro.tests.test_spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None

    def test_remetente():
        enviador = Enviador()
        resultado=enviador.enviar(
            'miranda_garcya@hotmail.com',
            'meg_amorcarol@hotmail.com',
            'Curso Python Pro',
            'Primeira turma Guido Von Rossum aberta.'
        )
        assert 'miranda_garcya@hotmail.com' in resultado
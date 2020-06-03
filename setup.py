 codecs de importação
importação  os
 sys de importação

de  distutils . util  importação  convert_path
de  fnmatch  import  fnmatchcase
de  setuptools  import  setup , find_packages


def  lido ( fname ):
     codecs de retorno . aberto ( os . path . join ( os . path . dirname ( __file__ ), fname )). read ()


# Fornecido como um atributo, para que você possa anexá-los
# de replicá-los:
standard_exclude  = [ "* .py" , "* .pyc" , "* $ py.class" , "* ~" , ". *" , "* .bak" ]
standard_exclude_directories  = [
    ". *" , "CVS" , "_darcs" , "./build" , "./dist" , "EGG-INFO" , "* .egg-info"
]


(c) 2005 Ian Bicking e colaboradores; escrito para colar (http://pythonpaste.org)
# Licenciado sob a licença MIT: http://www.opensource.org/licenses/mit-license.php
# Nota: você pode copiar isso para o arquivo setup.py literalmente, como
# você não pode importar isso de outro pacote, quando não sabe se
# esse pacote já está instalado.
def  find_package_data (
    onde = "." ,
    package = "" ,
    exclude = standard_exclude ,
    exclude_directories = standard_exclude_directories ,
    only_in_packages = True ,
    show_ignored = False ):
    "" "
    Retorne um dicionário adequado para uso em `` package_data``
    em um arquivo distutils `` setup.py``.
    O dicionário se parece com:
        {"pacote": [arquivos]}
    Onde `` files`` é uma lista de todos os arquivos nesse pacote que
    não corresponde a nada em `` excluir``.
    Se `` only_in_packages`` for verdadeiro, os diretórios de nível superior que
    pacotes não serão incluídos (mas diretórios sob pacotes
    vai).
    Diretórios que correspondem a qualquer padrão em `` exclude_directories``
    ser ignorado; por diretórios padrão com os principais `` .``, `` CVS``,
    e `` _darcs`` serão ignorados.
    Se `` show_ignored`` for verdadeiro, todos os arquivos que não estão "t
    incluídos nos dados do pacote são mostrados no stderr (para depuração
    finalidades).
    Os padrões de anotações usam curingas ou podem ser caminhos exatos (incluindo
    levando ``. / ``), e toda a pesquisa não diferencia maiúsculas de minúsculas.
    "" "
    out  = {}
    pilha  = [( caminho_convertido ( onde ), "" , pacote , somente_em_pacotes )]
    while  stack :
        onde , prefixo , pacote , only_in_packages  =  pilha . pop ( 0 )
        para o  nome  em  os . listdir ( onde ):
            fn  =  os . caminho . junção ( onde , nome )
            se  os . caminho . isdir ( fn ):
                bad_name  =  False
                para  padrão  em  exclude_directories :
                    if ( fnmatchcase ( nome , padrão )
                        ou  fn . padrão inferior () ==  . inferior ()):
                        bad_name  =  True
                        se  show_ignored :
                            print  >>  sys . stderr , (
                                "Diretório% s ignorado pelo padrão% s"
                                % ( fn , padrão ))
                        quebrar
                se  bad_name :
                    continuar
                if ( os . path . isfile ( os . path . join ( fn , "__init__.py" ))
                    e  não  prefixo ):
                    se  não  for o pacote :
                        new_package  =  name
                    mais :
                        new_package  =  pacote  +  "."  +  nome
                    pilha . acrescentar (( fn , "" , new_package , False ))
                mais :
                    pilha . acrescentar (( fn , prefixo  +  nome  +  "/" , pacote , apenas em pacotes )))
             pacote  elif ou  não  only_in_packages :
                # é um arquivo
                bad_name  =  False
                para  padrão  em  excluir :
                    if ( fnmatchcase ( nome , padrão )
                        ou  fn . padrão inferior () ==  . inferior ()):
                        bad_name  =  True
                        se  show_ignored :
                            print  >>  sys . stderr , (
                                "Arquivo% s ignorado pelo padrão% s"
                                % ( fn , padrão ))
                        quebrar
                se  bad_name :
                    continuar
                fora . setdefault ( pacote , []). acrescentar ( prefixo + nome )
    voltar  para fora


PACOTE  =  "blackpython"
NAME  =  "PACOTE"
DESCRIPTION  =  "Módulo de exemplo de projeto no curso pytools"
AUTOR  =  "Renzo Nuccitelli"
AUTHOR_EMAIL  =  "miranda_garcya@hotmail.com"
URL  =  "https://github.com/Marco1357/blackpython"
VERSÃO  =  __import__ ( PACOTE ). __versão__


configuração (
    name = NAME ,
    version = VERSION ,
    description = DESCRIÇÃO ,
    long_description = read('README.md') ,
    long_description_content_type='text/markdow',
    author = AUTHOR ,
    author_email = AUTHOR_EMAIL ,
    licença = ('LICENSE') ,
    url = URL ,
    packages = find_packages ( exclude = [ "testes. *" , "testes" ]),
    package_data = find_package_data ( PACKAGE , only_in_packages = False ),
    classificadores = [
        "Status do desenvolvimento :: 5 - Produção / Pre-Alpha" ,
        "Ambiente :: Console" ,
        "Público-alvo: desenvolvedores" ,
        "Licença :: OSI Aprovado :: Licença Pública Geral Menor GNU v3 ou posterior (LGPLv3 +)" ,
        "Sistema operacional :: Independente do SO" ,
        "Linguagem de programação :: Python" ,
        "Linguagem de programação :: Python :: 3,7",
        "Framework :: Paste" ,
    ],
    install_requists=[
      'requests'
    ]
    zip_safe = False ,
)
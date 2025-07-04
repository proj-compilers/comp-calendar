grammar Compilador;

// Analise Lexica
CRIAR : 'criar' ;
REPETIR : 'repetir' ;
CONSULTAR : 'consultar' ;
DELETAR : 'deletar' ;
EVENTO : 'evento' ;
ACHAV : '{' ;
FCHAV : '}' ;
HORA : (([0-1][0-9])|([2][0-4])) ':' ([0-5][0-9]) ;
DATA : DIA '-' MES '-' ANO ;
DIA : ([0][0-9])|([1-2][0-9])|([3][0-1]) ;
MES : ([0][0-9])|([1][0-2]) ;
ANO : ([1][9][0-9][0-9])|([2-3][0-9][0-9][0-9]) ;
NOME : '"' ([a-zA-Z]|' ')+ '"' ;                        //não aceita utf-8
//NOME : '"' ([\wÀ-ÿ]+|[áéíóúãõçàèìòùâêîôûÁÉÍÓÚÃÕÇÀÈÌÒÙÂÊÎÔÛ' '])+ '"';  //aceita utf-8
NUM : [1-9] ;

BRANCO : ( ' ' | '\n' | '\r'  ) -> skip ;

// Analise Sintatica
prog : com+ EOF ; 
com : CRIAR EVENTO NOME DATA HORA DATA HORA 
    | DELETAR EVENTO NOME
    | DELETAR EVENTO DATA
    | REPETIR EVENTO NUM ACHAV (com)+ FCHAV
    | CONSULTAR EVENTO NOME
    ;
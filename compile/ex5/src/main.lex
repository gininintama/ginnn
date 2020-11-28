%option nounput
%{
#include "common.h"
#include "main.tab.h"  // yacc header
int lineno=1;
%}
EOL	(\r\n|\r|\n)
WHILTESPACE [[:blank:]]

/*数据类型*/
INTEGER [0-9]+
CHAR \'.?\'
STRING \".+\"
IDENTIFIER [[:alpha:]_][[:alpha:][:digit:]_]*
%%

/*变量声明*/
"int" return INT;
"char" return CHAR;
"string" return STRING;
/*语句*/
"return" return RETURN;
"while" return WHILE;
"if" return IF;
"else" return ELSE;
"for" return FOR;
"=" return ASSIGN;
";" return  SEMICOLON;
"printf" return PRINTF;
"scanf" return SCANF;
/*表达式*/
"+" return PLUS;
"-" return MINUS;
"*" return MUL;
"/" return DIV;
"%" return MOD;
"==" return EQ;
">" return BT;
"<" return ST;
">=" return BE;
"<=" return SE;
"!=" return NE;
"&&" return AND;
"||" return OR;
"!" return NOT;
"(" return LP;
")" return RP;
"{" return BLP;
"}" return BRP;

{INTEGER} {
    TreeNode* node = new TreeNode(lineno, NODE_CONST);
    node->type = TYPE_INT;
    node->int_val = atoi(yytext);
    yylval = node;
    return INTEGER;
}

{CHAR} {
    TreeNode* node = new TreeNode(lineno, NODE_CONST);
    node->type = TYPE_CHAR;
    node->ch_val = yytext[1];
    yylval = node;
    return CHAR;
}

{STRING} {
    TreeNode* node = new TreeNode(lineno, NODE_CONST);
    node->type = TYPE_STRING;
    node->str_val = string(yytext);
    yylval = node;
    return STRING;
}
{IDENTIFIER} {
    TreeNode* node = new TreeNode(lineno, NODE_VAR);
    node->var_name = string(yytext);
    yylval = node;
    return IDENTIFIER;
}

{EOL} lineno++;

. {
    cerr << "[line "<< lineno <<" ] unknown character:" << yytext << endl;
}
%%
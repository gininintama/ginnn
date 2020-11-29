%{
    #include "common.h"
    #define YYstype TreeNode *  
    TreeNode* root;
    extern int lineno;
    int yylex();
    int yyerror( char const * );
%}
/*变量声明*/
%token T_CHAR T_INT T_STRING T_BOOL
/*语句*/
%token ASSIGN
%token IF ELSE WHILE FOR RETURN
%token BLP BRP LP RP SEMICOLON
%token TRUE FALSE
/*数据类型*/
%token IDENTIFIER INTEGER CHAR STRING BOOL
%token PRINTF SCANF
/*表达式*/
%left ASSIGN
%left OR
%left AND
%left NE
%left EQ
%left SE ST BE BT
%left PLUS MINUS
%left MUL DIV MOD
%right NOT
%nonassoc LOWER_THEN_ELSE
%nonassoc ELSE 
%%

program
: statements {root = new TreeNode(0, NODE_PROG); root->addChild($1);}
;

/*语句块*/
statements
:  statement {$$=$1;}
|  statements statement {$$=$1; $$->addSibling($2);}
;

/*语句*/
statement
    : declaration {$$=$1;}
    | if_else {$$=$1;}
    | while {$$=$1;}
    | BLP statements BRP {$$=$2;}
    ;
if_else
    : IF bool_statment statement %prec LOWER_THEN_ELSE {
        TreeNode *node=new TreeNode($1->lineno,NODE_STMT);
        node->stype=STMT_IF;
        node->addChild($2);
        node->addChild($3);
        $$=node;
    }
    | IF bool_statment statement ELSE statement {
        TreeNode *node=new TreeNode($1->lineno,NODE_STMT);
        node->stype=STMT_IF;
        node->addChild($2);
        node->addChild($3);
        node->addChild($5);
        $$=node;
    }
    ;
while
    : WHILE bool_statment statement {
        TreeNode *node=new TreeNode($1->lineno,NODE_STMT);
        node->stype=STMT_WHILE;
        node->addChild($2);
        node->addChild($3);
        $$=node;
    }
    ;
bool_statment
    : LP bool_expr RP {$$=$2;}
    ;
/*声明*/
declaration
: T IDENTIFIER ASSIGN expr SEMICOLON{ 
    TreeNode* node = new TreeNode($1->lineno, NODE_STMT);
    node->stype = STMT_DECL;
    node->addChild($1);
    node->addChild($2);
    node->addChild($4);
    $$ = node;   
} 
| T IDENTIFIER SEMICOLON{
    TreeNode* node = new TreeNode($1->lineno, NODE_STMT);
    node->stype = STMT_DECL;
    node->addChild($1);
    node->addChild($2);
    $$ = node;   
}
| printf SEMICOLON {$$=$1;}
| scanf SEMICOLON {$$=$1;}
;
printf
    : PRINTF LP expr RP {
        TreeNode *node=new TreeNode($1->lineno,NODE_STMT);
        node->stype=STMT_PRINTF;
        node->addChild($3);
        $$=node;
    }
    ;
scanf
    : SCANF LP expr RP {
        TreeNode *node=new TreeNode($1->lineno,NODE_STMT);
        node->stype=STMT_SCANF;
        node->addChild($3);
        $$=node;
    }
    ;
bool_expr
    : TRUE {$$=$1;}
    | FALSE {$$=$1;}
    | expr EQ expr {
        TreeNode *node=new TreeNode($1->lineno,NODE_EXPR);
        node->optype=OP_EQ;
        node->addChild($1);
        node->addChild($3);
        $$=node;
    }
    | expr AND expr {
        TreeNode *node=new TreeNode($1->lineno,NODE_EXPR);
        node->optype=OP_EQ;
        node->addChild($1);
        node->addChild($3);
        $$=node;
    }
    | expr OR expr {
        TreeNode *node=new TreeNode($1->lineno,NODE_EXPR);
        node->optype=OP_EQ;
        node->addChild($1);
        node->addChild($3);
        $$=node;
    }
    | NOT bool_expr {
        TreeNode *node=new TreeNode($1->lineno,NODE_EXPR);
        node->optype=OP_NOT;
        node->addChild($2);
        $$=node;        
    }
    ;
/*表达式*/
expr
: IDENTIFIER {
    $$ = $1;
}
| INTEGER {
    $$ = $1;
}
| CHAR {
    $$ = $1;
}
| STRING {
    $$ = $1;
}
| expr PLUS expr {
    TreeNode *node=new TreeNode($1->lineno,NODE_EXPR);
    node->optype=OP_PLUS;
    node->addChild($1);
    node->addChild($3);
    $$=node;   
}
| expr MINUS expr {
    TreeNode *node=new TreeNode($1->lineno,NODE_EXPR);
    node->optype=OP_MINUS;
    node->addChild($1);
    node->addChild($3);
    $$=node;   
}
| expr MUL expr {
    TreeNode *node=new TreeNode($1->lineno,NODE_EXPR);
    node->optype=OP_MUL;
    node->addChild($1);
    node->addChild($3);
    $$=node;   
}
| expr DIV expr {
    TreeNode *node=new TreeNode($1->lineno,NODE_EXPR);
    node->optype=OP_DIV;
    node->addChild($1);
    node->addChild($3);
    $$=node;   
}
| expr MOD expr {
    TreeNode *node=new TreeNode($1->lineno,NODE_EXPR);
    node->optype=OP_MOD;
    node->addChild($1);
    node->addChild($3);
    $$=node;   
}
| expr NE expr {
    TreeNode *node=new TreeNode($1->lineno,NODE_EXPR);
    node->optype=OP_NE;
    node->addChild($1);
    node->addChild($3);
    $$=node;   
}
| expr EQ expr {
    TreeNode *node=new TreeNode($1->lineno,NODE_EXPR);
    node->optype=OP_EQ;
    node->addChild($1);
    node->addChild($3);
    $$=node;   
}
| expr SE expr {
    TreeNode *node=new TreeNode($1->lineno,NODE_EXPR);
    node->optype=OP_SE;
    node->addChild($1);
    node->addChild($3);
    $$=node;   
}
| expr ST expr {
    TreeNode *node=new TreeNode($1->lineno,NODE_EXPR);
    node->optype=OP_ST;
    node->addChild($1);
    node->addChild($3);
    $$=node;   
}
| expr BE expr {
    TreeNode *node=new TreeNode($1->lineno,NODE_EXPR);
    node->optype=OP_BE;
    node->addChild($1);
    node->addChild($3);
    $$=node;   
}
| expr BT expr {
    TreeNode *node=new TreeNode($1->lineno,NODE_EXPR);
    node->optype=OP_BT;
    node->addChild($1);
    node->addChild($3);
    $$=node;   
}
;

T: T_INT {$$ = new TreeNode(lineno, NODE_TYPE); $$->type = TYPE_INT;} 
| T_CHAR {$$ = new TreeNode(lineno, NODE_TYPE); $$->type = TYPE_CHAR;}
| T_STRING {$$ = new TreeNode(lineno, NODE_TYPE); $$->type = TYPE_STRING;}
| T_BOOL {$$ = new TreeNode(lineno, NODE_TYPE); $$->type = TYPE_BOOL;}
;

%%

int yyerror(char const* message)
{
  cout << message << " at line " << lineno << endl;
  return -1;
}
#include "tree.h"
int NodeIndex=0;
void TreeNode::addChild(TreeNode* chil) {
    if(this->child==nullptr)
    {
        this->child=chil;
    }
    else
    {
        this->child->addSibling(chil);
    }
    
}

void TreeNode::addSibling(TreeNode* sib){
    if(this->sibling==nullptr)//加到链表的最末
    {
        this->sibling=sib;
    }
    else
    {
        this->sibling->addSibling(sib);
    }
    
}

TreeNode::TreeNode(int lino, NodeType type) {
    this->lineno=lino;
    this->nodeType=type;
}

void TreeNode::genNodeId() {
    if(this==nullptr)
        return;
    this->nodeID=NodeIndex++;
    this->child->genNodeId();
    this->sibling->genNodeId();
}

void TreeNode::printNodeInfo() {
    if(this==nullptr)
        return;
    //NODE_PROG NODE_STMT NODE_EXPR
    cout<<"lno@"<<this->lineno<<"   "<<"@"<this->nodeID<<" "<<this->nodeType2String(this->nodeType);
    if(this->nodeType==NODE_VAR)
    {
        cout<<" varname: "<<this->var_name;
        return;
    }
    if(this->nodeType==NODE_CONST)
    {
        if(this->type==TYPE_INT)
            cout<<" type: "<<this->int_val;
        else if(this->type==TYPE_CHAR)
            cout<<" type: "<<this->ch_val;
        else
            cout<<" type: "<<this->str_val;
        return;
    }
    if(this->nodeType==NODE_TYPE)
    {
        if(this->type==TYPE_INT)
            cout<<" type: "<<this->int_val;
        else if(this->type==TYPE_CHAR)
            cout<<" type: "<<this->ch_val;
        else
            cout<<" type: "<<this->str_val;
        return;
    }
}  

void TreeNode::printChildrenId() {
    if (this->child == nullptr)
        return;
    cout << " children: [";
    cout << this->child->nodeID << " ";
    if (this->child->sibling == nullptr)
        return;
    else {
        cout << this->child->sibling->nodeID << " ";
        TreeNode* temp = this->child->sibling->sibling;
        while (temp != nullptr)
        {
            cout << temp->nodeID << " ";
                temp = temp->sibling;
        }
    }
    cout << " ]";
    if(this->nodeType==NODE_STMT)
    {
        cout<<" stmt: "<<this->sType2String(this->stype)<<endl;
        return;
    }
    if(this->nodeType==NODE_EXPR)
    {
        cout<<" expression: "<<this->opType2String(this->optype)<<endl;
        return;
    }
    cout<<endl;
}

void TreeNode::printAST() {//先序遍历
    if(this==nullptr)
    {
        return;
    }
    this->printNodeInfo();
    this->printChildrenId();
    this->child->printAST();
    this->sibling->printAST();
}


// You can output more info...
void TreeNode::printSpecialInfo() {
    switch(this->nodeType){
        case NODE_CONST:
            break;
        case NODE_VAR:
            break;
        case NODE_EXPR:
            break;
        case NODE_STMT:
            break;
        case NODE_PROG:
            break;
        case NODE_TYPE:
            break;
        default:
            break;
    }
}

string TreeNode::sType2String(StmtType type) {
   switch(type){
        case STMT_SKIP:
            printf("skip");
            break;
        case STMT_DECL:
            printf("decl");
            break;
        case STMT_IF:
            printf("if");
            break;
        case STMT_WHILE:
            printf("while");
            break;
        case STMT_PRINTF:
            printf("printf");
            break;
         case STMT_SCANF:
            printf("sacnf");
            break;
        default:
            break;
    }
}


string TreeNode::nodeType2String (NodeType type){
    switch(type){
        case NODE_CONST:
            printf("const");
            break;
        case NODE_VAR:
            printf("variable");
            break;
        case NODE_EXPR:
            printf("expression");
            break;
        case NODE_TYPE:
            printf("type");
            break;
        case NODE_STMT:
            printf("statement");
            break;
        case NODE_PROG:
            printf("program");
            break;
        default:
            break;
    }
}

string opType2String (OperatorType type){
    switch(type){
        case OP_EQ:
            printf("EQ");
            break;
        case OP_NOT:
            printf("NOT");
            break;
        case OP_OR:
            printf("OR");
            break;
        case OP_AND:
            printf("AND");
            break;
        case OP_NE:
            printf("NE");
            break;
        case OP_SE:
            printf("SE");
            break;
        case OP_BE:
            printf("BE");
            break;
        case OP_BT:
            printf("BT");
            break;
        case OP_PLUS:
            printf("PLUS");
            break;
        case OP_MINUS:
            printf("MINUS");
            break;
        case OP_MUL:
            printf("MUL");
            break;
        case OP_DIV:
            printf("DIV");
            break;
        case OP_MOD:
            printf("MOD");
            break;
        default:
            break;
    }
}
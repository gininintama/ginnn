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
    TreeNode* node= this;
    if(node!=nullptr){
        node->nodeID=NodeIndex++;
        node->child->genNodeId();
        node->sibling->genNodeId();
    }
    else return;
}

void TreeNode::printNodeInfo() {
    TreeNode* node= this;
    if(node!=nullptr)
    {
        //NODE_PROG NODE_STMT NODE_EXPR
        cout<<"lno@"<<node->lineno<<"   "<<"@"<<node->nodeID<<" "<<node->nodeType2String(node->nodeType);
        if(node->nodeType==NODE_VAR)
        {
            cout<<" varname: "<<node->var_name;
            return;
        }
        if(node->nodeType==NODE_CONST)
        {
            if(node->type->type==VALUE_INT)
                cout<<" type: "<<node->int_val;
            else if(node->type->type==VALUE_CHAR)
                cout<<" type: "<<node->ch_val;
            else if(node->type->type==VALUE_STRING)
                cout<<" type: "<<node->str_val;
            else
                cout<<" type: "<<node->b_val;
            return;
        }
        if(node->nodeType==NODE_TYPE)
        {
            if(node->type->type==VALUE_INT)
                cout<<" type: int";
            else if(node->type->type==VALUE_CHAR)
                cout<<" type: char";
            else if(node->type->type==VALUE_STRING)
                cout<<" type: string";
            else
                cout<<" type: bool";
            return;
        }
    }
    else return;
}  

void TreeNode::printChildrenId() {
    if (this->child == nullptr)
        return;
    cout << " children: [";
    cout <<"@"<< this->child->nodeID << " ";
    if (this->child->sibling == nullptr)
        return;
    else {
        cout <<"@"<< this->child->sibling->nodeID << " ";
        TreeNode* temp = this->child->sibling->sibling;
        while (temp != nullptr)
        {
            cout <<"@"<< temp->nodeID << " ";
                temp = temp->sibling;
        }
    }
    cout << " ]";
    if(this->nodeType==NODE_STMT)
    {
        cout<<" stmt: "<<this->sType2String(this->stype)<<endl;
        return;
    }
    
    cout<<endl;
}

void TreeNode::printAST() {//先序遍历
    TreeNode* node= this;
    if(node!=nullptr)
    {
        node->printNodeInfo();
        if(node->nodeType!=NODE_VAR&&node->nodeType!=NODE_CONST&&node->nodeType!=NODE_TYPE)
            node->printChildrenId();
        else cout<<endl;
        node->child->printAST();
        node->sibling->printAST();
    }
    else return;
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
            return"skip";
            break;
        case STMT_DECL:
            return"decl";
            break;
        case STMT_IF:
            return"if";
            break;
        case STMT_WHILE:
            return"while";
            break;
        case STMT_PRINTF:
            return"printf";
            break;
         case STMT_SCANF:
            return"sacnf";
            break;
        default:
            return"?";
            break;
    }
}


string TreeNode::nodeType2String (NodeType type){
    switch(type){
        case NODE_CONST:
            return"const";
            break;
        case NODE_VAR:
            return"variable";
            break;
        case NODE_EXPR:
            return"expression";
            break;
        case NODE_TYPE:
            return"type";
            break;
        case NODE_STMT:
            return"statement";
            break;
        case NODE_PROG:
            return"program";
            break;
        default:
            return"<>";
            break;
    }
}

string opType2String (OperatorType type){
    switch(type){
        case OP_EQ:
            return"EQ";
            break;
        case OP_NOT:
            return"NOT";
            break;
        case OP_OR:
            return"OR";
            break;
        case OP_AND:
            return"AND";
            break;
        case OP_NE:
            return"NE";
            break;
        case OP_SE:
            return"SE";
            break;
        case OP_BE:
            return"BE";
            break;
        case OP_BT:
            return"BT";
            break;
        case OP_PLUS:
            return"PLUS";
            break;
        case OP_MINUS:
            return"MINUS";
            break;
        case OP_MUL:
            return"MUL";
            break;
        case OP_DIV:
            return"DIV";
            break;
        case OP_MOD:
            return"MOD";
            break;
        default:
            return"!";
            break;
    }
}
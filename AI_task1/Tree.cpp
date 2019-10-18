#include <bits/stdc++.h>
using namespace std;
#define max_Tree_Size   100

class tree_Class
{
    vector <int> Tree[max_Tree_Size];

public:

    void push_Node(int child, int parent)
    {
        Tree[parent].push_back(child);
    }

    void print_Nodes()
    {
        for(int i=0 ; i<max_Tree_Size; i++)
        {
            if (Tree[i].size())
                cout<<"Nodes of "<<i<<": ";
            for(int j=0 ; j<Tree[i].size() ; j++)
            {
                cout<<Tree[i][j]<<" ";
            }
            if (Tree[i].size())
                cout<<endl;
        }
    }
    /* Returns the parent node if found
        Or -1 otherWise */
    int find_Node(int val)
    {
        for(int i=0 ; i<max_Tree_Size; i++)
        {

            for(int j=0 ; j<Tree[i].size() ; j++)
            {
                if (Tree[i][j] == val)
                {
                    return i;
                }
            }
        }
        return -1;
    }
    /* Return 1 : if deleted
       Return 0 : not found to delete*/
    bool del_Node(int value)
    {
        int x = find_Node(value);
        if (x==-1)
            return 0;

        Tree[x].erase(remove(Tree[x].begin(), Tree[x].end(), value), Tree[x].end());
        return 1;
    }
};


int main()
{
    tree_Class newTree;
    newTree.push_Node(2 , 0);
    newTree.push_Node(5 , 0);
    newTree.push_Node(3 , 2);
    newTree.push_Node(4 , 3);
    newTree.print_Nodes();
    int f = newTree.find_Node(4);
    if (f != -1)
        cout<<"Node: "<<4<<" Found as a child of: "<<f<<endl;
    bool d = newTree.del_Node(4);
    if(d)
        cout<<"deleted..\n";
    newTree.print_Nodes();
}

//implementation of Minheap using array - 
#include<vector>
#include<iostream>
using namespace std;

class MinHeap{

    public:
        vector<int> array;
        int size;


        int returnLeftChildIndex(int index){
            return ((2*index)+1);
        }


        int returnRightChildIndex(int index){
            return ((2*index)+2);
        }


        int returnParentIndex(int index){
            return ((index-1)/2);
        }

        int returnLeftChild(int index){
            int i = returnLeftChildIndex(index);
            return array[i];

        }

    
        int returnRightChild(int index){
            int i = returnRightChildIndex(index);
            return array[i];
        }


        int returnParent(int index){
            int i = returnParentIndex(index);
            return array[i];
        }

        bool hasParent(int index){
            if(returnParentIndex(index) >-1 && returnParentIndex(index) < size)
                return true;
            return false;
        }


        bool hasLeftChild(int index){
            if(returnLeftChildIndex(index) >-1 && returnLeftChildIndex(index) < size)
                return true;
            return false;
        }

        bool hasRightChild(int index){
            if(returnRightChildIndex(index) >-1 && returnRightChildIndex(index) < size)
                return true;
            return false;
        }

        void swapValue(int index, int leftChildIndex){//swaps value of node with given child node

            int temp;
            temp = array[index];
            array[index] = array[leftChildIndex];
            array[leftChildIndex] = temp;


        
            
        }



int peek(){ //returns the root of heap
    if(size == 0)
        return -1;
    return array[0];

}


int extract_min(){ //returns the miniumum/root and deletes it from the heap

    int min = array[0];
    array[0] = array[size-1];
    size--;
    heapifyDown();
    return min;

}


void insertNode(int value){ //insert node left to right then heapify up until node < LC and RC

    array.push_back(value);
    size++;
    
    cout << "added to array";


    heapifyUp();

}

void heapifyUp(){ //start from last node of the array and bubble up fixing it until node <LC and RC

    int index = size-1;//last node

    while(hasParent(index) && array[index] < returnParent(index) ){ //because heap rpoperty
        //bubble up
        swapValue(returnParentIndex(index), index);
        index = returnParentIndex(index);
    }

}

void heapifyDown(){//fix the array from root and bubbling down till leftchild and rightchild > node 

    int index = 0; //start from the root
    while(hasLeftChild(index)){  //executes as long as there is a left child, no need to check for right since complete binary tree
    
        if(hasRightChild(index) && (returnLeftChild(index) > returnRightChild(index))){
            if(returnRightChild(index) > array[index] )
                return;
            else{
                swapValue(index, returnRightChildIndex(index));
                index = returnRightChildIndex(index);
            }
        }
    
        if((!hasRightChild(index)) || returnLeftChild(index) < returnRightChild(index)){
            if(returnLeftChild(index) > array[index]){
                return;

            }

        
            else{
                swapValue(index, returnLeftChildIndex(index));
                index = returnLeftChildIndex(index);

            }

        }   
}
}
};

int main(){

    MinHeap heap;
    cout <<"input size of array:";
    cin >> heap.size;
    int s = heap.size;
    int input;

    for(int i = 0; i < s; i++){
       cout <<"input: ";
       cin >> input;
       heap.array.push_back(input); 

    }

    heap.heapifyDown();
    cout <<"pass";
    cout << "min value is now = " << heap.extract_min();
    
    //insert new Node
    cout <<"inserting node - 2" << endl;
    heap.insertNode(2);

    
    int a = heap.size;
    cout << endl;
    for(int i = 0; i <a; i++){
        cout << heap.array[i];
    }
    return 0;
        

}

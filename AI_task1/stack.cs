using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Stack
    {
        private int[] ele;
        private int top;
        private int max;
        public Stack(int size)
        {
            ele = new int[size];
            top = -1;
            max = size;
        }

        public void push(int item)
        {
            if (top == max - 1)
            {
                Console.WriteLine("Stack Overflow");
                return;
            }
            else
            {
                ele[++top] = item;

            }
        }

        public void pop()
        {
            if (top == -1)
            {
                Console.WriteLine("Stack Underflow");

            }
            else
            {
                Console.WriteLine("Poped element is: " + ele[top]);
                top--;


            }
        }
        public void TopElement()
        {
            Console.WriteLine("Top element is: "+ ele[top]);
        }

        public bool IsEmpty()
        {
            if (top == -1)
                return true;
            else
                return false;
        }

        public void printStack()
        {
            if (!IsEmpty())
            {
                Console.WriteLine("Stack elements are : ");
                for (int i = 0; i <= top; i++)
                {
                    Console.Write(ele[i] + " ");

                }
                Console.WriteLine();
            }
            else
                Console.WriteLine("Stack is empty.");
        }
       
    }

    class Program
    {
        static void Main(string[] args)
        {
            Stack S = new Stack(5);
            Console.WriteLine("Before pushing : ");
            S.printStack();

            S.push(10);
            S.push(20);
            S.push(30);
            S.push(40);
            S.push(50);

            Console.WriteLine("\nAfter pushing items");
            S.printStack();
            Console.WriteLine();

            S.TopElement();
            S.pop();
            S.pop();
            S.pop();
            S.IsEmpty();
            Console.WriteLine();

            S.printStack();
            Console.WriteLine();

            S.pop();
            S.pop();
            Console.WriteLine();

            S.printStack();
            Console.ReadLine();
        }
    }
}
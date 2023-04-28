/*
Assume that the test results of a batch of students are stored in three different
classes. Class Students are storing the roll number. Class Test stores the
marks obtained in two subjects and class result contains the total marks
obtained in the test. The class result can inherit the details of the marks
obtained in the test and roll number of students. (Multiple Inheritance)
*/

#include<iostream>
using namespace std;

class student
{
    protected:
    int roll_number;
};

class test
{
    protected:
    int sub1, sub2;
};

class result: public student, public test
{
    protected:
    int total_marks;

    public:
    void getdata()
    {
        cout << "\nEnter Roll Number: ";
        cin >> roll_number;
        cout << "\nEnter Marks of Sub1: ";
        cin >> sub1;
        cout << "\nEnter marks of Sub2: ";
        cin >> sub2;
    }

    void totalmarks()
    {
        total_marks = sub1 + sub2;
    }

    void putdata()
    {
        cout << "\nRoll Number: " << roll_number;
        cout << "\nMarks of Sub1: " << sub1;
        cout << "\nMarks of Sub2: " << sub2;
        cout << "\nTotal Marks: " << total_marks;
    }
};

int main()
{
    result obj;
    obj.getdata();
    obj.totalmarks();
    obj.putdata();
}

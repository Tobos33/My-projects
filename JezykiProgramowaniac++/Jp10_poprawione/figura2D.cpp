#include "figura2D.h"


float dlugosc(punkt a, punkt b){
    float d;
    d = sqrt(pow((b.x-a.x), 2) + pow((b.y - a.y), 2));
    return d;
}

float kolo::pole(){
    P = pi*pow(R,2);
    return P; 
}

float kolo::obw(){
    L = 2*pi*R;
    return L;
}

void kolo::wypisz(){
    cout<<"pole = "<<P<<endl<<"; obwod = "<<L<<endl<<"figura jest kolem o promieniu "<<R<<endl;
}

float koloAnali::pole(){
    R = dlugosc(sr, ob);
    P = pi*pow(R,2);
    return P; 
}

float koloAnali::obw(){
    R = dlugosc(sr, ob);
    L = 2*pi*R;
    return L;
}

float kwadrat::pole(){
    P = A*B;
    return P; 
}

float kwadrat::obw(){
    L = 2*A+2*B;
    return L;
}

void kwadrat::wypisz(){
    cout<<"pole = "<<P<<endl<<"obwod = "<<L<<endl<<"figura jest kwadratem o wymiarach "<<A<<"x"<<B<<endl;
}

float kwadratAnali::pole(){
    A = dlugosc(a, b);
    B = dlugosc(a, d);
    P = A*B;
    return P; 
}

float kwadratAnali::obw(){
    A = dlugosc(a, b);
    B = dlugosc(a, d);
    L = 2*A+2*B;
    return L;
}


float trapez::pole(){
    P = (A+B)*C/2;  
    return P; 
}

float trapez::obw(){
    L = A+B+C+D;
    return L;
}

void trapez::wypisz(){
    cout<<"pole = "<<P<<endl<<"obwod = "<<L<<endl<<"figura jest trapezem o podstawach "<<A<<" i "<<B<<" oraz ramionach "<<C<<" i "<<D<<endl;
}

float trapezAnali::pole(){
    A = dlugosc(a, b);
    B = dlugosc(c, d);
    C = dlugosc(c, b);
    D = dlugosc(a, d);
    if (C > D) 
        P = (A+B)*D/2;
    else 
        P = (A+B)*C/2;    
    return P; 
}

float trapezAnali::obw(){
    A = dlugosc(a, b);
    B = dlugosc(c, d);
    C = dlugosc(c, b);
    D = dlugosc(a, d);
    L = A+B+C+D;
    return L;
}

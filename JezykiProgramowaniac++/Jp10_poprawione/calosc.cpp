#include <iostream>
#include <cmath>
#include <string>
#define pi 3.14

using namespace std;

class punkt{
    public:
    float x,y;
    punkt(float xp = 0, float yp = 0): x(xp), y(yp){}
    ~punkt(){}
};

float dlugos(punkt a, punkt b);

class figura2D{
    protected:
    float P, L;
    public:
    figura2D(){}
    virtual ~figura2D(){}
    void virtual wypisz() = 0;
};

class kolo:public figura2D{
    protected:
    float R;
    public:
    kolo(float promien = 0): R(promien){}
    ~kolo(){}
    float virtual pole();
    float virtual obw();
    void wypisz();
};

class koloAnali:public kolo{
    protected:
    punkt sr, ob;
    public:
    koloAnali(punkt srodek = (0,0), punkt pobw = (0,0)): sr(srodek), ob(pobw) {}
    ~koloAnali(){}
    float pole();
    float obw();
    
};


class kwadrat:public figura2D{
    protected:
    float A,B;
    public:
    kwadrat(float a1 = 0, float b1 = 0): A(a1), B(b1){}
    ~kwadrat(){}
    float virtual pole();
    float virtual obw();
    void wypisz();
};

class kwadratAnali:public kwadrat{
    protected:
    punkt a, b, c, d;
    public:
    kwadratAnali(punkt a1 = (0,0), punkt b1 = (0,0), punkt c1 = (0,0), punkt d1 = (0,0)): a(a1), b(b1), c(c1), d(d1) {}
    ~kwadratAnali(){}
    float pole();
    float obw();
};

class trapez:public figura2D{
    protected:
    float A,B,C, D;
    public:
    trapez(float a1 = 0, float b1 = 0, float c1 = 0, float d1 = 0): A(a1), B(b1), C(c1), D(sqrt(pow(a1-b1, 2)+pow(c1,2))){}
    ~trapez(){}
    float virtual pole();
    float virtual obw();
    void wypisz();
};

class trapezAnali:public trapez{
    protected:
    punkt a, b, c, d;
    public:
    trapezAnali(punkt a1 = (0,0), punkt b1 = (0,0), punkt c1 = (0,0), punkt d1 = (0,0)): a(a1), b(b1), c(c1), d(d1) {}
    ~trapezAnali(){}
    float pole();
    float obw();
};


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


int main(){
    /*
    float z;
    cout<<"podaj promien kola"<<endl;
    cin>>z;
    kolo K(z);
    K.pole();
    K.obw();
    K.wypisz();
    float xs, ys, yo, xo;
    cout<<"Podaj wspolrzedne srodka kola"<<endl;
    cout<<"Podaj wspolrzedna x srodka kola"<<endl;
    cin>>xs;
    cout<<"Podaj wspolrzedna y srodka kola"<<endl;
    cin>>ys;
    cout<<"Podaj wspolrzedne dowolnego punktu na kole";
    cout<<"Podaj wspolrzedna x punktu na kole"<<endl;
    cin>>xo;
    cout<<"Podaj wspolrzedna y punktu na kole"<<endl;
    cin>>yo;
    punkt s(xs, ys);
    punkt o(xo, yo);
    koloAnali K2(o,s);
    K2.pole();
    K2.obw();
    K2.wypisz();

    float A, B;
    
    cout<<"podaj boki kwadratów"<<endl;    
    cout<<"podaj 1 bok kwadratu"<<endl;    
    cin>>A;
    cout<<"podaj 2 bok kwadratu"<<endl; 
    cin>>B;

    kwadrat Kw(A, B);

    Kw.pole();
    Kw.obw();
    Kw.wypisz();

    float punkty_x[4];
    float punkty_y[4];
    cout<<"podaj współrzędne punktów w kwadracie"<<endl;
    for (int i = 0; i < 4; i++){
        cout<<"podaj wspolrzedne x "<<i+1<<" punktu"<<endl;
        cin>>punkty_x[i];
        cout<<"podaj wspolrzedne y "<<i+1<<" punktu"<<endl;
        cin>>punkty_y[i];
    }

    punkt a(punkty_x[0], punkty_y[0]);
    punkt b(punkty_x[1], punkty_y[1]);
    punkt c(punkty_x[2], punkty_y[2]);
    punkt d(punkty_x[3], punkty_y[3]);
    kwadratAnali Kw2(a,b,c,d);

    Kw2.pole();
    Kw2.obw();
    Kw2.wypisz();

    float C, D;
    cout<<"podaj boki trapezu"<<endl;    
    cout<<"podaj 1 podstawę trapezu"<<endl;    
    cin>>A;
    cout<<"podaj 2 podstawę trapezu"<<endl; 
    cin>>B;
    cout<<"podaj 1 ramię trapezu"<<endl;
    cin>>C;

    trapez T(A, B, C, D);
    T.pole();
    T.obw();
    T.wypisz();
    */
    float punkty2_x[4];
    float punkty2_y[4];
    cout<<"podaj współrzędne punktów w trapezie"<<endl;
    for (int i = 0; i < 4; i++){
        cout<<"podaj wspolrzedne x "<<i+1<<" punktu"<<endl;
        cin>>punkty2_x[i];
        cout<<"podaj wspolrzedne y "<<i+1<<" punktu"<<endl;
        cin>>punkty2_y[i];
    }

    punkt e(punkty2_x[0], punkty2_y[0]);
    punkt f(punkty2_x[1], punkty2_y[1]);
    punkt g(punkty2_x[2], punkty2_y[2]);
    punkt h(punkty2_x[3], punkty2_y[3]);
    trapezAnali T2(e,f,g,h);

    T2.pole();
    T2.obw();
    T2.wypisz();

}
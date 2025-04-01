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

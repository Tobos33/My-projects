#include<iostream>
using namespace std;


enum wody {niekreslone, slodkie, slone};

class zwierze {
    protected:
    string imie;
    unsigned int wiek;
    public:
    zwierze(string i = "-", unsigned int wi = 0): imie(i), wiek(wi) {};
    virtual ~zwierze(){};
    void virtual przedstaw(){cout<<"imie: "<<imie<<" wiek: "<<wiek<<" lat ";};
};

class ryba: public zwierze {
    protected:
    enum wody woda;
    public:
    ryba(string i = "-", unsigned int wi = 0, enum wody wo = niekreslone): 
    zwierze(i, wi), woda(wo) {};
    ~ryba(){};
    void przedstaw(){zwierze::przedstaw(); cout<<" woda: "<<woda<<endl;};
};

class plaz: public zwierze {
    protected:
    unsigned int dlugosc;
    public:
    plaz(string i = "-", unsigned int wi = 0, unsigned int d = 0): 
    zwierze(i, wi), dlugosc(d) {};
    ~plaz(){};
    void przedstaw(){zwierze::przedstaw(); cout<<" dlugosc: "<<dlugosc<<" cm"<<endl;};
};

class gad: public zwierze {
    protected:
    unsigned int dlugosc_zycia;
    public:
    gad(string i = "-", unsigned int wi = 0, unsigned int d_z = 0): 
    zwierze(i, wi), dlugosc_zycia(d_z) {};
    ~gad(){};
    void przedstaw(){zwierze::przedstaw();cout<<" dlugosc zycia: "<<dlugosc_zycia<<" lat"<<endl;};
};

class ptak: public zwierze {
    protected:
    string kolor;
    public:
    ptak(string i = "-", unsigned int wi = 0, string k = "-"): 
    zwierze(i, wi), kolor(k) {};
    ~ptak(){};
    void przedstaw(){zwierze::przedstaw();cout<<", kolor: "<<kolor<<endl;};
};

class ssak: public zwierze {
    protected:
    unsigned int dlugosc_ciazy;
    public:
    ssak(string i = "-", unsigned int wi = 0, unsigned int d_z = 0): 
    zwierze(i, wi), dlugosc_ciazy(d_z) {};
    ~ssak(){};
    void przedstaw(){zwierze::przedstaw();cout<<" dlugosc ciazy: "<<dlugosc_ciazy<<" tyg."<<endl;};
};




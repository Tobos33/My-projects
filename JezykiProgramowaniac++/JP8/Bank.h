#include <iostream>
#include <cmath>
#include <string>

using namespace std;


class KontoBankowe{
    float * konto;
    string nazwa_konta;
    static int counter;
    public:
    KontoBankowe(float=0, string = "bezimienne konto");
    KontoBankowe(const KontoBankowe&);
    ~KontoBankowe();
    void operator+=(float);
    friend ostream& operator<<(ostream&, KontoBankowe&);
    float wyplac(float);
    void liczbaczlonkow(){cout<<"Liczba czlonkow Banku wynosi "<<counter<<" czlonkow!"<<endl;}
};

ostream& operator<<(ostream&, KontoBankowe&);
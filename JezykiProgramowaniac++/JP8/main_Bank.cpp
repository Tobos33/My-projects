#include "Bank.h"

int main(){
    KontoBankowe lokata(0, "Prywatna lokata");
    KontoBankowe sklep(200,"Sklep");
    KontoBankowe pustalokata;
    cout<<pustalokata;
    lokata += 2.7;
    cout<<lokata;
    cout<<sklep;
    cout<<endl;
    sklep += lokata.wyplac(1.2);
    cout<<lokata;
    cout<<sklep;
    lokata.liczbaczlonkow();
}


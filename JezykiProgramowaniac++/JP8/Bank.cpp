#include "Bank.h"


int KontoBankowe::counter = 0;

KontoBankowe::KontoBankowe(float stan, string nazwa){
    konto = new float;
    *konto = stan;
    nazwa_konta = nazwa;
    counter++;
}

KontoBankowe::KontoBankowe(const KontoBankowe& B){
    konto = new float;
    konto = B.konto;
    counter++;
}

KontoBankowe::~KontoBankowe(){
    delete konto;
    counter--;
}


void KontoBankowe::operator+=(float wplata){
    *konto += wplata;
}

ostream& operator<<(ostream& out, KontoBankowe& B){
    out<<"Stan konta - "<<B.nazwa_konta<<" : "<<*B.konto<<" PLN"<<endl;
    return out;  
}

float KontoBankowe::wyplac(float w){
    *konto -= w;
    return w;
}
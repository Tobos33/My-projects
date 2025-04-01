#include "figura2D.h"

int main(){
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
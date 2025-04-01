#include <iostream>
#include <fstream>
#include <string>
#include "/home/students/fiz2023/pawstr/JP/Jp5_poprawione2/losowe.h"
using namespace std;

template <class type>   
void wypisz(type tab[], int N){
    for (int i = 0l; i<N; i++)
        cout<<tab[i]<<" ";
    cout<<endl<<endl;
}

template <class type>
void sortuj_rosnaco(type tab[], int N){
    for(int i = 0; i<N; i++){
        for (int j = 0; j+1<N-i; j++){
            if(tab[j]>tab[j+1])
                swap(tab[j], tab[j+1]);

        }
    }
}

template <class type>
void sortuj_malejaco(type tab[], int N){
    for(int i = 0; i<N; i++){
        for (int j = 0; j+1<N-i; j++){
            if(tab[j]<tab[j+1])
                swap(tab[j], tab[j+1]);

        }
    }
}

int main(){
    fstream fin;
    fin.open("int.dat", ios::in);
    
    int N;
    fin>>N;

    int tab[N];

    for(int i = 0; i<N; i++){
        fin>>tab[i];
    }

    fin.close();

    //cout<<N<<endl;

    wypisz(tab, N);
    sortuj_malejaco(tab, N);
    wypisz(tab, N);

    fstream fout;
    fout.open("nowe_int.dat", ios::out);
    fout<<N<<'\n';
    for(int i = 0; i<N; i++){
        fout<<tab[i]<<" ";
    }

    fin.open("char.dat", ios::in);
    
    fin>>N;

    char tab_2[N];

    for(int i = 0; i<N; i++){
        fin>>tab_2[i];
    }

    fin.close();

    //cout<<N<<endl;

    wypisz(tab_2, N);
    sortuj_rosnaco(tab_2, N);
    wypisz(tab_2, N);  

    fout.open("nowe_char.dat", ios::out);
    fout<<N<<'\n';
    for(int i = 0; i<N; i++){
        fout<<tab_2[i]<<" ";
    }

    int a,c,m,seed;
    a = 263;
    c = 499;
    m = 569;
    seed = 199;
    cout<<"podaj liczbe elemntow"<<endl;
    cin>>N;
    Generator gen(N, a, c, m, seed);
    generacja(gen);
    skalowanie(gen);
    cout<<"podaj sposob sortowanania 1 - rosnaco, 2 - malejaco"<<endl;
    int x;
    cin>>x;
    if(x == 1){
        sortuj_rosnaco(gen.tab, N);
        wypisz(gen.tab, N);}
    else if(x == 2){
        sortuj_rosnaco(gen.tab, N);
        wypisz(gen.tab, N);}
    //gen.PrintGenerator();

}
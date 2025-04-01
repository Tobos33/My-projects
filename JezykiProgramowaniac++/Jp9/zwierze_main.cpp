#include "zwierze.h"

int main(){
    zwierze *z1 = new zwierze;
    zwierze *z2 = new zwierze("Bartek", 2);
    ryba *r1 = new ryba("plotka", 3, slodkie);
    plaz *pl1 = new plaz("zaba", 4, 10);
    gad *g1 = new gad("kameleon", 5, 3);
    ptak *pt1 = new ptak("orzelo", 6, "bialy");
    ssak *s1 = new ssak("kot", 7, 7);
    z1->przedstaw();
    cout<<endl;
    z2->przedstaw();
    cout<<endl;
    r1->przedstaw();
    pl1->przedstaw();
    g1->przedstaw();
    pt1->przedstaw();
    s1->przedstaw();
    cout<<endl<<endl;
    z1 = z2;
    z1->przedstaw();
    cout<<endl;
    z1 = r1;
    z1->przedstaw();
    z1 = pl1;
    z1->przedstaw();
    z1 = g1;
    z1->przedstaw();
    z1 = pt1;
    z1->przedstaw();
    z1 = s1;
    z1->przedstaw();
    return 0;
}
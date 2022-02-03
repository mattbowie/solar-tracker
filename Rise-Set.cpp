#include<iostream>
#include<stdio.h>
#include<math.h>

int main(){
    /* source:
    Almanac for Computers, 1990
	published by Nautical Almanac Office
	United States Naval Observatory
	Washington, DC 20392*/

    float pi=3.14159, latitude=37.210388, longitude=-93.297256, longh, rise, set, maRise, maSet, lRise, lSet, raRise, raSet, lQuadRise, lQuadSet, raQuadRise, raQuadSet, raRiseH, raSetH, sinDecRise, sinDecSet, cosDecRise, cosDecSet, zenith, cosHRise, cosHSet, hRise, hSet, tRise, tSet, utcRise, utcSet;
    short doy=150;

    //convert long to hour and calculate time
    longh=longitude/15;
    rise=doy+(6-longh)/24;
    set=doy+(18-longh)/24;
    //calculate sun's mean anomaly
    maRise=0.9856*rise-3.289;
    maSet=0.9856*set-3.289;
    //calculate sun's true longitude
    lRise=maRise+(1.916*sin(maRise))+(0.02*sin(2*maRise));
    lSet=maSet+(1.916*sin(maSet))+(0.02*sin(2*maSet));
    if(lRise>360){
        lRise=lRise-360;
    }
    if(lRise<0){
       lRise=lRise+360;
    }
    if(lSet>360){
        lSet=lSet-360;
    }
    if(lSet<0){
       lSet=lSet+360;
    }
    //calculate sun's right ascention
    raRise=atan(0.91764*tan(lRise));
    raSet=atan(0.91764*tan(lSet));
    if(raRise>360){
        raRise=raRise-360;
    }
    if(raRise<0){
        raRise=raRise+360;
    }
    if(raSet>360){
        raSet=raSet-360;
    }
    if(raSet<0){
       raSet=raSet+360;
    }
    //right ascention needs to be in the same quadrant as the sun's true longitude
    lQuadRise=floor(lRise/90)*90;
    lQuadSet=floor(lSet/90)*90;
    raQuadRise=floor(raRise/90)*90;
    raQuadSet=floor(raSet/90)*90;
    raRise=raRise+(lQuadRise-raQuadRise);
    raSet=raSet+(lQuadSet-raQuadSet);
    //convert right ascention to hours
    raRiseH=raRise/15;
    raSetH=raSet/15;
    //calculate sun's declination
    sinDecRise=0.39782*sin(lRise);
    sinDecSet=0.39782*sin(lSet);
    cosDecRise=cos(asin(sinDecRise));
    cosDecSet=cos(asin(sinDecSet));
    //calculate sun's local hour angle
    zenith=90-raRise;
    cosHRise=(cos(zenith)-(sinDecRise*sin(latitude)))/(cosDecRise*cos(latitude));
    cosHSet=(cos(zenith)-(sinDecSet*sin(latitude)))/(cosDecSet*cos(latitude));
    //calculate sun's local hour
    hRise=360-acos(cosHRise);
    hSet=acos(cosHSet);
    hRise=hRise/15;
    hSet=hSet/15;
    //calculate mean time of rising and setting
    tRise=hRise+raRiseH-(0.06571*rise)-6.622;
    tSet=hSet+raSetH-(0.06571*set)-6.622;
    //adjust back to UTC
    utcRise=tRise-longh;
    utcSet=tSet-longh;
    if(utcRise>24){
        utcRise=utcRise-24;
    }
    if(utcRise<0){
        utcRise=utcRise+24;
    }
    if(utcSet>24){
        utcSet=utcSet-24;
    }
    if(utcSet<0){
        utcSet=utcSet+24;
    }

    return 0;
}
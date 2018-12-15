#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <fstream>
#include <cstring>
using namespace std;

ofstream fout;

//Pre-defined structure, used for Hour, Minute
typedef pair<int, int> Tp;

//Structure for saving input data
struct csv{
    string LOC_DT;
    string LOCKER_ID;
    string LOC_X;
    string LOC_Y;
    string LOC_OLD;
    string LOC_SEX;

    csv(string dt, string lid, string x, string y, string dold, string dsex){
        LOCKER_ID = lid;
        LOC_X = x;
        LOC_Y = y;
        LOC_OLD = dold;
        LOC_SEX = dsex;
        LOC_DT = dt;
    }

    void printAll(){
		cout << "Printing data for [" << LOCKER_ID << "] with old : [" << LOC_OLD << "]\n";
		fout << LOCKER_ID << " " << LOC_OLD << " " <<  LOC_SEX << endl;
    }
};

//Structure for save data about each person
struct People{
    string pNum, old;
    Tp startTime[43], rTime[43];
    int bef, plsec[43], sec[43];
    int WoM;
	//Save time data. Compare with previous data, and accumulate.
    void inputST(int tH, int tM, int tS, int plNum){
        if(bef == plNum) {
            rTime[plNum].first += tH - startTime[plNum].first;
            rTime[plNum].second += tM - startTime[plNum].second;
			plsec[plNum] += tS - sec[plNum];
			if (tM < startTime[plNum].second){
				rTime[plNum].first -= 1;
				rTime[plNum].second += 60;
			}
			if (tS < sec[plNum]){
				rTime[plNum].second -= 1;
				plsec[plNum] += 60;
			}
            if(plsec[plNum] >= 60){
                plsec[plNum] -= 60;
                rTime[plNum].second += 1;
            }
            if(rTime[plNum].second >= 60){
                rTime[plNum].second -= 60;
                rTime[plNum].first += 1;
            }
        }
		startTime[plNum] = make_pair(tH, tM);
        sec[plNum] = tS;
		bef = plNum;
		
    }

    void printAll(){
		cout << "Printing data for " << pNum  << " old " << old << "\n";
		fout << pNum << " " << old << " " <<  WoM << endl;
    }

	//Initialize
    People(){
        memset(plsec, 0, sizeof(plsec));
        memset(sec, 0, sizeof(sec));
    }
};

//Using vector instead of array, cause we don't know size of the data.
vector<People> user;
vector<csv> dataF;
vector<int> delOld[10];

int main(int argc, char** argv){
    ios_base::sync_with_stdio(0);
    string dLine, lid, zid, x, y, dt, dOld, dSex;
	// if(argc < 3){
	// 	cout << "Usage : " << argv[0] << " [file for analyze] [file for standards]\n";
	// 	exit(-1);
	// }
	
    bool fnd = false;
    int placeNum, Timetmp;
	char buf[20], namebuf[20], stnamebuf[20], outname[20] = "out_";
	string strBuf, toktmp;
	int i = 0, th = 0, tm = 0, ts, w, m, dold = 0;

	cout << "Choose file..\n> ";
	cin >> namebuf;

    ifstream fData(namebuf);
	
	//for print data to a file. Unused.
	strcat(outname, namebuf);
	strtok(outname, ".");
	strcat(outname, ".txt");
	fout.open(outname);

	cout << "reading " << namebuf << "...\n";
	i = 0;
	//Reading data until end of file
    while(!fData.eof()){

		i++;
        getline(fData, dLine, ',');
        dt = dLine;
        getline(fData, dLine, ',');
        lid = dLine;
        getline(fData, dLine, ',');
        x = dLine;
        getline(fData, dLine, ',');
        y = dLine;
        getline(fData, dLine, ',');
        dOld = dLine;
        getline(fData, dLine, '\n');
        dSex = dLine;

		if (lid.length() >= 2 && lid != "LOCKER_ID" && dt.length() > 12) //Filtering abnormal data
            for(auto &v : dataF){
                if(lid == v.LOCKER_ID && dOld == v.LOC_OLD) goto Exist;
            }
			dataF.push_back(csv(dt, lid, x, y, dOld, dSex));
Exist:
    continue;
    }
    
	
	// cout << "Now working...\n";
    // for(auto v : dataF){
	// 	fnd = false;
	// 	strcpy(buf, v.LOC_DT.c_str());

	// 	//Filtering abnormal data
	// 	//Find people with data's LOCKER_ID. If fails, makes new data field with the LOCKER_ID
    //     for(auto& p : user){
    //        if(p.pNum == v.LOCKER_ID && p.old == v.LOC_OLD){
    //             fnd = true;
    //             ts = atoi(buf + 12); buf[12] = 0; buf[13] = 0;
    //             tm = atoi(buf + 10); buf[10] = 0; buf[11] = 0;
    //             th = atoi(buf + 8); 
				
    //             p.inputST(th, tm, ts, placeNum);
    //             break;
    //        }
    //     }
    //     if(!fnd){
    //         user.push_back(People());
    //         auto *p = &user[user.size() - 1];
    //         p->pNum = v.LOCKER_ID;
    //         p->old = v.LOC_OLD;
    //         ts = atoi(buf + 12); buf[12] = 0; buf[13] = 0;
    //         tm = atoi(buf + 10); buf[10] = 0; buf[11] = 0;
    //         th = atoi(buf + 8); 
				
    //         p->inputST(th, tm, ts, placeNum);
    //     }
       
    // }
	
	//Print all
    for(auto p : dataF){
        p.printAll();
    }

	cout << "Job finished\n";
}  
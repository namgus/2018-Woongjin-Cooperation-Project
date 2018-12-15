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
    string LOCKER_ID;
    string ZONE_ID;
    string LOC_X;
    string LOC_Y;
    string LOC_DT;

    csv(string lid, string zid, string x, string y, string dt){
        LOCKER_ID = lid;
        ZONE_ID = zid;
        LOC_X = x;
        LOC_Y = y;
        LOC_DT = dt;
    }
};

//Structure for save data about each person
struct People{
    string pNum;
    Tp startTime[43], rTime[43];
    int bef, plsec[43], sec[43];
    int WoM, old;
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
		cout << "Printing data for " << pNum << "\n";
		fout << "LOCKER_ID = " << pNum << " [ " << "old : " << old << "x || gender : " <<  WoM << " ] " << endl;
        for(int i = 0; i < 43; i++){
            if(rTime[i].first || rTime[i].second || plsec[i])
                fout << i << "th Location : " << rTime[i].first << "h " << rTime[i].second << "m " << plsec[i] << "s" << endl;
        }
		fout << endl;
    }

	//Initialize
    People(){
        memset(plsec, 0, sizeof(plsec));
        memset(sec, 0, sizeof(sec));
    }
};

int seperate(string SC_ID, int x, int y){
    int area_num = 0;
    if (!SC_ID.compare("B2-C-S7")|| !SC_ID.compare("B2-C-S8")||!SC_ID.compare("B2-C-S9")||!SC_ID.compare("B2-C-S10")||!SC_ID.compare("B2-D-S1")
				|| !SC_ID.compare("B2-D-S2") || !SC_ID.compare("B2-D-S3") || !SC_ID.compare("B2-D-S4") || !SC_ID.compare("B2-D-S5") || !SC_ID.compare("B2-D-S36")
				|| !SC_ID.compare("B2-D-S7") || !SC_ID.compare("B2-D-S8") || !SC_ID.compare("B2-D-S9") || !SC_ID.compare("B2-D-S10")) {
			if (x>=44.1 && y>=27.6 && x<=63.7 && y<=51)
				area_num = 14;
			else if (x>=29.4 && y>=55 && x<=58.8 && y<=63.9)
				area_num = 15;
			else if (x>=59 && y>=55 && x<=78.4 && y<=63.9)
				area_num = 16;
			else if (x>=68.6 && y>=29.7 && x<=86.5 && y<=51)
				area_num = 17;
			else if (x>=32.6 && y>=32.6 && x<=50 && y<=50)
				area_num = 18;
			else if (x>=86.5 && y>=16 && x<=98 && y<=32.6)
				area_num = 19;
			else if (x>=0 && y>=21.9 && x<=15 && y<=51)
				area_num = 20;
			else if (x>=15 && y>=21.9 && x<=20 && y<=51)
				area_num = 21;
		}
		
		//SN01
		else if (!SC_ID.compare("1F-Out-S1")|| !SC_ID.compare("1F-Out-S2")||!SC_ID.compare("1F-Out-S3")||!SC_ID.compare("1F-Out-S4")) {
			if (x>=110 && y>=10 && x<=140 && y<=50)
				area_num = 27;
			else if (x>=75 && y>=0 && x<=100 && y<=50)
				area_num = 28;
			else if (x>=45 && y>=20 && x<=70 && y<=50)
				area_num = 29;
			else if (x>=5 && y>=10 && x<=30 && y<=50)
				area_num = 30;
		}
		
		//LC01
		else if (!SC_ID.compare("B1-C-S1")|| !SC_ID.compare("B1-C-S2")||!SC_ID.compare("B1-C-S3")||!SC_ID.compare("B1-C-S4")||!SC_ID.compare("B1-C-S5")
				|| !SC_ID.compare("B1-D-S1") || !SC_ID.compare("B1-D-S2") || !SC_ID.compare("B1-D-S3") || !SC_ID.compare("B1-D-S4")) {
			if (x>=12.8 && y>=45.3 && x<=57.9 && y<=63.9)
				area_num = 22;
			else if (x>=58 && y>=45.3 && x<=91.2 && y<=63.9)
				area_num = 23;
			else if (x>=62.5 && y>=17 && x<=91.2 && y<=41.4)
				area_num = 24;
			else if (x>=52 && y>=17 && x<=62 && y<=45.3)
				area_num = 25;
			else if (x>=0 && y>=20 && x<=12.8 && y<=48)
				area_num = 26;
		}
		//WP01
		else {
			if (x>=70 && y>=21.9 && x<=105 && y<=57)
				area_num = 1;
			else if (x>=0 && y>=0 && x<=8 && y<=7)
				area_num = 10;
			else if (x>=0 && y>=27.6 && x<=25 && y<=35.4)
				area_num = 11;
			else if (x>=68.6 && y>=60.8 && x<=107.8 && y<=66)
				area_num = 12;
			else if (x>=107.8 && y>=43.2 && x<=117 && y<=66.6)
				area_num = 13;
			else if (x>=29.4 && y>=10 && x<=61.8 && y<=14)
				area_num = 41;//2.1
			else if (x>=9.8 && y>=35.4 && x<=19.6 && y<=58.8)
				area_num = 42;//2.2
			else if (x>=78.4 && y>=3 && x<=107.8 && y<=19)
				area_num = 3;
			else if (x>=58.3 && y>=3 && x<=78.4 && y<=12)
				area_num = 4;
			else if (x>=19.6 && y>=5 && x<=29.4 && y<=26)
				area_num = 5;
			else if (x>=19.6 && y>=37.5 && x<=49 && y<=53.1)
				area_num = 6;
			else if (x>=29.4 && y>=19 && x<=39.2 && y<=26)
				area_num = 7;
			else if (x>=58.8 && y>=19.8 && x<=68.6 && y<=27.6)
				area_num = 8;
		}
    return area_num;
}


//Using vector instead of array, cause we don't know size of the data.
vector<People> user;
vector<csv> dataF;
vector<int> delOld[10];

int main(int argc, char** argv){
    ios_base::sync_with_stdio(0);
    string dLine, lid, zid, x, y, dt;
	// if(argc < 3){
	// 	cout << "Usage : " << argv[0] << " [file for analyze] [file for standards]\n";
	// 	exit(-1);
	// }
	
    bool fnd = false;
    int placeNum, Timetmp;
	char buf[20], namebuf[20], stnamebuf[20], outname[20] = "out_";
	string strBuf, toktmp;
	int i = 0, th = 0, tm = 0, ts, w, m, dold = 0;

	cout << "Choose file to analyze\n> ";
	cin >> namebuf;
	cout << "Choose file to be standard\n> ";
	cin >> stnamebuf;

    ifstream fData(namebuf);
	ifstream stData(stnamebuf);
	stData >> buf;
	m = atoi(buf);
	stData >> buf;
	w = atoi(buf);

	cout << "reading " << stnamebuf << "...\n";
	while(!stData.eof()){
		stData >> strBuf;
		while((th = strBuf.find(",")) != string::npos){
			toktmp = strBuf.substr(0, th);
			delOld[dold].push_back(atoi(toktmp.c_str()));
//			cout << toktmp << " " << dold << endl;
			strBuf.erase(0, th + 1);
		}
		delOld[dold++].push_back(atoi(strBuf.substr(tm, strBuf.length()).c_str()));
	}

	
	//for print data to a file. Unused.
	
	strcat(outname, namebuf);
	strtok(outname, ".");
	strcat(outname, ".txt");
	fout.open(outname);
	ofstream fout(outname);
	

	cout << "reading " << namebuf << "...\n";
	i = 0;
	//Reading data until end of file
    while(!fData.eof()){
		i++;
        getline(fData, dLine, ',');
        lid = dLine;
        getline(fData, dLine, ',');
        zid = dLine;
        getline(fData, dLine, ',');
        x = dLine;
        getline(fData, dLine, ',');
        y = dLine;
        getline(fData, dLine, '\n');
        dt = dLine;
		if (lid.length() >= 2 && lid != "LOCKER_ID" && dt.length() > 12) //Filtering abnormal data
			dataF.push_back(csv(lid, zid, x, y, dt));
    }
    
	
	cout << "Now working...\n";
    for(auto v : dataF){
		fnd = false;
		strcpy(buf, v.LOC_DT.c_str());

		//Filtering abnormal data
		if (!(placeNum = seperate(v.ZONE_ID, atoi(v.LOC_X.c_str()), atoi(v.LOC_Y.c_str())))) continue;

		//Find people with data's LOCKER_ID. If fails, makes new data field with the LOCKER_ID
        for(auto& p : user){
           if(p.pNum == v.LOCKER_ID){
                fnd = true;
                ts = atoi(buf + 12); buf[12] = 0; buf[13] = 0;
                tm = atoi(buf + 10); buf[10] = 0; buf[11] = 0;
                th = atoi(buf + 8); 
				
                p.inputST(th, tm, ts, placeNum);
                break;
           }
        }
        if(!fnd){
            user.push_back(People());
            auto *p = &user[user.size() - 1];
            p->pNum = v.LOCKER_ID;
            ts = atoi(buf + 12); buf[12] = 0; buf[13] = 0;
            tm = atoi(buf + 10); buf[10] = 0; buf[11] = 0;
            th = atoi(buf + 8); 
				
            p->inputST(th, tm, ts, placeNum);
        }
       
    }
	
	//Print all
    for(auto p : user){
		th = -1; tm = -1; 
		for(i = 0; i < dold; i++){
			ts = 0;
			for(int v : delOld[i]){
				ts += (p.rTime[v].first * 10000 + p.rTime[v].second * 100 + p.plsec[v]);
			}

			if(th < ts){
				tm = i;
				th = ts;
			}
		}
		th = p.rTime[22].first * 10000 + p.rTime[23].second * 100 + p.plsec[23] + p.rTime[23].first * 10000 + p.rTime[23].second * 100 + p.plsec[23];
		ts = p.rTime[24].first * 10000 + p.rTime[24].second * 100 + p.plsec[24] + p.rTime[25].first * 10000 + p.rTime[25].second * 100 + p.plsec[25];
		if(th > ts) p.WoM = w;
		else if(th < ts) p.WoM = m;
		else p.WoM = -1;

		p.old = tm;
        p.printAll();
    }

	cout << "Job finished\n";
}  
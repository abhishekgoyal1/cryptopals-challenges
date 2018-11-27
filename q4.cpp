#include <iostream>
#include <fstream>
#include <bits/stdc++.h>

using namespace std;


int hextoint(char hexnum){
	if (hexnum>='a' && hexnum<='f'){
		return hexnum-'a'+10;
	}
	else{
		return hexnum-'0';
	}
}

char inttohex(int num){
	if (num>=0 && num<=9){
		return '0'+num;
	}
	else{
		return num-10+'a';
	}
}


string decode(string s1, int key){
	int x1,x2,x3,y;
	char c;
	string output="";
	for (int i=0;i<s1.length();i=i+2){
		x1= hextoint(s1[i]);
		x2= hextoint(s1[i+1]);
		x3=(x1<<4)+x2;
		y= x3^key;
		char c=  (char)y;
		output=output+c;

	}
	return output;
}

int main(){
	ifstream infile("4.txt");
	string s1;
	int linecount=0;
	while (infile >> s1){
		cout << "s1 is " << s1 << " " << linecount << endl << endl;
		linecount++;
		for (int i=0;i<256;i++){
			string output= decode(s1,i);
			int check=0;
			for (int j=0;j<output.length();j++){
				if (!((output[j]>=0 && output[j]<=14)||(output[j]>=32 && output[j]<=40)||(output[j]>=65 && output[j]<=172))){
					check=1;
					break;	
				}
			}
			if (check!=1)
				cout << output << " " << i << endl;
		}
	}
	cout << linecount << endl;
	//cout << endl << endl << "KEY IS " << 88 << endl;
	cout << "Line: 207, KEY: 88" << endl;
}
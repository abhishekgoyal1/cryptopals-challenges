#include <iostream>
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


string encode(string s1, string key){
	char c;
	int x1,y;
	string output="";
	int j=0;
	int curkey;
	for (int i=0;i<s1.length();i++){
		x1= s1[i];
		curkey=key[j];
		j++;
		if (j==key.length())
			j=0;
		y= x1^curkey;
		char c=  (char)y;
		output=output+c;
	}
	return output;
}



string stringtohex(string s1){
	string output="";
	for (int i=0;i<s1.length();i++){
		int cur= s1[i];
		int first= cur & 15;
		int second= cur & 255;
		second= second >> 4;
		char a= inttohex(first);
		char b=inttohex(second);
		output=output+b;
		output=output+a;
	}
	return output;
}

string hextostring(string s1){
	int x1, x2, x3, y;
	string output="";
	for (int i=0;i<s1.length();i=i+2){
		x1= hextoint(s1[i]);
		x2= hextoint(s1[i+1]);
		x3=(x1<<4)+x2;
		y= x3;
		char c=  (char)y;
		output=output+c;

	}
	return output;
}



int main(){
	string s1="Burning 'em, if you ain't quick and nimble I go crazy when I hear a cymbal";
	string key="ICE";
	string output= encode(s1, key);
	cout << output << endl;
	string hexout= stringtohex(output);
	cout << hexout << endl;
	cout << encode(hextostring(hexout),key) << endl;
}
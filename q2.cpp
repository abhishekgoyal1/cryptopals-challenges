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

string hex_xor(string s1, string s2){
	int x1,x2,x3;
	string output="";
	for (int i=0;i<s1.length();i++){
		x1= hextoint(s1[i]);
		x2= hextoint(s2[i]);
		x3= x1^x2;
		output= output+ inttohex(x3);
	}
	return output;
}

int main(){
	string s1="1c0111001f010100061a024b53535009181c";
	string s2="686974207468652062756c6c277320657965";
	string output= hex_xor(s1,s2);
	cout << output << endl;
}
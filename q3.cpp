// char ascii= 53
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
	//string s1="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736";
	string s1="7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f";
	//int keyval= xor_key(s1);
	for (int i=0;i<256;i++){
		string output= decode(s1,i);
		cout << "STRING IS "<< output << " " << i << endl;
	}
	cout << endl << endl << "KEY IS " << 88 << endl;

}
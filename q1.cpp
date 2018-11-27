#include <iostream>
#include <bits/stdc++.h>

using namespace std;
char base64(int x){
	char output;
	if (x>=0 && x<=25){
		output= 'A' + x;
	}
	else if (x>=26 && x<=51){
		output='a'+x-26;
	}
	else if (x>=52 && x<=61){
		output= '0'+x-52;
	}
	else{
		if (x==62)
			output='+';
		else
			output='/';
	}
	return output;
}

int hextoint(char hexnum){
	if (hexnum>='a' && hexnum<='f'){
		return hexnum-'a'+10;
	}
	else{
		return hexnum-'0';
	}
}

string hexto64(string s){
	int x,y,z;
	int bit1, bit2;
	string output="";
	for (int i=0;i<s.length();i=i+3){
		if (i+1==s.length()){
			y=0;
			z=0;
			x=hextoint(s[i]);
		}
		else if (i+2==s.length()){
			z=0;
			x=hextoint(s[i]);
			y=hextoint(s[i+1]);
		}
		else{
			x=hextoint(s[i]);
			y=hextoint(s[i+1]);
			z=hextoint(s[i+2]);
		}
		bit1= (x<<2) + (y>>2);
		bit2= ((y&3)<<4)+z;
		output= output+ base64(bit1)+ base64(bit2);
	}
	return output;
}

int main(){
	string input="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
	string output= hexto64(input);
	cout << output << endl;
}
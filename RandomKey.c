#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>


void SecretKey(char * key);
void charSecretKey();
void intSecretKey(int * key);
int checkDoubleKey(int * key, int val);

int main(){
	
	//generating a secret key.. ..
	charSecretKey();

	return 0;
}



/*************> Funtion definition  <********************************/

void SecretKey(char * key){
	FILE * opfile;
	opfile = fopen("secretKey.txt","w");

	if(opfile==NULL)
		printf("File not Open..\n");
	else{
		for(int i=0;i<26;i++)
			fputc(key[i], opfile);
		fputs("\n", opfile);
	}
	fclose(opfile);
}

//generating Final secret Key for
//the substitution cipher... ...
void charSecretKey(){

	int key[26];
	char charKey[26];
	for(int i=0;i<26;i++)
		key[i] = -1;


	intSecretKey(key);
	for(int i=0;i<26;i++)
		charKey[i] = (char)key[i];

	SecretKey(charKey);
}

//Generating Secret key...
//return an intger in range 65-90..
void intSecretKey(int * key){
	/*
	 * Finding the key for substitution cipher..
	 * alpha[26] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	 * key[26]   = "DSQR .. .. .. .. .. .. ZKI"
	 */

	srand(time(0));
	for(int i=0;i<26;i++){
		int keyPoint = rand()%26;
		keyPoint += 65;
		
		while(checkDoubleKey(key, keyPoint)==1){
			keyPoint = rand()%26;
			keyPoint += 65;
		}
		key[i] = keyPoint;
	}
}

//Utility function used by
//intSecretKey() function.. ...
int checkDoubleKey(int * key, int val){
	int i = 0;
	while(key[i]!=-1){
		if(key[i]==val)
			return 1;
		i++;
	}
	return 0;
}
/*****************>  END    <***************************************/

#import <stdio.h>
#import <strings.h>
#import <stdlib.h>

int most_likely_to_bind( char* s1, char* s2 );
int comp(char a, char b);

int comp(char a, char b) {
  return (a == "T" && b == "A" || a == "A" && b == "T" || a == "C" && b == "G" || a == "G" && b == "C");
}

int most_likely_to_bind( char* s1, char* s2 ){
  int c1 = 0;
  int temp = 0;
  int most = 0;
  while(s1[c1] && s2[c1]) {
    if ( comp(s1[c1], s2[c1]) ) {
      temp++;
    }
    c1++;
  }
  most = temp; //first run comps all strands as if the thing were entirely complementary
  //  Currently does not take into account if the complementary nucleotides are close together or far apart
  //  E.g a return value of five may be 0000000001100000100010000001, and not 11111000000000000000000000
  int c2 = 0;
  int temp = 0;
  c1 = 0;
  //This loop should run on string of size max - n on the nth loop and compare that substring to each possible 
  //substring in the second loop
  while (s1[c1]) {
    c2 = 0;
    while(s2[c2]) {
      
      c2++;
    }
    c1++;
  }
}

int main() {
  
}

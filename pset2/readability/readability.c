#include <cs50.h> 
#include <stdio.h>
#include<string.h>
#include<ctype.h>
#include<math.h>

int main(void)
{ 
    float letters = 0;
    float words = 0;
    float sentences = 0;
    // Get an input from the user 
    string s = get_string("Text: ");
    
    // Find number of sentences, words and letters
    for(int i = 0,n = strlen(s); i<n; i++)
    {
        char ch = s[i];
        if(isalpha(ch))
        {
            letters++;
        }
       else if(isspace(ch))
        {
            words++;
        }
    
        if(ch == '.'|| ch == '!'|| ch =='?')
          {
            sentences++;
          }
    }
         
    words++;
// formula
int index = 0;
float X = (letters * 100.00/words);

float Y = (sentences * 100.00/words);

index = round(0.0588 * X - 0.296 * Y - 15.8);

// Result
    if(index > 16)
     {
      printf("Grade 16+\n");  
      }
  
  
     else if (index < 1)
      {
       printf("Before Grade 1\n");
      }
     else
      {
    printf("Grade %i\n", index);
       }
}

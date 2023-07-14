#include<stdio.h>
#include<string.h>
#include<cs50.h>
#include<stdlib.h>
#include<ctype.h>

int main(int argc, string argv[])
{
    // check for arguments equal to 2 
    if(argc != 2) 
    {
        printf("Usage: ./caesar key\n");
        
    }
    // conversion of string to int 
    int k = atoi(argv[1]);
    
    if (k <0)
    {
        printf("Usage: ./caesar key\n");
    }
    // get text from user 
    string s = get_string("plaintext: ");
    printf("ciphertext: "); 
    
    for(int i=0, n=strlen(s); i<n; i++)
    { 
        if(isalpha(s[i]))
        {
            // print uppercase as it is
            if(isupper(s[i])) 
            {
                char ch_up = ((s[i] - 65 + k) % 26) + 65; // reposition the pointer to starting letter of the alphabet if the key count crosses 'Z' or 'z' 
                printf("%c", ch_up);
            }
            
            //print lowercase as it is 
                if(islower(s[i]))
                {
                    char ch_low = ((s[i] - 97 + k) % 26) + 97;
                    printf("%c",ch_low);
                }
        }

                     else
                    {
                       printf("%c",s[i]);
                    }
    }
    
    printf("\n");
}

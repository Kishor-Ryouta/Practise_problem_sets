#include <stdio.h>
#include <stdlib.h>
#include<stdint.h>
#include <stdbool.h>
#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
      // Check usage
    if (argc != 2)
    {
        printf("usage: ./recover image");
        return 1;
    }

    // Open file
    FILE *file = fopen(argv[1], "r");
    // check if file is empty
    if (!file)
    {
        return 1;
    }

    typedef uint8_t BYTE;
    BYTE buffer[BLOCK_SIZE];
    size_t bytes_read;
    bool first_jpeg;
    FILE *current_file;
    int file_number = 0;
    char file_name[100];
    bool found_jpeg = false;

    while (true)
    {
        // read until end of card
        // read 512 bytes
        bytes_read = fread(buffer, sizeof(BYTE), BLOCK_SIZE, file);
        if (bytes_read == 0)
        {
            break;
        }
        // start of first jpeg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            found_jpeg = true;

            // if first jpeg
            // mark as first jpeg
            if (!first_jpeg)
            {
                first_jpeg = true;
            }

            // close the current file being written to
            else
            {
                fclose(current_file);

            }
            sprintf(file_name, "%03i.jpeg", file_number);
            current_file = fopen(file_name, "w");
            fwrite(buffer, sizeof(BYTE), bytes_read, current_file);
            file_number++;
        }
        else
        {
            // if already found a new jpeg
            // keep writing to it
            if (found_jpeg)
            {
                fwrite(buffer, sizeof(BYTE), bytes_read, current_file);
            }
        }
    }
    fclose(current_file);
}
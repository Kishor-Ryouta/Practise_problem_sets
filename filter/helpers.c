#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
              int new_pixel_value = round((float)(image[i][j].rgbtRed + image[i][j].rgbtBlue  + image[i][j].rgbtGreen ) / 3);

              // max value is 255
            if (new_pixel_value > 255)
            {
                new_pixel_value = 255;
            }

            image[i][j].rgbtRed = new_pixel_value;
            image[i][j].rgbtBlue = new_pixel_value;
            image[i][j].rgbtGreen = new_pixel_value;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int temp[3];

     for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {

            // swap pixels from right to left
            temp[0] = image[i][j].rgbtBlue;
            temp[1] = image[i][j].rgbtGreen;
            temp[2] = image[i][j].rgbtRed;

            image[i][j].rgbtBlue = image[i][width - j - 1].rgbtBlue;
            image[i][j].rgbtGreen = image[i][width - j - 1].rgbtGreen;      
            image[i][j].rgbtRed = image[i][width - j - 1].rgbtRed;

            image[i][width - j - 1].rgbtBlue = temp[0];
            image[i][width - j - 1].rgbtGreen = temp[1];
            image[i][width - j - 1].rgbtRed = temp[2];

        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

   RGBTRIPLE temp[height][width];

    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            // boundary values of an element in a matrix
            int count  = 0;
            int rowc[] = { row-1, row, row+1};
            int colc[] = { col-1, col, col+1};
            float totalR = 0, totalG = 0, totalB = 0;

            for (int r = 0; r < 3; r++)
            {
                for (int c = 0; c < 3; c++)
                {
                    int currow = rowc[r];
                    int curcol = colc[c];

                    if (currow >=0 && currow < height && curcol >=0 && curcol < width)
                    {
                        RGBTRIPLE pixel = image[currow][curcol];

                // sum of all the boundary values for an element
                        totalR += pixel.rgbtRed;
                        totalG += pixel.rgbtGreen;
                        totalB += pixel.rgbtBlue;
                        count++;
                    }
                }
            }
               // average of all boundary values
            temp[row][col].rgbtRed = round(totalR / count);
            temp[row][col].rgbtGreen = round(totalG / count);
            temp[row][col].rgbtBlue = round(totalB / count);
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    }
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp[height][width];

    int Gx[3][3] = {
        {-1, 0, 1},
        {-2, 0, 2},
        {-1, 0, 1}
    };
    int Gy[3][3] = {
        {-1, -2, -1},
        { 0, 0, 0},
        {1, 2, 1}
    };

   for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            float Gx_red = 0, Gx_green = 0, Gx_blue = 0;
            float Gy_red = 0, Gy_green = 0, Gy_blue = 0;

            int count  = 0;
            int rowc[] = { row-1, row, row+1};
            int colc[] = { col-1, col, col+1};

            for (int r = 0; r < 3; r++)
            {
                for (int c = 0; c < 3; c++)
                {
                    int currow = rowc[r];
                    int curcol = colc[c];

                    if (currow >=0 && currow < height && curcol >=0 && curcol < width)
                    {
                        RGBTRIPLE pixel = image[currow][curcol];
                        
                         // sobel operation
                        Gx_red += Gx[r][c] * pixel.rgbtRed;
                        Gx_green += Gx[r][c] * pixel.rgbtGreen;
                        Gx_blue += Gx[r][c] * pixel.rgbtBlue;

                        Gy_red += Gy[r][c] * pixel.rgbtRed;
                        Gy_green += Gy[r][c] * pixel.rgbtGreen;
                        Gy_blue += Gy[r][c] * pixel.rgbtBlue;
                    }
                }
            }
                  
                  int new_red = round(sqrt(Gx_red * Gx_red + Gy_red * Gy_red));
                  int new_green = round(sqrt(Gx_green * Gx_green + Gy_green * Gy_green));
                  int new_blue = round(sqrt(Gx_blue * Gx_blue + Gy_blue * Gy_blue));

                  temp[row][col].rgbtRed = new_red > 255 ? 255 : new_red;
                  temp[row][col].rgbtGreen = new_green > 255 ? 255 : new_green;
                  temp[row][col].rgbtBlue = new_blue > 255 ? 255 : new_blue;
        }
    }
    
// copy to final image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = temp[i][j];
        }
    } return;
}


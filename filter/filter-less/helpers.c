#include "helpers.h"

    // Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop through every row
    for (int i = 0; i < height; i++)
    {
        // Loop through every pixel in the row
        for (int j = 0; j < width; j++)
        {
            // Calculate the average of Red, Green, and Blue
            // Add 0.5 before casting to int to properly round the result
            int rgbtAverage = (int) ((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0 + 0.5);

            // Set all color channels to the average value
            image[i][j].rgbtRed = rgbtAverage;
            image[i][j].rgbtGreen = rgbtAverage;
            image[i][j].rgbtBlue = rgbtAverage;
        }
    }
    return;
}


    // Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Store original values
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue = image[i][j].rgbtBlue;

            // Compute sepia values using the formula
            int sepiaRed = (int) (.393 * originalRed + .769 * originalGreen + .189 * originalBlue + 0.5);
            int sepiaGreen = (int) (.349 * originalRed + .686 * originalGreen + .168 * originalBlue + 0.5);
            int sepiaBlue = (int) (.272 * originalRed + .534 * originalGreen + .131 * originalBlue + 0.5);

            // Cap the values at 255 if they overflow
            image[i][j].rgbtRed = (sepiaRed > 255) ? 255 : sepiaRed;
            image[i][j].rgbtGreen = (sepiaGreen > 255) ? 255 : sepiaGreen;
            image[i][j].rgbtBlue = (sepiaBlue > 255) ? 255 : sepiaBlue;
        }
    }
    return;
}

    // Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        // Loop only up to the middle of the row
        for (int j = 0; j < width / 2; j++)
        {
            // Swap the pixels
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - 1 - j];
            image[i][width - 1 - j] = temp;
        }
    }
    return;
}


// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{

    // Create a temporary copy of the image to read from
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    // Loop through each pixel to calculate the blur
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int totalRed = 0, totalGreen = 0, totalBlue = 0;
            float counter = 0.00;

            // Loop through the 3x3 neighborhood box
            for (int r = -1; r < 2; r++)
            {
                for (int c = -1; c < 2; c++)
                {
                    int neighborRow = i + r;
                    int neighborCol = j + c;

                    // Make sure the neighboring pixel is within bounds
                    if (neighborRow >= 0 && neighborRow < height && neighborCol >= 0 && neighborCol < width)
                    {
                        totalRed += copy[neighborRow][neighborCol].rgbtRed;
                        totalGreen += copy[neighborRow][neighborCol].rgbtGreen;
                        totalBlue += copy[neighborRow][neighborCol].rgbtBlue;
                        counter++;
                    }
                }
            }

            // Assign the rounded average colors to the original image
            image[i][j].rgbtRed = (int) (totalRed / counter + 0.5);
            image[i][j].rgbtGreen = (int) (totalGreen / counter + 0.5);
            image[i][j].rgbtBlue = (int) (totalBlue / counter + 0.5);
        }
    }
    return;
}


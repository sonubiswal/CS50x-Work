#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Define block size for memory card reading
#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{
    // Ensure correct usage
    if (argc != 2)
    {
        printf("Usage: ./recover card.raw\n");
        return 1;
    }

    // Open the forensic card image
    FILE *raw_file = fopen(argv[1], "r");
    if (raw_file == NULL)
    {
        printf("Could not open file %s.\n", argv[1]);
        return 1;
    }

    // Create a buffer array to store 512-byte blocks
    uint8_t buffer[BLOCK_SIZE];

    // Trackers for open files and image counts
    FILE *img_file = NULL;
    int image_count = 0;
    char filename[8];

    // Read 512-byte blocks continuously until the end of the file
    while (fread(buffer, 1, BLOCK_SIZE, raw_file) == BLOCK_SIZE)
    {
        // Check if the block indicates the start of a new JPEG file
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If a JPEG file is already open, close it first
            if (img_file != NULL)
            {
                fclose(img_file);
            }

            // Generate the new filename (e.g., 000.jpg, 001.jpg)
            sprintf(filename, "%03i.jpg", image_count);
            image_count++;

            // Open the new image file for writing
            img_file = fopen(filename, "w");
            if (img_file == NULL)
            {
                fclose(raw_file);
                printf("Could not create output file %s.\n", filename);
                return 1;
            }
        }

        // If an output JPEG file is currently open, write the block to it
        if (img_file != NULL)
        {
            fwrite(buffer, 1, BLOCK_SIZE, img_file);
        }
    }

    // Clean up open file pointers
    if (img_file != NULL)
    {
        fclose(img_file);
    }
    fclose(raw_file);

    return 0;
}

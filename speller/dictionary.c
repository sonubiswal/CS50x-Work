// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// Number of buckets in hash table
const unsigned int N = 10007;

// Hash table
node *table[N];

// Number of words loaded into the dictionary
unsigned int word_count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Hash the word to find its bucket
    unsigned int index = hash(word);

    // Traverse the linked list at that bucket
    node *cursor = table[index];
    while (cursor != NULL)
    {
        // Compare case-insensitively
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // djb2 hash — starts at 5381, multiplies by 33, adds each char
    unsigned long hash_value = 5381;
    int c;
    while ((c = tolower(*word++)))
    {
        hash_value = ((hash_value << 5) + hash_value) + c;
    }
    return hash_value % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open the dictionary file
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        return false;
    }

    // Buffer to hold each word
    char word[LENGTH + 1];

    // Read each word from the file
    while (fscanf(dict, "%s", word) != EOF)
    {
        // Allocate a new node
        node *new_node = malloc(sizeof(node));
        if (new_node == NULL)
        {
            fclose(dict);
            return false;
        }

        // Copy the word into the node
        strcpy(new_node->word, word);

        // Hash the word to get an index
        unsigned int index = hash(word);

        // Insert at the front of the bucket's linked list
        new_node->next = table[index];
        table[index] = new_node;

        // Keep count for size()
        word_count++;
    }

    // Close the file
    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Iterate over every bucket
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *tmp = cursor;
            cursor = cursor->next;
            free(tmp);
        }
    }
    return true;
}

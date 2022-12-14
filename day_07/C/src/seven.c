#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LINE_SIZE      50
#define DIR_NUMBER     512
#define SIZE_THRESHOLD 100000

typedef struct directory
{
    int size;
    int n_children;
    struct directory** children;
} directory;

int readDirectory(FILE* p_file, directory* p_dir, directory** dirList, int* p_dirCount) {
    char line[LINE_SIZE], dirname[LINE_SIZE];
    int childrenExplored = 0, filesize;; // Number of children explore with cd
    // Loop reading lines
    while(fgets(line, LINE_SIZE, p_file)) {
        // File case
        if (sscanf(line, "%d %*s",&filesize))
            p_dir->size += filesize;
        // Subdirectory case
        if (sscanf(line, "dir %s\n",dirname)) {
            // Init new dir
            directory* dir = malloc(sizeof(directory));
            dirList[(*p_dirCount)++] = dir;
            dir->size = 0;
            dir->n_children = 0;
            // Makes a larger list
            p_dir->children = realloc(p_dir->children, (p_dir->n_children + 1)*sizeof(directory*));
            (p_dir->children)[p_dir->n_children++] = dir;
        }
        if (sscanf(line,"$ cd %s",dirname)) {
            if (strcmp(dirname,"..") == 0) {
                return p_dir->size; 
            } else {
                p_dir->size += readDirectory(p_file,p_dir->children[childrenExplored++], dirList, p_dirCount);
            }
        }
    }
    return p_dir->size;
}

int main(int argc, char const *argv[])
{
    // Input file
    FILE* p_file = fopen("../data/input", "r");
    if (p_file == NULL) {
        printf("File not found, please be sure to be in bin directory\n");
        exit(1);
    }
    // Line buffer
    char line[LINE_SIZE];
    directory** dirList = malloc(DIR_NUMBER*sizeof(directory*));
    int dirCount = 0;

    fgets(line, LINE_SIZE, p_file); // Eliminates first line
    directory* root = malloc(sizeof(directory));
    dirList[dirCount++] = root;
    root->size = 0;
    root->n_children = 0;
    readDirectory(p_file,root, dirList, &dirCount); // Big recursive call
    fclose(p_file); // File closing
  
    int tot_size = 0, this_size;
    int extra = root->size - 40000000; // How much space to clean
    int minSize = __INT32_MAX__;

    for (int i = 0; i < dirCount; i++) {
        tot_size += (this_size = dirList[i]->size) <= SIZE_THRESHOLD ? this_size : 0;
        minSize = (this_size >= extra && this_size < minSize) ? this_size : minSize;
    }
    printf("Total size : %d\nMin Size : %d\n",tot_size, minSize);
    return 0;
}
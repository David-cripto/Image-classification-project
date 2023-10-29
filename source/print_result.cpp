#include <fcntl.h>
#include <iostream>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <unistd.h>

int main() {
    char* transferFifo = "/tmp/trans";
    int fdData;
    char data[100];

    fdData = open(transferFifo, O_RDONLY);
    int res = read(fdData, &data, sizeof(data));
    std::cout << res << std::endl;
    std::cout << data << std::endl;
    close(fdData);
    unlink(transferFifo);
    return 0;
}

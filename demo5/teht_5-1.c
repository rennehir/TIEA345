/*
    pulse.c

    gcc -o teht1 teht_5-1.c -lpigpio -lrt -lpthread

    sudo ./teht1
*/

#include <stdio.h>
#include <pigpio.h>

int main(int argc, char *argv[])
{
    if (gpioInitialise() < 0)
    {
        fprintf(stderr, "pigpio initialisation failed\n");
        return 1;
    }

    int led = 18;
    int pir = 4;

    /* Set GPIO modes */
    gpioSetMode(led, PI_OUTPUT); // LED
    gpioSetMode(pir, PI_INPUT); // PIR sensor

    double start = time_time();

    while((time_time() - start) < 60.0)
    {
        gpioWrite(led, gpioRead(pir));
        time_sleep(2);
    }

    gpioTerminate();

    return 0;
}

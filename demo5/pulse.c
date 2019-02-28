/*
    pulse.c

    gcc -o pulse pulse.c -lpigpio -lrt -lpthread

    sudo ./pulse
*/

#include <stdio.h>
#include <pigpio.h>

int main(int argc, char *argv[])
{
    double start;

    if (gpioInitialise() < 0)
    {
        fprintf(stderr, "pigpio initialisation failed\n");
        return 1;
    }

    /* Set GPIO modes */
    gpioSetMode(18, PI_OUTPUT); // LED red
    gpioSetMode(23, PI_OUTPUT); // LED green
    gpioSetMode(21, PI_INPUT); // Button

    start = time_time();

    while((time_time() - start) < 60.0)
    {
        gpioWrite(18, 1); // LED red on
        time_sleep(0.5);
        gpioWrite(18, 0); // LED red off
        time_sleep(0.5);

        gpioWrite(23, gpioRead(21));
    }

    gpioTerminate();

    return 0;
}

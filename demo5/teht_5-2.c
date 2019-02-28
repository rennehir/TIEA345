/*
    teht_5-2.c

    gcc -o teht2 teht_5-2.c -lpigpio -lrt -lpthread

    sudo ./teht2
*/

#include <stdio.h>
#include <pigpio.h>

int carRed = 17;
int carYellow = 27;
int carGreen = 22;
int pedestrianSignal = 13;
int pedestrianRed = 19;
int pedestrianGreen = 26;

int pedestrianButton = 6;
int motionSensor = 18;

void setPedestrianSignal(void)
{
    gpioWrite(pedestrianSignal, 1);
    return;
}

void blinkPedestrianGreen(void)
{
    gpioWrite(pedestrianGreen, 0);
    time_sleep(0.2);
    gpioWrite(pedestrianGreen, 1);
    time_sleep(0.2);
    gpioWrite(pedestrianGreen, 0);
    time_sleep(0.2);
    gpioWrite(pedestrianGreen, 1);
    time_sleep(0.2);
    gpioWrite(pedestrianGreen, 0);
    return;
}

void allowPedestriansCrossing(void)
{
    gpioWrite(pedestrianSignal, 0);
    gpioWrite(carGreen, 0);
    gpioWrite(carYellow, 1);
    time_sleep(1.5);
    gpioWrite(carYellow, 0);
    gpioWrite(carRed, 1);
    time_sleep(1.5);
    gpioWrite(pedestrianRed, 0);
    gpioWrite(pedestrianGreen, 1);
    return;
}

void denyPedestriansCrossing(void)
{
    blinkPedestrianGreen();
    gpioWrite(pedestrianGreen, 0);
    gpioWrite(pedestrianRed, 1);
    time_sleep(1.5);
    gpioWrite(carYellow, 1);
    time_sleep(1);
    gpioWrite(carRed, 0);
    gpioWrite(carYellow, 0);
    gpioWrite(carGreen, 0);
    return;
}

void runTrafficLights(void)
{
    allowPedestriansCrossing();
    time_sleep(5);
    denyPedestriansCrossing();
}

int main(int argc, char *argv[])
{
    if (gpioInitialise() < 0)
    {
        fprintf(stderr, "pigpio initialisation failed\n");
        return 1;
    }

    /* Set GPIO modes */
    /* Outputs */
    gpioSetMode(carRed, PI_OUTPUT);
    gpioSetMode(carYellow, PI_OUTPUT);
    gpioSetMode(carGreen, PI_OUTPUT);
    gpioSetMode(pedestrianSignal, PI_OUTPUT);
    gpioSetMode(pedestrianRed, PI_OUTPUT);
    gpioSetMode(pedestrianGreen, PI_OUTPUT);
    /* Inputs */
    gpioSetMode(pedestrianButton, PI_INPUT);
    gpioSetMode(motionSensor, PI_INPUT);

    /* Initial light setup */
    gpioWrite(carRed, 0);
    gpioWrite(carYellow, 0);
    gpioWrite(carGreen, 1);
    gpioWrite(pedestrianSignal, 0);
    gpioWrite(pedestrianRed, 1);
    gpioWrite(pedestrianGreen, 0);

    double start = time_time();

    while((time_time() - start) < 120.0)
    {
        int buttonState = gpioRead(pedestrianButton);

        if (buttonState)
        {
            setPedestrianSignal();
            time_sleep(1);

            int motionState = gpioRead(motionSensor);

            if (!motionSensor)
            {
                runTrafficLights();
            }
            else
            {
                time_sleep(4);
                runTrafficLights();
            }
        }
    }

    gpioTerminate();

    return 0;
}

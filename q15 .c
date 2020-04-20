#include<stdio.h>
#include <stdlib.h>
#include <math.h>

float F(float x,float y)
{
    float F;
    F = y - x*x + 1;
    return(F);
}

void Eular(float *y , float xi ,float xf, float h)
{
    int n,i;
    n = ((xf-xi)/h);
    float x=xi;
    float yext[n],err[n],bound[n];
    bound[0]=0;

    for(i=0;i<=n;++i)
    {

        y[i+1] = y[i] + h*F(x,y[i]);
        x = x+h;
    }
    x=xi;
    for (int i = 0; i <= n+1; ++i)
    {
        yext[i]=pow(x+1,2)-0.5*exp(x);
        x = x+h;
    }

    x=xi;
    for (int i = 0; i < n+1; ++i)
    {
        y[i+1]=y[i]+h*(y[i]-pow(x,2)+1);
        err[i+1]=fabs(y[i+1]-yext[i+1]);
        bound[i+1]=.1*(.5*exp(2)-2)*(exp(x+h)-1);
        x=x+h;
    }
    printf("t\tApp. Solution\texact soln:\n");
    x=xi;
    for (int i = 0; i < n+2; ++i)
    {
        printf("%f %f %f\n", x,y[i],yext[i]);
        x=x+h;
    }
    printf("Error and Error bound:\n");

    for (int i = 0; i < n+2; ++i)
    {
        printf("%f  %f\n",err[i],fabs(bound[i]));
    }


}

void main()
{
    float y[10];
    y[0]=0.5;
    float xi = 0;
    float xf = 2;
    float h = 0.2;
    Eular(y,xi,xf,h);

}

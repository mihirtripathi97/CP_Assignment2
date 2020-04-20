#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main(){
int n=11;
double t[n],y[n],yext[n],err[n],bound[n],h=0.2,a=0;
bound[0]=0;
y[0]=0.5;

for (int i = 0; i < n; ++i)
{
	t[i]=a+i*h;
}

for (int i = 0; i < n; ++i)
{
	yext[i]=pow(t[i]+1,2)-0.5*exp(t[i]);
}

for (int i = 0; i < n-1; ++i)
{
	y[i+1]=y[i]+h*(y[i]-pow(t[i],2)+1);
	err[i+1]=fabs(y[i+1]-yext[i+1]);
	bound[i+1]=.1*(.5*exp(2)-2)*(exp(t[i+1])-1);
}

printf("t\tApp. Solution\texact soln:\n");
for (int i = 0; i < n; ++i)
{
	printf("%f %f %f\n", t[i],y[i],yext[i]);
}
printf("Error and Error bound:\n");
for (int i = 0; i < n; ++i)
{
	printf("%f  %f\n",err[i],fabs(bound[i]));
}
return(0);
}

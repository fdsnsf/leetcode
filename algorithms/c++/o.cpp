/***

������������ ������n����Ϊһϵ�в��ظ�������֮��,���ж�������ϡ�

������NUM   ����N
      M     MΪNUM�ɻ��ֵ��������(֮��)�ĸ��� 
      S     SΪM����������ϵĵ�һλ�������ֵ
�㷨����̬�滮
      �ȼ�������3���������1��3=1+2����������3����������������4���������
	  �Դ�����ֱ�����������N���������
***/

#include <stdio.h>

#define NUM  506
#define M    31
#define S    252

double count[NUM+1][M+1][S+1] = {0}; 
                              
int count_s(int n, int m)  //����S 
{
    int s = 0;
    if (m % 2)
    {
      s = n/m - m/2;
    }
    else
    {
      s = (n-m/2)/m - (m/2-1);
    }
    return s;
}  

void count_n() 
{
    int N = 3;     //N��СΪ3�������Ϊ1
    int m = 0;
    for (; N<=NUM; N++)  
    {
      if (N % 2)   //��������N��3~NUM������Ϊ2��M=2��������֮�͵������ NΪż��
      {
         count[N][2][0] = N/2;
      }
      else         //NΪ����
      {
        count[N][2][0] = N / 2-1;
      }
      
      int i;
      for(i=1; i<=count[N][2][0]; i++)
      {
        count[N][2][i] = 1;    //2���������������һ�����Ѿ�ȷ�����������ֻ��Ϊ1
      }
	  
      int m;
      int s = 0;
      for(m=3; m<=M; m++) 
      { 
	    s = count_s(N, m);
        if (s<=0)   //С��NUM�����ɻ��ֵ���������С��M�����Ի���ΪM��������ϲ�����
        {
          break;
        }
              
		for (i=1; i<=s; i++)  //M�������������NUMǰ���ɸ�������Ϊs����M-1���������������
		{
          double temp = 0;
          for (int j=1; j<=i; j++)  
          {
             temp += count[N-i][m-1][j];
          }
          count[N][m][i] = count[N-i][m-1][0]-temp; 

          count[N][m][0] += count[N][m][i];  //M�����������
        }
      }
    }
}

void display()
{
    int N = NUM;
    int j;
    for (; N<=NUM; N++)
    {
      for (j=2; j<=M; j++)  //���M�����������
      {
         count[N][32][0] += count[N][j][0];
         printf ("%f\n", count[N][j][0]);
      }
   
      printf ("%f\n", count[N][32][0]);  //����ܵ������
    }
}           
int main()
{ 
    count_n();
    display();

    return 0;
}

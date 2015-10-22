/***

整数划分问题 将整数n划分为一系列不重复正整数之和,求共有多少种组合。

变量：NUM   整数N
      M     M为NUM可划分的最多整数(之和)的个数 
      S     S为M个整数的组合的第一位数的最大值
算法：动态规划
      先计算整数3的组合数（1；3=1+2），由整数3的组合数计算出整数4的组合数，
	  以此类推直至计算出整数N的组合数。
***/

#include <stdio.h>

#define NUM  506
#define M    31
#define S    252

double count[NUM+1][M+1][S+1] = {0}; 
                              
int count_s(int n, int m)  //计算S 
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
    int N = 3;     //N最小为3，组合数为1
    int m = 0;
    for (; N<=NUM; N++)  
    {
      if (N % 2)   //计算整数N（3~NUM）划分为2（M=2）个整数之和的组合数 N为偶数
      {
         count[N][2][0] = N/2;
      }
      else         //N为奇数
      {
        count[N][2][0] = N / 2-1;
      }
      
      int i;
      for(i=1; i<=count[N][2][0]; i++)
      {
        count[N][2][i] = 1;    //2个数的组合数，且一个数已经确定，则组合数只能为1
      }
	  
      int m;
      int s = 0;
      for(m=3; m<=M; m++) 
      { 
	    s = count_s(N, m);
        if (s<=0)   //小于NUM的数可划分的整数个数小于M，所以划分为M个数的组合不存在
        {
          break;
        }
              
		for (i=1; i<=s; i++)  //M个数的组合数由NUM前若干个数（即为s）的M-1个数的组合数决定
		{
          double temp = 0;
          for (int j=1; j<=i; j++)  
          {
             temp += count[N-i][m-1][j];
          }
          count[N][m][i] = count[N-i][m-1][0]-temp; 

          count[N][m][0] += count[N][m][i];  //M个数的组合数
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
      for (j=2; j<=M; j++)  //输出M个数的组合数
      {
         count[N][32][0] += count[N][j][0];
         printf ("%f\n", count[N][j][0]);
      }
   
      printf ("%f\n", count[N][32][0]);  //输出总的组合数
    }
}           
int main()
{ 
    count_n();
    display();

    return 0;
}

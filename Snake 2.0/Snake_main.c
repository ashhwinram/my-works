#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#include<time.h>
#define N 22
#define M 34
char arr[N][M],dir;
int size,score,end_flag,food_flag,speed;
struct pos
{
    int x;
    int y;
    struct pos *next;
};
struct pos *head=NULL;
void delay(int k)
{
    for(unsigned int i=0;i<=k;i++)
        for(unsigned int j=0;j<=64000;j++);
}
void setup()
{
    size=3;
    score=0;
    end_flag=1;
    food_flag=1;
    dir='n';
    speed=10000;
    for(int i=0;i<N;i++)
    {
        arr[i][0]='#';
        arr[i][M-1]='#';
    }
    for(int i=1;i<M-1;i++)
    {
        arr[0][i]='#';
        arr[N-1][i]='#';
    }
    srand(time(0));
    struct pos *one,*two,*three;
    one=malloc(sizeof(struct pos));
    two=malloc(sizeof(struct pos));
    three=malloc(sizeof(struct pos));
    one->x=(N/2);
    two->x=(N/2)+1;
    three->x=(N/2)+2;

    one->y=two->y=three->y=M/2;
    one->next=two;
    two->next=three;
    three->next=NULL;
    head=one;
}
void assign()
{
    struct pos *temp;
    temp=head;
    arr[temp->x][temp->y]='X';
    temp=temp->next;
    while(temp!=NULL)
    {
        arr[temp->x][temp->y]='O';
        temp=temp->next;
    }
}
void clear()
{
    struct pos *temp;
    temp=head;
    while(temp!=NULL)
    {
        arr[temp->x][temp->y]='\0';
        temp=temp->next;
    }
}
void foodclear()
{
    for(int i=1;i<N-1;i++)
    {
        for(int j=1;j<M-1;j++)
        {
            if(arr[i][j]=='$')
            {
                arr[i][j]='\0';
                return;
            }
        }
    }
}
void move(char input)
{
    int xtemp1,xtemp2,ytemp1,ytemp2,temp_flag=0;
    int cur_x,cur_y;
    struct pos *temp;
    temp=head;
    cur_x=temp->x;
    cur_y=temp->y;
    if(input=='q')
    {
        switch(dir)
        {
        case 'n':
            {
                cur_x--;
                break;
            }
        case 's':
            {
                cur_x++;
                break;
            }
        case 'e':
            {
                cur_y++;
                break;
            }
        case 'w':
            {
                cur_y--;
                break;
            }
        }
    }
    else if(input=='w')
    {
        if(dir=='e' || dir=='w')
        {
            cur_x--;
            dir='n';
        }
        else
        {
            switch(dir)
            {
                case 'n':
                {
                    cur_x--;
                    break;
                }
                case 's':
                {
                    cur_x++;
                    break;
                }
            }
        }
    }
    else if(input=='s')
    {
        if(dir=='e' || dir=='w')
        {
            cur_x++;
            dir='s';
        }
        else
        {
            switch(dir)
            {
                case 'n':
                {
                    cur_x--;
                    break;
                }
                case 's':
                {
                    cur_x++;
                    break;
                }
            }
        }
    }
    else if(input=='d')
    {
        if(dir=='n' || dir=='s')
        {
            cur_y++;
            dir='e';
        }
        else
        {
            switch(dir)
            {
                case 'e':
                {
                    cur_y++;
                    break;
                }
                case 'w':
                {
                    cur_y--;
                    break;
                }
            }
        }
    }
    else if(input=='a')
    {
        if(dir=='n' || dir=='s')
        {
            cur_y--;
            dir='w';
        }
        else
        {
            switch(dir)
            {
                case 'e':
                {
                    cur_y++;
                    break;
                }
                case 'w':
                {
                    cur_y--;
                    break;
                }
            }
        }
    }
    if(cur_x==0 || cur_y==0 || cur_x==N-1 || cur_y==M-1)
        end_flag=0;
    else if(arr[cur_x][cur_y]=='O')
        end_flag=0;
    else if(arr[cur_x][cur_y]=='$')
    {
        food_flag=1;
        temp_flag=1;
        score+=10;
        speed-=1000;
        if(speed<1000)
            speed=1000;
        goto next;
    }
    else
    {
        next:
        clear();
        temp=head;
        xtemp1=temp->x;
        ytemp1=temp->y;
        temp=temp->next;
        while(temp!=NULL)
        {
            xtemp2=temp->x;
            ytemp2=temp->y;
            temp->x=xtemp1;
            temp->y=ytemp1;
            xtemp1=xtemp2;
            ytemp1=ytemp2;
            temp=temp->next;
        }
        temp=head;
        temp->x=cur_x;
        temp->y=cur_y;
        if(temp_flag)
        {
            struct pos *last;
            last=malloc(sizeof(struct pos));
            last->x=xtemp1;
            last->y=ytemp1;
            last->next=NULL;
            temp=head;
            while(temp->next != NULL)
                temp=temp->next;
            temp->next=last;
        }
    }
}
void food()
{
    if(food_flag)
    {
        int i,j;
        struct pos *temp;
        again:
        temp=head;
        i=rand()%(N-1);
        j=rand()%(M-1);
        if(i==0) i++;
        if(j==0) j++;
        while(temp!=NULL)
        {
            if((temp->x)==i || (temp->y)==j)
                goto again;
            temp=temp->next;
        }
        arr[i][j]='$';
        food_flag=0;
    }
}
void print()
{
    for(int i=0;i<N;i++)
    {
        for(int j=0;j<M;j++)
            printf("%c",arr[i][j]);
        printf("\n");
    }
    printf("Score: %d\n",score);
}
void blink()
{
    struct pos *temp;
    temp=head;
    for(int k=0;k<3;k++)
    {
        assign();
        print();
        delay(5000);
        system("cls");
        clear();
        print();
        delay(5000);
        system("cls");
    }
}
void main()
{
    char input,c;
    printf("\n\t------SNAKE 2.0------\n\nRules: Use the following keys for navigation\n\t\t^\n\t\t|\n\t\tW\n\t  <-A\t    D->\n\t\tS\n\t\t|\n\t\tv\n");
    printf("\nEnter 'c' to enter the game: ");
    abc:
    c=getch();
    if(c=='c')
    {
        newgame:
        system("cls");
        setup();
        while(end_flag)
        {
            if(kbhit())
            {
                input=getch();
                if((input!='w') && (input!='s') && (input!='a') && (input!='d'))
                    input='q';
            }
            else
            input='q';
            assign();
            food();
            print();
            delay(speed);
            move(input);
            system("cls");
        }
        blink();
        clear();
        foodclear();
        repeat:
        system("cls");
        printf("\n\t   Gameover!\n\tYour score : %d\nEnter 'c' for a new game or 'x' to exit ",score);
        c=getch();
        if((c!='c') && (c!='x'))
            goto repeat;
        if(c=='c')
            goto newgame;
    }
    else
    goto abc;
}

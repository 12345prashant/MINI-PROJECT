#include<iostream>
#include<cmath>
using namespace std;

float addition(){
    int p;
    cout<<"enter the total numbers which you want to add"<<endl;
    cin>>p;
    float arr[p];
    float sum=0;
    for(int i=0;i<p;i++){
        cin>>arr[i];
        sum+=arr[i];
    }
    return sum;
}
float subtraction(){
    int p;
    cout<<"enter the total numbers which you want to subtract"<<endl;
    cin>>p;
    float arr[p];
    float sum=0;
    for(int i=0;i<p;i++){
        cin>>arr[i];
        sum-=arr[i];
    }
    return sum;
}
float multiplication(){
    int p;
    cout<<"enter the total numbers which you want to multiply"<<endl;
    cin>>p;
    float arr[p];
    float sum=1;
    for(int i=0;i<p;i++){
        cin>>arr[i];
        sum*=arr[i];
    }
    return sum;
}
float division(){
    int p;
    cout<<"enter the total numbers which you want to divide"<<endl;
    cin>>p;
    float arr[p];
    float sum=1;
    for(int i=0;i<p;i++){
        cin>>arr[i];
        sum/=arr[i];
    }
    return sum;
}
float squareroot(){
    int p;
    cout<<"enter the number for which you want to find square root"<<endl;
    float sum=sqrt(p);
    return sum;
}
float power(){
    cout<<"enter the base and power values"<<endl;
    int b,p;
    cin>>b>>p;
    float sum=pow(b,p);
    return sum;
}
float sine(){
    cout<<"Enter the number whose sine value you want"<<endl;
    float n;
    float sum = sin(n);
    return sum;
}
float cosine(){
    cout<<"Enter the number whose cosine value you want"<<endl;
    float n;
    float sum = cos(n);
    return sum;
}
float tangent(){
    cout<<"Enter the number whose Tangent value you want"<<endl;
    float n;
    float sum = tan(n);
    return sum;
}
float log(){
    cout<<"Enter the number whose log value you want"<<endl;
    float n;
    float sum = log(n);
    return sum;
}
int main(){
    cout<<"Welcome to online maths calculator"<<endl;
    cout<<"Enter want you want to execute.."<<endl;
    cout<<"1.Adition  / 2. subtraction/ 3. multiplication/ 4. division"<<endl;
    cout<<"5. Sqrt, 6. power, 7. sin, 8. cosine , 9. tan "<<endl;
    cout<<"10. log 11. log10(x) 12. absolute value"<<endl;
    cout<<"13. rrots for quad equation "<<endl;
    int n;
    cout<<"Enter the serial number of the operation you want to perform"<<endl;
    cin>>n;
    if(n==1){
       float p1= addition();
       cout<<"Addition is: "<<p1<<endl;
    }
    else if(n==2){
        float p2= subtraction();
        cout<<"Subtraction is: "<<p2<<endl;
    }
    else if(n==3){
        float p3= multiplication();
        cout<<"Multiplication is: "<<p3<<endl;
    }
    else if(n==4){
        float p4= division();
        cout<<"Divison is: "<<p4<<endl;
    }
    else if(n==5){
        float p5= squareroot();
        cout<<"Square root is: "<<p5<<endl;
    }
    else if(n==6){
        float p6 = power();
        cout<<"given power is: "<<p6<<endl;
    }
    else if(n==7){
        float p7 = sine();
        cout<<"Sin of given number is: "<<p7<<endl;
    }
    else if(n==8){
        float p8 = cosine();
        cout<<"cosine of given number is: "<<p8<<endl;
    }
    else if(n==9){
        float p9 = tangent();
        cout<<"Tangent of given number is: "<<p9<<endl;
    }
    else if(n==10){
        float p10 = log();
        cout<<"Log of given number is: "<<p10<<endl;
    }



}
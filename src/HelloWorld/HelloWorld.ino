/*
 * rosserial Publisher Example
 * Prints "hello world!"
 */

#include <ros.h>
#include <zed_slam/Distancias.h>
#include <zed_slam/MovimentoBase.h>
#include <Ultrasonic.h>

#define pinMotorEP 5
#define pinMotorEM 6
#define pinMotorDP 9
#define pinMotorDM 10

#define pino_trigger 3
#define pino_echo 2

void setarMotores(const zed_slam::MovimentoBase&);

ros::NodeHandle  nh;

zed_slam::Distancias dist;

ros::Publisher chatter("SensoresDistancia", &dist);
ros::Subscriber<zed_slam::MovimentoBase> sub("MovimentoBase", setarMotores);

Ultrasonic ultrasonic(pino_trigger, pino_echo);
float MetersMsec;
long microsec;

void setarMotores(const zed_slam::MovimentoBase& mb){
  if(mb.VelMotorE > 0){
    analogWrite(pinMotorEP, mb.VelMotorE);
    analogWrite(pinMotorEM, 0);
  }else{
    analogWrite(pinMotorEP, 0);
    analogWrite(pinMotorEM, -mb.VelMotorE);
  }
  
  if(mb.VelMotorD > 0){
    analogWrite(pinMotorDP, mb.VelMotorD);
    analogWrite(pinMotorDM, 0);
  }else{
    analogWrite(pinMotorDP, 0);
    analogWrite(pinMotorDM, -mb.VelMotorD);
  }
}

void setup()
{
  nh.initNode();
  nh.advertise(chatter);
  nh.subscribe(sub);
  pinMode(1, OUTPUT);
  pinMode(4, OUTPUT);
  digitalWrite(1, LOW);
  digitalWrite(4, HIGH);
}

void loop()
{

  // Obter dados dos sensores
  microsec = ultrasonic.timing();
  MetersMsec = ultrasonic.convert(microsec, Ultrasonic::CM)/100;
  
  // Interface com o ROS
  dist.SensorL = MetersMsec+1;
  dist.SensorC = MetersMsec;
  dist.SensorR = MetersMsec-1;
  
  chatter.publish( &dist );
  nh.spinOnce();
  delay(200);
}

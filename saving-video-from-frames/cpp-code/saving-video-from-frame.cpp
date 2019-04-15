/*
Created on Thu Apr 11 11:56:40 2019

@author: brijesh Gupta

*/

// CPP code for saving video from the frame 

// include library opencv
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/opencv.hpp>
#include <iostream>
using namespace std;
using namespace cv;
double framerate;
// video codec 
int ex = VideoWriter::fourcc('M', 'J', 'P', 'G');
bool value;
VideoWriter saving;
Mat frame;	
int main(int argc, char** argv)
{
	time_t timer;
	tm * time;
	std::time(&timer);
	time = localtime(&timer);
	std::ostringstream strs;
	strs <<time->tm_mday<<"::"<< time->tm_hour<<":"<<time->tm_min<<":"<<time->tm_sec;
	string str = strs.str();
	// video recording in .avi formate
	str ="Record --"+str+".avi";
	// video captured from IP camera
	//VideoCapture cap("rtsp://username:password@ipadress:port");
	// video captured from user command line input type . eg: 0/1 for webcam/USB camera
	VideoCapture cap(stoi(argv[1]));
	double width  = cap.get(CAP_PROP_FRAME_WIDTH);
	double height = cap.get(CAP_PROP_FRAME_HEIGHT);
	framerate=cap.get(CAP_PROP_FPS);
	saving.open(str,ex,framerate,Size(width,height),true);
  	if(!cap.isOpened())  // check if we succeeded
	{
		cout<<"cam is not opened"<<endl;
		return -1;
	}
	for(;;)
	{
		if(!cap.grab())
		{
			return 0;
		}
		cap.read(frame);
		saving.write(frame);
		namedWindow("image",WINDOW_NORMAL);
		imshow("image",frame);
		if(waitKey(1)==27) break;
	}
}
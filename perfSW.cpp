#include <opencv2/opencv.hpp>
#include <iostream>

int main() {
    //тут эта дичь открывает камеру
    cv::VideoCapture cap(0, cv::CAP_V4L2);
    //тут она типо создает окно
    cv::namedWindow("ВЕБ-КАМЕРА", cv::WINDOW_NORMAL);
    cv::resizeWindow("ВЕБ-КАМЕРА", 800, 600);
    //создаем переменную
    bool destroy_window = false;
    //капец
    cv::Mat frame;
    int frameCount = 0;

    while (!destroy_window) {
        cap >> frame;
        cv::imshow("ВЕБ-КАМЕРА", frame);
        int key = cv::waitKey(1);
        if (key == 'q' || key == 27) {
            cv::destroyAllWindows();
            destroy_window = true;
        }
    }

    //чтобы нормально заработала
    return 0;
}


# augmentation_for_yolo
only using yolo_mark_type

image and bbox augmentation
very simple code

Please refer to the picture below.

enter your directory path in line 7 ""

![image](https://user-images.githubusercontent.com/85820789/122518239-ea7b3600-d04b-11eb-81fd-5d39a8ebb42d.png)

yolo mark 형식에서 사용할 수 있는 간단한 augmentation 코드입니다.
yolo mark 형식은 많이 사용하는 이미지 크기의 좌표가 아닌 0~1로 변환한 좌표를 사용하여 이미지의 사이즈가 변경되도 bbox의 좌표가 변경되지 않음
![image](https://user-images.githubusercontent.com/85820789/122520845-1a780880-d04f-11eb-9b5f-143bc47ebb43.png)
yolo mark 는 [class] [x_axis] [y_axis] [widht] [height] 의 형태로 저장됨
한개의 사진에 클래스가 여러개일 경우 줄을 바꿔 저장해줌
![image](https://user-images.githubusercontent.com/85820789/122521077-5dd27700-d04f-11eb-8445-40ad172a4dee.png)


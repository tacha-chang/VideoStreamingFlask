import cv2
url = 'rtsp://169.254.99.133:554' #RTSP URL ที่ได้มาจากข้อก่อนหน้า
#rtsp://ip:port/
#rtsp://ip:port/video
#rtsp://ip:port/h264_stream
#rtsp://ip:port/H.264
#rtsp://ip:port/stream_h264
#rtsp://ip:port/Streaming/Channles/001/

#admin คือชื่อแล้วแต่คนตั้ง
#rtsp://admin:ip:port/
#rtsp://admin:ip:port/video
#rtsp://admin:ip:port/h264_stream
#rtsp://admin:ip:port/Streaming/Channles/001/

#admin คือชื่อแล้วแต่คนตั้ง password รหัสเครื่อง
#rtsp://admin@password:ip:port/
#rtsp://admin@password:ip:port/video
#rtsp://admin@password:ip:port/h264_stream
#rtsp://admin@password:ip:port/H.264
#rtsp://admin@password:ip:port/stream_h264
#rtsp://admin@password:ip:port/Streaming/Channles/001/
#https://www.ispyconnect.com/camera/ezviz หาpathในนี้ดู

capture = cv2.VideoCapture(url)
while True:
  ret, frame = capture.read()
  cv2.imshow('Output', frame)
  k = cv2.waitKey(10) &0xFF
  if k == 27:
     break
capture.release()
cv2.destroyAllWindows()

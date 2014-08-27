outputVideo=VideoWriter('perkymon_125.avi');
outputVideo.FrameRate=4;
open(outputVideo);

for p=1:125000
    p
    filename=strcat('./life_frames/',num2str(p),'.png');
    img=imread(filename);
    img=single(img);
    writeVideo(outputVideo,img);
end

close(outputVideo);